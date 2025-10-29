# https://gist.github.com/braian87b/bba9da3a7ac23c35b7f1eecafecdd47d
# ========================================================
# Setup a Dumb AP, Wired backbone for OpenWRT / LEDE
# ========================================================
# Set lan logical interface as bridge (to allow bridge multiple physical interfaces)
uci set network.lan.type='bridge'
# assign WAN physical interface to LAN (will be available as an additional LAN port now)
uci set network.lan.ifname="$(uci get network.lan.ifname) $(uci get network.wan.ifname)"
uci del network.wan.ifname
# Remove wan logical interface, since we will not need it.
uci del network.wan

# Disable Dnsmasq completely (it is important to commit or discard dhcp)
uci commit dhcp; echo '' > /etc/config/dhcp
/etc/init.d/dnsmasq disable
/etc/init.d/dnsmasq stop

# Set static network configuration (sample config for 192.168.1.0/24)
# 192.168.1.1 is the Main Router
uci set network.lan.ipaddr='192.168.1.2'
uci set network.lan.dns='192.168.1.1'
uci set network.lan.gateway='192.168.1.1'
uci set network.lan.netmask='255.255.255.0'
uci set network.lan.broadcast='192.168.1.255'

# Set DHCP on LAN (not recommended, but useful when Dumb AP is moveable from one building to another)
uci del network.lan.broadcast
uci del network.lan.dns
uci del network.lan.gateway
uci del network.lan.ipaddr
uci del network.lan.netmask
uci set network.lan.proto='dhcp'

# To identify better when connected to SSH and when seen on the network
uci set system.@system[0].hostname='DumbAP1'
uci set network.lan.hostname="`uci get system.@system[0].hostname`"

# ========================================================
# Optional, Disable IPv6
# ========================================================
uci del network.lan.ip6assign
uci set network.lan.delegate='0'
uci del dhcp.lan.dhcpv6
uci del dhcp.lan.ra
uci del dhcp.odhcpd
/etc/init.d/odhcpd disable
/etc/init.d/odhcpd stop

# ========================================================
# Commit changes, flush, and restart network
# ========================================================
# This way we will get internet on this AP and we must reconnect
uci commit
sync
/etc/init.d/network restart
# If all is OK then reboot and test again:
reboot

# How to setup Wireless Links to avoid Wired backbone using WDS on Atheros for OpenWRT / LEDE
https://gist.github.com/braian87b/8a524a8ad74a36407a8f481e9d16a5c9
# How to setup Client Bridged / Client Mode / RelayD and IGMPProxy for OpenWRT / LEDE
https://gist.github.com/braian87b/821e9e4f399918510c55619192a31871
