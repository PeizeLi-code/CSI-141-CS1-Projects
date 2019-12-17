"""
create html files for website_mode
Filename: website_mode.py
Language: python 3.7
Author: Peize(Peter)Li

"""

import css_builder
import website_content_info


def check_image(image_lst):
    """
    returns a list of all images info in string
    :param image_lst: a list image data stored
    :return: a list of all image info texts
    """
    image_text = []
    if len(image_lst) == 0:
        image_text.append(" \n")
    else:
        for i in range(len(image_lst)):
            if image_lst[i][1] is None:
                image_text.append('<img src="')
                image_text.append(image_lst[i][0])
                image_text.append('" class="center"> \n')
            else:
                image_text.append('<img src="')
                image_text.append(image_lst[i][0])
                image_text.append('" width="')
                image_text.append(image_lst[i][1])
                image_text.append('" class="center"> \n')

    return image_text


def construct_content(queue):
    """
    returns a list of all info data in string
    :param queue: queue of all info data stored
    :return: a list of all info in string
    """
    unstatic_text = []
    website_content_info.dequeue_content(queue)
    while queue.front is not None:
        unstatic_text.append('<h2>')
        unstatic_text.append(queue.front.p_title)
        unstatic_text.append('</h2> \n')
        unstatic_text.append('<p>')
        unstatic_text.append(queue.front.content)
        unstatic_text.append('</p> \n')
        unstatic_image_lst = check_image(queue.front.image)

        for i in range(len(unstatic_image_lst)):
            unstatic_text.append(unstatic_image_lst[i])
        website_content_info.dequeue_content(queue)

    return unstatic_text


def create_html(filename, static_filename1, static_filename2, all_content, static_title1, static_title2):
    """
    create respective web page according to the 2 file names provided
    :param filename: filename contains all inputs
    :param static_filename1: filename
    :param static_filename2: the other linked filename
    :param all_content: queue of all data stored
    :param static_title1: the title of the first first file
    :param static_title2: the title of the other file
    :return: title of each web page
    """
    html_file = filename[0:(len(filename)-4)]
    html_file += '.html'
    static_html_file = static_filename1[0:(len(static_filename1) - 4)]
    static_html_file += '.html'
    other_html_file = static_filename2[0: (len(static_filename2)-4)]
    other_html_file += '.html'
    final_file = open(html_file, 'w')
    style_file = open('style_template.txt', 'r')
    static_text = ['<!DOCTYPE html> \n', '<html> \n', '<head> \n', '<meta charset="UTF-8"> \n',
                   '<title>', all_content.front.title, '</title>\n', style_file.read(), ' \n', '</head> \n',
                   '<body> \n', '<h1>', all_content.front.title, '</h1> \n', '<hr/> \n', '<p align="center"><a href="',
                   static_html_file, '">', static_title1, '</a>---<a href="', other_html_file, '">',
                   static_title2, '</a>--- \n', '</p> \n', '<h2>', all_content.front.p_title, '</h2> \n', '<p> \n',
                   all_content.front.content, '</p> \n']
    front_image_lst = check_image(all_content.front.image)

    for i in range(len(front_image_lst)):
        static_text.append(front_image_lst[i])
    unstatic_text = construct_content(all_content)

    for i in range(len(unstatic_text)):
        static_text.append(unstatic_text[i])

    static_text.append('</body> \n')
    static_text.append('</html> \n')

    final_file.writelines(static_text)
    final_file.close()


def read_command(filename1, filename2):
    """
    read_command function that organises all functions and finalises creating html files
    :return: None
    """
    css_builder.modify_template(2)
    queue_1 = website_content_info.construct_content_queue(filename1)  # all website info stored in queue
    queue_2 = website_content_info.construct_content_queue(filename2)
    website1_title = queue_1.front.title
    website2_title = queue_2.front.title
    create_html(filename1, filename1, filename2, queue_1, website1_title, website2_title)
    create_html(filename2, filename1, filename2, queue_2, website1_title, website2_title)











