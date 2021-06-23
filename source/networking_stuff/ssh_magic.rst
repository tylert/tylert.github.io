Vagrant Test VM
---------------

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
