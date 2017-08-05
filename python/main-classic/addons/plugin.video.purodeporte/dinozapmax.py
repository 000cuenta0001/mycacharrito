# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Parser de http://www.dinozap.info by Bad-Max
# Version 0.9 (19.06.2016)
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

import plugintools, requests
from resolvers import *
from media_analyzer import *
from __main__ import *
from datetime import datetime


playlists = xbmc.translatePath(os.path.join('special://userdata/playlists', ''))
temp = xbmc.translatePath(os.path.join('special://userdata/playlists/tmp', ''))

addonName           = xbmcaddon.Addon().getAddonInfo("name")
addonVersion        = xbmcaddon.Addon().getAddonInfo("version")
addonId             = xbmcaddon.Addon().getAddonInfo("id")
addonPath           = xbmcaddon.Addon().getAddonInfo("path")

thumbnail = 'http://i.imgur.com/OxBXS4I.png'
fanart = 'http://i.imgur.com/VlYoRet.png'

#url = 'http://www.dinozap.info'
#url_ref = 'http://www.dinozap.info/'
#url_agenda = 'http://www.dinozap.info/prog.txt'
#url = 'http://www.dinozap.tv'
url = 'http://dinozap.info'
#url_ref = 'http://www.dinozap.tv/'
url_ref = 'http://dinozap.info/'
url_agenda = 'http://www.dinozap.tv/prog.txt'

def dinozap_max(params):
	plugintools.log("[%s %s] http://www.dinozap.tv %s " % (addonName, addonVersion, repr(params)))

	r = requests.get(url)	
	data = r.content

	plugintools.add_item(action="",url="",title="[COLOR blue][B]                 DinoZap[/B] [I](v1.02)[/I][/COLOR][COLOR yellow][I]    **** by Bad-Max ****[/I][/COLOR]",thumbnail=thumbnail,fanart=fanart,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=thumbnail, fanart=fanart, folder=False, isPlayable=False)

	periodo_agenda = plugintools.find_single_match(data,'Schedule(.*?)<')
	periodo_agenda = "[COLOR red][I]Agenda: " + periodo_agenda.strip().upper().replace("FROM","Desde el  ").replace("TO","  a el  ") + "[/I][/COLOR]"

	plugintools.add_item(action="dinozaping",url="",title="[COLOR skyblue]·····¿Hacemos DinoZapping?·····[/COLOR]",thumbnail=thumbnail,fanart=fanart,folder=True,isPlayable=False)

	plugintools.add_item(action="",url="",title="",thumbnail=thumbnail, fanart=fanart, folder=False, isPlayable=False)
	plugintools.add_item(action="",url="",title=periodo_agenda,thumbnail=thumbnail, fanart=fanart, folder=False, isPlayable=False)
	
	r = requests.get(url_agenda)	
	data = r.content
	
	fh = open(temp + "/prog.txt", "wb")
	fh.write(data)
	fh.close()
	
	agendatxt = open(temp + "/prog.txt",'r')
	lineas=agendatxt.readlines()
	agendatxt.close()

	accion = ""
	canal = ""
	for lin_actu in lineas:
		
		milinea = ""
		es_dia = False
		
		if lin_actu.upper().find("MONDAY") >= 0:
			milinea = "[COLOR lightgreen][B]···" + lin_actu.upper().replace("MONDAY","Lunes") + "···[/B][/COLOR]"
			es_dia = True

		elif lin_actu.upper().find("TUESDAY") >= 0:
			milinea = "[COLOR lightgreen][B]···" + lin_actu.upper().replace("TUESDAY","Martes") + "···[/B][/COLOR]"
			es_dia = True

		elif lin_actu.upper().find("WEDNESDAY") >= 0:
			milinea = "[COLOR lightgreen][B]···" + lin_actu.upper().replace("WEDNESDAY","Miercoles") + "···[/B][/COLOR]"
			es_dia = True

		elif lin_actu.upper().find("THURSDAY") >= 0:
			milinea = "[COLOR lightgreen][B]···" + lin_actu.upper().replace("THURSDAY","Jueves") + "···[/B][/COLOR]"
			es_dia = True

		elif lin_actu.upper().find("FRIDAY") >= 0:
			milinea = "[COLOR lightgreen][B]···" + lin_actu.upper().replace("FRIDAY","Viernes") + "···[/B][/COLOR]"
			es_dia = True

		elif lin_actu.upper().find("SATURDAY") >= 0:
			milinea = "[COLOR lightgreen][B]···" + lin_actu.upper().replace("SATURDAY","Sabado") + "···[/B][/COLOR]"
			es_dia = True

		elif lin_actu.upper().find("SUNDAY") >= 0:
			milinea = "[COLOR lightgreen][B]···" + lin_actu.upper().replace("SUNDAY","Domingo") + "···[/B][/COLOR]"
			es_dia = True
			
		elif lin_actu.upper().find("EMBED") >= 0:
			milinea = "[COLOR green][B]" + lin_actu.upper().replace("EMBED","Canal") + "[/B][/COLOR]"
			accion = "opciones_dino"
			lin_provi = lin_actu.upper()
			canal = plugintools.find_single_match(lin_provi,'EMBED (.*?)\t').replace("'","").replace('"','')
			canal = canal.replace("#","")
			
		else:
			hora = plugintools.find_single_match(lin_actu,'(.*?)\t')

			if len(hora) == 0:  # Es una linea en Blanco
				lin_actu = "XXXX"

			else:
				if len(hora) == 4:  # Le falta un 0 delante
					hora = "0" + hora

				hora = "[COLOR red]" + hora + "-> [/COLOR]"
					
				partido = plugintools.find_single_match(lin_actu,'\t(.*?)\t')
				partido = "[COLOR yellow]" + partido + "[/COLOR]"
				lin_actu = lin_actu.replace("(","DMO1").replace(")","DMO2")
				idioma = plugintools.find_single_match(lin_actu,'DMO1(.*?)DMO2')
				idioma = "[COLOR red][I]    [" + idioma + "] [/I][/COLOR]"
				
				milinea = hora + partido + idioma
		
		if accion == "" or es_dia == True:
			esreproducible = False
		else:
			esreproducible = True
			
		if lin_actu.upper().find("XXXX") >= 0:  # Para la linea de X q pone entre un día y otro y no sirve para nada
			hacer = "Nada"
		else:
			milinea = milinea.replace("\t","").replace("\n","")
			
			if es_dia == True:
				plugintools.add_item(action="", title=milinea, url="", thumbnail=thumbnail, fanart=fanart, folder = False, isPlayable=False)
			else:
				plugintools.add_item(action=accion, title=milinea, url=canal, thumbnail=thumbnail, fanart=fanart, folder = True, isPlayable=False)
		
			
			
