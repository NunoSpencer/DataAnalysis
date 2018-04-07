#
#   DATALOTT - 
# 
#   DRAWINGS functions:
#
#   1) FUNCTION "COUNT_Drawings": counts all drawings from file "WM_ALL_drawings_clean.txt"

#   2) FUNCTION "PLOT_Drawing_RANGE_01-10": plots relation between DRAWINGS(x) -> #HITS(y) for range [01 - 10] BALL NUMBERs
#   3) FUNCTION "PLOT_Drawing_RANGE_11-20": plots relation between DRAWINGS(x) -> #HITS(y) for range [11 - 20] BALL NUMBERs
#   4) FUNCTION "PLOT_Drawing_RANGE_21-30": plots relation between DRAWINGS(x) -> #HITS(y) for range [21 - 30] BALL NUMBERs
#   5) FUNCTION "PLOT_Drawing_RANGE_31-35": plots relation between DRAWINGS(x) -> #HITS(y) for range [30 - 35] BALL NUMBERs
#
#   NOTE: data includes all drawings from 2016, 2017, 2018
#   
#################################################################################################################################################

#-----------------------------------------------------------------------------------------------------------------------------------------------
# FUNCTION "COUNT_Drawings": counts all drawings from file "WM_ALL_drawings_clean.txt"
#
# Returns: # of drawings (lines) in the file
#-----------------------------------------------------------------------------------------------------------------------------------------------


infile = open("C:\\Users\\Nuno\\OneDrive - Rhode Island College\\[programming_PROJECTS]\\DataLott\\Documentation\\WM_ALL_drawings_clean.txt", "r") #open the file

dataFromFile = infile.read()                    #read data (lines) in file

numDrawings = len(dataFromFile.splitlines())    #count the lines in file

print(numDrawings)                              #print number of lines (drawings)
