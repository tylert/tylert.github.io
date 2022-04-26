#!/usr/bin/env python

import uuid

import click
import shortuuid


@click.command()
@click.option(
    '--alphabet',
    '-a',
    default='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',
    help='Alphabet to use to decode/encode a short UUID (default base58)',
)
@click.option(
    '--lengthen',
    '-l',
    default=None,
    help='Convert a short UUID to a long UUID',
)
@click.option(
    '--shorten',
    '-s',
    default=None,
    help='Convert a long UUID to a short UUID',
)
@click.help_option('--help', '-h')
def main(alphabet, lengthen, shorten):
    ''' '''

    # default alphabet '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz' (base57)
    # desired alphabet '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz' (base58)
    # 122 bits of entropy for UUIDv4

    if lengthen:
        print(shortuuid.ShortUUID(alphabet=alphabet).decode(lengthen))
    elif shorten:
        print(shortuuid.ShortUUID(alphabet=alphabet).encode(uuid.UUID(shorten)))
    else:
        print(shortuuid.ShortUUID(alphabet=alphabet).encode(uuid.uuid4()))


if __name__ == '__main__':
    main()


# https://github.com/skorokithakis/shortuuid
# https://pypi.org/project/shortuuid/

# https://github.com/anarcher/shortuuid
# https://pkg.go.dev/github.com/anarcher/shortuuid
