# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Analizador de medios de PalcoMax
# Version 0.1 (11/12/2015)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a Juarrox
#------------------------------------------------------------

import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
import plugintools
import urllib2
import HTMLParser
import urllib,urlparse

from BeautifulSoup import BeautifulSoup as bs
import json

from __main__ import *

addonName           = xbmcaddon.Addon().getAddonInfo("name")
addonVersion        = xbmcaddon.Addon().getAddonInfo("version")
addonId             = xbmcaddon.Addon().getAddonInfo("id")
addonPath           = xbmcaddon.Addon().getAddonInfo("path")

def plugin_analyzer(data, title, plot, datamovie, thumbnail, fanart):
    plugintools.log("[%s %s] Analizando plugin... %s " % (addonName, addonVersion, fanart))
    
    if data.startswith("plugin://plugin.video.SportsDevil/") == True:
        url = data.strip()
        plugintools.add_item( action = "play" , title = '[COLOR white]' + title + '[/COLOR]', url = url , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = True , isPlayable = False )

    elif data.startswith("plugin://plugin.video.f4mTester") == True:
        plugintools.add_item( action = "runPlugin" , title = '[COLOR white]' + title + '[/COLOR]', plot = plot , url = data.strip() , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = False , isPlayable = True )
                    
    elif data.startswith("plugin://plugin.video.youtube") == True:
        if data.startswith("plugin://plugin.video.youtube/channel/") == True:
            plugintools.add_item( action = "runPlugin" , title = '[COLOR white]' + title + '[/COLOR]', url = data.strip() , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = True , isPlayable = False )            
        elif data.startswith("plugin://plugin.video.youtube/user/") == True:
            plugintools.add_item( action = "runPlugin" , title = '[COLOR white]' + title + '[/COLOR]', url = data.strip() , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = True , isPlayable = False )
        elif data.startswith("plugin://plugin.video.youtube/playlist/") == True:
            plugintools.add_item( action = "runPlugin" , title = '[COLOR white]' + title + '[/COLOR]', url = data.strip() , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = True , isPlayable = False )            
        elif data.startswith("plugin://plugin.video.youtube/play/?playlist_id") == True:
            plugintools.add_item( action = "runPlugin" , title = '[COLOR white]' + title + '[/COLOR]', url = data.strip() , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = True , isPlayable = False )            
        else:
            plugintools.runAddon( action = "play" , title = '[COLOR white]' + title + '[/COLOR]', url = data.strip() , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = False , isPlayable = True )
       
    elif data.find("plugin.video.p2p-streams") == True:                        
        if data.find("mode=1") >= 0 :  # Acestream
            plugintools.add_item( action = "runPlugin" , title = '[COLOR white]' + title + '[COLOR lightyellow][I] [Acestream][/I][/COLOR]' , plot = plot , url = data.strip() , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = False , isPlayable = True )
                        
        elif data.find("mode=2") >= 0 :  # Sopcast
            plugintools.add_item( action = "runPlugin" , title = '[COLOR white]' + title + '[COLOR lightyellow][I] [SopCast][/I][/COLOR]' , plot = plot , url = data.strip() , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = False , isPlayable = True )

        elif data.find("mode=401") >= 0 :  # P2P-Streams Parser
            plugintools.add_item( action = "runPlugin" , title = '[COLOR white]' + title + '[COLOR lightyellow][I] [p2p][/I][/COLOR]' , plot = plot , url = data.strip() , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = True , isPlayable = False )            

    elif data.startswith("plugin://plugin.video.p2psport") == True:
        plugintools.add_item( action = "runPlugin" , title = '[COLOR white]' + title + '[COLOR lightyellow][I] [p2p][/I][/COLOR]', url = data.strip() , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = True , isPlayable = False )

    elif data.startswith("plugin://plugin.video.live.streamspro") == True:
        if data.strip().find("mode=1&name=") >=0 or data.strip().find("makelist") >=0 :  # Parcheado por DMO: Soporte de pseudo parsers de LSP y listas  (DMO)
            plugintools.add_item( action = "runPlugin" , title = '[COLOR white]' + title + '[/COLOR]', url = data.strip() , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = True , isPlayable = False )
        else:
            plugintools.runAddon( action = "runPlugin" , title = '[COLOR white]' + title + '[/COLOR]', url = data.strip() , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = False , isPlayable = False )
            
    elif data.startswith("plugin://plugin.video.dailymotion_com") == True:  # Dailymotion (2.1.5)
        if data.find("mode=showPlaylist") >= 0:
            plugintools.add_item( action = "runPlugin" , title = '[COLOR white]' + title + '[/COLOR]', url = data , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = True , isPlayable = False )
        else:
            plugintools.runAddon( action = "play" , title = '[COLOR white]' + title + '[/COLOR]', url = data , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = False , isPlayable = False )

    elif data.startswith("plugin://plugin.video.videodevil") == True:  # VideoDevil modules
        plugintools.add_item( action = "play" , title = '[COLOR white]' + title + '[/COLOR]', url = data.strip() , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = True , isPlayable = False )          
		
    elif data.startswith("plugin://plugin.video.pelisalacarta") == True:  # Pelisalacarta
        plugintools.add_item( action = "runPlugin" , title = '[COLOR white]' + title + '[/COLOR]' , url = data.strip() , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = True , isPlayable = False )

    elif data.startswith("plugin://script.extendedinfo") == True:
        plugintools.add_item( action = "runPlugin" , title = '[COLOR white]' + title + '[/COLOR]' , url = data.strip() , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = True , isPlayable = False )

    elif data.startswith("plugin://plugin.video.pulsar/movie/") == True:
        plugintools.add_item( action = "runPlugin" , title = '[COLOR white]' + title + '[COLOR lightyellow][I] [p2p][/I][/COLOR]' , url = data.strip() , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = True , isPlayable = False )        

    else:        
        plugintools.add_item( action = "play" , title = '[COLOR white]' + title + '[/COLOR]' , url = data.strip() , info_labels = datamovie, thumbnail = thumbnail , fanart = fanart , folder = True , isPlayable = False )
      

