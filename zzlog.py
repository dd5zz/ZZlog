#!/usr/bin/python
# -*- coding: utf-8 -*-

######## ######## ##        #######   ######   
     ##       ##  ##       ##     ## ##    ##  
    ##       ##   ##       ##     ## ##        
   ##       ##    ##       ##     ## ##   #### 
  ##       ##     ##       ##     ## ##    ##  
 ##       ##      ##       ##     ## ##    ##  
######## ######## ########  #######   ######   

import pymysql
import sys
import os
import time


os.system('clear')
title = "DD5ZZ's simple logger Version ";
version = "0.23";

host = "dd5zz-pc"
port = 3306
dbUser = "log4omdm5emUser"
dbPass = "log4omdm5emUser"
dbName = "log4omdm5em"

quitkey = "q"
errorkey = "e"
mainmenukey = "m"

lastqsoid = 0

############################
#        functions         #
############################

def newid():
    cursor = db.cursor()
    cursor.execute("SELECT MAX(QsoId) AS QsoId FROM log;")
    maxqsoid = cursor.fetchone()
    newqsoid = maxqsoid[0] + 1
    return newqsoid

################################################################################################################################################

def loginput():

    ###########
    # logging #
    ###########

    loglogo()

    CallToLog = raw_input("                       Callsign to log: ")

    if CallToLog == mainmenukey: 
        menu()
    else:
        1 #nothing to do here

    print ("")
    BandToLog = raw_input("                               On band: ")
    print ("")
    ModeToLog = raw_input("                               In Mode: ")
    print ("")
    RSTr = raw_input("                          RST Received: ")
    print ("")
    RSTs = raw_input("                              RST Sent: ")    
    TimeToLog = time.strftime("%H%M%S",time.gmtime())  
    DateToLog = time.strftime("%Y%m%d",time.gmtime())
    nextid = newid()
    print ("")

    ##########################
    #      write to db       #
    ##########################

    try:
        cursor = db.cursor() 
        cursor.execute("INSERT INTO log (QsoId, `Call`, Band, Mode,  TimeOn, QsoDate, RstRcvd, RstSent) VALUES ("+str(nextid)+", '"+str(CallToLog)+"', '"+str(BandToLog)+"', '"+str(ModeToLog)+"', '"+str(TimeToLog)+"', '"+str(DateToLog)+"','"+str(RSTr)+"', '"+str(RSTs)+"');")
        db.commit()
    except Exception as e:
        print("Something went wrong.")
        print("Please try again later.")
        print("73!")
        sys.exit("")
    else:
        print "\033[0;5mLogged!\033[0m"   
        print("")
        time.sleep(2)
        
        #print (CallToLog + " " + BandToLog + " " + ModeToLog + " " + TimeToLog + " " + DateToLog + " " + RSTs + " " + RSTr)
        #print (nextid)

    loginput()

   #####################################################################################################################################################################

def loginputpastqso():

    ###########
    # logging #
    ###########

    loglogo()

    CallToLog = raw_input("                       Callsign to log: ")

    if CallToLog == mainmenukey: 
        menu()
    else:
        1 #nothing to do here

    print ("")
    BandToLog = raw_input("                               On band: ")
    print ("")
    ModeToLog = raw_input("                               In Mode: ")
    print ("")
    RSTr = raw_input("                          RST Received: ")
    print ("")
    RSTs = raw_input("                              RST Sent: ")    
    print ("")
    TimeToLog = raw_input("                     Time UTC (hhmmss): ") 
    print ("")
    DateToLog = raw_input("                        Date (yyymmdd): ")
    nextid = newid()
    print ("")

    ##########################
    #      write to db       #
    ##########################

    try:
        cursor = db.cursor() 
        cursor.execute("INSERT INTO log (QsoId, `Call`, Band, Mode,  TimeOn, QsoDate, RstRcvd, RstSent) VALUES ("+str(nextid)+", '"+str(CallToLog)+"', '"+str(BandToLog)+"', '"+str(ModeToLog)+"', '"+str(TimeToLog)+"', '"+str(DateToLog)+"','"+str(RSTr)+"', '"+str(RSTs)+"');")
        db.commit()
    except Exception as e:
        print("Something went wrong.")
        print("Please try again.")
        print("")
        time.sleep(2)
        loginputpastqso()
        
    else:
        print "\033[0;5mLogged!\033[0m"   
        print("")
        time.sleep(2)
        
        #print (CallToLog + " " + BandToLog + " " + ModeToLog + " " + TimeToLog + " " + DateToLog + " " + RSTs + " " + RSTr)
        #print (nextid)

    loginputpastqso()

