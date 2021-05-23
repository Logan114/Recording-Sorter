#TV-recording sorter, compresser. Linux only

import os
from datetime import date, datetime
x = datetime.now()
year = str(x.year)
month = x.strftime("%Y_""%b") #month with name
month1 = str(x.month) #current month
current = "2021-0"+str(month1) # current year and month, should be changed yearly, and when the month becomes double digit
files =  "2021-0"+ str(month1) +"*"
def delete_source():
    confirmation = input("should i delete the source file? Y/N ")
    if confirmation in ['y', 'y', "i", "I", "yes"]:
        os.system("rm " + files)

if not os.path.exists(month): # if the folder exists skip it
    os.mkdir(month)

os.system('ls /home/logan/TV-tapes/') 
automatic = input ("\n \n Should i go semi-automatic? Y/N ")

if automatic in ['Y',"y","i","I","yes"]:
    outputfile = input("\n \n what should the output file be named? ")
    lrz = str(("ffmpeg -i 2021-0"+ str(month1) +"* " "-c:v libx265 " + month+ "/" +outputfile + ".mkv && beep -f 600"))
    
else:
    files = "~/TV-tapes/" + input("\n \n Which file should i compress? ") + "* "
    os.system('ls '+ files)
    outputfile = input("\n \n what should the output file be named? ")
    lrz = str(("ffmpeg -i " + files +  "-c:v libx265 " + month+ "/" +outputfile + ".mkv && beep -f 600"))
 

print (files)

print (lrz)
os.system(lrz)
delete_source()