def p2p_builder_url(url, title_fixed, p2p):

    if p2p == "ace":
        p2p_launcher = plugintools.get_setting("p2p_launcher")
        plugintools.log("p2p_launcher= "+p2p_launcher)        
        if p2p_launcher == "0":
            url = 'plugin://program.plexus/?url='+url+'&mode=1&name='+title_fixed
        else:
            url = 'plugin://plugin.video.p2p-streams/?url='+url+'&mode=1&name='+title_fixed

    elif p2p == "sop":
        p2p_launcher = plugintools.get_setting("p2p_launcher")
        plugintools.log("p2p_launcher= "+p2p_launcher)
        if p2p_launcher == "0":
            url = 'plugin://program.plexus/?url='+url+'&mode=2&name='+title_fixed
        else:
            url = 'plugin://plugin.video.p2p-streams/?url='+url+'&mode=2&name='+title_fixed

    elif p2p == "torrent":
        url = urllib.quote_plus(url)
        addon_torrent = plugintools.get_setting("addon_torrent")
        if addon_torrent == "0":  # Stream (por defecto)
            url = 'plugin://plugin.video.stream/play/'+url
        elif addon_torrent == "1":  # Pulsar
            url = 'plugin://plugin.video.pulsar/play?uri=' + url
        elif addon_torrent == "2":  # Kmediatorrent
            url = 'plugin://plugin.video.kmediatorrent/play/'+url
        elif addon_torrent == "3":  # XBMCtorrent
            url = 'plugin://plugin.video.xbmctorrent/play?uri=' + url             
        elif addon_torrent == "4":  # Quasar
            url = 'plugin://plugin.video.quasar/play?uri=' + url
        elif addon_torrent == "5":  # YATP
            url = 'plugin://plugin.video.yatp/play?uri=' + url               

    elif p2p == "magnet":
        addon_magnet = plugintools.get_setting("addon_magnet")
        if addon_magnet == "0":  # Stream (por defecto)
            url = 'plugin://plugin.video.stream/play/'+url
        elif addon_magnet == "1":  # Pulsar
            url = 'plugin://plugin.video.pulsar/play?uri=' + url
        elif addon_magnet == "2":  # Kmediatorrent
            url = 'plugin://plugin.video.kmediatorrent/play/'+url
        elif addon_magnet == "3":  # XBMCtorrent
            url = 'plugin://plugin.video.xbmctorrent/play?uri=' + url             
        elif addon_magnet == "4":  # Quasar
            url = 'plugin://plugin.video.quasar/play?uri=' + url
        elif addon_magnet == "5":  # YATP
            url = 'plugin://plugin.video.yatp/play?uri=' + url               

    plugintools.log("[%s %s] Creando llamada para URL P2P... %s " % (addonName, addonVersion, url))
    return url

