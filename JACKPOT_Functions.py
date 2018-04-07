#
#   DATALOTT - 
# 
#   JACKPOT functions:
#   1) FUNCTION "Parse_Raw_Data": parse and organize raw data from 2017 prizes/JACKPOTS: remove "$", "." and leading spaces/indentations from original file
#   2) FUNCTION "Find_Jackpots": find all JACKPOTS from all prizes/JACKPOTS 
#   3) FUNCTION "Consecutiveness_Of_JACKPOTS": finds #of prizes before each JACKPOTS 
#   4) FUNCTION "PLOT_Consecutiveness_Of_JACKPOTS": plots relation between JACKPOTS(x) -> CONSECUTIVENESS(y) 
#
#   NOTE: data includes all prizes/JACKPOTS from 2017
#   NOTE: sorting order: older drawings are first in the file, most recent drawings are last in file
#################################################################################################################################################


#---------------------------------------------------------------------------------------------------------------------------------------------------
# FUNCTION "Parse_Raw_Data": finds and removes "$", "." and leading spaces/indentations from original file, outputs clean data to new file
#---------------------------------------------------------------------------------------------------------------------------------------------------

#read file
inFile = open("C:\\Users\\Nuno\\OneDrive - Rhode Island College\\[programming_PROJECTS]\\DataLott\\Documentation\\Jackpot_Prizes_in_dollars_RAW_DATA.txt", "r")
outFile = open("C:\\Users\\Nuno\\OneDrive - Rhode Island College\\[programming_PROJECTS]\\DataLott\\Documentation\\Jackpot_Prizes_in_dollars_clean_reversed.txt", "w")

lines = inFile.readlines()          #read input file
lines.reverse()                     #reverse lines, so oldest drawings are printed first (i.e. 1st element in array)

#--  Find "." "$" and spaces, and truncate them
line_count = 0

for line in lines:
    line = line.strip()             #remove tab spaces, and extra spaces
    line = line.replace("$" , "")   #remove "$"
    line = line.replace("," , "")   #remove ","
    
    line_count += 1

    outFile.write(line + "\n")      #write output to "Jackpot_Prizes_in_dollars_clean.txt"

    #print(line)                    #print output to screen
   
    #print(line_count)              #print # of prizes (i.e. # of lines in the file)
    
    inFile.close()                  #close in file
    


#-----------------------------------------------------------------------------------------------------------------------------------------------
# FUNCTION "FindJackpots", finds JACKPOTS in range of N prizes (in this case we are using all 2017 WildMoney prizes incluing JACKPOTs)
# How to: loop the list of drawings, if ___ retunr lines[j]
#-----------------------------------------------------------------------------------------------------------------------------------------------

outFile = open("C:\\Users\\Nuno\\OneDrive - Rhode Island College\\[programming_PROJECTS]\\DataLott\\Documentation\\Jackpot_Prizes_in_dollars_clean_reversed.txt", "r")
ListOfJackpots = []                                         #list of Jackpots contains Jackpot prizes
outFileLines = outFile.readlines()                          #get each number in text file (on each line, as string)
outFileLines_INT = [int(x) for x in outFileLines]           #convert each number from string to int

for x, y in zip(outFileLines_INT, outFileLines_INT[1:]):
    if(x > y):
        ListOfJackpots.append(int(x))

#-- print JACKPOTS to screen (loop ListOfJackpots[])
print("All JACKPOT amounts:")
for item in ListOfJackpots:
    print(item)



#---------------------------------------------------------------------------------------------------------------------------------------------------
# FUNCTION "ConsecutivenessOfJACKPOTS", finds #of prizes before each JACKPOTS
# Do: count # of drawings until a jackpot is found... if previous is < current prize, count... 
#         else add counter value to list and reset counter... continue same process until end of file. 
#         NOTE that each JACKPOT will have a corresponding number of consecutiveness (i.e. a X/Y correspondence later used to plot the correspondence JACKPOT(x) -> CONSECUTIVENESS)(y)
#---------------------------------------------------------------------------------------------------------------------------------------------------

DrawingsBeforeJackpot = []                                #list to which  EACH # of drawings before JACKPOT will be collected
counter = 0                                               #counter for # of drawings before EACH JACKPOT
for x, y in zip(outFileLines_INT, outFileLines_INT[1:]):
    if(x < y):
        counter += 1
    else: 
        DrawingsBeforeJackpot.append(counter)
        counter = 0
    continue

print("Consecutiveness of JACKPOTS :")
for i in DrawingsBeforeJackpot:
    print(i)


#---------------------------------------------------------------------------------------------------------------------------------------------------
# FUNCTION "PLOT_Consecutiveness_Of_JACKPOTS": 
# each JACKPOT (X indep var) has a corresponding consecutivess (Y dep var)... 
# We want to plot X in terms of Y...
#
# Do: note that we already have the lists for X and Y, i.e. 
# "ListOfJAckpots" and "DrawingsBeforeJackpot" respectively
#---------------------------------------------------------------------------------------------------------------------------------------------------









    




