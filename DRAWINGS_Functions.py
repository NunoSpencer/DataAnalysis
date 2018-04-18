# 
#   //...work
#
#################################################################################################################################################

#-----------------------------------------------------------------------------------------------------------------------------------------------
# 1) NumDrawings(f) 
#-----------------------------------------------------------------------------------------------------------------------------------------------

def NumDrawings(inFile):
    inputFile = open(inFile, "r")
    dataFromFile = inputFile.read()                        
    drawings = len(dataFromFile.splitlines())    
    print(drawings)                              

#-----------------------------------------------------------------------------------------------------------------------------------------------
# 2) RANGES 
#-----------------------------------------------------------------------------------------------------------------------------------------------

#defines ranges as ints... not what we want
# Range1 = list(range(1, 11))                 #range [01 - 10] 
# Range2 = list(range(11, 21))                #range [11 - 20]
# Range3 = list(range(21, 31))                #range [21 - 30]
# Range4 = list(range(31, 36))                #range [30 - 35]

#defines ranges a strings 
Range1 = list(format(i, '02d') for i in range(1, 11))
Range2 = list(format(i, '02d') for i in range(11, 21))
Range3 = list(format(i, '02d') for i in range(21, 31))
Range4 = list(format(i, '02d') for i in range(31, 36))

#print ranges 
# print(Range1)
# print(Range2)
# print(Range3)
# print(Range4)

#-----------------------------------------------------------------------------------------------------------------------------------------------
# 3) function HitsPerRange(f)
#-----------------------------------------------------------------------------------------------------------------------------------------------

def HitsPerRange (inputFile):
    counterR1 = 0
    counterR2 = 0
    counterR3 = 0
    counterR4 = 0
    with open(inputFile, 'r') as inputFile:
        for line in inputFile:              
            for ball in line.split():       
                if ball in Range1:          
                    counterR1 += 1          
                if ball in Range2:
                    counterR2 += 1
                if ball in Range3:
                    counterR3 += 1
                if ball in Range4:
                    counterR4 += 1
    print ("Range [01-10] hits: " + str(counterR1))
    print ("Range [11-20] hits: " + str(counterR2))
    print ("Range [21-30] hits: " + str(counterR3))      
    print ("Range [30-35] hits: " + str(counterR4))

#-----------------------------------------------------------------------------------------------------------------------------------------------
# 3) Poll(f)  //definitely not "pythonic" ;(
#-----------------------------------------------------------------------------------------------------------------------------------------------
            
