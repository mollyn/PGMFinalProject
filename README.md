# PGMFinalProject

### Final Project
### 625.492 - Probabilistic Graphical Models
### Molina Nichols
### Due: 15 May 2018

Data files are too big to be committed to a github repository.  They will be zipped and submitted on Blackboard.
In order to access the data yourself, please complete the following steps...
1. Pull the contents of this repository into a folder.  All files, including the jupyter notebooks, props.py, and helpers.py should be at the same level.
2. Unzip the csv's into a folder of your choice (logically, something along the lines of C:\Users\yourname\\...\NicholsProject\data
3. Open the file props.py
4. Commend out the variables usbDriveLetter, projectFolder, and baseFolder, and the following lines with chdir and allContent and sys.path.append.
5. Set the variable dataFolder to the fully qualified path where you placed the csv's.
6. Set the variable baseFolder to the fully qualified path to where you pulled down the repository.
7. After this variable assignment, add the lines os.chdir(baseFolder) and sys.path.append(os.listdir('.'))
8. You should now be able to run any of the Jupyter notebooks with no trouble.  If you have difficulty, please contact me.


#### Note: Running loadData.ipynb will load in the June 2017 csv - this may take up to around 5 minutes.  Be patient!  It will eventually finish.  Just do not do other things in the notebook until the [*] next to the cell (indicates that it is running) goes away, and the kernel indicates that it is not busy.
