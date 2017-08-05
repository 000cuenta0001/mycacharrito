# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Parser de VerLiga.net by Bad-Max
# Version 0.1 (07.06.2017)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
#------------------------------------------------------------

import os
import sys
import urllib
import urllib2
import re

import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
import time

import plugintools, requests, resolvers, media_analyzer
from __main__ import *
#from datetime import datetime
import datetime, locale
from datetime import datetime, timedelta



playlists = xbmc.translatePath(os.path.join('special://userdata/playlists', ''))
temp = xbmc.translatePath(os.path.join('special://userdata/playlists/tmp', ''))

addonName           = xbmcaddon.Addon().getAddonInfo("name")
addonVersion        = xbmcaddon.Addon().getAddonInfo("version")
addonId             = xbmcaddon.Addon().getAddonInfo("id")
addon_path           = xbmcaddon.Addon().getAddonInfo("path")

thumbnail = 'http://i.imgur.com/VMVcrCl.png'
fanart = 'http://i.imgur.com/CKigSre.png'

#Para compatibilidad con Kodis inferiores al 17
kodi_viejo = xbmc.translatePath(os.path.join(addon_path+"/kodi16.txt"))
kodi16 = False
if os.path.exists(kodi_viejo):
	kodi16 = True

url = 'http://www.verliga.net'
	
url_ref = 'http://www.verliga.net/'


version = "(v0.0.2)"

def verliganet_max(params):
	plugintools.log("[%s %s] http://wwww.verliga.net %s " % (addonName, addonVersion, repr(params)))

	plugintools.add_item(action="",url="",title="[COLOR blue][B]                 VerLiga.net[/B]   [I]"+version+"[/I][/COLOR][COLOR yellow][I]    **** byBad-Max ****[/I][/COLOR]",thumbnail=thumbnail,fanart=fanart,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=thumbnail, fanart=fanart, folder=False, isPlayable=False)
	
	r = requests.get(url)	
	data = r.content
	#vamos a agrupar la agenda x dias
	agenda = plugintools.find_multiple_matches(data,'p><center><h3(.*?)</tbody')

	for item in agenda:
		dia = "[COLOR orange]   ***" + plugintools.find_single_match(item,'>(.*?)<') + "***[/COLOR]"
		plugintools.add_item(action="",url="",title=dia,thumbnail="http://i.imgur.com/fsnLX0I.png",fanart=fanart,folder=False,isPlayable=False)

		eventos = plugintools.find_multiple_matches(item,'<span class="t(.*?)/a>')
		
		for evento in eventos:
			hora = "[COLOR red][B][I](" + plugintools.find_single_match(evento,'>(.*?)<') + "h)->[/B][/I][/COLOR]"
			partido = "[COLOR green][B](" + plugintools.find_single_match(evento,'<strong>(.*?)</td') + "h)[/B][/COLOR]"
			partido = partido.replace("</strong>" , "")
			link =  plugintools.find_single_match(evento,'href="(.*?)"')
			logo =""
			logo =  plugintools.find_single_match(evento,'src="(.*?)"')
			if len(logo) == 0:
				logo = thumbnail
			
			linea = hora + partido

			url_montada = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='+link+"%26icon%3d"+logo+'%26referer='+url_ref
			plugintools.add_item(action="runPlugin",title=linea,url=url_montada,thumbnail=logo,fanart=fanart,folder=False,isPlayable=True)
			
			
			
		

	
	
	
	
	
	
	
	
