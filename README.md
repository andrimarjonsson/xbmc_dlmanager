XBMC script.service.dlmanager
==============

An addon for xbmc which stops sickbeard and throttles transmission speed during video playback.

I run XBian on a Raspberry Pi which I've found is unable to playback HD video while Sickbeard is doing a scan or if torrents in transmission are downloading at more than ~200k/s. This addon stops the sickbeard service and turns on speed limited mode in transmission any time the XBMC screensaver is disabled. Once the screensaver comes back on, sickbeard is restarted and the transmission speed limit mode is disabled.

##installation##

 *  configure your speed limit settings in transmission by editing your settings.json
 *  extract the files into your xbmc/addons directory in a subdir called "script.service.dlmanager"
 *          chmod 744 transmission_limit.sh
 *  in XBMC go to the addon's config and enter your transmission RPC port, username and password
 *  this addon uses sudo to stop the sickbeard service, so you will need to edit your /etc/sudoers file to allow the user which XBMC runs under to run "sudo /etc/init.d/sickbeard stop|start" with out prompting for password. The easiest way is to just allow all sudo commands with out password prompt by putting something like this in your /etc/sudoers file: 

            xbian ALL=(ALL) NOPASSWD: ALL #where xbian is the user which runs my XBMC.

There is some debug logging if you need to confirm that its working, just switch on debug in XBMC and check your xbmc.log.

##todo##

 *  replace shell script with python curl wrapper to control transmission
 *  add support for couchpotato and headphones?

##change log##

v0.2
----

 *  replaced hardcoded path with XBMC way of working out script location
 *  added settings.xml so transmission rpc port, user and pass can be set from with in XBMC rather than editing files
 *  refactored into one shell script

v0.1
----

 *  initial build
 *  has hardcoded paths (naughty)