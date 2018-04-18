#
# work...
#
#################################################################################################################################################


#---------------------------------------------------------------------------------------------------------------------------------------------------
# FUNCTION "Parse_Raw_Data": cleaning
#---------------------------------------------------------------------------------------------------------------------------------------------------

#read file
inFile = open("A:\\filein.txt "r")
outFile = open("A:\\fileout.txt, "w")

lines = inFile.readlines()          
lines.reverse()                     #lines reversed


line_count = 0

for line in lines:
    line = line.strip()             #remove tab spaces, and extra spaces
    line = line.replace("$" , "")   #remove "$"
    line = line.replace("," , "")   #remove ","
    
    line_count += 1

    outFile.write(line + "\n")      #write out

    #print(line)                   
   
    #print(line_count)              
    
    inFile.close()                 
    


#-----------------------------------------------------------------------------------------------------------------------------------------------
# ...
#-----------------------------------------------------------------------------------------------------------------------------------------------

outFile = open("A:\\fileout.txt", "r")
ListOfJackpots = []                                         
outFileLines = outFile.readlines()                         
outFileLines_INT = [int(x) for x in outFileLines]           

for x, y in zip(outFileLines_INT, outFileLines_INT[1:]):
    if(x > y):
        ListOfJackpots.append(int(x))

print("All JACKPOT amounts:")
for item in ListOfJackpots:
    print(item)



#---------------------------------------------------------------------------------------------------------------------------------------------------
# ....
#---------------------------------------------------------------------------------------------------------------------------------------------------

DrawingsBeforeJackpot = []                                
counter = 0                                               
for x, y in zip(outFileLines_INT, outFileLines_INT[1:]):
    if(x < y):
        counter += 1
    else: 
        DrawingsBeforeJackpot.append(counter)
        counter = 0
    continue

print("Consecutiveness :")
for i in DrawingsBeforeJackpot:
    print(i)









    




