from PIL import Image
import os
from pathlib import Path
import glob
import math
import shutil
import re
import argparse

def create_PDF(input_file):

    parser = argparse.ArgumentParser(description='Create a proxy deck')
    parser.add_argument('--no_leader_back', action="store_true", default=False, help='will not add leader back when leader front is present')
    parser.add_argument('--lower_res', action="store_true", default=False, help='will use cards in Cards_lower_res folder')

    args = parser.parse_args()

    if args.lower_res:
        dpi=105
        height=364
        width=260
        page_height = 1155
        page_width = 893
        input_folder = "Cards_lower_res"
    else:
        dpi=300
        height=1039
        width=744
        page_height = 3300
        page_width = 2550
        input_folder = "Cards"

    output_folder = ''

    # Reads input file, formats, and writes output
    regex_pattern = re.compile(r"[a-zA-Z]{1,2}\d{0,2}-\d{2,3}_{0,1}[a-zA-Z]{0,3}\d{0,2}_{0,1}b{0,1}")
    malformed_lines = []
    cards_not_found = []
    card_ids = []
    card_nums = []
    total_num = 0
    with open('CardList_Formatted.txt', 'w') as f_num:
        with open(input_file, 'r') as f_input:
            for line in f_input:
                line = line.strip()
                if line:
                    card_id = regex_pattern.search(line)
                    if card_id is not None:
                        card_id = card_id.group(0)
                        card_id = card_id.upper()
                        card_num = line.split(' ', 1)[0]
                        if card_num.isdigit():
                            card_num = int(card_num)
                            file_path = os.path.join(input_folder, card_id + ".png")
                            if os.path.isfile(file_path):
                                f_num.write(str(card_num)+' '+card_id+'\n')
                                card_ids.append(card_id)
                                card_nums.append(card_num)
                                if args.no_leader_back != True:
                                    leader_back_file_path = os.path.join(input_folder, card_id + "_b.png")
                                    if os.path.isfile(leader_back_file_path):
                                        card_ids.append(card_id+"_b")
                                        card_nums.append(card_num)
                            else:
                                cards_not_found.append(card_id)
                        else:
                            malformed_lines.append(line)
                            
    if malformed_lines:                   
        print("The following Card IDs were found but their line entry was malformed")
        print("Please check your input to verify the card line is formatted correctly")
        for each in malformed_lines:
            print(each)
    if cards_not_found:
        print("The following Card IDs were not found")
        print("Please check your input to verify the card ID is correct")
        print("If this card exists, please file a report on GitHub")
        for each in cards_not_found:
            print(each)

    card_images = []

    for index,card in enumerate(card_ids):
        file_path = os.path.join(input_folder, card + ".png")
        for _ in range(int(card_nums[index])):
            card_images.append(Image.open(file_path))

    num_cards = len(card_images)
    counter = 0

    margin_width = (page_width - width*3)/2
    margin_height = (page_height - height*3)/2

    # Creates the grids
    grids = []
    for grid_num in range(math.ceil(num_cards/9)):
        grid = Image.new('RGB',(page_width,page_height), (255,255,255))
        for y in range (3):
            for x in range (3):
                if counter <= num_cards-1:
                    grid.paste(card_images[counter],(int(width*x+margin_width),int(height*y+margin_height)))
                    counter += 1
        grids.append(grid)
    file_path = os.path.join(output_folder, "Cards.pdf")
    grids[0].save(file_path, save_all=True, append_images=grids[1:], resolution=dpi)

if __name__ == "__main__":
    create_PDF('CardList.txt')

