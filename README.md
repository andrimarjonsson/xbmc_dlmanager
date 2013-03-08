XBMC script.service.dlmanager
==============

An addon for xbmc which stops sickbeard and throttles transmission speed during video playback.

I run XBian on a Raspberry Pi which I've found is unable to playback HD video while Sickbeard is doing a scan or if torrents in transmission are downloading at more than ~200k/s. This addon stops the sickbeard service and turns on speed limited mode in transmission any time the XBMC screensaver is disabled. Once the screensaver comes back on, sickbeard is restarted and the transmission speed limit mode is disabled.

##installation##

 *  configure your speed limit settings in transmission by editing your settings.json (located at /usr/local/etc/transmission/settings.json by default)
 *  extract the files into your xbmc/addons in a sub-directorycalled "script.service.dlmanager"
 *  in XBMC go to the addon's config: system -> settings -> add-ons -> enabled add-ons -> services -> Download Manager -> config
 *  enter your transmission RPC username / password (there is also an option for the directory path where your transmission-remote binary is stored the default should be correct for any normal apt-get install of transmission)
 *  enter the sudo password for the user which runs XBMC

##todo##

 *  allow configuration of speed limit settings with in XBMC addon config
 *  add support for couchpotato and headphones?

##change log##

v0.3
----

 *  replaced shell script with python call to transmission-remote to control transmission
 *  changed sudo command to control sickbeard to include password in command line (removing the need to edit your /etc/sudoers file)
 *  added changelog.txt so these notes can be seen inside XBMC

v0.2
----

 *  replaced hardcoded path with XBMC way of working out script location
 *  added settings.xml so transmission rpc port, user and pass can be set from with in XBMC rather than editing files
 *  refactored into one shell script

v0.1
----

 *  initial build
 *  has hardcoded paths (naughty)