"""
font pop-up window python file for users if needed

Filename: font_menu.py
Language: python 3.7
Author: Peize(Peter)Li

"""
import turtle as t


def font_window(option):
    """
    font style option pop-up window
    if option == yes, a menu of fonts will pop up
    if users input other things, the option menu will directly be layout for them
    :param option: str
    :return: a string(@FONTSTYLE) corresponding to style_template
    """

    if option == 'yes' or option == "":
        t.title('Font Options')
        t.setup(250, 280)
        t.setworldcoordinates(-250, -250, 250, 250)
        print('Close the window when you have made your choice')
        t.speed(0)
        t.hideturtle()
        t.up()
        t.left(90)
        t.forward(170)
        t.right(90)
        t.backward(150)
        t.down()
        t.write('Arial', align='left', font=("Arial", 16, "normal"))
        t.up()
        t.right(90)
        t.forward(50)
        t.left(90)
        t.down()
        t.write('Comic Sans MS', align='left', font=("Comic Sans MS", 16, "normal"))
        t.up()
        t.right(90)
        t.forward(45)
        t.left(90)
        t.down()
        t.write('Lucida Grande', align='left', font=('Lucida Grande', 16, 'normal'))
        t.up()
        t.right(90)
        t.forward(50)
        t.left(90)
        t.down()
        t.write('Tahoma', align='left', font=('Tahoma', 16, 'normal'))
        t.up()
        t.right(90)
        t.forward(45)
        t.left(90)
        t.down()
        t.write('Verdana', align='left', font=('Verdana', 16, 'normal'))
        t.up()
        t.right(90)
        t.forward(45)
        t.left(90)
        t.down()
        t.write('Helvetica', align='left', font=('Helvetica', 16, 'normal'))
        t.up()
        t.right(90)
        t.forward(45)
        t.left(90)
        t.down()
        t.write('Times New Roman', align='left', font=('Times New Roman', 16, 'normal'))
        t.done()
    else:
        pass