def video_analyzer(url):
    plugintools.log("[%s %s] Análisis de URL de vídeo... " % (addonName, addonVersion))

    if url.find("allmyvideos") >=0: server = "allmyvideos"
    elif url.find("vidspot") >= 0: server = "vidspot"
    elif url.find("played") >= 0: server = "playedto"
    elif url.find("streamin.to") >= 0: server = "streaminto"
    elif url.find("streamcloud") >= 0: server = "streamcloud"
    elif url.find("nowvideo") >= 0: server = "nowvideo"
    elif url.find("veehd") >= 0: server = "veehd"
    elif url.find("vk") >= 0: server = "vk"
    elif url.find("lidplay") >= 0: server = "vk"   
    elif url.find("tumi") >= 0: server = "tumi"
    elif url.find("novamov") >= 0: server = "novamov"
    elif url.find("moevideos") >= 0: server = "moevideos"
    elif url.find("gamovideo") >= 0: server = "gamovideo"
    elif url.find("movshare") >= 0: server = "movshare"
    elif url.find("powvideo") >= 0: server = "powvideo"
    elif url.find("mail.ru") >= 0: server = "mailru"
    elif url.find("mediafire") >= 0: server = "mediafire"
    elif url.find("netu") >= 0: server = "netu"
    elif url.find("movreel") >= 0: server = "movreel"
    elif url.find("videobam") >= 0: server = "videobam"
    elif url.find("vimeo/videos") >= 0: server = "vimeo"
    elif url.find("vimeo/channels") >= 0: server = "vimeo_pl"        
    elif url.find("veetle") >= 0: server = "veetle"
    elif url.find("videoweed") >= 0: server = "videoweed"
    elif url.find("streamable") >= 0: server = "streamable"
    elif url.find("rocvideo") >= 0: server = "rocvideo"
    elif url.find("realvid") >= 0: server = "realvid"
    elif url.find("videomega") >= 0: server = "videomega"
    elif url.find("video.tt") >= 0: server = "videott"
    elif url.find("flashx") >= 0: server = "flashx"
    elif url.find("waaw") >= 0: server = "waaw"
    elif url.find("openload") >= 0: server = "openload"
    elif url.find("turbovideos") >= 0: server = "turbovideos"
    elif url.find("ok.ru") >= 0: server = "okru"
    elif url.find("vidto") >= 0: server = "vidtome"
    elif url.find("playwire") >= 0: server = "playwire"     
    elif url.find("vimple") >= 0: server = "vimple"
    elif url.find("vidgg") >= 0: server = "vidggto"
    elif url.find("uptostream") >= 0: server = "uptostream"
    elif url.find("youwatch") >= 0: server = "youwatch"
    elif url.find("idowatch") >= 0: server = "idowatch"
    elif url.find("cloudtime") >= 0: server = "cloudtime"
    elif url.find("allvid") >= 0: server = "allvid"
    elif url.find("vodlocker") >= 0: server = "vodlocker"
    elif url.find("vidzi") >= 0: server = "vidzitv"
    elif url.find("streame") >= 0: server = "streamenet"
    elif url.find("myvideoz") >= 0: server = "myvideoz"
    elif url.find("streamplay") >= 0: server = "streamplay"
    elif url.find("watchonline") >= 0: server = "watchonline"
    elif url.find("rutube") >= 0: server = "rutube"
    elif url.find("dailymotion") >= 0: server = "dailymotion"
    elif url.find("auroravid") >= 0: server = "auroravid"
    elif url.find("wholecloud") >= 0: server = "wholecloud"
    elif url.find("bitvid") >= 0: server = "bitvid"
    elif url.find("spruto") >= 0: server = "spruto"
    elif url.find("stormo") >= 0: server = "stormo"
    elif url.find("myvi.ru") >= 0: server = "myviru"
    elif url.find("youtube") >= 0: server = "youtube"
    elif url.find("filmon") >= 0: server = "filmon"
    elif url.find("thevideo.me") >= 0: server = "thevideome"
    elif url.find("videowood") >= 0: server = "videowood"
    elif url.find("neodrive") >= 0: server = "neodrive"
    elif url.find("thevideobee") >= 0: server = "thevideobee"
    elif url.find("fileshow") >= 0: server = "fileshow"
    elif url.find("vid.ag") >= 0: server = "vid"
    elif url.find("vidxtreme") >= 0: server = "vidxtreme"
    elif url.find("vidup") >= 0: server = "vidup"
    elif url.find("watchvideo") >= 0: server = "watchvideo"
    elif url.find("speedvid") >= 0: server = "speedvid"
    elif url.find("chefti.info") >= 0: server = "exashare"
    elif url.find("vodbeast") >= 0: server = "vodbeast"
    elif url.find("nosvideo") >= 0: server = "nosvideo"
    elif url.find("noslocker") >= 0: server = "noslocker"
    elif url.find("exashare") >= 0: server = "exashare"
    elif url.find("thevideobee") >= 0: server = "thevideobee"
    elif url.find("letwatch") >= 0: server = "letwatch"
    elif url.find("greevid") >= 0: server = "greevid"
    elif url.find("smartvid") >= 0: server = "smartvid"    
    else: server = 'unknown'

    return server
    

