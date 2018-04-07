#
#   1) define RANGES : sets ranges for a playing slip. A playing slip has 4 ranges: [1-10], [11-20], [21-30], [30-35]
#   2) define HitsPerRange : gets number of hits per each range
#   3) define Poll         : polls hits for each ball numbers (1-35)
#   
#   
#################################################################################################################################################

#-----------------------------------------------------------------------------------------------------------------------------------------------
# 1) RANGES (formated as strings since the ball numbers are strings)
#-----------------------------------------------------------------------------------------------------------------------------------------------

#defines ranges as ints... not what we want
# Range1 = list(range(1, 11))                 #range [01 - 10] 
# Range2 = list(range(11, 21))                #range [11 - 20]
# Range3 = list(range(21, 31))                #range [21 - 30]
# Range4 = list(range(31, 36))                #range [30 - 35]

#defines ranges a strings.. because each ball number is a string '01', '02', etc
Range1 = list(format(i, '02d') for i in range(1, 11))
Range2 = list(format(i, '02d') for i in range(11, 21))
Range3 = list(format(i, '02d') for i in range(21, 31))
Range4 = list(format(i, '02d') for i in range(31, 36))

#print ranges 
print(Range1)
print(Range2)
print(Range3)
print(Range4)

#-----------------------------------------------------------------------------------------------------------------------------------------------
# 1) function HitsPerRange()
#-----------------------------------------------------------------------------------------------------------------------------------------------

def HitsPerRange (inputFile):
    counterR1 = 0
    counterR2 = 0
    counterR3 = 0
    counterR4 = 0
    with open(inputFile, 'r') as inputFile:
        for line in inputFile:             #"line" is each line in the file, i.e. each drawing
            for ball in line.split():   #"ball" is each ball in a drawing
                if ball in Range1:      #for each ball in a drawing, if it is Range1...
                    counterR1 += 1      #count it for all ranges in all drawings...
                if ball in Range2:
                    counterR2 += 1
                if ball in Range3:
                    counterR3 += 1
                if ball in Range4:
                    counterR4 += 1
    print ("Range [1-10] hits: " + str(counterR1))
    print ("Range [11-20] hits: " + str(counterR2))
    print ("Range [21-30] hits: " + str(counterR3))      
    print ("Range [30-35] hits: " + str(counterR4))


#inFile = "C:\\Users\\Nuno\\OneDrive - Rhode Island College\\[programming_PROJECTS]\\DataLott\\Documentation\\testfile.txt"

HitsPerRange("C:\\Users\\Nuno\\OneDrive - Rhode Island College\\[programming_PROJECTS]\\DataLott\\Documentation\\testfile.txt")


            


