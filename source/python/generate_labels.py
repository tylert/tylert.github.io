#!/usr/bin/env python

from uuid import uuid4
# import io

import click
from shortuuid import ShortUUID
import segno
from svglib.svglib import svg2rlg
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF


def get_short_uuid(alphabet):
    ''''''

    return ShortUUID(alphabet=alphabet).encode(uuid4())


def dump_qr_code(shortuuid, filename):
    segno.make(shortuuid).save(filename)


@click.command()
@click.option('--alphabet', '-a',
              default='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',
              help='Alphabet to use with UUID shortener (default base58)')
@click.option('--thingy', '-t', default=None, help='Filename to write PDF into')
@click.option('--whatzit', '-w', default=None, help='Filename to write SVG into')
@click.help_option('--help', '-h')
def main(alphabet, thingy, whatzit):
    '''Main function'''

    # buff = io.BytesIO()
    # svg = segno.make(a_short_uuid).save(buff, kind='svg', xmldecl=False, svgns=False)

    canv = canvas.Canvas(thingy, pagesize=letter)

    a_short_uuid = get_short_uuid(alphabet)
    dump_qr_code(a_short_uuid, whatzit)
    drawing = svg2rlg(whatzit)
    renderPDF.draw(drawing, canv, 35, 725)
    canv.drawString(70, 745, 'asset.link')
    canv.drawString(70, 731, a_short_uuid)

    a_short_uuid = get_short_uuid(alphabet)
    dump_qr_code(a_short_uuid, whatzit)
    drawing = svg2rlg(whatzit)
    renderPDF.draw(drawing, canv, 35, 675)
    canv.drawString(70, 695, 'asset.link')
    canv.drawString(70, 681, a_short_uuid)

    a_short_uuid = get_short_uuid(alphabet)
    dump_qr_code(a_short_uuid, whatzit)
    drawing = svg2rlg(whatzit)
    renderPDF.draw(drawing, canv, 35, 625)
    canv.drawString(70, 645, 'asset.link')
    canv.drawString(70, 631, a_short_uuid)

    canv.save()


if __name__ == '__main__':
    main()


# https://www.blog.pythonlibrary.org/2018/04/12/adding-svg-files-in-reportlab/
# https://segno.readthedocs.io/en/latest/
# https://github.com/deeplook/svglib
