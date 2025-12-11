# Simple Stuff

* <https://stackoverflow.com/questions/44712874/how-do-i-run-a-container-from-the-command-line-in-kubernetes-like-docker-run/44712875#44712875>
* <https://gc-taylor.com/blog/2016/10/31/fire-up-an-interactive-bash-pod-within-a-kubernetes-cluster>
* <https://blog.radwell.codes/2022/07/single-node-kubernetes-cluster-via-kubeadm-on-ubuntu-22-04>
* <https://github.com/mr-karan/homelab> single-node Nomad with Consul
* <https://medium.com/@senthilrch/woot-kubernetes-adds-support-for-swap-memory-92541aad01a0>
* <https://talos.dev/latest/introduction/quickstart>
* <https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/#ephemeral-container>
* <https://stencel.io/posts/build-cheapest-kubernetes-i7-cluster.html>
* <https://reclaim-the-stack.com>
* <https://shadybraden.com/articles/gitopshomelab> k8s-less homelab
* <https://linuxcontainers.org/incus/docs/main> VMM and container host all-in-one?
* <https://komo.do>


# Swap

* <https://kubernetes.io/blog/2023/08/24/swap-linux-beta>
* <https://github.com/misko/bigmaac>


# Container Hosts

* <https://uncloud.run> distributed homelab fun?


# Official OS Images

* <https://github.com/debuerreotype/debuerreotype> Debian et al.
* <https://github.com/debuerreotype/docker-debian-artifacts> Debian
* <https://github.com/tianon/docker-brew-ubuntu-core> Ubuntu
* <https://github.com/alpinelinux/docker-alpine> Alpine Linux
* <https://partner-images.canonical.com/oci> Ubuntu root fs tarballs for containers 'FROM scratch'
* <https://cloud-images.ubuntu.com> OVA, VDI, IMG, etc.
* <https://cloud-images.ubuntu.com/locator> AMIs, etc.
* <https://hub.docker.com/_/debian> Voldemorthub Debian
* <https://hub.docker.com/_/ubuntu> Voldemorthub Ubuntu
* <https://hub.docker.com/_/alpine> Voldemorthub Alpine
* <https://ubuntu.com/blog/craft-custom-chiselled-ubuntu-distroless>
* <https://github.com/canonical/chisel>
* <https://xenialinux.com> immutable Gentoo?
* <https://grahamc.com/blog/erase-your-darlings> NixOS
* <https://imil.net/blog/posts/2023/netbsd-as-a-docker-container>
* <https://gitlab.com/iMil/mksmolnb> containerized NetBSD microVMs (boot in under a second)
* <https://talos.dev> Talos Linux (k8s OS)
* <https://github.com/siderolabs/talos> Talos Linux
* <https://sean.thrailkill.cloud/posts/you-need-to-know-about-bootc>
* <https://iximiuz.com/en/posts/iximiuz-labs-story> building a Firecracker-powered platform for containers

Typical OS container image 'Dockerfile':

    FROM scratch
    ADD ${DISTRO}-${ARCH}-rootfs.tar.gz
    CMD ["bash"]


# Container Stuff

