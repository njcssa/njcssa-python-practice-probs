# Here's a full tutorial on how to start editing the code in the njcssa practice problems repository:
-By Chris Gu

## Starting out:
1. Download git & install from here: https://git-scm.com/downloads. Also, make sure you have a python supported IDE. We <b>strongly</b> recommend you get [Visual Studio Code](https://code.visualstudio.com/), as you can have extensions, a great GUI, and easy to push, pull, and commit changes.
<br /><br />
 2. Now, you will need to fork the repository. Basically this means you will make you're own copy of the code in its most updated state. To do this, go here: https://github.com/njcssa/njcssa-python-practice-probs and click the fork button on the top right: 

    <img src="https://github.com/njcssa/njcssa-python-practice-probs/blob/master/git_tutorials/creating_fork_imgs/fork.PNG" width="200" height="50" />.

    Fork it into your own account. Now, if you go to "Your Repositories", you should see your new copy of the final draft which is 👍👍:

    <img src="https://github.com/njcssa/njcssa-python-practice-probs/blob/master/git_tutorials/creating_fork_imgs/Repositories.PNG" width="800" height="300" />
<br />

3. Next, we're gonna clone the newly created repository. To do that in command prompt, cd to the directory you want to clone or download the copy to (so we can edit it). In the example below, I want my files to be in my desktop, so I cd to "C:\Users\gammi\Desktop" In this case, my user name is <i>"gammi"</i>. Make sure to use your user name if you want to do so:

    <img src="https://github.com/njcssa/njcssa-python-practice-probs/blob/master/git_tutorials/creating_fork_imgs/cmd1.PNG" width="650" height="300" />
<br />

4. Once you've figured out where you want to clone your repository, go back to github.com, click on that "njcssa-python-practice-probs" that was seen in step 2, click the bright green "Clone or Download" button, and then copy that URL. It should be "https://github/*yourname*/njcssa-python-practice-probs" In this case, mine is: https://github.com/njcssa/njcssa-python-practice-probs.git since njcssa is my username.

    <img src="https://github.com/njcssa/njcssa-python-practice-probs/blob/master/git_tutorials/creating_fork_imgs/Clone.PNG" width="550" height="300" />
    
<br />

5. Go back to cmd. Type "git clone (*the url that you just copied*)" and press enter. Congratulations, you have now set up your own repository to edit with! To make sure the files are there, cd into that "njcssa-python-practice-probs" and then type "dir". You should see a list of all the files we've written in there: 

    <img src="https://github.com/njcssa/njcssa-python-practice-probs/blob/master/git_tutorials/creating_fork_imgs/cmd2.PNG" width="650" height="500" />

    And to edit those files in an IDE, simply "Open Folder", navigate to that "njcssa-python-practice-probs" folder you downloaded, and you should have a streamlined way of editing files.
    

<br /><br />
## Steps to add suggestions to the njcssa practice problems repository (for Visual Code):
1. Make your changes and save. Then go click on the <img src="https://github.com/njcssa/njcssa-python-practice-probs/blob/master/git_tutorials/creating_fork_imgs/Trident.PNG" width="50" height="50" />  thing right underneath the magnifiying glass on the left. All your changes should show up like so:

    <img src="https://github.com/njcssa/njcssa-python-practice-probs/blob/master/git_tutorials/creating_fork_imgs/Changes.PNG" width="200" height="400" />

2. Commit your changes by pressing the check mark. Say yes to the dialog button that pops up (and make sure you've add a message to the commit)<br />

    <img src="https://github.com/njcssa/njcssa-python-practice-probs/blob/master/git_tutorials/creating_fork_imgs/Check.PNG" width="200" height="400" />

3. Go to the bottom left with the arrows and stuff. Click on that to push changes to your repository: Say yes to the dialog.

    <img src="https://github.com/njcssa/njcssa-python-practice-probs/blob/master/git_tutorials/creating_fork_imgs/Arrows.PNG" width="150" height="100" />

4. Once you've got that done, go to the original repository (https://github.com/njcssa/njcssa-python-practice-probs) and then click "New pull request."

    <img src="https://github.com/njcssa/njcssa-python-practice-probs/blob/master/git_tutorials/creating_fork_imgs/new.PNG" width="225" height="110">

5. Click (new pull request) & then click compare across forks:

    <img src="https://github.com/njcssa/njcssa-python-practice-probs/blob/master/git_tutorials/creating_fork_imgs/Compare.PNG" width="605" height="110">

6. Make the "Head Fork" your fork (*yourusername*/njcssa-python-practice-problems). So mine would be njcssa/njcssa-python-practice-problems as my user name is njcssa:

    <img src="https://github.com/njcssa/njcssa-python-practice-probs/blob/master/git_tutorials/creating_fork_imgs/user.PNG" width="425" height="50">

7. Press "Pull new request".

<br />
Congratulations you have now successfully suggested a change to the njcssa practice problems repository! Ben C. and other members will review it, and if they ❤❤ it they will add it, and if they doesn't, they will add comments to it for you to change it and redo it.