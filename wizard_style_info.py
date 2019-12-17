"""
store all style information as dataclass objects for the head part of the website
Filename: wizard_style_info.py
Language: Python 3.7
Author: Peize(Peter)Li

"""

from dataclasses import dataclass
from typing import Any
import font_menu

###############################################################################################
GLOBAL_COLOR_LIST = ['peachpuff', 'slateblue', 'powderblue', 'lightcyan',
                     'chartreuse', 'moccasin', 'mediumseagreen', 'lawngreen',
                     'seagreen', 'mintcream', 'azure', 'goldenrod', 'lightblue',
                     'firebrick', 'lightseagreen', 'chocolate', 'yellowgreen',
                     'darkolivegreen', 'violet', 'ivory', 'sandybrown', 'wheat',
                     'mediumvioletred', 'bisque', 'lightgreen', 'cyan', 'hotpink',
                     'gray', 'indianred', 'antiquewhite', 'royalblue', 'yellow',
                     'indigo', 'lightcoral', 'darkslategrey', 'sienna', 'lightslategray',
                     'mediumblue', 'red', 'khaki', 'darkviolet', 'mediumorchid', 'darkblue',
                     'lightskyblue', 'turquoise', 'lightyellow', 'grey', 'whitesmoke',
                     'blueviolet', 'orchid', 'mediumslateblue', 'darkturquoise', 'coral',
                     'forestgreen', 'gainsboro', 'darkorange', 'cornflowerblue', 'lightsteelblue',
                     'plum', 'lavender', 'palegreen', 'darkred', 'dimgray', 'floralwhite', 'orangered',
                     'oldlace', 'darksalmon', 'lavenderblush', 'darkslategray', 'tan', 'cadetblue', 'silver',
                     'tomato', 'darkkhaki', 'slategray', 'maroon', 'olive', 'deeppink', 'linen', 'magenta',
                     'crimson', 'mistyrose', 'lime', 'saddlebrown', 'blanchedalmond', 'black', 'snow',
                     'seashell', 'darkcyan', 'gold', 'midnightblue', 'darkgoldenrod', 'palevioletred',
                     'fuchsia', 'teal', 'lightpink', 'darkgrey', 'mediumspringgreen', 'aquamarine',
                     'lightsalmon', 'navajowhite', 'darkgreen', 'burlywood', 'rosybrown', 'springgreen',
                     'purple', 'olivedrab', 'lightslategrey', 'orange', 'aliceblue', 'mediumaquamarine',
                     'navy', 'salmon', 'rebeccapurple', 'darkmagenta', 'limegreen', 'deepskyblue', 'pink',
                     'mediumpurple', 'skyblue', 'aqua', 'blue', 'slategrey', 'darkslateblue', 'honeydew',
                     'darkseagreen', 'paleturquoise', 'brown', 'thistle', 'lemonchiffon', 'peru', 'cornsilk',
                     'papayawhip', 'green', 'lightgoldenrodyellow', 'mediumturquoise', 'steelblue', 'lightgray',
                     'lightgrey', 'beige', 'palegoldenrod', 'darkgray', 'white', 'ghostwhite', 'dodgerblue',
                     'greenyellow', 'dimgrey', 'darkorchid']
GLOBAL_HEX_NUM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
GLOBAL_HEX_LETTER = ['a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']
#################################################################################################


@dataclass
class StyleInfo:
    """
    setup information of a web page

    FIELD DESCRIPTION:
    title: title of the website
    bg_color: background color
    font_option: the font style which users decide
    text_color: paragraph text color
    heading_color: heading color

    """
    title: Any
    bg_color: str
    font_option: str
    text_color: str
    heading_color: str


def font_option(option):
    """
    get users' input and return its according string
    :param option: which font users decide to choose
    :return: the font string
    """
    if option == '0':
        return 'Arial'
    elif option == '1':
        return 'Comic Sans MS'
    elif option == '2':
        return 'Lucida Grande'
    elif option == '3':
        return 'Tahoma'
    elif option == '4':
        return 'Verdana'
    elif option == '5':
        return 'Helvetica'
    elif option == '6':
        return 'Times New Roman'
    else:
        return 'Illegal input'


def color_upper_lst():
    """
    create a list with all possible uppercase color names
    :return: all possible uppercase color names
    """
    color_lower_lst = GLOBAL_COLOR_LIST
    color_upper_list = []
    for i in range(len(color_lower_lst)):
        color_upper_list.append(color_lower_lst[i].upper())
    return color_upper_list


def color_first_upper_lst():
    """
    create a list with all possible first letter uppercase color names
    :return: all possible first letter uppercase color names
    """
    color_lower_lst = GLOBAL_COLOR_LIST
    color_upper_list = []
    for i in range(len(color_lower_lst)):
        color_upper_list.append(color_lower_lst[i].capitalize())
    return color_upper_list


def color_input():
    """
    color error handling and prompts for color
    :return: color
    """
    color_lower = GLOBAL_COLOR_LIST
    color_upper = color_upper_lst()
    color_first_upper = color_first_upper_lst()
    hex_num = GLOBAL_HEX_NUM
    hex_letter = GLOBAL_HEX_LETTER
    color = input("Choose the name of a color, or in format '#XXXXXX':")
    if color[0] == '#':
        for i in range(1, len(color)):
            if (color[i] not in hex_num) and (color[i] not in hex_letter):
                print('illegal format')
                return color_input()
            else:
                continue
        return color
    else:
        if (color not in color_lower) and (color not in color_upper) and (color not in color_first_upper):
            print('illegal format')
            return color_input()
        else:
            return color


def store_all_style_info():
    """
    it prompts for all style information and store them as an object
    :return: the object which stores all style information
    """
    title = input('What is the title of your website?')
    print('Background Color')
    bg_color = color_input()
    print('You will now choose a font.')
    menu_pullout = input('Do you want to see what the fonts look like? [yes]')
    font_menu.font_window(menu_pullout)
    print("Choose a font by its number.")
    print("0: Arial, size 16")
    print("1: Comic Sans MS, size 16")
    print("2: Lucida, size 16")
    print("3: Tahoma, size 16")
    print("4: Verdana, size 16")
    print("5: Helvetica, size 16")
    print("6: Times New Roman, size 16")
    font = input("")
    font_choice = font_option(font)
    while font_choice == 'Illegal input':
        print(font_choice, 'choose again')
        font = input("")
        font_choice = font_option(font)
    print('Paragraph Text Color')
    text_color = color_input()
    print('Heading Color')
    heading_color = color_input()
    return StyleInfo(title, bg_color, font_choice, text_color, heading_color)

