#creating a dumb access point from scratch

# ------------- EDIT SETTINGS HERE -------------

#basic setup
hostname='openwrt-wap'
rootpass='qwerty'
#zonename='America/Iqaluit' #default is ???
#timezone='EST5EDT,M3.2.0,M11.1.0' #default is UTC
darkmode='yes'

#setup network
deletewan='yes'
disableLANdhcpserver='yes'
setLANdhcpclient='yes'
#setstaticip='192.168.1.2'; setstaticnetmask='255.255.255.0'; setstaticdns='192.168.1.1'; setstaticgateway='192.168.1.1'
#disablednsmasq='yes' # turning off dnsmasq will stop ntp client from working automatically
enableigmpsnoop='yes'
disableipv6='yes' # only if ipv6 is not available, to avoid warning messages like  "No default route present, overriding ra_lifetime to 0!"

# WAN briding
WANbridgingmethod='singlevlan' # choices are "no", "vlanoff", "vlanbridging", "singlevlan" # vlanoff is not working correctly

#wifi country code
#wificountry='CA'

# radio 0 setup
enableradio0='yes'; radio0ssid='MYHOMEWIFI'; radio0encryption='psk'; radio0key='MYHOMEWIFIPASSWORD'; radio0disablelegacymode='yes'

# radio 1 setup
enableradio1='yes'; radio1ssid='MYHOMEWIFI'; radio1encryption='psk'; radio1key='MYHOMEWIFIPASSWORD'; radio1htmode='HT40'; radio1disablelegacymode='yes'

# install packages after boot
installpackages='tcpdump nano'

#setup ssh key
sshrootkey='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNWROS7FCEfWIAdvVnkAaFa75hmHrtdvfycf72DpaXz2una1rRRO/9XtBSZ/dOaRYS1pojIBVsrO88yhraf2IjTUhYZRFr957F7Gbo9SzBryX6NTRx2qdz4AsSTIKc9fwUo4rLNSF0Lp+04rA0QSywbIvHM/rgVKDO8xRrgE5fCBbo0BvJFtxVYdSK8M8GNNJYRIyinX/0r7Q3hKx+92oZ/9vYd6AUwHG9sRKtMVqStNx1Qe6UjqjtYDa3frih17ctXeAHspdefe6BeDDZrREVMXS8lDkYEzlTLRGFNbOnTJ20zorCG5Ih+yRrM659aWdCDDdbWFjOQsx1NmnbgW8D rsa-key-20250810'

# ------------- END OF SETTINGS -------------

#set root password
echo -e "$rootpass\n$rootpass" | passwd root

#add ssh key
mkdir -p ~/.ssh
echo "$sshrootkey" >> "/etc/dropbear/authorized_keys"

#set hostname and timezone
uci set system.@system[0].hostname="$hostname"
[ -n "$zonename" ] && uci set system.@system[0].zonename="$zonename"
[ -n "$timezone" ] && uci set system.@system[0].timezone="$timezone"

#disable dhcp server on bridge
[ "${disableLANdhcpserver:-}" = "yes" ] && uci set dhcp.lan.ignore='1'

#set bridge as dhcp client or static
[ "${setLANdhcpclient:-}" = "yes" ] && uci del network.lan.ipaddr
[ "${setLANdhcpclient:-}" = "yes" ] && uci del network.lan.netmask
[ "${setLANdhcpclient:-}" = "yes" ] && uci del network.lan.ip6assign
[ "${setLANdhcpclient:-}" = "yes" ] && uci set network.lan.proto='dhcp'
[ -n "$setstaticip" ] && uci set network.lan.ipaddr="$setstaticip"
[ -n "$setstaticip" ] && uci set network.lan.proto='static'
[ -n "$setstaticnetmask" ] && uci set network.lan.netmask="$setstaticnetmask"
[ -n "$setstaticdns" ] && uci set network.lan.gateway="$setstaticdns"
[ -n "$setstaticgateway" ] && uci set network.lan.dns="$setstaticgateway"


