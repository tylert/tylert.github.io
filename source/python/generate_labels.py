#!/usr/bin/env python

import uuid
import io

import shortuuid
import click
import segno
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


@click.command()
@click.option('--alphabet', '-a',
              default='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',
              help='Alphabet to use with UUID shortener (default base58)')
@click.option('--thingy', '-t', default=None, help='Filename to write into')
@click.help_option('--help', '-h')
def main(alphabet, thingy):
    '''Main function'''

    shortener = shortuuid.ShortUUID(alphabet=alphabet)
    a_short_uuid = shortener.encode(uuid.uuid4())

    buff = io.BytesIO()
    svg = segno.make(a_short_uuid).save(buff, kind='svg', xmldecl=False, svgns=False)

    canv = canvas.Canvas(thingy, pagesize=letter)
    canv.drawString(100,750,a_short_uuid)
    canv.save()


if __name__ == '__main__':
    main()
