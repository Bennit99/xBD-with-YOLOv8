import json
import os
from typing import TextIO

"""
change the annotation from xBD format to an yolo readable annotation format
"""

folder_path = 'E:\\path\\to\\data'

# for all files in the destination folder that end with ".json" and contain "post".
for filename in os.listdir(folder_path + '\\labels'):
    if filename.endswith('.json') and 'post' in filename:
        file_path = os.path.join(folder_path + '\\labels', filename)

        # load json file
        with open(file_path, 'r') as file:
            annotations = json.load(file)

        # Create txt file for new YOLO format
        yolo_annos_file = open(folder_path + '\\new_labels\\' + filename[0:-4] + 'txt', 'w')

        # select building list
        buildings = annotations['features']['xy']
        text = ''  #
        # iterate over buildings
        for i in range(len(buildings)):

            # parse building damage and translate to numerical scala
            damage = buildings[i]['properties']['subtype']
            if damage == 'no-damage'    :   text += '0'
            if damage == 'minor-damage' :   text += '1'
            if damage == 'major-damage' :   text += '2'
            if damage == 'destroyed'    :   text += '3'
            if damage == 'un-classified':   text += '4'

            # parse coordinates of polygon from string to float
            polygon_list = buildings[i]['wkt'][10:-2].replace(',', '').split()
            # bring coordinates to range 0 to 1 from range 0 to 1024
            for j in range(len(polygon_list)):
                text += ' ' + str(float(polygon_list[j]) / 1024)

            text += '\n'  # new line

        yolo_annos_file.write(text)  # write text to file
        yolo_annos_file.close()  # close file
