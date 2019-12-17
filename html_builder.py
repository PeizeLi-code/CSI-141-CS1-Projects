"""
main program that calls all modules

Filename: html_builder.py
Language: python 3.7
Author: Peize(Peter)Li

Final Grade: 96/100
Comments: didn't deal with multiple websites on the command line

"""

import website_mode
import wizard_mode
import sys


def main():
    """
    main function of the entire HTML program
    :return: None
    """
    if len(sys.argv) == 1:
        wizard_mode.create_html()
    else:
        website_mode.read_command(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()


