#!/usr/bin/env python

from typing import Optional

from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.derivations import BIP44Derivation
from hdwallet.utils import generate_mnemonic
import click


@click.command()
@click.option(
    '--language',
    '-l',
    help='Use this language for the generated mnemnoic.',
    default='english',
    required=False,
)
@click.option(
    '--mnemonic',
    '-m',
    help='Use this mnemnoic rather than generate a new random one.',
    default=None,
    required=False,
)
@click.option(
    '--passphrase',
    '-p',
    help='Use this passphrase rather than generate a new random one.',
    default=None,
    required=False,
)
@click.option(
    '--subwallets',
    '-s',
    help='Generate this number of subwallets (default 3).',
    default=3,
    required=False,
)
def main(language, mnemonic, passphrase, subwallets):

    if mnemonic is None:
        # Generate english mnemonic words
        MNEMONIC: str = generate_mnemonic(language=language, strength=256)
    else:
        MNEMONIC = mnemonic

    if passphrase is None:
        # Secret passphrase/password for mnemonic
        PASSPHRASE: Optional[str] = ''
    else:
        PASSPHRASE = passphrase

    # Initialize Ethereum mainnet BIP44HDWallet
    bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)
    # Get Ethereum BIP44HDWallet from mnemonic
    bip44_hdwallet.from_mnemonic(
        mnemonic=MNEMONIC, language=language, passphrase=PASSPHRASE
    )
    # Clean default BIP44 derivation indexes/paths
    bip44_hdwallet.clean_derivation()

    print('Mnemonic:', bip44_hdwallet.mnemonic())
    print('Passphrase:', bip44_hdwallet.passphrase())
    print()

    print('Private Key:', bip44_hdwallet.private_key())
    print('Public Key:', bip44_hdwallet.public_key())
    print()

    # Get Ethereum BIP44HDWallet information from address index
    for address in range(subwallets):
        # Derivation from Ethereum BIP44 derivation path
        bip44_derivation: BIP44Derivation = BIP44Derivation(
            cryptocurrency=EthereumMainnet, account=0, change=False, address=address
        )
        # Derive Ethereum BIP44HDWallet
        bip44_hdwallet.from_path(path=bip44_derivation)
        # Print address_index, path, address and private_key
        print(
            f'({address}) {bip44_hdwallet.path()} {bip44_hdwallet.address()} 0x{bip44_hdwallet.private_key()}'
        )
        # Clean derivation indexes/paths
        bip44_hdwallet.clean_derivation()


if __name__ == '__main__':
    main()


# $0 --passphrase "$(pwgen-passphrase --length 24 --wordlist eff-short)"
