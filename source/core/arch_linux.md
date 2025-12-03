# Pacman

    # -i = --info
    # -S = --sync

    pacman -Si foo  # show info about available package 'foo'
    pacman -Ss bar  # show names of available packages with 'bar' in the name

    pacman -Qi foo  # show files installed by package 'foo'


# Arch Linux AMIs

* <http://mathcom.com/arch.aws.ami.html>
* <https://github.com/sormy/arch-ami-builder>
* <https://snapcraft.io/install/amazon-ssm-agent/arch>
* <https://wiki.archlinux.org/index.php/Arch_Linux_AMIs_for_Amazon_Web_Services>
* <https://uplinklabs.net/projects/arch-linux-on-ec2>
* <https://gitlab.com/bitfehler/archlinux-ec2>
* <https://packer.io/docs/builders/amazon-ebssurrogate.html>
* <https://github.com/aws/amazon-ssm-agent>


# Diagnostics

    # Show open ports
    netstat -tunap

    # Show open ports again
    ss -arpt4  # TCP/IPv4
    ss -arpt6  # TCP/IPv6
    ss -arpu4  # UDP/IPv4
    ss -arpu6  # UDP/IPv6
