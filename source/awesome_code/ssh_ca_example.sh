#!/usr/bin/env bash

hosts='
'

users='
'


gen_ssh_keypair() {
    local comment="${1}"
    local private_key_filename="${2}"

    if [ -z "${comment}" ]; then
        echo "Undefined comment"
        return 1
    fi

    if [ -z "${private_key_filename}" ]; then
        echo "Undefined private key filename"
        return 2
    fi

    ssh-keygen                       \
        -C "${comment}"              \
        -N ''                        \
        -a 2147483647                \
        -f "${private_key_filename}" \
        -t ed25519

    # -C, comment
    # -N, symmetric passphrase
    # -a, rounds for key derivation function (max value 2^31-1)
    # -f, private key filename (append .pub to this for public key filename)
    # -t, key type (-b bitsize option ignored for this key type)
}


sign_ssh_pubkey() {
    local type="${1}"
    local identity="${2}"
    local principals="${3}"
    local key_to_sign="${4}"
    local signing_key="${5}"

    if [ -z "${type}" ]; then
        echo "Undefined type"
        return 1
    fi

    if [ -z "${identity}" ]; then
        echo "Undefined identity"
        return 2
    fi

    if [ -z "${principals}" ]; then
        echo "Undefined principals"
        return 3
    fi

    if [ -z "${key_to_sign}" ]; then
        echo "Undefined key to sign"
        return 4
    fi

    if [ -z "${signing_key}" ]; then
        echo "Undefined signing key"
        return 5
    fi

    if [ "host" == "${type}" ]; then
        ssh-keygen              \
            -I "${identity}"    \
            -V "-5m:+403d"      \
            -h                  \
            -n "${principals}"  \
            -s "${signing_key}" \
            -z 1                \
            "${key_to_sign}"
    elif [ "user" == "${type}" ]; then
        ssh-keygen              \
            -I "${identity}"    \
            -V "-5m:+403d"      \
            -n "${principals}"  \
            -s "${signing_key}" \
            -z 1                \
            "${key_to_sign}"
    else
        echo "Undefined type"
    fi

    # -I, identity
    # -V, validity interval (5 minutes ago to 1*Y+M+W+D from now)
    # -h, create a host certificate instead of a user certificate
    # -n, principals
    # -s, signing private key
    # -z, serial number
    # public key file to sign
}


main() {
    gen_ssh_keypair "hostca" "hostca"
    gen_ssh_keypair "userca" "userca"

    for host in ${hosts}; do
        gen_ssh_keypair "root@${host}" "host_${host}"
        sign_ssh_pubkey "host" "${host}" "${host}" "host_${host}" "hostca"
    done

    for user in ${users}; do
        gen_ssh_keypair "${user}" "user_${user}"
        sign_ssh_pubkey "user" "${user}" "${user}" "user_${user}" "userca"
    done
}


main


# For hosts, add to /etc/ssh/sshd_config on each host:
#   HostCertificate /etc/ssh/new_host_key-cert.pub
#   (uncomment HostKey /etc/ssh/new_host_key.pub)
# Add to ~/.ssh/known_hosts:
#   @cert-authority * $(cat hostsca.pub)

# For users,...


# https://betterprogramming.pub/how-to-use-ssh-certificates-for-scalable-secure-and-more-transparent-server-access-720a87af6617
# https://gist.github.com/seanw2020/924c50e4c8428ad2d030db99cc819e20
# https://github.com/cloudtools/ssh-ca
# https://github.com/cloudtools/ssh-cert-authority
# https://github.com/lgxz/sshca
# https://ibug.io/blog/2019/12/manage-servers-with-ssh-ca/
# https://jameshfisher.com/2018/03/16/how-to-create-an-ssh-certificate-authority/
# https://smallstep.com/blog/use-ssh-certificates/
# https://thinkingeek.com/2020/06/06/using-ssh-certificates/
# https://www.lorier.net/docs/ssh-ca.html
