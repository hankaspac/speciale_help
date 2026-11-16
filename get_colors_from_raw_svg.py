svgs = ['area_gradient_ex.txt', 'bubble_ex.txt', 'bubble_legend.txt', 'diverging_point.txt', 'four_cols-lum65.txt', 'four_cols.txt', 'line_chart.txt', 'map_categ.txt', 'stacked_bar.txt', 'stacked_bar_2_vals.txt', 'svg_ex_1.txt', 'svg_ex_2.txt', 'svg_ex_3.txt', 'svg_ex_4.txt', 'svg_ex_5.txt', 'svg_ex_6.txt', 'svg_ex_heatmap.txt', 'too_many_colors.txt', 'too_many_test.txt', 'wrong_chart_maps_colors.txt', 'wrong_map.txt']

input_file = "input_svgs/"+svgs[5]
output_file = "new_txt.txt"
start = '<'
end = '>'

def write_line(out_file, line):
    file = open(out_file, "a")
    file.write(line + "\n")
    file.close()

def split_long_line_into_lines():
    with open(input_file, 'r') as file:
        my_long_line = file.read()
        len_line = len(my_long_line)
        while(len_line > 1):
            index_start = my_long_line.find(start)
            index_end = my_long_line.find(end)
            if index_start != -1 and index_end != -1:
                short_line = my_long_line[index_start + len(start):index_end+1]
                write_line(output_file, short_line)
                my_long_line = my_long_line.replace(short_line, "")
                len_line = len(my_long_line)
            else:
                print('Nope!')

def extract_labels_description():
    with open(output_file, 'r') as file:
        for line in file:
            if "role-legend" in line:
                if "aria-label" in line:
                    my_index = line.index("aria-label")
                    my_len = len("aria-label")
                    print("Here is the legend description: ", line[my_index+my_len:-2])
                
list_of_colors = []
def extract_color_hex():
    with open(output_file, 'r') as file:
        for line in file:
            if "path transform=\"translate" in line:
                if "fill=" in line:
                    my_index = line.index("fill=")
                    my_len = len("my_index")
                    end_len = len(line[my_index+my_len-3:])
                    hex_len = 9
                    list_of_colors.append(line[my_index+my_len-3:-(end_len-hex_len)])
    print("We have", len(list_of_colors), "classes.")
    print("They have colors: ", list_of_colors)

def clear_output_file():
    with open(output_file, "r+") as my_file:
        my_file.seek(0)
        my_file.truncate()
        print("done")

print("The file: ", input_file)
split_long_line_into_lines()
extract_labels_description()
extract_color_hex()
clear_output_file()