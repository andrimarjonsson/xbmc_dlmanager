import xbmc
import subprocess,os
class Screensaver(xbmc.Monitor) :
        xbmc.log(msg="DLMGR: Checking PlayBackState",level=xbmc.LOGDEBUG)
        def __init__ (self):
                xbmc.Monitor.__init__(self)

        def onScreensaverDeactivated(self):
		xbmc.log(msg="DLMGR: XBMC in use",level=xbmc.LOGDEBUG)
		os.system("sudo /etc/init.d/sickbeard stop") #stops the sickbeard service
		os.system("special://home/addons/script.service.dlmanager/trans_speedlimit_on.sh") #puts transmission into speed limited mode

        def onScreensaverActivated(self):
		xbmc.log(msg="DLMGR: XBMC in Standby",level=xbmc.LOGDEBUG)
		os.system("sudo /etc/init.d/sickbeard start") #starts the sickbeard service
		os.system("special://home/addons/script.service.dlmanager/trans_speedlimit_off.sh") #disables transmission speed limited mode

        def onAbortRequested(self):
		xbmc.log(msg="DLMGR: XBMC is closing",level=xbmc.LOGDEBUG)
		os.system("sudo /etc/init.d/sickbeard start") #starts the sickbeard service
		os.system("special://home/addons/script.service.dlmanager/trans_speedlimit_off.sh") #disables transmission speed limited mode

xbmc.log(msg="DLMGR: Working",level=xbmc.LOGDEBUG)

monitor=Screensaver()

while not xbmc.abortRequested: #End if XBMC closes
        xbmc.sleep(5000) #Repeat (ms) 
