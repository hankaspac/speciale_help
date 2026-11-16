svg_lines_dir = ['area_gradient_ex_lines.txt', 'bubble_ex_lines.txt', 'bubble_legend_lines.txt', 'diverging_point_lines.txt', 'four_cols-lum65_lines.txt', 'four_cols_lines.txt', 'line_chart_lines.txt', 'map_categ_lines.txt', 'stacked_bar_2_vals_lines.txt', 'stacked_bar_lines.txt', 'svg_ex_1_lines.txt', 'svg_ex_2_lines.txt', 'svg_ex_3_lines.txt', 'svg_ex_4_lines.txt', 'svg_ex_5_lines.txt', 'svg_ex_6_lines.txt', 'svg_ex_heatmap_lines.txt', 'too_many_colors_lines.txt', 'too_many_test_lines.txt', 'wrong_chart_maps_colors_lines.txt', 'wrong_map_lines.txt']

input_file = "svgs_lines/"+svg_lines_dir[20]


def extract_labels_description():
    with open(input_file, 'r') as file:
        for line in file:
            if "role-legend" in line:
                if "aria-label" in line:
                    my_index = line.index("aria-label")
                    my_len = len("aria-label")
                    print("Here is the legend description: ", line[my_index+my_len:-2])
                
list_of_colors = []
def extract_color_hex():
    with open(input_file, 'r') as file:
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


print("The file: ", input_file)
extract_labels_description()
extract_color_hex()
