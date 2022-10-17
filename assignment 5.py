#=====================
#IMPORT MODULES
#=====================
import numpy
from psychopy import core, gui, visual, event
import json
import os
import itertools
import glob
#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()
#-define the directory where you will save your data
data_dir = os.path.join(main_dir, "data")
#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir, "images")
#-check that these directories exist
os.path.isdir(image_dir)
os.path.isdir(data_dir)

if not os.path.isdir(image_dir):
    raise Exception("Could not find img path")
if not os.path.isdir(data_dir):
    raise Exception("Could not find data path")
#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, 
    #handedness
#get date and time
#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#Number of Trials and Blocks
nTrials = 10
nBlocks = 2 
#-stimulus names (and stimulus extensions, if images) 
nums = []
for i in range(10) : 
    nums.append(i+1)
pics = ["face" + (str(i).zfill(2)) + ".jpg" for i in nums]

print(pics)
#-stimulus properties like 200x200px, orientation, center of screen, 1 second 
stimSize = [200,200]
stimDur = 1
stimLoc = [0,0]
#-start message text 
startMsg = "Welcome to the Experiment. Press any key to begin."

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
ims_in_dir = sorted(os.listdir(image_dir))

for x in pics :
    if x in ims_in_dir:
        print(x, "was found!")
    else :
        raise Exception("image not found")

#-create counterbalanced list of all conditions 
numpy.random.shuffle(pics)
print(pics)
#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is 
    #correct") 
correctkey = []
#-create an empty list for participant responses (e.g., "on this trial, response was a 
    #X") *
responses = []
#-create an empty list for response accuracy collection (e.g., "was participant 
    #correct?") *
corrects = []
#-create an empty list for response time collection *
RT = []
#-create an empty list for recording the order of stimulus identities *
picidentity = []
#-create an empty list for recording the order of stimulus properties *
picprops = []

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
# Set up the 2 blocks
for thisBlock in range(nBlocks) :
    print("Welcome to Block", str(thisBlock+1))
    numpy.random.shuffle(pics)
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    # Set up the 10 trials per Block - nest the loop, DON'T mess with the indents
    for thisTrial in range(nTrials) :
        print("This is Trial", str(thisTrial+1))
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment