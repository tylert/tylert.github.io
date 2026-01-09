# Zelda3

* <https://github.com/snesrev/zelda3>
* <https://github.com/snesrev/zelda3/wiki>
* <https://github.com/cjhoward/smc2sfc>
* <https://archive.org/details/legend-of-zelda-the-a-link-to-the-past-u_202407>
* <https://aur.archlinux.org/packages/zelda3-git>

    # Strip headers from a SNES ROM
    $ wget https://raw.githubusercontent.com/cjhoward/smc2sfc/refs/heads/master/smc2sfc.cpp
    $ g++ smc2sfc.cpp -o smc2sfc
    $ ./smc2sfc zelda3.smc zelda3.sfc

    # Only generate assets needed to play
    $ git clone https://github.com/snesrev/zelda3 ; cd zelda3
    $ python -m venv .venv && source .venv/bin/activate
    $ python -m pip install --upgrade --requirement requirements.txt  # pillow PyYAML
    # Put zelda3.sfc in the top-level directory of the project
    $ python assets/restool.py --extract-from-rom

    # Checksums you might care about
    $ sha256sum zelda3.smc  # header included
    d9c69c5270b2f7eac54f254688a43cc767fd5cb4f21fc079a0f9fbe09978eaec  zelda3.smc
    $ sha256sum zelda3.sfc  # header excluded
    66871d66be19ad2c34c927d6b14cd8eb6fc3181965b6e517cb361f7316009cfb  zelda3.sfc
    $ sha256sum zelda3_assets.dat
    0fe2e4bd75d70f06fb9a74cd3a9cb336c838149b831b56e8792114a89292c793  zelda3_assets.dat

    # Just play the damn game
    $ git clone https://github.com/snesrev/zelda3 ; cd zelda3
    $ sudo pacman -S sdl2
    $ python -m venv .venv && source .venv/bin/activate
    $ python -m pip install --upgrade --requirement requirements.txt  # pillow PyYAML
    # Put zelda3.sfc in the top-level directory of the project
    $ make
    $ ./zelda3


# Game Stuff

* <https://github.com/kentonv/lanparty>
* <https://news.ycombinator.com/item?id=31590724>
* <https://bazzite.gg> immutable desktop for Steam Decks?
* <https://renpy.org/doc/html/build.html#archives> .rpa scripts and images files example
* <https://reddit.com/r/RenPy/comments/wq6jms/how_to_compress_un_rpa>
* <https://reddit.com/r/RenPy/comments/sv92zp/rpa_files> .rpa files are just Python pickle files maybe?
* <https://github.com/Lattyware/unrpa> RenPy data file unpacking
* <https://pypi.org/project/unrpa> pip install unrpa
* <https://github.com/shizmob/rpatool> RenPy data file repacking thing maybe?
* <https://github.com/Steam-Headless/docker-steam-headless> access your big game machine from any web browser?
* <https://diymultideck.mauri.app> fancy deck of cards
* <https://naikari.github.io> open-source space game thing
* <https://aperture-software.github.io/colditz-escape>
* <https://github.com/aperture-software/colditz-escape>
* <https://zero-k.info>
* <https://zerok.itch.io/zero-k>
* <https://veloren.net>
* <https://openmw.org>
* <https://wesnoth.org>
* <https://slipseer.com/index.php?resources/quake-brutalist-jam-iii.549> Quake Brutalist Jam III
* <https://github.com/andrei-drexler/ironwail> Quake patch/upgrade


# RPG Stuff

* <https://adventurekeep.com>
* <https://github.com/stassa/nests-and-insects> TTRPG
* <https://gitlab.com/wargames_tex/wargame_tex>
* <https://gitlab.com/wargames_tex/bfm_tex>
* <http://www.ericharshbarger.org/dice/go_first_dice.html> (mandatory 'http' and 'www' here)
* <https://elleosiliwood.itch.io/the-missing-locksmith>
* <https://perchance.org/dnd-draconic-names>
* <http://mewo2.com/notes/terrain> OMG awesome
* <http://mewo2.com/notes/naming-language> OMG awesome
* <https://github.com/mewo2/deserts> code for 2 items above
* <https://github.com/mewo2/terrain> Jabbascript version??
* <https://github.com/mewo2/naming-language> more Jabbascript for name generation??
* <https://gist.github.com/munificent/b1bcd969063da3e6c298be070a22b604> random dungeon generator on a business card
* <https://olano.dev/blog/deconstructing-the-role-playing-videogame> GURPS, TWERPS, Dinky Dungeons, etc.


# Retro Computing

* <https://kilograham.github.io/rp2040-doom>
* <https://github.com/pod-arcade/pod-arcade> k8s + RetroArch???
* <https://lakka.tv> neato interface like RetroArch, RetroPie, Kodi?
* <https://jamesfmackenzie.com/2021/02/06/mister-ao486-core-part-1-dos-quick-start> 486SX in an FPGA
* <https://0mhz.net>
* <https://amiga.vision>
* <https://medium.com/@8bitsten/start-with-c-programming-on-amiga-1e8312cec2db>
* <http://compilers.de/vbcc.html> vintage CPU/computer C99-compiler, assembler, linker
* <https://aminet.net/tree?path=dev>
* <https://misterreplay.com/mister-fpga-guide.html>
* <https://krystof.io/mister-fpga-initial-setup-and-network-mounting>
* <https://mister-devel.github.io/MkDocs_MiSTer/advanced/computer/#ppp-connection>
* <https://brutman.com/mTCP> DHCP, HTGET, PING, TELNET, etc.
* <https://github.com/AnttiTakala/SSH2DOS>
* <https://misterfpga.org/viewtopic.php?t=478> change hostname, MAC address, etc.
* <https://datagubbe.se/adosmyst> AmigaDOS tips and tricks
* <https://sttmedia.com/newline> Amiga line endings should be the same as Linux/Unix
* <https://wiki.amigaos.net/wiki/AmigaOS_Apps_Productivity_%26_Utilities>
* <https://ocawesome101.github.io/486-linux.html> Linux on a i486SX
* <http://slackware.com/install/sysreq.php> Slackware claims to run on a 486
* <https://knopper.net/knoppix-info/index-en.html> Knoppix claims to run on a 486
* <https://retrocomputing.stackexchange.com/questions/1811/which-linux-or-bsd-distributions-do-still-support-i386-i486-or-i586-cpus#1815> more ancient CPU discussions
* <https://github.com/rasteri/HIDman> using your favourite USB keyboards and mice with a computer that only talks PS/2, AT, XT, etc.
* <https://snes.nesdev.org/wiki/ROM_file_formats> .SFC, .SMC, .SWC, .FIG ROM files
* <https://github.com/franckverrot/EmulationResources/blob/master/consoles/megadrive/genesis_rom.txt> .BIN, .MD, .SMD ROM files
* <https://theblackzone.net/posts/2018/msdos622-in-qemu>
* <https://github.com/jessodum/ngrom> convert Genesis/MegaDrive SMD format ROMs to BIN format ROMs
* <https://zeldix.net/t1662-remove-header> stripping SNES ROM headers
* <https://r-roms.github.io>
* <https://pukepals.com/2025/06/05/mister-fpga-console>
* <https://github.com/Abdess/retroarch_system> BIOS
* <https://retropie.org.uk/docs/3do> BIOS md5sums
* <https://aterik.github.io/Transpiler.and.similar.List> Go to C???
* <https://en.wikipedia.org/wiki/Newline#Representation>
* <https://en.wikipedia.org/wiki/EBCDIC>
* <https://en.wikipedia.org/wiki/End-of-file>
* <https://ultibo.org> Raspberry Pi bare metal magic?
* <https://reddit.com/r/fpgagaming/comments/7uvp0h/baremetal_raspberry_pi_emulators>
* <https://pcem-emulator.co.uk/index.html>
* <https://dansanderson.com/lab-notes/mister-in-an-amiga-600> pretty
* <https://printables.com/model/1060816-gutbombs-retrodeck-amiga-ish-style-for-de10-nano-m> pretty
* <https://ravener.is-a.dev/posts/compressing-games-to-chd> converting various CD images to CHD format
* <https://retrogamecorps.com/2023/02/06/the-ultimate-rom-file-compression-guide> chdman
* <https://retrogamecoders.com/roguelike-multiplatform> also using cc65, vbcc, etc. C compilers
* <https://github.com/wickerwaka/PicoROM> RP2040 simulating a ROM
* <https://zuzebox.wordpress.com/2023/12/31/raspberry-pi-pico-rp2040-retro-vintage-home-computer-emulation>
* <https://benjamin.computer/posts/2025-07-28-amiga40.html> Amiga Workbench installs with modern conveniences
* <https://kazeta.org> console appliance distro?
* <https://the-ventureweaver.itch.io> The Labyrinth of Time's Edge text adventure
* <https://nemanjatrifunovic.substack.com/p/history-of-the-gem-desktop-environment> OpenGEM, FreeGEM, etc.???
* <https://cmaiolino.wordpress.com/dosbian> apt-get install dosbox?
* <https://cmaiolino.wordpress.com/amiga-pi> apt-get install uae4arm?
* <https://cmaiolino.wordpress.com> apt-get install vice?
* <https://onerom.org>
* <https://github.com/piersfinlayson/one-rom>
* <https://bytecellar.com/bbsing>
* <https://misterfpga.org/viewtopic.php?t=9699&start=30> Gravis UltraSound settings on ao486
* <https://franke.ms/git/bebbo/bebbossh> SSH2 client and server for Amiga m68k
* <https://franke.ms/git/bebbo/bebboget> tiny HTTPS file fetcher for Amiga m68k
* <https://markround.com/blog/2023/08/30/amiga-systems-programming-in-2023>
* <https://amikit.amiga.sk/devpack>
* <https://scenelist.org> old-school BBS stuff
* <https://github.com/bquenin/interpreter> translate JRPGs into English?
* <https://github.com/reinauer/amifuse> Amiga filesystems mounted using FUSE in Linux and so on

    myrient?

