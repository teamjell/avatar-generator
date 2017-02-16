#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

"""
    Generates default avatars from a given string (such as username).

    Usage:

    >>> from avatar_generator import Avatar
    >>> photo = Avatar.generate(128, "example@sysnove.fr", "PNG")
"""

import os
from random import randint, seed
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

__all__ = ['Avatar']


class Avatar(object):
    FONT_COLOR = (255, 255, 255)

    @classmethod
    def generate(cls, image_size, font_size, string, filetype="JPEG"):
        """
            Generates a squared avatar with random background color.

            :param image_size: size of the avatar, in pixels
            :param font_size: size of the text font, in points
            :param string: string to be used to print text and seed the random
            :param filetype: the file format of the image (i.e. JPEG, PNG)
        """
        image = Image.new('RGB', (image_size, image_size),
                          cls._background_color(string))
        draw = ImageDraw.Draw(image)
        font = cls._font(font_size)
        text = cls._text(string)
        draw.text(cls._text_position(image_size, text, font),
            text,
            fill=cls.FONT_COLOR,
            font=font)
        stream = BytesIO()
        image.save(stream, format=filetype, optimize=True)
        return stream.getvalue()

    @staticmethod
    def _background_color(s):
        """
            Generate a random background color.
            Brighter colors are dropped, because the text is white.

            :param s: Seed used by the random generator
            (same seed will produce the same color).
        """
        seed(s)
        r = v = b = 255
        while r + v + b > 255*2:
            r = randint(0, 255)
            v = randint(0, 255)
            b = randint(0, 255)
        return (r, v, b)

    @staticmethod
    def _font(size):
        """
            Returns a PIL ImageFont instance.

            :param size: size of the avatar, in pixels
        """
        path = os.path.join(os.path.dirname(__file__), 'data',
            'Roboto-Regular.ttf')
        return ImageFont.truetype(path, size=size)

    @staticmethod
    def _text(string):
        """
            Returns the text to draw.
        """
        if len(string) == 0:
            return "#"
        else:
            return string[0:2].upper()

    @staticmethod
    def _text_position(size, text, font):
        """
            Returns the left-top point where the text should be positioned.
        """
        text_width, text_height = font.getsize(text)
        offset_left, offset_top = font.getoffset(text)
        left = (size - text_width)  / 2.0 - offset_left
        top  = (size - text_height) / 2.0 - offset_top
        return left, top
