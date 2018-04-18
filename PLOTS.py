#   
# go
#
#################################################################################################################################################

import re
import pandas as pd

#-----------------------------------------------------------------------------------------------------------------------------------------------
# ..
#-----------------------------------------------------------------------------------------------------------------------------------------------

def CleanPoll(inF, outF):
    cleanData = []
    with open(inF, 'r') as inF, open(outF, 'w') as outF:
        for line in inF:
            cleanData = re.sub("[^0-9]", " ", line)
            #print (cleanData) #prints output to console... output to a file instead
            outF.write(cleanData + "\n")
    print("Done cleaning poll data!")


#-----------------------------------------------------------------------------------------------------------------------------------------------
# ..
#-----------------------------------------------------------------------------------------------------------------------------------------------

def plotR1(inF):
    r1Balls = []
    r1Poll = []
    with open(inF) as inF:
        r1 = inF.readlines()[0:10]
    #print (r1)                                 #test that r1 contains r[01-10] poll
    for line in r1:
        r1Balls.append(line.split(None, 1)[0])
        r1Poll.append(line.split(None, 1)[1])
    #print (r1Balls)                             #test that r1Balls contains [01-10] balls
    #print (r1Poll)                              #test that r1Poll contains [01-10] poll
    pandasDF = {'Balls [01 - 10]': r1Balls, "Hits per ball": r1Poll}
    R1DF = pd.DataFrame(pandasDF)                       
    print(R1DF)



#################################################################################################################################################
# calls
#################################################################################################################################################

pollFile = "C:\\Users\\Nuno\\OneDrive - Rhode Island College\\[programming_PROJECTS]\\DataLott\\Documentation\\poll_all_255_drawings.txt"
cleanPollFile = "C:\\Users\\Nuno\\OneDrive - Rhode Island College\\[programming_PROJECTS]\\DataLott\\Documentation\\poll_all_255_drawings_clean.txt"

#CleanPoll(pollFile, cleanPollFile)

plotR1(cleanPollFile)