def dinozaping(params):			
	thumbnail = params.get("thumbnail")
	fanart = params.get("fanart")

	plugintools.add_item(action="",url="",title="[COLOR blue][B]                 DinoZapping[/B][/COLOR]",thumbnail=thumbnail,fanart=fanart,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=thumbnail, fanart=fanart, folder=False, isPlayable=False)

	canal=111
	while canal <= 150:
			
		plugintools.add_item(action="opciones_dino", title="Zapping canal "+str(canal), url=str(canal), thumbnail=thumbnail, fanart=fanart, folder = True, isPlayable=False)
		canal = canal + 1
		

		
		
def opciones_dino(params):
	thumbnail = params.get("thumbnail")
	fanart = params.get("fanart")
	titulo = params.get("title")
	milinea = params.get("title")
	canal = params.get("url")

	'''
	if "Zapping" in titulo:
		titulo2 = titulo + " ...Opción F4M"
	else:
		titulo2 = "Ver Evento de Canal " + canal + " ...Opción F4M"

	#enlace = "http://www.dinozap.info/redirect/channel.php?id=" + canal + "&width=650&height=450&autostart=true"
	enlace = "http://www.sunhd.info/channelsa.php?file=" + canal + "&width=650&height=450&autostart=true"
	url_montada = 'plugin://plugin.video.f4mTester/?streamtype=HLS&name=&url='+enlace.encode("utf8")            
	plugintools.add_item(action="runPlugin", title=titulo2, url=url_montada, thumbnail=thumbnail, fanart=fanart, folder = False, isPlayable=True)
	'''
	
	if "Zapping" in titulo:
		hacer = "Nada"
	else:	
		plugintools.add_item(action="",url="",title=milinea,thumbnail=thumbnail,fanart=fanart,folder=False,isPlayable=False)
		plugintools.add_item(action="",url="",title="**Paciencia, pueden tardar en cargar... Si tarda mucho, haz click una 2ª Vez**",thumbnail=thumbnail,fanart=fanart,folder=False,isPlayable=False)
		plugintools.add_item(action="",url="",title="",thumbnail=thumbnail, fanart=fanart, folder=False, isPlayable=False)

	if "Zapping" in titulo:
		titulo2 = titulo + " ...Opción SunHD"
	else:
		titulo2 = "Ver Evento de Canal " + canal + " ...Opción SunHD"
	enlace = "http://www.sunhd.info/channelsa.php?file=" + canal + "&width=650&height=450&autostart=true"
	url_montada = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url='+enlace+'%26referer='+"http://www.sunhd.info/"
	plugintools.add_item(action="runPlugin", title=titulo2, url=url_montada, thumbnail=thumbnail, fanart=fanart, folder = False, isPlayable=True)

	if "Zapping" in titulo:
		titulo2 = titulo + " ...Opción DinoZap"
	else:
		titulo2 = "Ver Evento de Canal " + canal + " ...Opción DinoZap"

	enlace = "http://www.dinozap.info/redirect/channel.php?id=" + canal + "&width=650&height=450&autostart=true"
	url_montada = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url='+enlace+'%26referer='+"http://www.dinozap.info/"
	plugintools.add_item(action="runPlugin", title=titulo2, url=url_montada, thumbnail=thumbnail, fanart=fanart, folder = False, isPlayable=True)
	'''
	if "Zapping" in titulo:
		titulo2 = titulo + " ...Opción DinoStream"
	else:
		titulo2 = "Ver Evento de Canal " + canal + " ...Opción DinoStream"

	enlace = "http://www.dinostream.pw/channel.php?file=" + canal + "&width=650&height=450&autostart=true"
	url_montada = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url='+enlace+'%26referer='+"http://www.dinostream.pw/"
	plugintools.add_item(action="runPlugin", title=titulo2, url=url_montada, thumbnail=thumbnail, fanart=fanart, folder = False, isPlayable=True)
	'''

