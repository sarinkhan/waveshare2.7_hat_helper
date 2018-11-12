#!/usr/bin/env python


import epd2in7
import Image
import ImageFont
import ImageDraw


def draw_filled_rect(draw, pos_x, pos_y, size_x, size_y, color=0):
    """
        Draws a rectangle at the given coordinates, of the given size.
        arguments:
            draw : the drawing surface
            pos_x : horizontal position
            pos_y : vertical position
            size_x : horizontal dimension
            size_x : vertical dimension
            color : the color of the rectangle (0=black, 1 = white)
    """
    r_fill = 1
    if color != 1:
        r_fill = 0
    draw.rectangle((pos_x, pos_y, pos_x+size_x, pos_y + size_y), fill=r_fill)


def draw_rect_border(draw, pos_x, pos_y, size_x, size_y, border = 2,  color=0):
    """
        Draws a rectangle at the given coordinates, of the given size.
        The center of the rectangle is of the opposite color of the border.
        arguments:
            draw : the drawing surface
            pos_x : horizontal position
            pos_y : vertical position
            size_x : horizontal dimension
            size_x : vertical dimension
            color : the color of the rectangle (0=black, 1 = white)
            border : the thickness of the rect border, in pixels
    """
    color1=color
    color2 = 0
    if color1 == 0:
        color2 = 1
    draw_filled_rect(draw, pos_x, pos_y, size_x, size_y, color1)
    draw_filled_rect(draw, pos_x+border, pos_y+border, size_x-border*2, size_y-border*2, color2)


def main():
    epd = epd2in7.EPD()
    epd.init()

    image = Image.new('1', (epd2in7.EPD_WIDTH, epd2in7.EPD_HEIGHT), 255)
    #image = Image.new('1', (epd2in7.EPD_WIDTH, epd2in7.EPD_HEIGHT), 255)    # 255: clear the image with white
    draw = ImageDraw.Draw(image)


    #draw_rectangle(draw, 0, 100, 50 , 100, color=0)

    draw_rect_border(draw, 0, 23, 112, 90, border = 2,  color=0)
    epd.display_frame(epd.get_frame_buffer(image))

if __name__ == '__main__':
    main()