EOL:

    Linux,Unix,Amiga  LF
    Commodore,MacOld  CR
    CP/M,OS/2,DOS     CRLF
    BBCMicro          CR or LFCR
    RISCOS            LF or LFCR
    EvilOS            LCFR
    SortedOS          CFLR
    MorseCode         BT

    CR  0x0d  13  \r
    LF  0x0a  10  \n


# Controllers

* <https://thearcadestick.com> review arcade sticks
* <https://gp2040-ce.info> RP2040 based arcade sticks
* <https://github.com/OpenStickCommunity> RP2040 based arcade sticks
* <https://osa-stick.com> Open Source Arcade stick (nearly all 3D-printed)
* <https://github.com/Technische-Dienstleistungen-Niggemann/osa-stick> Open Source Arcade stick
* <https://multi-console-controller.com>
* <https://learn.adafruit.com/super-nintendo-usb-controller/overview>
* <https://github.com/misteraddons/Reflex-CTRL> NES, SNES, MD controller replacement PCBs
* <https://github.com/RWeick/N64-Controller-CFS8120-700010> KiCAD PCB for N64 controller
* <https://phobgcc.com> replacement GC controller PCB
* <https://github.com/PhobGCC/PhobGCCv2-HW> PhobGCC STEP files
* <https://3dprinting.stackexchange.com/questions/12258/step-f3d-to-scad-file/21488#21488> STEP files in OpenSCAD
* <https://github.com/ashley-hawkins/openscad-step-reader> STEP files in OpenSCAD
* <https://aliexpress.com/item/1005009088913192.html> USB GC controllers
* <https://elecrow.com/phobgcc-v2-gamecube-controller-motherboard.html>
* <https://compendium.dol-003.info> more detailed GC controller details
* <https://github.com/darthcloud/cube64-dx> GC vs N64 button comparisons
* <https://github.com/timville85/4dapter> all-in-one adapter for NES, SNES, MD, N64, GC controllers
* <https://raphnet.net/electronique/gc_to_n64/index_en.php>
* <https://raphnet-tech.com/products/gc_usb_adapter_v4/index.php>
* <https://amazon.ca/Mayflash-GameCube-Controller-Adapter-Switch/dp/B00RSXRLUE> Linux-friendly GC USB adapter (9 ms latency?)
* <https://raphnet.net/electronique/gcn64_usb_adapter_gen3/index_en.php> another GC USB adapter option (6 ms latency?)
* <https://retrorgb.com/open-source-usb-to-gamecube-adapter-from-robert-dale-smith.html>
* <https://github.com/joypad-ai/joypad-os>
* <https://github.com/FreeJoy-Team/FreeJoy>
* <https://github.com/FreeJoy-Team/FreeJoyConfiguratorQt>


