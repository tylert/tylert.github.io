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
    '--decode',
    '-d',
    default=None,
    help='Convert (decode) a short UUID to a long UUID',
)
@click.option(
    '--encode',
    '-e',
    default=None,
    help='Convert (encode) a long UUID to a short UUID',
)
@click.option(
    '--name',
    '-n',
    default=None,
    help='Generate a UUIDv5 using a specified name instead of a UUIDv4',
)
@click.option(
    '--namespace',
    '-s',
    default='DNS',
    help='Namespace to use for the UUIDv5 name (default "DNS")',
)
@click.help_option('--help', '-h')
def main(alphabet, decode, encode, name, namespace):
    '''Generate a short UUIDv4 if no parameters specified'''

    # default alphabet '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz' (base57)
    # desired alphabet '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz' (base58)
    # 122 bits of entropy for UUIDs

    if decode:
        print(shortuuid.ShortUUID(alphabet=alphabet).decode(string=decode))
    elif encode:
        print(shortuuid.ShortUUID(alphabet=alphabet).encode(uuid=uuid.UUID(encode)))
    elif name:
        match namespace:
            case 'DNS':
                print(
                    shortuuid.ShortUUID(alphabet=alphabet).encode(
                        uuid=uuid.uuid5(namespace=uuid.NAMESPACE_DNS, name=name)
                    )
                )
            case 'OID':
                print(
                    shortuuid.ShortUUID(alphabet=alphabet).encode(
                        uuid=uuid.uuid5(namespace=uuid.NAMESPACE_OID, name=name)
                    )
                )
            case 'URL':
                print(
                    shortuuid.ShortUUID(alphabet=alphabet).encode(
                        uuid=uuid.uuid5(namespace=uuid.NAMESPACE_URL, name=name)
                    )
                )
            case 'X500':
                print(
                    shortuuid.ShortUUID(alphabet=alphabet).encode(
                        uuid=uuid.uuid5(namespace=uuid.NAMESPACE_X500, name=name)
                    )
                )
            case _:
                raise ValueError
    else:
        print(shortuuid.ShortUUID(alphabet=alphabet).encode(uuid=uuid.uuid4()))


if __name__ == '__main__':
    main()


# https://github.com/skorokithakis/shortuuid  python implementation
# https://pypi.org/project/shortuuid/  python implementation
# https://github.com/lithammer/shortuuid  go implementation
# https://pkg.go.dev/github.com/lithammer/shortuuid  go implementation
# https://docs.python.org/3/library/uuid.html  python uuid standard library
