# Written by Eric Martin for COMP9021


'''
Draws three coloured dodecagrams, separed by a distance of one third
the length of the edges, and centred in the window that displays them.
'''


from turtle import *


edge_length = 50
angle = 60

def draw_dodecagram(colour1,colour2):

    for _ in range(3):
        color(colour1)
        forward(edge_length)
        right(angle)
        color(colour2)
        forward(edge_length)
        left(angle * 2)
        forward(edge_length)
        right(angle)
        color(colour1)
        forward(edge_length)
        left(angle*2)
def teleport(distance):
    penup()
    right(angle)
    forward(distance)
    pendown()


# Make sure that the dodecagrams are centred horizontally in the window that displays them.
# Without the following statement, the left end of the horizontal edge of the green dodecagram,
# from which the drawing starts, would be at the centre of the screen
# (so the dodecagrams are not quite centred vertically).
teleport(-edge_length // 2 )
# Draw the middle dodecagram, then the left dodecagram, then the right dodecagram.
draw_dodecagram('blue','red')

