#   
# 
#   1) FUNCTION "CleanPoll" , cleans Poll results file by stripping non-numeric chars from each number poll 
#   2) FUNCTION "plotR1": use clean poll data to plot x-> relation in r[01-10]
#   3) FUNCTION "plotR2": use clean poll data to plot x-> relation in r[11-20]
#   4) FUNCTION "plotR3": use clean poll data to plot x-> relation in r[21-30]
#   5) FUNCTION "plotR4": use clean poll data to plot x-> relation in r[30-35]
#   6) FUNCTION "PLOT_Consecutiveness_Of_JACKPOTS":
#
#################################################################################################################################################

import re

#-----------------------------------------------------------------------------------------------------------------------------------------------
# 1) #function CleanPoll(inF, outF)
#-----------------------------------------------------------------------------------------------------------------------------------------------

def CleanPoll(inF, outF):
    cleanData = []
    with open(inF, 'r') as inF, open(outF, 'w') as outF:
        for line in inF:
            cleanData = re.sub("[^0-9]", " ", line)
            #print (cleanData) #prints output to console... output to a file instead
            outF.write(cleanData + "\n")
    print("Done cleaning poll data!")


#################################################################################################################################################
# function calls
#################################################################################################################################################

pollFile = "C:\\Users\\Nuno\\OneDrive - Rhode Island College\\[programming_PROJECTS]\\DataLott\\Documentation\\poll_all_255_drawings.txt"
cleanPollFile = "C:\\Users\\Nuno\\OneDrive - Rhode Island College\\[programming_PROJECTS]\\DataLott\\Documentation\\poll_all_255_drawings_clean.txt"

CleanPoll(pollFile, cleanPollFile)
