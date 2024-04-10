# Notes from reading

git fetch: just pulls from a remote
git pull: pulls from a remote that you've set up a branch to track
tracking branches is the key differentiator

Discrete process:

- set up remote
- push branch up to remote or clone existing remote branch
- set your local branch to track remote branch (a tracking branch) using --set-upstream

Changing history: when rebase is ok

- we generally abide by the idea that a branch belongs to the person who publishes it and it may change

HEAD/index/working directory

- Last commit, staging area, current dir
- repo is a .git dir, working dir is unpacked version of the dir.
- > the other two trees store their content in an efficient but inconvenient manner, inside the .git folder. The working directory unpacks them into actual files

  7.7- reset demystified

- good explanation of the standard git edit/stage/commit process

clean working directory = no modified, unstaged files

git reset

- reset soft: moves HEAD and branch to commit, leaves index and working dir alone
  - so now any changes between the current commit and your previous state are staged in the index
- reset mixed: moves HEAD, branch, and index to commit, leaves working dir alone
  - any changes are now unstaged in the working dir
- reset hard: moves HEAD, branch, index, and working dir to commit
  - nukes any uncommited changes (ie, the working dir), so they'll be lost

# Outline

## What it does and why you should use it

## Foundational principles

- basic unit is the blob, created by staging/git add
- commit: a blob with ancestry and metadata
- branch: a reference to a specific commit lineage

## Normal behavior: branch, commit, merge

## Advanced: rebase, reset, recover

## GitHub: Cloud server + tools

## Common Questions/Issues
