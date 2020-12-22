#!/usr/bin/env python

import uuid
import io

import click
from shortuuid import ShortUUID
import segno
from svglib.svglib import svg2rlg
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF


@click.command()
@click.option('--alphabet', '-a',
              default='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',
              help='Alphabet to use with UUID shortener (default base58)')
@click.option('--thingy', '-t', default=None, help='Filename to write PDF into')
@click.option('--whatzit', '-w', default=None, help='Filename to write SVG into')
@click.help_option('--help', '-h')
def main(alphabet, thingy, whatzit):
    '''Main function'''

    # Make the UUID
    shortening = ShortUUID(alphabet=alphabet)
    a_short_uuid = shortening.encode(uuid.uuid4())

    # Make the QR code containing the UUID
    buff = io.BytesIO()
    # svg = segno.make(a_short_uuid).save(buff, kind='svg', xmldecl=False, svgns=False)
    segno.make(a_short_uuid).save(whatzit)

    # Place the QR code and the human-readable UUID in the PDF
    canv = canvas.Canvas(thingy, pagesize=letter)
    drawing = svg2rlg(whatzit)
    renderPDF.draw(drawing, canv, 35, 730)
    canv.drawString(70, 750, 'asset.link')
    canv.drawString(70, 735, a_short_uuid)
    canv.save()


if __name__ == '__main__':
    main()


# https://www.blog.pythonlibrary.org/2018/04/12/adding-svg-files-in-reportlab/
# https://segno.readthedocs.io/en/latest/
# https://github.com/deeplook/svglib
