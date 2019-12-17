"""
modify style_template.txt and replace all variable strings

Filename: css_builder.py
Language: python 3.7
Author: Peize(Peter)Li

"""

import wizard_style_info
import website_style_info


def modify_template(mode):
    """
    modify the style_template.txt using variables stored in style_info modules
    :return: all style info data stored in objects
    """
    if mode == 1:
        all_style_info = wizard_style_info.store_all_style_info()
    elif mode == 2:
        all_style_info = website_style_info.store_all_style_info()

    file = open('style_template.txt', 'r')
    data = file.read()
    data = data.replace('@BACKCOLOR', all_style_info.bg_color)
    file.close()

    file = open('style_template.txt', 'w')
    file.write(data)
    file.close()

    file = open('style_template.txt', 'r')
    data = file.read()
    data = data.replace('@HEADCOLOR', all_style_info.heading_color)
    file.close()

    file = open('style_template.txt', 'w')
    file.write(data)
    file.close()

    file = open('style_template.txt', 'r')
    data = file.read()
    data = data.replace('@FONTSTYLE', all_style_info.font_option)
    file.close()

    file = open('style_template.txt', 'w')
    file.write(data)
    file.close()

    file = open('style_template.txt', 'r')
    data = file.read()
    data = data.replace('@FONTCOLOR', all_style_info.text_color)
    file.close()

    file = open('style_template.txt', 'w')
    file.write(data)
    file.close()

    return all_style_info