########################################################################################################################################################################

def loglogo():

    os.system('clear')
    print ("            ****************************************************************************************************")
    print ("            *                                                                                                  *")
    print ("            *                                           Logging Mode                                           *")
    print ("            *                                                                                                  *")
    print ("            ****************************************************************************************************")
    print ("")
    print ('                Use "' + mainmenukey + '" at callsign prompt to get back to the main menu.')
    print ('                To correct a mistake and start over use "' + errorkey + '" at any input prompt.')
    print ("")


########################################################################################################################################################################
    
def loginput59():

    ################
    # logging - 59 #
    ################

    loglogo()


    CallToLog = raw_input("                       Callsign to log: ")

    if CallToLog == mainmenukey: 
        menu()
    else:
        1 #nothing to do here

    print ("")
    BandToLog = raw_input("                               On band: ")
    print ("")
    ModeToLog = raw_input("                               In Mode: ")
    RSTr = 59
    RSTs = 59   
    TimeToLog = time.strftime("%H%M%S",time.gmtime())  
    DateToLog = time.strftime("%Y%m%d",time.gmtime())
    nextid = newid()
    print ("")


    ##########################
    #      write to db       #
    ##########################

    try:
        cursor = db.cursor() 
        cursor.execute("INSERT INTO log (QsoId, `Call`, Band, Mode,  TimeOn, QsoDate, RstRcvd, RstSent) VALUES ("+str(nextid)+", '"+str(CallToLog)+"', '"+str(BandToLog)+"', '"+str(ModeToLog)+"', '"+str(TimeToLog)+"', '"+str(DateToLog)+"','"+str(RSTr)+"', '"+str(RSTs)+"');")
        db.commit()
    except Exception as e:
        print("Something went wrong.")
        print("Please try again later.")
        print("73!")
        sys.exit("")
    else:
        print "\033[0;5mLogged!\033[0m"   
        print("")
        time.sleep(2)
        
        #print (CallToLog + " " + BandToLog + " " + ModeToLog + " " + TimeToLog + " " + DateToLog + " " + RSTs + " " + RSTr)
        #print (nextid)

    loginput59()


######################################################################################################################################################################## 

def lastqso():
    
    #==========#
    # last qso #
    #==========#
   
    os.system('clear')
    logo()
    cursor = db.cursor()
    cursor.execute("SELECT band,mode,`call`,QsoDate,TimeOn FROM log WHERE QsoId=" + str(lastqsoid) + ";")
    lastqso = cursor.fetchall()
    print ("")
    print ("Last logged QSO in Database:")
    print ("")
    print (lastqso[0][2] + " on " + lastqso[0][0] + " in " +  lastqso[0][1] + " Date: " + lastqso[0][3] + " Time (UTC) " + lastqso[0][4])
    print ("")
    


########################################################################################################################################################################

def menu():

    os.system('clear')
    logo()
    
    print ("                              Main menu")
    print                                   
    print
    print ("       1  -> Log QSO using real time")
    print ("       2  -> Log QSO with fixed 59/59 reports using real time")
    print ("       3  -> Log past QSO")
    print ("       4  -> Show last 5 log entrys")
    print ("       73 -> Quit ZZlog")
    print ("")
    print ("")
    usersel = raw_input ("       => ")

    if usersel == "1":
        loginput()
    elif usersel == "2":
        loginput59()
    elif usersel == "3":
        loginputpastqso()
    elif usersel == "4":
        lastqso()
    elif usersel == "73":
        db.close()
        print ("")
        print ("")
        print ("		       Tnx for using ZZlog - 73!")
        print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
        sys.exit()
    else:
        menu()

        
