""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# file: SwimSight.py
# Author: Olivia O'Driscoll
# Date: Winter 2021
# file summary:
#   prototype file for a sonar solution to assist swimmers with visual impairments.
#   Gives swimmer audio feedback as to where they are in the lane and how they need to
#   correct their position.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""IMPORT MODULES"""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
from playsound import playsound
from copy import deepcopy
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""" DEFINE VARIABLES """""""""""""""""""""""""""""""""""""""""""""
right = "C:/Users/olivi/Documents/jackRight.mp3"
left = "C:/Users/olivi/Documents/jackLeft.mp3"
turnAround = "C:/Users/olivi/Documents/jackTurn.mp3"
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""DEFINE FUNCTIONS"""""""""""""""""""""""""""""""""""""""""""""""


def alert(cue):
    """alerts the swimmer as to the direction in which they need to correct"""
    print("go {}".format(cue))
    playsound(cue)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""MAIN PROGRAM"""""""""""""""""""""""""""""""""""""""
# read data from stdin
for line in sys.stdin:
    data = line.split(",")

    # check if data has the correct number of arguments
    if len(data) == 21:

        # get the x position and y position from the data
        y_pos_current = data[4]
        x_pos_current = data[3]

        try:
            if float(y_pos_current) - float(y_pos_last) >= 0:
                direction = 'positive'
            else:
                direction = 'negative'
        except NameError:
            pass

        y_pos_last = deepcopy(y_pos_current)

        # Compute if the swimmer is veering left
        if float(y_pos_current) < -6.3:
            alert(right)

        # Compute if the swimmer is veering right
        elif float(y_pos_current) > -5.7:
            alert(left)

        else:
            # swimmer is in middle of lane
            pass

        # check if the swimmer is about to hit the wall
        if 1.2 < float(x_pos_current) < 0.8 and direction == 'positive':
            alert(turnAround)
        elif 12.8 > float(x_pos_current) > 12.48 and direction == 'negative':
            alert(turnAround)

    else:
        pass

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

