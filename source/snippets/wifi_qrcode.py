#!/usr/bin/env python


# import io

import click
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import segno
from svglib.svglib import svg2rlg


def dump_qr_code(thing, filename):
    ''' '''

    segno.make(thing).save(filename)


@click.command()
@click.option(
    '--passwd',
    '-p',
    help='Password to encode in the barcode',
    default=None,
)
@click.option(
    '--output_pdf',
    '-o',
    help='Filename of output PDF (default "wifi.pdf")',
    default='wifi.pdf',
)
@click.option(
    '--ssid',
    '-s',
    help='SSID to encode in the barcode',
    default=None,
)
@click.option(
    '--temp_svg',
    '-t',
    help='Filename of output SVG (default "wifi.svg")',
    default='wifi.svg',
)
@click.option(
    '--wifi_type',
    '-w',
    help='Type to encode in the barcode',
    default='WPA',
)
@click.help_option('--help', '-h')
def main(passwd, output_pdf, ssid, temp_svg, wifi_type):
    ''' '''

    # buff = io.BytesIO()
    # temp_svg = segno.make(a_short_uuid).save(buff, kind='svg', xmldecl=False,
    #                                     svgns=False)

    canv = canvas.Canvas(output_pdf, pagesize=letter)
    wifi = f'WIFI:T:{wifi_type};S:"{ssid}";P:"{passwd}";;'

    dump_qr_code(wifi, temp_svg)
    drawing = svg2rlg(temp_svg)
    renderPDF.draw(drawing, canv, 35, 700)
    canv.setFont('Courier', 8)
    canv.drawString(40, 745, wifi)

    canv.save()


if __name__ == '__main__':
    main()


# https://www.blog.pythonlibrary.org/2018/04/12/adding-svg-files-in-reportlab/
# https://segno.readthedocs.io/en/latest/
# https://github.com/deeplook/svglib

# https://github.com/zxing/zxing/wiki/Barcode-Contents#wi-fi-network-config-android-ios-11