def parser_title(title):
    #plugintools.log('[%s %s].parserr_title %s' % (addonName, addonVersion, title))

    cyd=title;patcolor=plugintools.find_multiple_matches(cyd, '\[([^\]]+)')
    for entry in patcolor:
        entry='['+entry+']'
        cyd=cyd.replace(entry, "")

    cyd=cyd.replace("/", "").replace("[", "").replace("]", "").replace("&quot;", '"')
    cyd=cyd.replace("[/COLOR]", "").replace("[B]", "").replace("[/B]", "").replace("[I]", "").replace("[/I]", "")
    cyd=cyd.replace("[Auto]", "").replace("[Parser]", "").replace("[TinyURL]", "").replace("[Auto]", "").replace("[Filtros]", "").replace("[Filtro]", "")    
    cyd = cyd.replace("[", "").replace("]", "").replace("[B]", "").replace("[I]", "").replace("[/B]", "").replace("[/I]", "")  # Control para evitar errores al crear archivos

    # Control para evitar filenames con corchetes
    cyd = cyd.replace(" [Lista M3U]", "")
    cyd = cyd.replace(" [Lista PLX]", "")
    cyd = cyd.replace(" [Multilink]", "")
    cyd = cyd.replace(" [Multi]", "").replace("[Multi]", "")
    cyd = cyd.replace(" [Multiparser]", "")
    cyd = cyd.replace(" [COLOR orange][Lista [B]PLX[/B]][/COLOR]", "")
    cyd = cyd.replace(" [COLOR orange][Lista [B]M3U[/B]][/COLOR]", "")
    cyd = cyd.replace(" [COLOR lightyellow][B][Dailymotion[/B] playlist][/COLOR]", "")
    cyd = cyd.replace(" [COLOR lightyellow][B][Dailymotion[/B] video][/COLOR]", "")
    cyd = cyd.replace(' [COLOR gold][CBZ][/COLOR]', "")
    cyd = cyd.replace(' [COLOR gold][CBR][/COLOR]', "")
    cyd = cyd.replace(' [COLOR gold][Mediafire][/COLOR]', "")
    cyd = cyd.replace(' [CBZ]', "")
    cyd = cyd.replace(' [CBR]', "")
    cyd = cyd.replace(' [Mediafire]', "")
    cyd = cyd.replace(' [EPG-TXT]', "")    

    title=cyd
    if title.endswith(" .plx") == True:
        title = title.replace(" .plx", ".plx")

    return cyd


