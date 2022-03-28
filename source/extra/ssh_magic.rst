Local Test VM
-------------

You might "vagrant up" something and then "vagrant ssh" into it (perhaps with
"config.ssh.forward_agent = true" in your Vagrantfile) and you then wish to
jump past the crappy NAT from the VM host into the VM guest to do stuff...

Execute the following on the VM guest::

    ssh -fN -R 2222:localhost:22 10.0.2.2 -l user_on_the_vm_host

Execute the following on the VM host::

    ssh -p 2222 localhost -l user_on_the_vm_guest \
        -i .vagrant/machines/default/virtualbox/private_key


Remote Assistance Fu
--------------------

Add a new user::

    USER='stimpy'
    useradd --create-home --comment 'New User,,,,' ${USER}

Prepare ssh::

    mkdir --mode=0700 --parents ~/.ssh
    ssh-keygen -t ed25519 -C "${USER}@${HOSTNAME}" -N '' -f ~/.ssh/id_ed25519
    ssh-copy-id ${USER}@${HOSTNAME}

Prepare sshd::

    SSHD_PORT='22'
    # sed -i '/^#PasswordAuthentication yes /s/^#//' /etc/ssh/sshd_config
    # echo "PasswordAuthentication no" >> /etc/ssh/sshd_config

Do password stuff for a user::

    passwd --delete --lock ${USER}
    # passwd ${USER}

Turn on (password-less) sudo access for a given user::

    GROUP='wheel'
    echo "${USER} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USER}
    echo "# ${USER} ALL=(ALL) ALL" >> /etc/sudoers.d/${USER}
    echo "# %${GROUP} ALL=(ALL) ALL" >> /etc/sudoers.d/${USER}

Tunnel through da hinterweebz::

    VPNUSER='ren'
    slave$ ssh -R 2222:localhost:${SSHD_PORT} ${VPNUSER}@master
    master$ ssh -p 2222 ${USER}@localhost

Screen magic::

    screen -S foobar
    screen -x foobar
    ^ad


Network
-------

Execute on hostA, reverse tunnel from port1 on hostC to port0 on hostA
A => C::

    PORT0='22'
    PORT1='2222'
    ssh -R *:${PORT1}:localhost:${PORT0} ${CHOST} -l ${CUSER}
    # putty.exe -ssh -R *:${PORT1}:localhost:${PORT0} ${CHOST} -l ${CUSER}

Execute on hostB, tunnel from port2 on hostB to port1 on hostC
B -> C::

    PORT2='22222'
    ssh -L *:${PORT2}:localhost:${PORT1} ${CHOST} -l ${CUSER}
    # putty.exe -ssh -L *:${PORT2}:localhost:${PORT1} ${CHOST} -l ${CUSER}

Execute on hostB, connect to port2 on hostB via port1 on hostC to port0 on hostA
B -> A::

    ssh localhost -p ${PORT2} -l ${AUSER}
    # putty.exe -ssh localhost -P ${PORT2} -l ${AUSER}

* https://superuser.com/questions/315523/ssh-connection-between-two-behind-nat-computers-through-third-public-ip-computer?rq=1
* https://blog.trackets.com/2014/05/17/ssh-tunnel-local-and-remote-port-forwarding-explained-with-examples.html
* https://robotmoon.com/ssh-tunnels/
* https://infosec.mozilla.org/guidelines/openssh


Session Stuff
-------------

::

    Use the undocumented option "UseRoaming=no'  on the command line:
    example: ssh -oUseRoaming=no pacharest@mc.pubb-it.com

    Or, force the option for all future outgoing connections:
    Edit the /etc/ssh/ssh_config or ~/.ssh/config file to add "UseRoaming no" under the "Host *" section.


VPN Magic
---------

* https://orth.uk/ssh-over-cloudflare/
* https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation
* https://github.com/cloudflare/cloudflared


WG/SSH Evil
-----------

* https://0xcc.re/2022/02/01/dangerous-toys-anything-to-ed25519-ssh-keys.html
* https://github.com/mikalv/anything2ed25519
* https://fly.io/blog/our-user-mode-wireguard-year/


SSH CA/Agent/Sudo/SSM
---------------------

# https://betterprogramming.pub/how-to-use-ssh-certificates-for-scalable-secure-and-more-transparent-server-access-720a87af6617
# https://gist.github.com/seanw2020/924c50e4c8428ad2d030db99cc819e20
# https://github.com/cloudtools/ssh-ca
# https://github.com/cloudtools/ssh-cert-authority
# https://github.com/lgxz/sshca
# https://ibug.io/blog/2019/12/manage-servers-with-ssh-ca/
# https://jameshfisher.com/2018/03/16/how-to-create-an-ssh-certificate-authority/
# https://thinkingeek.com/2020/06/06/using-ssh-certificates/
# https://www.lorier.net/docs/ssh-ca.html
* http://evans.io/legacy/posts/ssh-agent-for-sudo-authentication/
* http://unixwiz.net/techtips/ssh-agent-forwarding.html
* https://github.com/jbeverly/pam_ssh_agent_auth
* https://github.com/netflix/bless
* https://github.com/uber/pam-ussh  sudo after SSH
* https://graystum.com/aws-ssm-do-you-really-need-ssh/  AWS SSM
* https://hackernoon.com/ditch-your-ssh-keys-and-enable-aws-ssm-ec1c2b27350c
* https://smallstep.com/blog/use-ssh-certificates/
* https://www.hashicorp.com/blog/managing-ssh-access-at-scale-with-hashicorp-vault
* https://www.sweharris.org/post/2022-02-06-ssh-certs-again/
* https://www.toptal.com/aws/ssh-log-with-ssm
