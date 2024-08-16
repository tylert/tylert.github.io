Simple Stuff
------------

* https://stackoverflow.com/questions/44712874/how-do-i-run-a-container-from-the-command-line-in-kubernetes-like-docker-run/44712875#44712875
* https://gc-taylor.com/blog/2016/10/31/fire-up-an-interactive-bash-pod-within-a-kubernetes-cluster


Official OS Images
------------------

* https://github.com/debuerreotype/debuerreotype  Debian et al.
* https://github.com/debuerreotype/docker-debian-artifacts  Debian
* https://github.com/tianon/docker-brew-ubuntu-core  Ubuntu
* https://github.com/alpinelinux/docker-alpine  Alpine Linux
* https://partner-images.canonical.com/oci  Ubuntu root fs tarballs for containers "FROM scratch"
* https://cloud-images.ubuntu.com  OVA, VDI, IMG, etc.
* https://cloud-images.ubuntu.com/locator  AMIs, etc.
* https://hub.docker.com/_/debian  Voldemorthub Debian
* https://hub.docker.com/_/ubuntu  Voldemorthub Ubuntu
* https://hub.docker.com/_/alpine  Voldemorthub Alpine
* https://ubuntu.com/blog/craft-custom-chiselled-ubuntu-distroless
* https://github.com/canonical/chisel
* https://xenialinux.com  immutable Gentoo?
* https://grahamc.com/blog/erase-your-darlings  NixOS
* https://imil.net/blog/posts/2023/netbsd-as-a-docker-container
* https://gitlab.com/iMil/mksmolnb  containerized NetBSD microVMs (boot in under a second)
* https://www.talos.dev  Talos Linux (k8s OS)
* https://github.com/siderolabs/talos  Talos Linux

Typical OS container image "Dockerfile"::

    FROM scratch
    ADD ${DISTRO}-${ARCH}-rootfs.tar.gz
    CMD ["bash"]


Container Stuff
---------------

