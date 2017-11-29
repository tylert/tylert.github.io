Remote Assistance Fu
--------------------

Add a new user::

    USER='stimpy'
    useradd --create-home --comment 'New User,,,,' ${USER}

Prepare ssh::

    mkdir --mode=0700 --parents ~/.ssh
    ssh-keygen -t rsa -b 8192 -C "${USER}@${HOSTNAME}" -N '' -f ~/.ssh/id_rsa
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
    echo "${USER} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/${USER}
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
