import os
import parse

# define input and output file directory and names
file_directory = r'C:\Users\johno\Desktop\BBBS_painting'
draw_file_name = 'layer_4.nc'
paint_file_name = 'layer_4_formatted.nc'

draw_file_path = os.path.join(file_directory, draw_file_name)
paint_file_path = os.path.join(file_directory, paint_file_name)

draw_gcode_file = open(draw_file_path, 'r')
paint_gcode_file = open(paint_file_path, 'w')

# convert gcode drawing to painting
parse.parse_gcode_file(draw_gcode_file, paint_gcode_file)