def parse_gcode_file(draw_gcode_file, paint_gcode_file):

    x_current = 0
    y_current = 0
    x_previous = 0
    y_previous = 0

    # for each line in the g code file
    for line in draw_gcode_file:
        line = line.strip()

        # g code command
        if line.startswith('G0'):
            x_current = get_number(line, 'X')
            y_current = get_number(line, 'Y')
            if (x_current != x_previous and y_current == y_previous) \
                    or (x_current == x_previous and y_current != y_previous)\
                    or (x_current != x_previous and y_current != y_previous):
                paint_gcode_file.write(line + '\n')
                x_previous = x_current
                y_previous = y_current
        elif line.startswith('X'):
            x_current = get_number(line, 'X')
            y_current = get_number(line, 'Y')
            if (x_current != x_previous and y_current == y_previous) \
                    or (x_current == x_previous and y_current != y_previous)\
                    or (x_current != x_previous and y_current != y_previous):
                line = 'G1 ' + line
                paint_gcode_file.write(line + '\n')
                x_previous = x_current
                y_previous = y_current

    draw_gcode_file.close()
    paint_gcode_file.close()


def get_number(line, command_letter):

    # character immediately after command letter
    n = line.find(command_letter) + 1
    m = line.find(' ', n)

    # if no space is found in the current line
    if m == -1:
        return float(line[n:])
    else:
        return float(line[n:m])