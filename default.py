import xbmc
import subprocess,os
import xbmcaddon

__settings__   = xbmcaddon.Addon(id="script.service.dlmanager")

class Screensaver(xbmc.Monitor) :
    print("DLMGR: Checking PlayBackState")

    def __init__ (self):
        xbmc.Monitor.__init__(self)
        
    def onScreensaverDeactivated(self):
        print("DLMGR: XBMC in use")
        os.system("sudo /etc/init.d/sickbeard stop") #stops the sickbeard service
        scriptPath = xbmc.translatePath("special://home/addons/script.service.dlmanager/transmission_limit.sh")
        os.system(scriptPath + " " + __settings__.getSetting( "trans_port" ) + " " + __settings__.getSetting( "trans_username" ) + " " + __settings__.getSetting( "trans_password" )) #puts transmission into speed limited mode
        xbmc.executebuiltin("Notification(Sickbeard stopped. Transmission throttled.)")

    def onScreensaverActivated(self):
        print("DLMGR: XBMC in Standby")
        os.system("sudo /etc/init.d/sickbeard start") #starts the sickbeard service
        scriptPath = xbmc.translatePath("special://home/addons/script.service.dlmanager/transmission_limit.sh")
        os.system(scriptPath + " " + __settings__.getSetting( "trans_port" ) + " " + __settings__.getSetting( "trans_username" ) + " " + __settings__.getSetting( "trans_password" )) #disables transmission speed limited mode

    def onAbortRequested(self):
        print("DLMGR: XBMC is closing")
        os.system("sudo /etc/init.d/sickbeard start") #starts the sickbeard service
        scriptPath = xbmc.translatePath("special://home/addons/script.service.dlmanager/transmission_limit.sh")
        os.system(scriptPath + " " + __settings__.getSetting( "trans_port" ) + " " + __settings__.getSetting( "trans_username" ) + " " + __settings__.getSetting( "trans_password" )) #disables transmission speed limited mode

print("DLMGR: Download Manager Script Loaded")

monitor=Screensaver()

while not xbmc.abortRequested: #End if XBMC closes
    xbmc.sleep(5000) #Repeat (ms) 