#####################################################################################################################################################################


def logo2():
    
    print ("")
    print ("****************************************************************************************************")
    print ("*                                                                                                  *")
    print ("*                                                                                                  *")
    print ("*                                  " + title + version + "                             *")
    print ("*                                                                                                  *")
    print ("*                                                                                                  *")
    print ("****************************************************************************************************")
    print ("")

######################################################################################################################################################################

def logo():


    print ("")
    print ("")
    print ("                             Welcome to")
    print ("")
    print ("")
    #print ("       ___           ___                         ___           ___          ")     
    #print ("      /  /\         /  /\                       /  /\         /  /\         ")
    #print ("     /  /::|       /  /::|                     /  /::\       /  /:/_        ")
    #print ("    /  /:/:|      /  /:/:|     ___     ___    /  /:/\:\     /  /:/ /\       ")
    #print ("   /  /:/|:|__   /  /:/|:|__  /__/\   /  /\  /  /:/  \:\   /  /:/_/::\      ")
    #print ("  /__/:/ |:| /\ /__/:/ |:| /\ \  \:\ /  /:/ /__/:/ \__\:\ /__/:/__\/\:\     ")
    #print ("  \__\/  |:|/:/ \__\/  |:|/:/  \  \:\  /:/  \  \:\ /  /:/ \  \:\ /~~/:/     ")
    #print ("      |  |:/:/      |  |:/:/    \  \:\/:/    \  \:\  /:/   \  \:\  /:/      ")
    #print ("      |  |::/       |  |::/      \  \::/      \  \:\/:/     \  \:\/:/       ")
    #print ("      |  |:/        |  |:/        \__\/        \  \::/       \  \::/        ")
    #print ("      |__|/         |__|/                       \__\/         \__\/         ")
    #print ("")
    #print ("")
    #print ("                           Version: " + version)
    #print ("")
    #print ("")

    print("         ________   ________   ___                                   ")                       
    print("        /\_____  \ /\_____  \ /\_ \                                  ")
    print("        \/____//'/'\/____//'/'\//\ \      ___      __                ")
    print("             //'/'      //'/'   \ \ \    / __`\  /'_ `\              ")
    print("            //'/'___   //'/'___  \_\ \_ /\ \L\ \/\ \L\ \             ")
    print("            /\_______\ /\_______\/\____\\ \____/\ \____ \            ")
    print("            \/_______/ \/_______/\/____/ \/___/  \/___L\ \           ")
    print("                                                   /\____/           ")
    print("                                                   \_/__/            ")
    print ("")
    print ("")
    print ("                            Version: " + version)
    print ("")
    print ("")

#####################################################################################################################################################################






#program starts here#

#show  logo
logo()

#ask if user wants to use the standard db 
standardDb = raw_input(" 		      Use standard db? Y/n -> ");

#if user wants to use another db, ask for the details
if standardDb == "N" or standardDb == "n":
    print("")
    host = raw_input("DB Server Hostname or IP? ");
    port = raw_input("DB Server Port? (default is 3306) ");
    dbUser = raw_input("DB Username? ");
    dbPass = raw_input("DB Password? ");
    dbName = raw_input("Database? ");
    print ("")
else:
    print ("")


    ########################
    #    Connect to db     #
    ########################

try:
    db = pymysql.connect(host,dbUser,dbPass,dbName)
except Exception as e:
   print("Sorry but couldnt connect to the database.")
   print("Please try again later.")
   print("73!")
   sys.exit("")
else: 
   print("Connected to Database")
   print("")
   time.sleep(2)
   
   cursor = db.cursor()
   cursor.execute("SELECT MAX(QsoId) AS QsoId FROM log;")
   maxqsoid = cursor.fetchone()
   lastqsoid = maxqsoid[0]
	
#show main menu
menu()

# disconnect from server
db.close()