* https://iximiuz.com/en/posts/container-networking-is-simple
* https://www.kubernetes.dev/blog/2023/03/01/introducing-kwok
* https://containers.gitbook.io/build-containers-the-hard-way/#walk-through-pulling-an-image-with-bash
* https://github.com/google/go-containerregistry#tools
* https://github.com/ko-build/ko#ko-easy-go-containers
* https://github.com/containers/skopeo
* https://github.com/jpetazzo/registrish
* https://www.gnu.org/software/guix/blog/2018/tarballs-the-ultimate-container-image-format
* https://blog.yadutaf.fr/2016/04/14/docker-for-your-users-introducing-user-namespace
* https://42notes.wordpress.com/2015/05/13/replace-boot2docker-with-coreos-and-vagrant-to-use-docker-containers
* http://www.iron.io/blog/2016/01/microcontainers-tiny-portable-containers.html
* http://blog.xebia.com/2014/07/04/create-the-smallest-possible-docker-container
* http://prakhar.me/docker-curriculum
* http://stackoverflow.com/questions/18274088/how-can-i-make-my-own-base-image-for-docker
* http://sysadvent.blogspot.ca/2015/12/day-12-introduction-to-nomad.html
* http://www.aossama.com/build-debian-docker-image-from-scratch
* https://blog.docker.com/2013/06/create-light-weight-docker-containers-buildroot
* https://developer.atlassian.com/blog/2015/12/atlassian-docker-orchestration
* https://github.com/openshift-evangelists/openshift-workshops/blob/master/modules/run-as-non-root.adoc#switching-the-user
* https://docs.openshift.org/latest/creating_images/guidelines.html#use-uid
* http://www.projectatomic.io/docs/docker-image-author-guidance
* https://www.ctl.io/developers/blog/post/gracefully-stopping-docker-containers
* https://www.ctl.io/developers/blog/post/dockerfile-entrypoint-vs-cmd
* https://blog.feabhas.com/2017/10/introduction-docker-embedded-developers-part-2-building-images
* https://wiki.apache.org/httpd/NonRootPortBinding
* https://nickjanetakis.com/blog/best-practices-around-production-ready-web-apps-with-docker-compose
* https://erkanerol.github.io/post/how-kubectl-exec-works
* https://www.youtube.com/watch?v=g4PCTodIm80  Why I use Rancher (2021) - Fleet awesomeness
* https://www.hashicorp.com/resources/hashinetes-combining-kubernetes-hashicorp-kelsey-hightower  Hashinetes
* https://www.youtube.com/watch?v=_dn4c9j7LUo
* https://github.com/containerd/nerdctl
* https://marcusnoble.co.uk/2021-09-01-migrating-from-docker-to-podman
* https://itnext.io/goodbye-docker-desktop-hello-minikube-3649f2a1c469
* https://github.com/k8s-at-home/charts
* https://github.com/k8s-at-home/awesome-home-kubernetes
* https://billglover.me/2020/01/12/the-sidecar-pattern
* https://github.com/ramitsurana/awesome-kubernetes
* https://ramitsurana.github.io/awesome-kubernetes
* https://github.com/run-x/awesome-kubernetes
* https://awesome-kubernetes.com
* https://earthly.dev/blog/aws-lambda-docker
* https://github.com/cloudposse/charts/tree/master/incubator/monochart  monochart
* https://github.com/itscontained/charts/tree/master/itscontained/raw  rawchart
* https://itnext.io/3-reasons-to-choose-a-wide-cluster-over-multi-cluster-with-kubernetes-c923fecf4644
* https://iximiuz.com/en/posts/container-networking-is-simple
* https://www.youtube.com/watch?v=k58WnbKmjdA&feature=emb_logo
* https://nix.dev/tutorials/building-and-running-docker-images
* https://ianthehenry.com/posts/how-to-learn-nix
* https://github.com/tianon/gosu
* https://docs.gocd.org/current
* https://github.com/routernetes/routernetes  dedicated router with k8s???
* https://k8s.voltaicforge.com  PXE boot bare metal + install Talos, Sidero, K8s
* https://driftingin.space/posts/complexity-kubernetes
* https://github.com/containers/skopeo/blob/main/docs/skopeo-standalone-sign.1.md#notes
* https://www.ianlewis.org/en/container-runtimes-part-2-anatomy-low-level-contai
* https://blog.ttulka.com/building-container-images-without-dockerfile
* https://iximiuz.com/en/posts/container-learning-path
* https://cast.ai/blog/kubernetes-cordon-how-it-works-and-when-to-use-it
* https://determinate.systems/posts/nix-to-kubernetes
* https://httptoolkit.com/blog/docker-image-registry-facade
* https://github.com/kubernetes/git-sync
* https://dev.to/ivan/go-build-a-minimal-docker-image-in-just-three-steps-514i
* https://docs.docker.com/language/golang/build-images
* https://github.com/stakater/Reloader  helm helper???
* https://github.com/tinyzimmer/k3p  air-gapped packages for k3s
* https://github.com/loft-sh/kiosk  multi-tenant k8s?
* https://blog.alexellis.io/github-actions-timesharing-supercomputer
* https://blog.alexellis.io/fixing-the-ux-for-one-time-tasks-on-kubernetes
* https://github.com/alexellis/run-job
* https://github.com/alexellis/actions-batch
* https://github.com/defenseunicorns/zarf
* https://zarf.dev
* https://mirrord.dev  local container joined to remote cluster (dev loop)
* https://github.com/kubernetes-csi/csi-driver-smb
* https://olivermaerz.org/2021/11/26/deploy-a-samba-smb-fileserver-on-your-k3s-kubernetes-cluster
* https://openfunction.dev
* https://github.com/harvester/harvester  VMs launched from k8s?
* https://paulbutler.org/2024/the-haters-guide-to-kubernetes
* https://www.youtube.com/watch?v=6NeQa_1YXbI  "AWS Summit Ottawa 2022:  Security and compliance for container-based microservices"
* https://github.com/mercari/tortoise  HPA/VPA for k8s?
* https://qmacro.org/blog/posts/2024/05/13/using-arg-in-a-dockerfile-beware-the-gotcha


Load-Balancing
--------------

* https://metallb.org
* https://fabiolb.net  uses HashiCorp Consul
* https://www.loxilb.io  uses eBPF
* https://ebpf.io
* https://samwho.dev/load-balancing  visualization of different load-balancing strategies