def Poll(inputFile):
    ball01Counter = 0
    ball02Counter = 0
    ball03Counter = 0
    ball04Counter = 0
    ball05Counter = 0
    ball06Counter = 0
    ball07Counter = 0
    ball08Counter = 0
    ball09Counter = 0
    ball10Counter = 0
    ball11Counter = 0
    ball12Counter = 0
    ball13Counter = 0
    ball14Counter = 0
    ball15Counter = 0
    ball16Counter = 0
    ball17Counter = 0
    ball18Counter = 0
    ball19Counter = 0
    ball20Counter = 0
    ball21Counter = 0
    ball22Counter = 0
    ball23Counter = 0
    ball24Counter = 0
    ball25Counter = 0
    ball26Counter = 0
    ball27Counter = 0
    ball28Counter = 0
    ball29Counter = 0
    ball30Counter = 0
    ball31Counter = 0
    ball32Counter = 0
    ball33Counter = 0
    ball34Counter = 0
    ball35Counter = 0
    with open(inputFile, 'r') as inputFile:
        for line in inputFile:
            for ball in line.split():
                if ball == '01':
                    ball01Counter += 1
                if ball == '02':
                    ball02Counter += 1
                if ball == '03':
                    ball03Counter += 1
                if ball == '04':
                    ball04Counter += 1
                if ball == '05':
                    ball05Counter += 1
                if ball == '06':
                    ball06Counter += 1
                if ball == '07':
                    ball07Counter += 1
                if ball == '08':
                    ball08Counter += 1
                if ball == '09':
                    ball09Counter += 1
                if ball == '10':
                    ball10Counter += 1
                if ball == '11':
                    ball11Counter += 1
                if ball == '12':
                    ball12Counter += 1
                if ball == '13':
                    ball13Counter += 1
                if ball == '14':
                    ball14Counter += 1
                if ball == '15':
                    ball15Counter += 1
                if ball == '16':
                    ball16Counter += 1
                if ball == '17':
                    ball17Counter += 1
                if ball == '18':
                    ball18Counter += 1
                if ball == '19':
                    ball19Counter += 1
                if ball == '20':
                    ball20Counter += 1
                if ball == '21':
                    ball21Counter += 1
                if ball == '22':
                    ball22Counter += 1
                if ball == '23':
                    ball23Counter += 1
                if ball == '24':
                    ball24Counter += 1
                if ball == '25':
                    ball25Counter += 1
                if ball == '26':
                    ball26Counter += 1
                if ball == '27':
                    ball27Counter += 1
                if ball == '28':
                    ball28Counter += 1
                if ball == '29':
                    ball29Counter += 1
                if ball == '30':
                    ball30Counter += 1
                if ball == '31':
                    ball31Counter += 1
                if ball == '32':
                    ball32Counter += 1
                if ball == '33':
                    ball33Counter += 1
                if ball == '34':
                    ball34Counter += 1
                if ball == '35':
                    ball35Counter += 1
        
        print("Ball 01 hits: " + str(ball01Counter) )
        print("Ball 02 hits: " + str(ball02Counter) )
        print("Ball 03 hits: " + str(ball03Counter) )
        print("Ball 04 hits: " + str(ball04Counter) )
        print("Ball 05 hits: " + str(ball05Counter) )
        print("Ball 06 hits: " + str(ball06Counter) )
        print("Ball 07 hits: " + str(ball07Counter) )
        print("Ball 08 hits: " + str(ball08Counter) )
        print("Ball 09 hits: " + str(ball09Counter) )
        print("Ball 10 hits: " + str(ball10Counter) )
        print("Ball 11 hits: " + str(ball11Counter) )
        print("Ball 12 hits: " + str(ball12Counter) )
        print("Ball 13 hits: " + str(ball13Counter) )
        print("Ball 14 hits: " + str(ball14Counter) )
        print("Ball 15 hits: " + str(ball15Counter) )
        print("Ball 16 hits: " + str(ball16Counter) )
        print("Ball 17 hits: " + str(ball17Counter) )
        print("Ball 18 hits: " + str(ball18Counter) )
        print("Ball 19 hits: " + str(ball19Counter) )
        print("Ball 20 hits: " + str(ball20Counter) )
        print("Ball 21 hits: " + str(ball21Counter) )
        print("Ball 22 hits: " + str(ball22Counter) )
        print("Ball 23 hits: " + str(ball23Counter) )
        print("Ball 24 hits: " + str(ball24Counter) )
        print("Ball 25 hits: " + str(ball25Counter) )
        print("Ball 26 hits: " + str(ball26Counter) )
        print("Ball 27 hits: " + str(ball27Counter) )
        print("Ball 28 hits: " + str(ball28Counter) )
        print("Ball 29 hits: " + str(ball29Counter) )
        print("Ball 30 hits: " + str(ball30Counter) )
        print("Ball 31 hits: " + str(ball31Counter) )
        print("Ball 32 hits: " + str(ball32Counter) )
        print("Ball 33 hits: " + str(ball33Counter) )
        print("Ball 34 hits: " + str(ball34Counter) )
        print("Ball 35 hits: " + str(ball35Counter) )
        

#################################################################################################################################################
# function calls
#################################################################################################################################################

inFile = "A:\\fabulous\\drive\\file.txt"

#NumDrawings(inFile)

#HitsPerRange(inFile)

Poll(inFile)
