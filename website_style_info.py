"""
store all style information as dataclass objects for the head part of the website
Filename: website_style_info.py
Language: Python 3.7
Author: Peize(Peter)Li

"""

from dataclasses import dataclass
import font_menu
import wizard_style_info


@dataclass
class WebsiteStyleInfo:
    """
    style information of a web page

    FIELD DESCRIPTION:
    bg_color: background color
    font_option: the font style which users decide
    text_color: paragraph text color
    heading_color: heading color
    """
    bg_color: str
    font_option: str
    text_color: str
    heading_color: str


def store_all_style_info():
    """
    it prompts for all style information and store them as an object
    :return: the object which stores all style information
    """
    print('Background Color')
    bg_color = wizard_style_info.color_input()
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
    font_choice = wizard_style_info.font_option(font)
    while font_choice == 'Illegal input':
        print(font_choice, 'choose again')
        font = input("")
        font_choice = wizard_style_info.font_option(font)
    print('Paragraph Text Color')
    text_color = wizard_style_info.color_input()
    print('Heading Color')
    heading_color = wizard_style_info.color_input()
    return WebsiteStyleInfo(bg_color, font_choice, text_color, heading_color)
