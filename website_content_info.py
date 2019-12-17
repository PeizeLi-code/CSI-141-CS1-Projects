"""
stores all info data into a queue structure
incorporates similar enqueue & dequeue implementation from cs_queue.py created by CS @rit.edu
Filename: website_content_info.py
Language: python 3.7
Author: Peize(Peter)Li & CS @rit.edu
"""

from dataclasses import dataclass
from typing import Any, Union
import wizard_content_info


@dataclass
class ContentInfo:
    """
    a node structure to store all content information

    FIELD DESCRIPTION:
    p_title: title of the paragraph
    content: content of the paragraph
    image: list of tuples(filename, width)
    rest: rest of the content info
    """
    title: Any
    p_title: Any
    content: Any
    image: list
    rest: Union[None, 'ContentInfo']


@dataclass
class ContentQueue:
    """
    Queue structure that stores all paragraph content

    FIELD DESCRIPTION:
    front: front node
    back: back node
    """
    front: Union[None, 'ContentInfo']
    back: Union[None, 'ContentInfo']


def enqueue_content(queue, title, p_title, content, image):
    """
    insert a ContentInfo into the queue
    :param queue: a queue
    :param title: title of the web page
    :param p_title: paragraph title
    :param content: paragraph content
    :param image: a list of image files
    :return: None
    """
    newp = ContentInfo(title, p_title, content, image, None)
    if queue.front is None:
        queue.front = newp
    else:
        queue.back.rest = newp
    queue.back = newp


def dequeue_content(queue):
    """
    get rid of the front node of the queue
    :param queue: a queue structure
    :return: None
    """
    wizard_content_info.dequeue_content(queue)


def construct_content_queue(filename):
    """
    given the text file, read through the file and create the queue of all info data
    :param filename: filename of the text provided
    :return: queue of all info data stored
    """
    all_data = ContentQueue(None, None)
    f = open(filename)
    title = f.readline().strip()
    p_title = ''
    images = []
    content = ''
    new_para = f.readline()
    for lines in f:
        lines = lines.strip()
        if lines != '!new_paragraph':
            if lines[0:6] == '!title':
                lines_lst = lines.split(' ')
                for i in range(1, len(lines_lst)):
                    p_title += lines_lst[i]
                    p_title += ' '
            elif lines[0:6] == '!image':
                lines_lst = lines.split(' ')
                if len(lines_lst) == 2:
                    images.append((lines_lst[1], None))
                else:
                    images.append((lines_lst[1], lines_lst[2]))
            else:
                content += lines
                content += ' '
        elif lines == '!new_paragraph':
            enqueue_content(all_data, title, p_title, content, images)
            p_title = ''
            images = []
            content = ''

    enqueue_content(all_data, title, p_title, content, images)

    return all_data











