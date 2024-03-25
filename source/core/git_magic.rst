Git Stuff
---------

* https://myme.no/posts/2023-01-22-git-commands-you-do-not-need.html
* https://drewdevault.com/2020/04/06/My-weird-branchless-git-workflow.html
* https://jg.gg/2018/09/29/stacked-diffs-versus-pull-requests
* https://github.com/newren/git-filter-repo  replacement for git-filter-branch below
* https://htmlpreview.github.io/?https://github.com/newren/git-filter-repo/blob/docs/html/git-filter-repo.html
* https://bneijt.nl/blog/merge-a-subdirectory-of-another-repository-with-git
* https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733
* https://verdantfox.com/blog/view/how-to-use-git-pre-commit-hooks-the-hard-way-and-the-easy-way
* https://github.com/git-big-picture/git-big-picture  Graphviz sub-graphs of git commit history

Use the new tooling for rewriting history::

    # Force an entire repo root to look like it was always under a subdirectory
    git filter-repo --to-subdirectory-filter my-module/

Fetch a single file::

    git archive \
        --format=tar \
        --output=foo.tar.gz \
        --remote=ssh://git@blablabla/blablabla.git ${BRANCH} \
        things_to_archive

    git archive \
        --format=tar \
        --output=foo.tar.gz \
        --remote=${LOCAL_REPO} ${BRANCH} \
        things_to_archive

    git archive \
        --format=tar \
        --output=foo.tar.gz \
        --remote=foo master \
        "**/requirements*" "requirements*"

