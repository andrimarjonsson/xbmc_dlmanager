import xbmc
import xbmcaddon
from subprocess import Popen, PIPE

addonHandle = xbmcaddon.Addon(id="script.service.dlmanager")


class Screensaver(xbmc.Monitor):
    xbmc.log("DLMGR: Checking PlayBackState", xbmc.LOGDEBUG)

    def __init__(self):
        xbmc.Monitor.__init__(self)

    def onScreensaverDeactivated(self):
        xbmc.log("DLMGR: XBMC in use", xbmc.LOGDEBUG)

        # Stop sickbeard
        sick_cmd = "echo " + addonHandle.getSetting("sudo_pass") + " | sudo /etc/init.d/sickbeard stop"
        p = Popen(sick_cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        xbmc.log("DLMGR: sickbeard stop: %s %s" % (out.rstrip(), err.rstrip()), xbmc.LOGDEBUG)

        # Throttle transmission
        trans_cmd = addonHandle.getSetting("trans_path") + 'transmission-remote --auth=' \
            + addonHandle.getSetting("trans_username") + ':' \
            + addonHandle.getSetting("trans_password") + ' -as'
        p = Popen(trans_cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        xbmc.log("DLMGR: transmission throttle: %s %s" % (out.rstrip(), err.rstrip()), xbmc.LOGDEBUG)

        xbmc.executebuiltin("Notification(Download Manager,Sickbeard stopped. Transmission throttled.)")

    def onScreensaverActivated(self):
        xbmc.log("DLMGR: XBMC in standby", xbmc.LOGDEBUG)

        # Start sickbeard
        sick_cmd = "echo " + addonHandle.getSetting("sudo_pass") + " | sudo /etc/init.d/sickbeard start"
        p = Popen(sick_cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        xbmc.log("DLMGR: sickbeard start: %s %s" % (out.rstrip(), err.rstrip()), xbmc.LOGDEBUG)

        # Disable transmission throttle
        trans_cmd = addonHandle.getSetting("trans_path") + 'transmission-remote --auth=' \
            + addonHandle.getSetting("trans_username") + ':' \
            + addonHandle.getSetting("trans_password") + ' -AS'
        p = Popen(trans_cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        xbmc.log("DLMGR: transmission unthrottle: %s %s" % (out.rstrip(), err.rstrip()), xbmc.LOGDEBUG)

    def onAbortRequested(self):
        xbmc.log("DLMGR: XBMC is closing", xbmc.LOGDEBUG)

        # Start sickbeard
        sick_cmd = "echo " + addonHandle.getSetting("sudo_pass") + " | sudo /etc/init.d/sickbeard start"
        p = Popen(sick_cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        xbmc.log("DLMGR: sickbeard start: %s %s" % (out.rstrip(), err.rstrip()), xbmc.LOGDEBUG)

        # Disable transmission throttle
        trans_cmd = addonHandle.getSetting("trans_path") + 'transmission-remote --auth=' \
            + addonHandle.getSetting("trans_username") + ':' \
            + addonHandle.getSetting("trans_password") + ' -AS'
        p = Popen(trans_cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        xbmc.log("DLMGR: transmission unthrottle: %s %s" % (out.rstrip(), err.rstrip()), xbmc.LOGDEBUG)

xbmc.log("DLMGR: Download Manager Script Loaded", xbmc.LOGDEBUG)

monitor = Screensaver()

while not xbmc.abortRequested:  # End if XBMC closes
    xbmc.sleep(5000)  # Repeat (ms)
