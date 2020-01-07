#!/usr/bin/env python

import uuid

import shortuuid
import click
# import segno


@click.command()
@click.option('--alphabet', '-a',
              default='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',
              help='Alphabet to use with UUID shortener (default base58)')
@click.option('--decode', '-d', default=None,
              help='Decode this string back to a UUID')
@click.help_option('--help', '-h')
def main(alphabet, decode):
    '''Main function'''

    shortener = shortuuid.ShortUUID(alphabet=alphabet)
    a_uuid = uuid.uuid4()

    if decode:
        print(shortener.decode(decode))
    else:
        print(shortener.encode(a_uuid))


if __name__ == '__main__':
    main()
