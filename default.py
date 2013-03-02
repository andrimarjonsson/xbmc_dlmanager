import xbmc
import subprocess,os
import xbmcaddon
from subprocess import Popen, PIPE

__settings__   = xbmcaddon.Addon(id="script.service.dlmanager")

class Screensaver(xbmc.Monitor) :
    print("DLMGR: Checking PlayBackState")

    def __init__ (self):
        xbmc.Monitor.__init__(self)
        self.scriptPath = xbmc.translatePath("special://home/addons/script.service.dlmanager/transmission_limit.sh")
        print("DLMGR: script path: " + self.scriptPath)
        
    def onScreensaverDeactivated(self):
        print("DLMGR: XBMC in use")
        os.system("sudo /etc/init.d/sickbeard stop") #stops the sickbeard service
        trans_cmd = self.scriptPath + ' on ' + __settings__.getSetting("trans_port") + ' ' + __settings__.getSetting("trans_username") + ' ' + __settings__.getSetting("trans_password") # the command line to put transmission into speed limited mode
        p = Popen(trans_cmd , shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        print("DLMGR: transmission throttle: ",out.rstrip(), err.rstrip())
        xbmc.executebuiltin("Notification(Sickbeard stopped. Transmission throttled.,5000)")

    def onScreensaverActivated(self):
        print("DLMGR: XBMC in Standby")
        os.system("sudo /etc/init.d/sickbeard start") #starts the sickbeard service
        trans_cmd = self.scriptPath + ' off ' + __settings__.getSetting("trans_port") + ' ' + __settings__.getSetting("trans_username") + ' ' + __settings__.getSetting("trans_password") # the command line to disable transmission speed limited mode
        p = Popen(trans_cmd , shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        print("DLMGR: transmission unthrottle: ",out.rstrip(), err.rstrip())

    def onAbortRequested(self):
        print("DLMGR: XBMC is closing")
        os.system("sudo /etc/init.d/sickbeard start") #starts the sickbeard service
        trans_cmd = self.scriptPath + ' off ' + __settings__.getSetting("trans_port") + ' ' + __settings__.getSetting("trans_username") + ' ' + __settings__.getSetting("trans_password") # the command line to disable transmission speed limited mode
        p = Popen(trans_cmd , shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        print("DLMGR: transmission unthrottle: ",out.rstrip(), err.rstrip())

print("DLMGR: Download Manager Script Loaded")

monitor=Screensaver()

while not xbmc.abortRequested: #End if XBMC closes
    xbmc.sleep(5000) #Repeat (ms) 
