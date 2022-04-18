#!/usr/bin/env python

from uuid import uuid4

import click
from shortuuid import ShortUUID


@click.command()
@click.option(
    '--alphabet',
    '-a',
    default='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',
    help='Alphabet to use with UUID shortener (default base58)',
)
@click.option(
    '--decode',
    '-d',
    default=None,
    help='Decode this string back to a UUID',
)
@click.help_option('--help', '-h')
def main(alphabet, decode):
    ''' '''

    shortening = ShortUUID(alphabet=alphabet)

    if decode:
        print(shortening.decode(decode))
    else:
        print(shortening.encode(uuid4()))


if __name__ == '__main__':
    main()
