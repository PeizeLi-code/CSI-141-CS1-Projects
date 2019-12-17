"""
stores and constructs information for the content of the body part in a website
incorporates similar enqueue & dequeue implementation from cs_queue.py created by CS @rit.edu
Filename: wizard_content_info.py
Language: python 3.7
Author: Peize(Peter)Li & CS @rit.edu

"""
from dataclasses import dataclass
from typing import Union, Any


@dataclass
class ContentInfo:
    """
    a node structure to store all content information

    FIELD DESCRIPTION:
    p_title: title of the paragraph
    content: content of the paragraph
    image: list of image file names
    rest: rest of the content info
    """
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


def enqueue_content(queue, p_title, content, image):
    """
    insert a ContentInfo into the queue
    :param queue: a queue
    :param p_title: paragraph title
    :param content: paragraph content
    :param image: a list of image files
    :return: None
    """
    newp = ContentInfo(p_title, content, image, None)
    if queue.front is None:
        queue.front = newp
    else:
        queue.back.rest = newp
    queue.back = newp


def dequeue_content(queue):
    """
    remove the front element from the queue.
    :param queue:
    :return: None
    """
    if queue.front is None:
        raise IndexError
    queue.front = queue.front.rest
    if queue.front is None:
        queue.back = None


def image_option():
    """
    prompts users if they want to add images or not
    :return: a list which contains all image files
    """
    all_images_lst = []
    image = input('Do you want to add images? [yes]')
    while image == 'yes' or image == '':
        image_file = input('Image file name:')
        all_images_lst.append(image_file)
        image = input('Do you want to add another image? [yes]')

    return all_images_lst


def add_paragraph_option():
    """
    prompts users if they want to add another paragraph
    :return: list contains ContentInfo objects if users ask for another paragraph
    """
    extra_content_lst = []
    paragraph = input('Do you want to add another paragraph to your website? [yes]')
    while paragraph == 'yes' or paragraph == '':
        title = input('Title of your paragraph?')
        content = input('Content of your paragraph (single line)')
        images = image_option()
        extra_content_lst.append((ContentInfo(title, content, images, None)))
        paragraph = input('Do you want to add another paragraph to your website? [yes]')

    return extra_content_lst


def store_all_content_info():
    """
    it prompts for information that is needed for the body part of the website
    and stores them in a queue
    :return: a queue which contains all content information for body part of the website
    """
    all_content = ContentQueue(None, None)
    title = input('Title of your paragraph?')
    content = input('Content of your paragraph (single line)')
    images = image_option()
    enqueue_content(all_content, title, content, images)
    extra_content = add_paragraph_option()
    if len(extra_content) == 0:
        pass
    else:
        for i in range(len(extra_content)):
            enqueue_content(all_content, extra_content[i].p_title, extra_content[i].content, extra_content[i].image)

    return all_content
