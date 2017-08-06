# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Addon de Acceso a las mejores webs de deportes en español by Bad-Max
# Version 0.0.1 (22.7.2017)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a la librería plugintools de Jesús (www.mimediacenter.info)


import os, sys, urllib, urllib2, re, shutil, zipfile
import xbmc, xbmcgui, xbmcaddon, xbmcplugin, time
import locale, time, random, plugintools, scrapertools
import plugintools
from arena_max import *
from dinozapmax import *
from verliganetmax import *
from dateutil.parser import parse

import requests


addon_path = xbmcaddon.Addon().getAddonInfo("path")

addonName           = xbmcaddon.Addon().getAddonInfo("name")
addonVersion        = xbmcaddon.Addon().getAddonInfo("version")
addonId             = xbmcaddon.Addon().getAddonInfo("id")
addonPath           = xbmcaddon.Addon().getAddonInfo("path")


home = xbmcaddon.Addon().getAddonInfo('path')+'/'
playlists = xbmc.translatePath(os.path.join('special://userdata/playlists', ''))
temp = xbmc.translatePath(os.path.join('special://userdata/playlists/tmp/', ''))
addons = xbmc.translatePath(os.path.join('special://home/addons/', ''))
art = xbmc.translatePath(os.path.join(addonPath,'art/'))
kodi = xbmc.translatePath(os.path.join('special://home/', ''))

thumbnail="http://i.imgur.com/pHeJ0Sy.png"
fanart="http://i.imgur.com/0InwiY9.png"



# Entry point
def run():
	plugintools.log('[%s %s] Running %s... ' % (addonName, addonVersion, addonName))
	datamovie={}
	# Obteniendo parámetros...
	params = plugintools.get_params()

	params["thumbnail"]=thumbnail
	params["fanart"]=fanart

    
	if params.get("action") is None:
		main_list(params)
	else:
		action = params.get("action")
		exec action+"(params)"
	'''

	main_list(params)
	#print '*'*35;sys.exit()
	'''

	plugintools.close_item_list()           



# Main menu
def act_home(params):xbmc.executebuiltin('ActivateWindow(10000,return)')

def main_list(params):
	plugintools.log("[%s %s] Checking updates... %s" % (addonName, addonVersion, repr(params)))    
	datamovie={}

	userdata = xbmc.translatePath(os.path.join('special://userdata/addon_data/plugin.video.purodeporte/', ''))
	if not os.path.exists(userdata):
		os.makedirs(userdata)
	
	plugintools.add_item(action="arena_badmax",url="",title="[COLOR red][B]-Arenavisión     [/B][COLOR blue][I](Parser p2p)[/I][/COLOR]",thumbnail="http://i.imgur.com/j0nm5TE.png",fanart="http://i52.fastpic.ru/big/2013/0411/4f/90ba9f4496ac42468023d639c407884f.jpg",info_labels=datamovie,folder=True,isPlayable=False)
	plugintools.add_item(action="verliganet_max",url="",title="[COLOR yellow][B]-VerLiga.net     [/B][COLOR blue][I](Parser Flash/Web)[/I][/COLOR]",thumbnail="http://i.imgur.com/VMVcrCl.png",fanart="http://i.imgur.com/CKigSre.png",info_labels=datamovie,folder=True,isPlayable=False)
	plugintools.add_item(action="dinozap_max",url="",title="[COLOR red][B]-DinoZap     [/B][COLOR blue][I](Parser Flash/Web)[/I][/COLOR]",thumbnail="http://i.imgur.com/OxBXS4I.png",fanart="http://i.imgur.com/VlYoRet.png",info_labels=datamovie,folder=True,isPlayable=False)
	plugintools.add_item(action="run_plugin",url="plugin://plugin.video.SportsDevil/?item=title%3dVipGoal.net%26url%3dlivesports%252Fvipgoal.cfg%26definedIn%3dlivesports.cfg%26director%3dVipGoal.net%26genre%3dLive%2bSports%26type%3drss%26icon%3dhttp%253A%252F%252Fwww.vipgoal.net%252FVIPgoal%252Fimg%252Flogo.png&mode=1",title="[COLOR yellow][B]-VipGoal.net     [/B][COLOR blue][I](Acceso a SportsDevil)[/I][/COLOR]",thumbnail="https://i1.wp.com/www.vipgoal.online/wp-content/uploads/2017/02/real-madris-vs-barcelona.jpg?fit=340%2C213",fanart="https://archive.is/gSuvP/35d863a4ba3005a091b94757b5d081d83016975f/scr.png",info_labels=datamovie,folder=True,isPlayable=False)
	plugintools.add_item(action="run_plugin",url="plugin://plugin.video.SportsDevil/?item=title%3dRojaDirecta.me%26url%3dlivesports%252Frojadirecta.me.cfg%26definedIn%3dlivesports.cfg%26director%3dRojaDirecta.me%26genre%3dLive%2bSports%26type%3drss%26icon%3dC%253A%255CUsers%255Cusuario%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.SportsDevil%255Cresources%255Cimages%255Croja.jpg&mode=1",title="[COLOR red][B]-RojaDirecta     [/B][COLOR blue][I](Acceso a SportsDevil)[/I][/COLOR]",thumbnail="http://rojadirectafg.com/wp-content/uploads/2014/04/rojadiredcta-hd.png",fanart="http://www.lavanguardia.com/r/GODO/LV/p4/WebSite/2017/02/08/Recortada/LV_20120831_LV_FOTOS_D_54345326425-kQ4H-U414135419318mPG-992x558@LaVanguardia-Web.jpg",info_labels=datamovie,folder=True,isPlayable=False)

	plugintools.add_item(action="act_home",url="",title="[COLOR green][B]-Salir del Addon[/B][/COLOR]",thumbnail="http://preguntame.net/wp-content/uploads/2014/04/Salir-adelante-SFW-Intro.jpg",fanart="http://radiobravissima.cl/wp-content/uploads/2017/05/e001-salida-de-emergencia-a-la-derecha.jpg")







	
		
run()


