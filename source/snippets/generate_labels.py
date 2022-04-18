#!/usr/bin/env python


from uuid import uuid4

# import io

import click
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from shortuuid import ShortUUID
import segno
from svglib.svglib import svg2rlg


def get_short_uuid(alphabet):
    ''' '''

    return ShortUUID(alphabet=alphabet).encode(uuid4())


def dump_qr_code(shortuuid, filename):
    ''' '''

    segno.make(shortuuid).save(filename)


@click.command()
@click.option(
    '--alphabet',
    '-a',
    default='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',
    help='Alphabet to use with UUID shortener (default base58)',
)
@click.option(
    '--banner',
    '-b',
    default='Evil Corp',
    help='Banner to stamp on tags (default "Evil Corp")',
)
@click.option(
    '--pdf',
    '-p',
    default='moo.pdf',
    help='Filename of output PDF (default "moo.pdf")',
)
@click.option(
    '--svg',
    '-s',
    default='moo.svg',
    help='Filename of output SVG (default "moo.svg")',
)
@click.help_option('--help', '-h')
def main(alphabet, banner, pdf, svg):
    ''' '''

    # buff = io.BytesIO()
    # svg = segno.make(a_short_uuid).save(buff, kind='svg', xmldecl=False,
    #                                     svgns=False)

    canv = canvas.Canvas(pdf, pagesize=letter)

    a_short_uuid = get_short_uuid(alphabet)
    dump_qr_code(a_short_uuid, svg)
    drawing = svg2rlg(svg)
    renderPDF.draw(drawing, canv, 35, 723)
    canv.setFont('Courier', 12)
    canv.drawString(70, 740, banner)
    canv.setFont('Courier', 8)
    canv.drawString(70, 730, a_short_uuid)

    a_short_uuid = get_short_uuid(alphabet)
    dump_qr_code(a_short_uuid, svg)
    drawing = svg2rlg(svg)
    renderPDF.draw(drawing, canv, 35, 673)
    canv.setFont('Courier', 12)
    canv.drawString(70, 690, banner)
    canv.setFont('Courier', 8)
    canv.drawString(70, 680, a_short_uuid)

    a_short_uuid = get_short_uuid(alphabet)
    dump_qr_code(a_short_uuid, svg)
    drawing = svg2rlg(svg)
    renderPDF.draw(drawing, canv, 35, 623)
    canv.setFont('Courier', 12)
    canv.drawString(70, 640, banner)
    canv.setFont('Courier', 8)
    canv.drawString(70, 630, a_short_uuid)

    canv.save()


if __name__ == '__main__':
    main()


# https://www.blog.pythonlibrary.org/2018/04/12/adding-svg-files-in-reportlab/
# https://segno.readthedocs.io/en/latest/
# https://github.com/deeplook/svglib