* <https://iximiuz.com/en/posts/container-networking-is-simple>
* <https://kubernetes.dev/blog/2023/03/01/introducing-kwok>
* <https://containers.gitbook.io/build-containers-the-hard-way/#walk-through-pulling-an-image-with-bash>
* <https://github.com/google/go-containerregistry#tools>
* <https://github.com/ko-build/ko#ko-easy-go-containers>
* <https://github.com/containers/skopeo>
* <https://github.com/jpetazzo/registrish>
* <https://gnu.org/software/guix/blog/2018/tarballs-the-ultimate-container-image-format>
* <https://blog.yadutaf.fr/2016/04/14/docker-for-your-users-introducing-user-namespace>
* <https://42notes.wordpress.com/2015/05/13/replace-boot2docker-with-coreos-and-vagrant-to-use-docker-containers>
* <https://blog.xebia.com/2014/07/04/create-the-smallest-possible-docker-container>
* <https://docker-curriculum.com>
* <https://sysadvent.blogspot.ca/2015/12/day-12-introduction-to-nomad.html>
* <https://blog.docker.com/2013/06/create-light-weight-docker-containers-buildroot>
* <https://developer.atlassian.com/blog/2015/12/atlassian-docker-orchestration>
* <https://github.com/openshift-evangelists/openshift-workshops/blob/master/modules/run-as-non-root.adoc#switching-the-user>
* <https://docs.openshift.org/latest/creating_images/guidelines.html#use-uid>
* <https://projectatomic.io/docs/docker-image-author-guidance>
* <https://ctl.io/developers/blog/post/gracefully-stopping-docker-containers>
* <https://ctl.io/developers/blog/post/dockerfile-entrypoint-vs-cmd>
* <https://blog.feabhas.com/2017/10/introduction-docker-embedded-developers-part-2-building-images>
* <https://wiki.apache.org/httpd/NonRootPortBinding>
* <https://nickjanetakis.com/blog/best-practices-around-production-ready-web-apps-with-docker-compose>
* <https://erkanerol.github.io/post/how-kubectl-exec-works>
* <https://youtube.com/watch?v=g4PCTodIm80> Why I use Rancher (2021) - Fleet awesomeness
* <https://hashicorp.com/resources/hashinetes-combining-kubernetes-hashicorp-kelsey-hightower> Hashinetes
* <https://youtube.com/watch?v=_dn4c9j7LUo>
* <https://github.com/containerd/nerdctl>
* <https://marcusnoble.co.uk/2021-09-01-migrating-from-docker-to-podman>
* <https://itnext.io/goodbye-docker-desktop-hello-minikube-3649f2a1c469>
* <https://github.com/k8s-at-home/charts>
* <https://github.com/k8s-at-home/awesome-home-kubernetes>
* <https://billglover.me/2020/01/12/the-sidecar-pattern>
* <https://github.com/ramitsurana/awesome-kubernetes>
* <https://ramitsurana.github.io/awesome-kubernetes>
* <https://github.com/run-x/awesome-kubernetes>
* <https://awesome-kubernetes.com>
* <https://earthly.dev/blog/aws-lambda-docker>
* <https://github.com/cloudposse/charts/tree/master/incubator/monochart> monochart
* <https://github.com/itscontained/charts/tree/master/itscontained/raw> rawchart
* <https://itnext.io/3-reasons-to-choose-a-wide-cluster-over-multi-cluster-with-kubernetes-c923fecf4644>
* <https://iximiuz.com/en/posts/container-networking-is-simple>
* <https://youtube.com/watch?v=k58WnbKmjdA&feature=emb_logo>
* <https://nix.dev/tutorials/building-and-running-docker-images>
* <https://ianthehenry.com/posts/how-to-learn-nix>
* <https://github.com/tianon/gosu>
* <https://docs.gocd.org/current>
* <https://github.com/routernetes/routernetes> dedicated router with k8s???
* <https://k8s.voltaicforge.com> PXE boot bare metal + install Talos, Sidero, K8s
* <https://driftingin.space/posts/complexity-kubernetes>
* <https://github.com/containers/skopeo/blob/main/docs/skopeo-standalone-sign.1.md#notes>
* <https://ianlewis.org/en/container-runtimes-part-2-anatomy-low-level-contai>
* <https://blog.ttulka.com/building-container-images-without-dockerfile>
* <https://iximiuz.com/en/posts/container-learning-path>
* <https://cast.ai/blog/kubernetes-cordon-how-it-works-and-when-to-use-it>
* <https://determinate.systems/posts/nix-to-kubernetes>
* <https://httptoolkit.com/blog/docker-image-registry-facade>
* <https://github.com/kubernetes/git-sync>
* <https://dev.to/ivan/go-build-a-minimal-docker-image-in-just-three-steps-514i>
* <https://docs.docker.com/language/golang/build-images>
* <https://github.com/stakater/Reloader> helm helper???
* <https://github.com/tinyzimmer/k3p> air-gapped packages for k3s
* <https://github.com/loft-sh/kiosk> multi-tenant k8s?
* <https://blog.alexellis.io/github-actions-timesharing-supercomputer>
* <https://blog.alexellis.io/fixing-the-ux-for-one-time-tasks-on-kubernetes>
* <https://github.com/alexellis/run-job>
* <https://github.com/alexellis/actions-batch>
* <https://github.com/defenseunicorns/zarf>
* <https://zarf.dev>
* <https://mirrord.dev> local container joined to remote cluster (dev loop)
* <https://github.com/kubernetes-csi/csi-driver-smb>
* <https://olivermaerz.org/2021/11/26/deploy-a-samba-smb-fileserver-on-your-k3s-kubernetes-cluster>
* <https://openfunction.dev>
* <https://github.com/harvester/harvester> VMs launched from k8s?
* <https://paulbutler.org/2024/the-haters-guide-to-kubernetes>
* <https://youtube.com/watch?v=6NeQa_1YXbI> \"AWS Summit Ottawa 2022: Security and compliance for container-based microservices\"
* <https://github.com/mercari/tortoise> HPA/VPA for k8s?
* <https://qmacro.org/blog/posts/2024/05/13/using-arg-in-a-dockerfile-beware-the-gotcha>
* <https://kops.sigs.k8s.io> HA k8s clusters in AWS, GCP, OpenStack, etc.
* <https://github.com/nyrahul/wisecow> puzzle for newbies
* <https://kardinal.dev>
* <https://abhisman.notion.site/Understanding-ReplicaSet-vs-StatefulSet-vs-DaemonSet-vs-Deployments-a521f9a46ea446219d98be4972f2e16e>
* <https://dagger.io/blog/dagger-shell>
* <https://docs.dagger.io/install>
* <https://github.com/rzane/docker2exe> turn a docker container into an executable (that still requires docker)
* <https://raymii.org/s/tutorials/High_Available_Mosquitto_MQTT_Broker_on_Kubernetes.html> all that for one service
* <https://matduggan.com/what-would-a-kubernetes-2-0-look-like>
* <https://github.com/k3s-io/kine> sqlite instead of etcd
* <https://github.com/melezhik/Sparrow6/blob/master/posts/Application%20Less%20Containers.md> application-less (empty) containers to run on k8s???
* <https://howtogeek.com/i-run-a-full-linux-desktop-in-docker-just-because-i-can>
* <https://nowsci.com/webbian> Debian desktop in a container accessible from a web browser
* <https://bottlefire.dev> container images to microVMs
* <https://ko.build>


