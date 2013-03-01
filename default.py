import xbmc
import subprocess,os

class Screensaver(xbmc.Monitor) :
    print("DLMGR: Checking PlayBackState")
    def __init__ (self):
        xbmc.Monitor.__init__(self)

    def onScreensaverDeactivated(self):
        print("DLMGR: XBMC in use")
        os.system("sudo /etc/init.d/sickbeard stop") #stops the sickbeard service
        os.system("/home/xbian/.xbmc/addons/script.service.dlmanager/trans_speedlimit_on.sh") #puts transmission into speed limited mode
        xbmc.executebuiltin('Notification(Download Manager,Sickbeard stopped. Transmission throttled.,5000)')

    def onScreensaverActivated(self):
        print("DLMGR: XBMC in Standby")
        os.system("sudo /etc/init.d/sickbeard start") #starts the sickbeard service
        os.system("/home/xbian/.xbmc/addons/script.service.dlmanager/trans_speedlimit_off.sh") #disables transmission speed limited mode

    def onAbortRequested(self):
        print("DLMGR: XBMC is closing")
        os.system("sudo /etc/init.d/sickbeard start") #starts the sickbeard service
        os.system("/home/xbian/.xbmc/addons/script.service.dlmanager/trans_speedlimit_off.sh") #disables transmission speed limited mode

print("DLMGR: Download Manager Loaded")

monitor=Screensaver()

while not xbmc.abortRequested: #End if XBMC closes
    xbmc.sleep(5000) #Repeat (ms) 
