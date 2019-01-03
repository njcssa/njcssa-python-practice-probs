@ECHO OFF
ECHO Update your repository for NJCSSA. Made By Ben & Chris
set /p id="Enter File Path: "
cd %id%
git remote add upstream https://github.com/njcssa/njcssa-python-practice-probs.git rem if this says fatal: blah blah then that is okay
git remote -v
git fetch upstream
git checkout master
git merge upstream/master
git push origin master
ECHO Sucessfully updated repo! 
PAUSE
EXIT