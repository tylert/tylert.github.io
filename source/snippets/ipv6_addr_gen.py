#!/usr/bin/env python

# Generate RFC-4193-compliant private IPv6 address prefixes and
# RFC-4291-compliant MAC-packed-in-IPv6 addresses

# https://tools.ietf.org/html/rfc4193#section-3.2.2
# https://tools.ietf.org/html/rfc4291#appendix-A
# https://tools.ietf.org/html/rfc4291#section-2.5.1

# http://souptonuts.sourceforge.net/readme_working_with_time.html
# https://en.wikipedia.org/wiki/MAC_address
# https://netaddr.readthedocs.io/en/latest/tutorial_02.html
# https://pythonhosted.org/pytz/

# python ipv6_addr_gen.py -m 112233445566 -n 3781380740.248752 -s 1 -l
# fd83c11dc5a7f4f4
# 112233fffe445566


from datetime import datetime  # timestamp magic
from hashlib import sha1  # hash magic
from random import randint, seed  # random magic
from struct import pack  # double-to-bytes magic
from uuid import getnode  # MAC address magic
# import ipaddress

from netaddr import EUI, mac_bare  # MAC address magic
# from netaddr import IPv6Address, IPv6Network  # IP address magic
# import pytz
import click


def debug_time():
    ''''''

    # XXX FIXME TODO Fix this up to help show examples of NTP timestamps!!!

    ntp = (datetime.utcnow() - datetime(1900, 1, 1)).total_seconds()
    unix = (datetime.utcnow() - datetime(1970, 1, 1)).total_seconds()

    print(ntp)
    print(unix)
    print(ntp - unix)


def get_ntp_time(ntp_time=''):
    '''Generate a 64-bit NTP time structure from "now" (in UTC) or a given
       timestamp'''

    if ntp_time == '':
        ntp = (datetime.utcnow() - datetime(1900, 1, 1)).total_seconds()
    else:
        # NTP Epoch is 1900-01-01, Unix Epoch is 1970-01-01
        # The difference between them is 2208988800 seconds
        ntp = (datetime.utcfromtimestamp(float(ntp_time) -
                                         2208988800) - datetime(1900, 1,
                                                                1)).total_seconds()
    if ntp > 2**32-1:
        # We ran out of NTP epoch time
        raise OverflowError('The POSIX world has ended!!!')

    # 8 bytes long
    return bytearray(pack('!d', ntp)).hex()


def get_mac_serial(mac_serial='', random_mac=False, random_seed=None):
    '''Generate fixed or random 48-bit identifier from MAC address or serial'''

    # Drop all the '0x', '-' and ':' junk from MAC addresses (dialect=mac_bare)

    if random_mac:
        if random_seed is not None:
            seed(random_seed)
        # Generate a totally-random MAC (registered OUIs be damned!!!)
        mac = EUI(bytearray([randint(0, 255)
                             for i in range(6)]).hex(), dialect=mac_bare)
    elif mac_serial == '':
        # Try to determine the current host's MAC
        mac = EUI(getnode(), dialect=mac_bare)
    else:
        # Use the predetermined hex string
        mac = EUI(mac_serial, dialect=mac_bare)

    # 6 bytes long
    return bytearray.fromhex(str(mac)).hex()


def get_global_id(mac_serial='', ntp_time='', random_mac=False,
                  random_seed=None):
    '''Grab last 40 bits of the SHA1 digest of NTP + MAC bytes for the Global
       ID'''

    ntp = bytearray.fromhex(get_ntp_time(ntp_time=ntp_time))

    mac = bytearray.fromhex(get_mac_serial(mac_serial=mac_serial,
                                           random_mac=random_mac,
                                           random_seed=random_seed))

    # Last 5 bytes
    return bytearray(sha1(b''.join([ntp, mac])).digest())[-5:].hex()


def get_rfc4193_network_prefix(mac_serial='', ntp_time='', random_mac=False,
                               random_seed=None):
    '''Provide a RFC-4193-compliant private IPv6 address range'''

    gid = bytearray.fromhex(get_global_id(mac_serial=mac_serial,
                                          ntp_time=ntp_time,
                                          random_mac=random_mac,
                                          random_seed=random_seed))

    if random_seed is not None:
        seed(random_seed)

    # 8 bytes long
    return bytearray(b''.join([bytearray([int(0xfd)]), gid,
                               bytearray([randint(0, 255) for i in range(2)])])).hex()


def get_rfc4291_eui64_suffix(local=True, mac_serial='', random_mac=False,
                             random_seed=None):
    '''Follow RFC-4291 to convert 48-bit IEEE 802 MAC identifier to 64-bit IEEE
       EUI-64'''

    # First 3 bytes
    mac_start = bytearray.fromhex(get_mac_serial(mac_serial=mac_serial,
                                                 random_mac=random_mac,
                                                 random_seed=random_seed))[0:3]

    # Last 3 bytes
    mac_end = bytearray.fromhex(get_mac_serial(mac_serial=mac_serial,
                                               random_mac=random_mac,
                                               random_seed=random_seed))[3:]

    # XXX FIXME TODO Might have to reverse the logic of the local flag!!!

    # Bit 6:  0=universal/global, 1=local
    # Bit 7:  0=individual/unicast, 1=group/multicast
    if local:
        # Set bit 6 of first byte
        mac_start[0] = mac_start[0] | 0x2

    # Stuff 0xFF, 0xFE in the middle
    # 8 bytes long
    return bytearray(b''.join([mac_start, bytearray([int(0xff), int(0xfe)]),
                               mac_end])).hex()


@click.command()
@click.option('--local', '-l', is_flag=True, default=True,
              help='Set bit 6 of RFC-4291 EUI-64')
@click.option('--mac_serial', '-m', default='', help='MAC serial number')
@click.option('--ntp_time', '-n', default='',
              help='NTP timestamp string (e.g.: "3781380740.248752")')
@click.option('--random_mac', '-r', is_flag=True, default=False,
              help='Random MAC')
@click.option('--random_seed', '-s', default=None,
              help='Seed randomness with a fixed value')
@click.help_option('--help', '-h')
# @click.version_option(None, '--version', '-v')
def main(local, mac_serial, ntp_time, random_mac, random_seed):
    '''Generate private IPv6 addresses'''

    # XXX FIXME TODO Spit these out in IPv6 notation rather than a list of
    #                bytes!!!

    print(get_rfc4193_network_prefix(mac_serial=mac_serial,
                                     ntp_time=ntp_time,
                                     random_mac=random_mac,
                                     random_seed=random_seed))

    print(get_rfc4291_eui64_suffix(local=local, mac_serial=mac_serial,
                                   random_mac=random_mac,
                                   random_seed=random_seed))


if __name__ == '__main__':
    main()


# https://stackoverflow.com/questions/159137/getting-mac-address
# https://stackoverflow.com/questions/19210414/byte-array-to-hex-string
# https://stackoverflow.com/questions/21017698/converting-int-to-bytes-in-python-3
# https://stackoverflow.com/questions/36893206/converting-a-float-to-bytearray
# https://stackoverflow.com/questions/5495492/random-byte-string-in-python
# https://stackoverflow.com/questions/5649407/hexadecimal-string-to-byte-array-in-python
# https://stackoverflow.com/questions/6624453/whats-the-correct-way-to-convert-bytes-to-a-hex-string-in-python-3
# https://stackoverflow.com/questions/8244204/ntp-timestamps-in-python
# https://www.devdungeon.com/content/working-binary-data-python