# Networking

* <https://friendshipcastle.zip/blog/glaceon> wireguard-go in k8s
* <https://github.com/Twi/glaceon>
* <https://github.com/Twi/glaceon-operator>
* <https://github.com/subtrace/subtrace> Wireshark-like functionality for containers
* <https://github.com/sanspareilsmyn/kforward> CLI tool for working with services in K8s


# Load-Balancing

* <https://metallb.org>
* <https://fabiolb.net> uses HashiCorp Consul
* <https://loxilb.io> uses eBPF
* <https://ebpf.io>
* <https://samwho.dev/load-balancing> visualization of different load-balancing strategies


# Experiments

Installing stuff:

    $ go install sigs.k8s.io/kind@latest
    # You'll also need kubectl and nerdctl/containerd

Creating cluster:

    $ KIND_EXPERIMENTAL_PROVIDER=nerdctl kind create cluster --name moo
    using nerdctl due to KIND_EXPERIMENTAL_PROVIDER
    Creating cluster "moo" ...
     ✓ Ensuring node image (kindest/node:v1.31.0) 🖼
     ✓ Preparing nodes 📦
     ✓ Writing configuration 📜
     ✓ Starting control-plane 🕹️
     ✓ Installing CNI 🔌
     ✓ Installing StorageClass 💾
    Set kubectl context to "kind-moo"
    You can now use your cluster with:

    kubectl cluster-info --context kind-moo

    Not sure what to do next? 😅  Check out https://kind.sigs.k8s.io/docs/user/quick-start/
    $ kubectl cluster-info --context kind-moo
    Kubernetes control plane is running at https://127.0.0.1:51361
    CoreDNS is running at https://127.0.0.1:51361/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

    To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
    $ kubectl config get-contexts
    CURRENT   NAME       CLUSTER    AUTHINFO   NAMESPACE
    *         kind-moo   kind-moo   kind-moo