Deprecated instructions???::

    # Snip out just a single directory
    git clone foo
    cd foo
    git remote rm origin
    git filter-branch --subdirectory-filter arf --prune-empty -- --all


    # Get rid of files permanently
    for i in foo.svg bar.svg ; do
        git filter-branch --index-filter "git rm -rf --cached --ignore-unmatch $i" --tag-name-filter cat --prune-empty --force -- --all --branches --tags
    done


    # Fix the size of the repository by losing unreferenced things
    git reflog expire --expire=now --all
    git fsck --full --unreachable
    git gc --prune=now --aggressive

    rm -rf .git/refs/original/ .git/refs/remotes/ .git/*_HEAD .git/logs/
    git reflog expire --expire-unreachable=now --all
    git repack -q -A -d
    git gc --aggressive --prune=now

    rm -rf .git/refs/original/*
    git reflog expire --all --expire-unreachable=0
    git repack -A -d
    git prune


    # Fix author/committer user.name/user.email for old commits
    git filter-branch --env-filter 'GIT_AUTHOR_NAME="Tyler Tidman" ; GIT_COMMITTER_NAME="Tyler Tidman"' -f -- --all
    git filter-branch --env-filter 'GIT_AUTHOR_EMAIL="tyler.tidman@draak.ca" ; GIT_COMMITTER_EMAIL="tyler.tidman@draak.ca"' -f -- --all
    git show-ref
    # Delete any refs that have the name "original"
    git update-ref -d refs/original/refs/heads/master


    # Cull a single directory
    git filter-branch --tree-filter 'rm -rf radio/logos/ares' -f HEAD
    git filter-branch --prune-empty -f HEAD


    # Stitch two repos together
    cd Adir
    mkdir Bdir
    git remote add -f Bproject /path/to/Brepo
    git merge --allow-unrelated-histories -s ours --no-commit Bproject/master
    git read-tree --prefix=Bdir -u Bproject/master
    git commit -m "Merge B project as our subdirectory"
    git pull -s subtree Bproject master


    # Rewrite an older commit
    git rebase --interactive deadbeef^
    # edit stuff
    git commit --all --amend --no-edit
    git rebase --continue


Workflow Stuff
--------------

* http://rogerdudler.github.io/git-guide
* http://www.catb.org/~esr/faqs/smart-questions.html
* https://12factor.net
* https://baatz.io/2015/how-many-git-repos
* https://barro.github.io/2016/02/a-succesful-git-branching-model-considered-harmful
* https://benjamincongdon.me/blog/2022/07/17/In-Praise-of-Stacked-PRs
* https://blog.carbonfive.com/always-squash-and-rebase-your-git-commits
* https://blog.danlew.net/2020/11/11/trello-androids-git-branching-strategy
* https://blog.sulami.xyz/posts/cleaning-up-git-history
* https://cbea.ms/git-commit
* https://cerfacs.fr/coop/coop-cactus-model
* https://coderwall.com/p/7aymfa/please-oh-please-use-git-pull-rebase
* https://davidwalsh.name/squash-commits-git
* https://docs.cloudposse.com
* https://docs.microsoft.com/en-us/archive/msdn-magazine/2013/april/alm-rangers-a-treasure-hunt-through-alm-readiness
* https://docs.microsoft.com/en-us/azure/architecture/patterns/sthttps://12factor.net/rangler
* https://engineering.shopify.com/blogs/engineering/refactoring-legacy-code-strangler-fig-pattern
* https://gitbetter.substack.com/p/how-to-squash-git-commits
* https://github.com/arxanas/git-branchless
* https://github.com/erlang/otp/wiki/writing-good-commit-messages
* https://github.com/naltun/ugit
* https://gitolite.com/git-pull--rebase
* https://infrastructure-as-code.com/book/2021/11/19/snowflakes-as-code.html
* https://leoneperdigao.medium.com/pull-request-best-practices-fa20f7daeb3c
* https://leosiddle.com/posts/2020/07/git-config-pull-rebase-autostash
* https://lethain.com/trunk-and-branches
* https://lukemerrett.com/different-merge-types-in-git
* https://makandracards.com/makandra/527-squash-several-git-commits-into-a-single-commit
* https://martinfowler.com/articles/ship-show-ask.html
* https://martinfowler.com/bliki/BranchByAbstraction.html
* https://martinfowler.com/bliki/StranglerFigApplication.html
* https://mechanicalrock.github.io/2019/07/01/continuous-deployment-the-first-step-on-the-road-to-recovery.html
* https://mechanicalrock.github.io/2020/05/04/strangler-pattern.html
* https://mechanicalrock.github.io/2020/10/06/manual-gates-git-flow-in-a-wig.html
* https://medium.com/better-programming/why-and-how-to-squash-git-commits-b508b3b0dba
* https://mtlynch.io/code-review-love
* https://ourmachinery.com/post/step-by-step-programming-incrementally
* https://paulhammant.com/2013/04/05/what-is-trunk-based-development
* https://semver.org
* https://squeaky.ai/blog/development/why-we-dont-use-a-staging-environment
* https://stokoe.me/summary-hammock-driven-development
* https://trunkbaseddevelopment.com/#scaled-trunk-based-development
* https://vsardata.blob.core.windows.net/projects/TFS%20Version%20Control%20Part%201%20-%20Branching%20Strategies.pdf
* https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development
* https://www.atlassian.com/git/tutorials/merging-vs-rebasing#the-golden-rule-of-rebasing
* https://www.cmcrossroads.com/article/pros-and-cons-four-kinds-code-reviews
* https://www.endoflineblog.com/gitflow-considered-harmful
* https://www.endoflineblog.com/oneflow-a-git-branching-model-and-workflow
* https://www.gitops.tech
* https://www.leshenko.net/p/ugit
* https://www.nomachetejuggling.com/2017/04/09/a-different-branching-strategy
* https://www.nomachetejuggling.com/2017/04/09/a-different-branching-strategy/#toc-use-feature-toggles
* https://xkcd.com/1296


Internals
---------

* https://mediocregopher.com/posts/git-proxy


Other
-----

* https://app.radicle.xyz/nodes/seed.radicle.garden/rad:z3gqcJUoA1n9HaHKufZs5FCSGazv5  another protocol?
