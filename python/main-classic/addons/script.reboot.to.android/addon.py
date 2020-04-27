import xbmcaddon
import xbmcgui
import os
import os.path
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

script_file = os.path.realpath(__file__)
directory = os.path.dirname(script_file)

os.system("sh "+directory+"/bin/reboot.to.android.sh "+directory)
