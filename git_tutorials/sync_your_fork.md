# Guide on how to sync your fork to the most updated version of the repository

Forks need to be syncronized periodically to the main repository they are forking. Otherwise they will get behind or ahead of the repository. This can lead to conflicts when trying to merge changes into the main repository.

This guide assumes you have already forked the main repository into your own copy and installed Git.

## Steps
### 1. Open up Git Bash on your PC
Search for "git bash" in your windows search bar

![](git_tutorials/sync_fork_imgs/search_program.png)

Git Bash looks like this 

![](git_tutorials/sync_fork_imgs/git_bash.png)

### 2. use the CD command to cd into your cloned directory
![](git_tutorials/sync_fork_imgs/cd_directory.png)
### 3. Add the remote repository as an upstream
You need to get the .git link to the repository. In this case it will look like https://github.com/njcssa/njcssa-python-practice-probs.git

Now enter the following command when you are in the forked directory
![](git_tutorials/sync_fork_imgs/addupstream.png)

### 4. Verify the new upstream repository you've specified for your fork.
![](git_tutorials/sync_fork_imgs/check_remote.png)

### 5. Fetch the remote repository
![](git_tutorials/sync_fork_imgs/fetch_upstream.png)
### 6. Checkout master branch
![](git_tutorials/sync_fork_imgs/checkout_master.png)
### 7. Merge the upstream branch from main repository into your master branch
There should not be a merge conflict because people should be working on separate parts. If there is a merge conflict dm Ben C. so he can sort it out.

![](git_tutorials/sync_fork_imgs/merge_upstream.png)
### 8. push new commits to master branch of your forked version
![](git_tutorials/sync_fork_imgs/push_origin.png)

You should now be up to date with the main repository!