def launch_magnet(params):
    plugintools.log('[%s %s] launch_magnet... %s' % (addonName, addonVersion, repr(params)))
    url = params.get("url")
    addon_magnet = plugintools.get_setting("addon_magnet")
    plugintools.log("Addon para ejecutar archivo Magnet: "+addon_magnet)
    #url = urllib.quote_plus(url)
    if addon_magnet == "0":  # Stream (por defecto)
        url = 'plugin://plugin.video.stream/play/'+url
        plugintools.log("Iniciando Stream... "+url)
    elif addon_magnet == "1":  # Pulsar
        url = 'plugin://plugin.video.pulsar/play?uri=' + url
        plugintools.log("Iniciando Pulsar... "+url)
    elif addon_magnet == "2":  # KMediaTorrent
        url = 'plugin://plugin.video.kmediatorrent/play/'+url
        plugintools.log("Iniciando KMediaTorrent... "+url)
    elif addon_magnet == "3":  # XBMCtorrent
        url = 'plugin://plugin.video.xbmctorrent/play/'+url
        plugintools.log("Iniciando XBMCtorrent... "+url)
    elif addon_magnet == "4":  # Quasar
        url = 'plugin://plugin.video.quasar/play?uri=' + url
        plugintools.log("Iniciando Quasar... "+url)      
        
    plugintools.log("Magnet URL= "+url)
    plugintools.play_resolved_url(url)



def launch_torrent(params):
    plugintools.log('[%s %s] launch_torrent... %s' % (addonName, addonVersion, repr(params)))
    url = params.get("url")

    addon_torrent = plugintools.get_setting("addon_torrent")
    #url = urllib.quote_plus(url)
    if addon_torrent == "0":  # Stream (por defecto)
        url = 'plugin://plugin.video.stream/play/'+url
        plugintools.log("Iniciando Stream... "+url)
    elif addon_torrent == "1":  # Pulsar
        url = 'plugin://plugin.video.pulsar/play?uri=' + url
        plugintools.log("Iniciando Pulsar... "+url)
    elif addon_torrent == "2":  # XBMCtorrent
        url = 'plugin://plugin.video.xbmctorrent/play/' + url
        plugintools.log("Iniciando XBMCtorrent... "+url)
    elif addon_torrent == "3":  # Plexus
        plugintools.log("Iniciando Plexus... "+url)
        url = 'plugin://plugin.program.plexus/?url=http://'+url+'&mode=1&name='
    elif addon_torrent == "4":  # Quasar
        url = 'plugin://plugin.video.quasar/play?uri=' + url
        plugintools.log("Iniciando Quasar... "+url)   

    plugintools.log("Torrent File= "+url)
    plugintools.play_resolved_url(url)
    



def devil_analyzer(url,ref):
    url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='+url+'%26referer='+referer
    xbmc.executebuiltin('XBMC.RunPlugin(' + url +')')
