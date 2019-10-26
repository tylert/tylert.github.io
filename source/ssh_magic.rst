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