# enable igmp snooping
[ "${enableigmpsnoop:-}" = "yes" ] && uci set network.lan.igmp_snooping='1'

# disable dnsmasq
[ "${disablednsmasq:-}" = "yes" ] && /etc/init.d/dnsmasq disable
[ "${disablednsmasq:-}" = "yes" ] && /etc/init.d/dnsmasq stop

# Disable IPv6 on LAN
[ "${disableipv6:-}" = "yes" ] && uci set dhcp.lan.dhcpv6='disabled'
[ "${disableipv6:-}" = "yes" ] && uci set dhcp.lan.ra='disabled'
[ "${disableipv6:-}" = "yes" ] && uci set dhcp.lan.ndp='disabled'
# disable odhcpd (IPv6 router advertisements)
[ "${disableipv6:-}" = "yes" ] && /etc/init.d/odhcpd disable && /etc/init.d/odhcpd stop

#set darkmode
[ "${darkmode:-}" = "yes" ] && uci set luci.main.mediaurlbase='/luci-static/bootstrap-dark'

# clear unneeded vlans
DeleteVLAN() { [ $# -ne 2 ] && echo "Usage: DeleteVLAN <switch> <vlan>" && return 1; for i in $(uci show network | grep "=switch_vlan" | cut -d[ -f2 | cut -d] -f1); do dev=$(uci get network.@switch_vlan[$i].device); vlan=$(uci get network.@switch_vlan[$i].vlan); [ "$dev" = "$1" ] && [ "$vlan" = "$2" ] && uci delete network.@switch_vlan[$i] && echo "Deleted VLAN $2 on $1" && return; done; echo "VLAN $2 on $1 not found"; }
[ "${WANbridgingmethod:-}" = "vlanoff" ] && DeleteVLAN switch0 1
[[ "${WANbridgingmethod:-}" == "vlanoff" || "${WANbridgingmethod:-}" == "singlevlan" ]] && DeleteVLAN switch0 2

# WAN bridging method "singlevlan", move WAN to vlan #2
[ "${WANbridgingmethod:-}" = "singlevlan" ] && uci set network.@switch_vlan[0].ports='0t 1 2 3 4 5 6t'
# bridge network interfaces, no vlan
[ "${WANbridgingmethod:-}" = "vlanoff" ] && uci del network.@device[0].ports
[ "${WANbridgingmethod:-}" = "vlanoff" ] && uci add_list network.@device[0].ports='eth0'
[ "${WANbridgingmethod:-}" = "vlanoff" ] && uci add_list network.@device[0].ports='eth1'
# WAN bridging method "vlanbridging", bridge vlan #1 and #2
[ "${WANbridgingmethod:-}" = "vlanbridging" ] && uci del network.@device[0].ports
[ "${WANbridgingmethod:-}" = "vlanbridging" ] && uci add_list network.@device[0].ports='eth0.1'
[ "${WANbridgingmethod:-}" = "vlanbridging" ] && uci add_list network.@device[0].ports='eth1.1'
# disable vlan
[ "${WANbridgingmethod:-}" = "vlanoff" ] && uci set network.@switch[0].enable_vlan='0'

# Delete WAN firewall rules
DeleteFirewallRuleByName() { idx=$(uci -q show firewall | sed -n "s/^firewall\.@rule\[\([0-9]\+\)\]\.name='$1'.*/\1/p" | head -n1) && [ -n "$idx" ] && uci -q delete firewall.@rule[$idx] && uci commit firewall; }
[ "${deletewan:-}" = "yes" ] && DeleteFirewallRuleByName Allow-DHCP-Renew
[ "${deletewan:-}" = "yes" ] && DeleteFirewallRuleByName Allow-DHCPv6
[ "${deletewan:-}" = "yes" ] && DeleteFirewallRuleByName Allow-ICMPv6-Forward
[ "${deletewan:-}" = "yes" ] && DeleteFirewallRuleByName Allow-ICMPv6-Input
[ "${deletewan:-}" = "yes" ] && DeleteFirewallRuleByName Allow-IGMP
[ "${deletewan:-}" = "yes" ] && DeleteFirewallRuleByName Allow-IPSec-ESP
[ "${deletewan:-}" = "yes" ] && DeleteFirewallRuleByName Allow-ISAKMP
[ "${deletewan:-}" = "yes" ] && DeleteFirewallRuleByName Allow-MKD
[ "${deletewan:-}" = "yes" ] && DeleteFirewallRuleByName Allow-MLD
[ "${deletewan:-}" = "yes" ] && DeleteFirewallRuleByName Allow-Ping
# Delete WAN firewall zone
DeleteFirewallZoneByName() { idx=$(uci -q show firewall | sed -n "s/^firewall\.@zone\[\([0-9]\+\)\]\.name='$1'.*/\1/p" | head -n1) && [ -n "$idx" ] && uci -q delete firewall.@zone[$idx] && uci commit firewall; }
[ "${deletewan:-}" = "yes" ] && DeleteFirewallZoneByName wan
#delete WAN and WAN6 interface
[ "${deletewan:-}" = "yes" ] && uci del dhcp.wan
[ "${deletewan:-}" = "yes" ] && uci del network.wan6
[ "${deletewan:-}" = "yes" ] && uci del network.wan

#enable wifi
[ "${enableradio0:-}" = "yes" ] && uci set wireless.radio0.channel='auto'
[ "${enableradio0:-}" = "yes" ] && uci set wireless.radio0.disabled='0'
[ "${enableradio1:-}" = "yes" ] && uci set wireless.radio1.channel='auto'
[ "${enableradio1:-}" = "yes" ] && uci set wireless.radio1.disabled='0'

#Setup radio0 wifi
[ -n "$wificountry" ] && uci set wireless.radio0.country="$wificountry"
[ "${enableradio0:-}" = "yes" ] && uci set wireless.default_radio0.ssid="$radio0ssid"
[ "${enableradio0:-}" = "yes" ] && uci set wireless.default_radio0.encryption="$radio0encryption"
[ "${enableradio0:-}" = "yes" ] && uci set wireless.default_radio0.key="$radio0key"
[ "${enableradio0:-}" = "yes" ] && [ "${radio0disablelegacymode:-}" = "yes" ] && uci set wireless.radio0.legacy_rates='0'
#Setup radio1 wifi
[ -n "$wificountry" ] && uci set wireless.radio1.country="$wificountry"
[ "${enableradio1:-}" = "yes" ] && uci set wireless.default_radio1.ssid="$radio1ssid"
[ "${enableradio1:-}" = "yes" ] && uci set wireless.default_radio1.encryption="$radio1encryption"
[ "${enableradio1:-}" = "yes" ] && uci set wireless.default_radio1.key="$radio1key"
[ "${enableradio1:-}" = "yes" ] && [ "${radio1disablelegacymode:-}" = "yes" ] && uci set wireless.radio1.legacy_rates='0'
[ "${enableradio1:-}" = "yes" ] && [ -n "$radio1htmode" ] && uci set wireless.radio1.htmode="$radio1htmode"

# Add RunOnce command
AddRunOnceCommand() { cmd="$*"; hash="$(echo "$cmd" | md5sum | awk '{print $1}')"; f="/etc/rc.d/S99RunOnce-$hash.sh"; echo -e "#!/bin/sh\nlogger -t runonce \"Running: $cmd\"; $cmd && logger -t runonce \"Success: $cmd\" || logger -t runonce \"Failed: $cmd\"; logger -t runonce \"Deleting self: \$0\"; rm -f \"\$0\"" > "$f"; chmod +x "$f"; }
[ -n "$installpackages" ] && AddRunOnceCommand "ntpd -n -q -p 0.openwrt.pool.ntp.org && opkg update && opkg install $installpackages"

uci commit && reboot
