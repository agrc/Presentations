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
  - nukes any uncommitted changes (ie, the working dir), so they'll be lost

# Outline

## What it does and why you should use it

- Edit history with so much more
  - Baking a cake analogy
- Undo (almost) anything
- Always have a known-good copy
- Work together with others
- Share your code easily

## Foundational principles

- What is a git repository?
  - A collection of snapshots of your files over time referenced by self-defined, human-readable names
- The basic units of git
  - blob: a compressed, machine-friendly version of each file
  - tree: a directory structure of blobs
  - commit: a tree of blobs with ancestry and metadata, including a user-provided message
    - now you know what your directory looked like just before you changed things
  - branch: a reference to a specific commit lineage
- Hashes and immutability
  - Blobs, trees, and commits are all identified by a SHA-1 hash, a long string that is the result of a mathematical operation on the data, author & committer info, time, etc
  - any difference in any of the inputs will create a unique hash
  - You can't alter an existing commit- any changes will create a new commit with a different hash
- The three (ok, four) storage areas
  - repo: collection of all the blobs, commits, branches, tags, everything, stored in compressed, machine-friendly files
  - HEAD: your last commit on the currently checked out branch
  - Index/Staging area: your proposed next commit as one or more blobs
  - Working Directory/working tree: sandbox, the current branch checked out as normal files along with any edits you may have made
    - no edits = clean working tree
- The same file can exist in all three areas with different content
  - HEAD: All your previous work
  - Index: Changes you've just made and staged for future inclusion into the branch
  - Working directory: The changes you're working on now that aren't finalized
- It's really, really hard to completely screw up committed data
  - Once a commit is made, it usually stays for a while unless you intentionally destroy it
  - It may be a little difficult to find it in the history, but it's there
  - Most processes have an abort or undo process that returns HEAD, the index, and/or the working tree back to a previously working state

## Normal process: branch, stage, commit, merge

- Start with working on just the main branch
  - Do some work in the working tree, stage it to the index, then commit it to the branch
- git log
  - Watch the branch reference move along the commit history
- Branching
  - Branches are cheap- don't be nervous about using them
  - Just a reference to a specific commit in a lineage
  - Create and checkout a new branch from main
  - Do your work, stage & commit
  - If you're happy with it, merge it back
  - If you don't like it, checkout main and discard the other branch- the commits are no longer part of any lineage and so don't appear anywhere, but will hang around for a while
    - Show reflog commits in git graph
- Merging
  - Creating a new commit with new parents and updating your branch to point to it
  - If the lineage doesn't split anywhere, it doesn't add a new commit, just moves the branch to the latest commit
  - If the lineage does split, it tries to combine all the files. If this works, everything is fine.
  - If there are conflicts and it doesn't know which version to use, it adds both and wraps the conflicting areas in conflict-resolution markers markers
    - You get to go in and choose which to use
    - You can always bail out at anytime and return to a known-good state

## GitHub: Cloud server + tools

- Git is a distributed vcs
  - Each clone of the repo has all the history (all the objects) of the repo. If the source repo were to disappear, the clone could immediately take its place
- remotes are links to other repositories (usually networked/internet, though could be local) that the local repo should mirror
  - local branches can be set to track branches on a remote for both reading and writing changes
  - fetch pulls down the commits from a tracked remote branch that don't appear in the local branch
  - you can then merge these commits into the local branch, effectively synchronizing them
    - Usually a fast-forward merge
  - git pull does the fetch and merge in one step
- GitHub is a remote git server combined with lots of collaboration tools
  - Issues
  - Pull Requests
  - Discussion boards
  - etc
- GitHub development model
  - Create repo on GitHub with a default main branch
  - Clone the repo locally
  - create a new local branch and commit there
  - Push your local branch to GitHub
  - open a Pull Request to merge your new branch into main on GitHub
  - After merging the branches in GitHub, checkout your local main branch and pull updates
  - delete the working branch both locally and on GitHub
- Pull Requests
  - Tools for getting a second set of eyes on the code
  - Gives the repo owner an avenue to review and verify incoming changes
- Issues
  - A way to track bugs, requests, or enhancement ideas
  - References issues in commit messages
- GitHub Forks
  - You clone another GitHub repo into your own GitHub space so that it is tracking the original
  - You then clone your fork locally, commit changes, and push back to your GitHub repo
  - You can then open a pull request in the original GitHub repo against a branch in your GitHub repo

## Advanced: rebase, reset, recover

- Rebase: rewriting history to keep things in line
  - takes all the commits from where the current branch leaves the other branch, creates diffs, and applies them as new commits on the other branch
  - keeps the history linear
  - Doesn't move commits- the old commits are left as dangling commits
  - Conflicts show up as merge conflicts at each commit stage, so you may have to choose the same resolution multiple times if you don't apply your desired changes at the right commit
- Rebase and merge
  - Take your incoming branch, rebase it on the end of main, then checkout main and merge the branch back in as a fast-forward merge
  - Common GitHub operation
- Cherry pick: give me one commit from somewhere
  - grabs the diff between that commit and HEAD and tries to create a new commit using that diff
- Reset: changing the commit HEAD and your current branch point to
  - soft: leaves both working dir and index the same. The state of your repo before the reset is now staged and ready to be committed
  - mixed: just leaves working dir the same. The state of your repo before the reset is now an uncommitted change
  - hard: HEAD, index, and working dir are moved to the new commit. Previous state of the repo is completely removed: any commits are left dangling, and any uncommitted work is lost
- When to use which reset?
  - I want to completely abandon my current line of work and pretend it never happened
    - hard
    - (or really just checkout a new branch at the last point you want to continue from)
  - I don't have any work in progress or anything I want to keep, I just want to point my branch at a different commit
    - hard
  - I did a commit but I want to go back and change something about my edits without adding an extra commit in the repo tree
    - mixed
  - I did a commit but I want to go back and make and stage more edits in addition to my original edits or change the commit message
    - soft
    - also git commit --amend for just the last commit

## Common Questions/Issues