# Cartridges

* <https://vkc.sh/sannis-open-source-cartridge-reader>
* <https://savethehero.builders>
* <https://github.com/sanni/cartreader>
* <https://cartreader.net>


# MiSTer

* <https://multisystem.uk/products/mister-multisystem-2>
* <https://shop.heber.co.uk/mister-multisystem2-fpga-analogue-console-system-black-enclosure>
* <https://boogermann.github.io/Bible_MiSTer> loads more customization and stuff
* <https://gamehacking.org> magic cheat codes for various games


# Zaparoo

* <https://zaparoo.org>
* <https://zaparoo.org/docs/readers/nfc/pn532-usb>
* <https://zaparoo.org/docs/tokens/nfc>
* <https://zaparoo.org/docs/zapscript>
* <https://github.com/ZaparooProject/zaparoo-core>
* <https://github.com/ZaparooProject/go-pn532>


# NFC

* <https://github.com/ItsDanik/rfidisk> fake floppy disks with NFC reader
* <https://github.com/ZaparooProject> NFC reader for MiSTer
* <https://zaparoo.org/docs/readers/nfc/pn532-usb> readers
* <https://zaparoo.org/docs/tokens/nfc/ntag> tags
* <https://zaparoo.org/docs/core/cli/#write> write to the tags
* <https://printables.com/model/955506-tapto-usb-c-reader-case-black-pn532-board> enclosure for PN532 board
* <https://printables.com/model/999381-tapto-card-reader-with-spring-loaded-ejection-butt> fancy eject mechanism
* <https://printables.com/model/1140054-zaparootapto-for-mister-fpga-add-on-enclosure> other enclosure option
* <https://printables.com/model/1053628-nfc-entertainment-system-pc-based>
* <https://printables.com/model/896333-tapto-pn532-v2-nfc-reader-case>
* <https://github.com/NyLan-1/Floppy_Disk_Labels> floppy disk labels
* <https://github.com/GSWXXN/NFCToolsGUI> maybe?
* <https://blog.sknk.ws/blog/2021/05/03/using-a-pn532-nfc-module-with-libnfc> maybe?
* <https://wakdev.com/en/apps/nfc-tools-pc-mac.html> closed-source AppImage, might not support PN532 readers
* <https://eccel.co.uk/how-to-set-a-password-for-the-read-write-operations-on-ntag2xx> password-protect stuff?
* <https://forums.adafruit.com/viewtopic.php?t=82031> password-protect stuff?
* <https://docs.mtoolstec.com/pn532-cli/how-to-start> CLI?
* <https://github.com/whywilson/pn532-python> CLI?
* <https://www.ecotner.com/blog/nfc-hacking> (mandatory 'www' here)
* <https://nfcpy.readthedocs.io/en/latest/index.html>
* <https://ndeftool.readthedocs.io/en/stable/index.html>

    NTAG216 has 888 user bytes
    NXP NTAG216 is a NFC Forum Type 2 tag?  ISO/IEC 14443 Type A?

    pip install ndeftool nfcpy


# Modern Floppy Discs

* <https://mariozechner.at/posts/2025-04-20-boxie>
* <https://hackaday.com/2024/07/12/making-sd-cards-more-nostalgic-with-more-cartridge-ness>
* <https://abe.today/blogs/main/floppy8-a-tiny-computer-in-a-floppy-drive>