Check container status:

    $ nerdctl namespace ls
    NAME                          CONTAINERS    IMAGES    VOLUMES    LABELS
    buildkit                      0             0         0
    buildkit_history              0             0         0
    default                       1             3         2
    rancher-desktop-extensions    0             1         0
    $ nerdctl --namespace default images --all
    REPOSITORY      TAG        IMAGE ID        CREATED           PLATFORM          SIZE          BLOB SIZE
    kindest/node    <none>     53df588e0408    27 minutes ago    linux/arm64       1010.1 MiB    391.2 MiB
    alpine          edge       b93f4f6834d5    3 months ago      linux/arm64/v8    9.0 MiB       3.9 MiB
    busybox         latest     9ae97d36d265    7 months ago      linux/arm64/v8    4.0 MiB       1.8 MiB
    $ nerdctl --namespace rancher-desktop-extensions images --all
    REPOSITORY                                           TAG       IMAGE ID        CREATED         PLATFORM       SIZE       BLOB SIZE
    ghcr.io/rancher-sandbox/rancher-desktop/rdx-proxy    latest    0899e99ad320    7 months ago    linux/arm64    4.9 MiB    4.9 MiB
    $ nerdctl --namespace default ps --all
    CONTAINER ID    IMAGE                                                                                             COMMAND                   CREATED           STATUS    PORTS                        NAMES
    0987d63e1569    docker.io/kindest/node@sha256:53df588e04085fd41ae12de0c3fe4c72f7013bba32a20e7325357a1ac94ba865    "/usr/local/bin/entr…"    10 minutes ago    Up        127.0.0.1:51361->6443/tcp    moo-control-plane
    $ KIND_EXPERIMENTAL_PROVIDER=nerdctl kind get clusters
    using nerdctl due to KIND_EXPERIMENTAL_PROVIDER
    moo

Basic operations:

    $ kubectl get namespaces
    NAME                 STATUS   AGE
    default              Active   38m
    kube-node-lease      Active   38m
    kube-public          Active   38m
    kube-system          Active   38m
    local-path-storage   Active   38m
    $ kubectl get nodes
    NAME                STATUS   ROLES           AGE   VERSION
    moo-control-plane   Ready    control-plane   39m   v1.31.0

Deleting cluster:

    $ KIND_EXPERIMENTAL_PROVIDER=nerdctl kind delete cluster --name moo
    using nerdctl due to KIND_EXPERIMENTAL_PROVIDER
    Deleting cluster "moo" ...
    Deleted nodes: ["moo-control-plane"]
    $ nerdctl namespace ls
    NAME                          CONTAINERS    IMAGES    VOLUMES    LABELS
    buildkit                      0             0         0
    buildkit_history              0             0         0
    default                       0             3         1
    rancher-desktop-extensions    0             1         0

* <https://github.com/lisenet/kubernetes-homelab>
* <https://iamsafts.com/posts/homelab-intro>
* <https://github.com/doitintl/kube-no-trouble>
* <https://blog.yaakov.online/replacing-kubernetes-with-systemd>
* <https://developertips.substack.com/p/how-to-create-and-manage-a-service>
* <https://codelucky.com/runit-linux-init-service-supervision> the complete guide to runit service supervision


# Linux From Scratch

* <https://landley.net/aboriginal/about.html>
* <https://serversfor.dev/linux-inside-out/the-linux-kernel-is-just-a-program>
