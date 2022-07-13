Git Stuff
---------

* https://drewdevault.com/2020/04/06/My-weird-branchless-git-workflow.html
* https://jg.gg/2018/09/29/stacked-diffs-versus-pull-requests/
* https://github.com/newren/git-filter-repo/  replacement for git-filter-branch below
* https://htmlpreview.github.io/?https://github.com/newren/git-filter-repo/blob/docs/html/git-filter-repo.html
* https://bneijt.nl/blog/merge-a-subdirectory-of-another-repository-with-git/
* https://gist.github.com/lisawolderiksen/a7b99d94c92c6671181611be1641c733

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
