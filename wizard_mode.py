"""
wizard_mode module which finalizes html file using all data stored

Filename: wizard_mode.py
Language: python 3.7
Author: Peize(Peter)Li

"""

import css_builder
import wizard_content_info


def contruct_image(image_lst):
    """
    construct all extra images to a list
    :param image_lst: all image file names in a list
    :return: a list of all img strings containing image file names in it
    """
    image_str_lst = []
    if len(image_lst) == 0:
        return image_str_lst
    else:
        while len(image_lst) > 1:
            image_str_lst.append('<img src="')
            image_str_lst.append(image_lst[0])
            image_str_lst.append('" class="center"> \n')
            image_lst = image_lst[1:]
        if len(image_lst) == 1:
            image_str_lst.append('<img src="')
            image_str_lst.append(image_lst[0])
            image_str_lst.append('" class="center"> \n')
        return image_str_lst


def construct_unstatic_content(content_queue):
    """
    dequeue the first content and return any extra content if exists
    :param content_queue: queue structure which stores all content
    :return:a list of strings which represent extra content
    """
    unstatic_content_lst = []
    wizard_content_info.dequeue_content(content_queue)
    while content_queue.front is not None:
        unstatic_content_lst.append('<h2>')
        unstatic_content_lst.append(content_queue.front.p_title)
        unstatic_content_lst.append('</h2> \n')
        unstatic_content_lst.append('<p>')
        unstatic_content_lst.append(content_queue.front.content)
        unstatic_content_lst.append('</p> \n')
        image = contruct_image(content_queue.front.image)
        for i in range(len(image)):
            unstatic_content_lst.append(image[i])
        wizard_content_info.dequeue_content(content_queue)

    return unstatic_content_lst


def create_html():
    """
    main function that creates the html file using data stored in other modules
    :return: None
    """
    all_style = css_builder.modify_template(1)
    all_content = wizard_content_info.store_all_content_info()
    final_file = open('index.html', 'w')
    style_file = open('style_template.txt', 'r')
    static_text = ['<!DOCTYPE html> \n', '<html> \n', '<head> \n', '<meta charset="UTF-8"> \n',
                   '<title>', all_style.title, '</title>\n', style_file.read(), ' \n', '</head> \n', '<body> \n',
                   '<h1>', all_style.title, '</h1> \n', '<hr/> \n', '<h2>', all_content.front.p_title, '</h2> \n',
                   '<p>', all_content.front.content, '</p> \n']
    static_text_image = contruct_image(all_content.front.image)
    for i in range(len(static_text_image)):
        static_text.append(static_text_image[i])

    unstatic_text = construct_unstatic_content(all_content)
    for i in range(len(unstatic_text)):
        static_text.append(unstatic_text[i])

    static_text.append('</body> \n')
    static_text.append('</html> \n')

    final_file.writelines(static_text)
    final_file.close()
    print('Your web page has been saved as index.html')


