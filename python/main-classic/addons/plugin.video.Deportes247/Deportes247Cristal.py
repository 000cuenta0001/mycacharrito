# -*- coding: utf-8 -*-

import sys,re,os
import urllib,urllib2
import urlparse

import xbmc,xbmcgui,xbmcaddon
import xbmcplugin
import threading

base_url        = sys.argv[0]
addon_handle    = int(sys.argv[1])
args            = urlparse.parse_qs(sys.argv[2][1:])
my_addon        = xbmcaddon.Addon()
addonName       = my_addon.getAddonInfo('name')
my_addon_id     = my_addon.getAddonInfo('id')

PATH            = my_addon.getAddonInfo('path')
DATAPATH        = xbmc.translatePath(my_addon.getAddonInfo('profile')).decode('utf-8')
RESOURCES       = PATH+'/resources/'

sys.path.append( os.path.join( RESOURCES, "lib" ) )

FANART=PATH+'/fanart.jpg'




def addLinkItem(name, url, mode, params=1, iconimage='DefaultFolder.png', infoLabels=False, IsPlayable=True,fanart=FANART,itemcount=1,contextmenu=None):
    u = build_url({'mode': mode, 'foldername': name, 'ex_link' : url, 'params':params})
    
    liz = xbmcgui.ListItem(name)
    
    art_keys=['thumb','poster','banner','fanart','clearart','clearlogo','landscape','icon']
    art = dict(zip(art_keys,[iconimage for x in art_keys]))
    art['landscape'] = fanart if fanart else art['landscape'] 
    art['fanart'] = fanart if fanart else art['landscape'] 
    liz.setArt(art)
    
    if not infoLabels:
        infoLabels={"title": name}
    liz.setInfo(type="video", infoLabels=infoLabels)
    if IsPlayable:
        liz.setProperty('IsPlayable', 'true')

    if contextmenu:
        contextMenuItems=contextmenu
        li.addContextMenuItems(contextMenuItems, replaceItems=True) 

    ok = xbmcplugin.addDirectoryItem(handle=addon_handle, url=u, listitem=liz,isFolder=False,totalItems=itemcount)
    xbmcplugin.addSortMethod(addon_handle, sortMethod=xbmcplugin.SORT_METHOD_NONE, label2Mask = "%R, %Y, %P")
    return ok

def addDir(name,ex_link=None, params=1, mode='folder',iconImage='DefaultFolder.png', infoLabels=None, fanart=FANART,contextmenu=None):
    url = build_url({'mode': mode, 'foldername': name, 'ex_link' : ex_link, 'params' : params})

    li = xbmcgui.ListItem(name)
    if infoLabels:
        li.setInfo(type="video", infoLabels=infoLabels)
    
    art_keys=['thumb','poster','banner','fanart','clearart','clearlogo','landscape','icon']
    art = dict(zip(art_keys,[iconImage for x in art_keys]))
    art['landscape'] = fanart if fanart else art['landscape'] 
    art['fanart'] = fanart if fanart else art['landscape'] 
    li.setArt(art)


    if contextmenu:
        contextMenuItems=contextmenu
        li.addContextMenuItems(contextMenuItems, replaceItems=True) 

    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,listitem=li, isFolder=True)
    xbmcplugin.addSortMethod(addon_handle, sortMethod=xbmcplugin.SORT_METHOD_NONE, label2Mask = "%R, %Y, %P")

def encoded_dict(in_dict):
    out_dict = {}
    for k, v in in_dict.iteritems():
        if isinstance(v, unicode):
            v = v.encode('utf8')
        elif isinstance(v, str):
            # Must be encoded in UTF-8
            v.decode('utf8')
        out_dict[k] = v
    return out_dict
    
def build_url(query):
    return base_url + '?' + urllib.urlencode(encoded_dict(query))


def Deportes247Thread(url):
    import Deportes247 as s
    from time import gmtime, strftime
    href,headers=url.split('|')
    header={}
    header['Referer']=urllib.unquote(re.compile('Referer=(.*?)&').findall(headers)[0])
    header['User-Agent']=urllib.unquote(re.compile('User-Agent=(.*?)&').findall(headers)[0])
    header['Origin']='http://h5.adshell.net'
    header['If-Modified-Since']=strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
    header['Connection']='keep-alive'
    header['etag']='"5820cda8-2b9"'
    print '#'*25
    print '#'*25
    xbmc.sleep(2000)    # speep
    player = xbmc.Player()
    player.pause()
    print 'Deportes247Thread: passed url: [%s] '%href
    #print header
    h=header
    while player.isPlaying():
        print 'Deportes247Thread: KODI IS PLAYING, sleeping 1s'
        a,hret=s.getUrlrh(href,header=header)
        header['etag'] = hret.get('etag','')
        header['date'] = hret.get('date','')
       
        #h.update(header)
        print a,hret
        xbmc.sleep(1000)
    print 'Deportes247Thread: KODI STOPPED, OUTSIDE WHILE LOOP ... EXITING'



def Deportes247Thread2(url,header):
    import Deportes247 as s
    import re
    
    player = xbmc.Player()
    xbmc.sleep(2000)    # speep
    print 'Deportes247Thread: passed url: [%s] '%url
    #print header
    player.pause()
    
    while player.isPlaying():
        print 'Deportes247Thread: KODI IS PLAYING, sleeping 4s'
        a,c=s.getUrlc(url,header=header,useCookies=True)
        banner =  re.compile('url:["\'](.*?)[\'"]').findall(a)[0]
        xbmc.log(banner)
        xbmc.sleep(2000)
        s.getUrlc(banner)
        xbmc.sleep(2000)
    print 'Deportes247Thread: KODI STOPED, OUTSIDE WHILE LOOP ... EXITING'


mode = args.get('mode', None)
fname = args.get('foldername',[''])[0]
ex_link = args.get('ex_link',[''])[0]
params = args.get('params',[{}])[0]

M3USERVICES={'telewizjada':'telewizjadabid',
             'amigostv': 'amigostv',
            'iklub':'iklub',
            'tele-wizja':'telewizja',
            'itivi':'itivi',
            'yoy.tv':'yoytv',
            'looknij.in':'looknijin',
            'wizja.tv':'wizjatv'}


if mode is None:

    addDir('[COLOR gold]                                                   *^Cristal Azul^*[/COLOR]',ex_link='',params={'_service':'cristalazul','_act':'ListChannels'}, mode='site2',iconImage=RESOURCES+'Deportes247.gif')
    addDir('[COLOR aqua]Deportes247[/COLOR]',ex_link='',params={'_service':'Deportes247','_act':'ListChannels'}, mode='site2',iconImage=RESOURCES+'icon.gif')


elif mode[0] == 'Opcje':
    path =  my_addon.getSetting('path')
    if not path: my_addon.setSetting('path',DATAPATH)
    my_addon.openSettings()  


elif mode[0] == 'UPDATE_IPTV':
    import pvr_m3u as pvr 
    fname = my_addon.getSetting('fname')
    path =  my_addon.getSetting('path')
    epgTimeShift = my_addon.getSetting('epgTimeShift')
    epgUrl = my_addon.getSetting('epgUrl')
    print 'UPDATE_IPTV',fname,path,epgTimeShift,epgUrl
    pvr.update_iptv(fname,path,epgTimeShift,epgUrl)

elif mode[0] == 'BUID_M3U':
    import pvr_m3u as pvr
    fname = my_addon.getSetting('fname')
    path =  my_addon.getSetting('path')
    service = my_addon.getSetting('service')
    error_msg=""
    if not fname:   error_msg +="Podaj nazwę pliku "
    if not path:    error_msg +="Podaj katalog docelowy "
    if not service: error_msg +="Wybierz jakieś Fuentes"
        
    if error_msg:
        xbmcgui.Dialog().notification('[COLOR red]ERROR[/COLOR]', error_msg, xbmcgui.NOTIFICATION_ERROR, 1000)
        pvr_path=  xbmc.translatePath(os.path.join('special://userdata/','addon_data','pvr.iptvsimple'))
        #print pvr_path
        if os.path.exists(os.path.join(pvr_path,'settings.xml')):
            print 'settings.xml exists'
    else:
        out_sum = pvr.build_m3u(fname,path,M3USERVICES.get(service))
        if len(out_sum)>1:
            xbmcgui.Dialog().ok('[COLOR green]Lista guardada[/COLOR] Kanałów: %d'%len(out_sum),'Plik: [COLOR blue]'+fname+'[/COLOR]','Uaktualnij ustawienia [COLOR blue]PVR IPTV Simple Client[/COLOR] i (re)aktywuj Live TV')
        else:
            xbmcgui.Dialog().ok('[COLOR red]Problema[/COLOR] ','Lista no guardada!!!')     
    my_addon.openSettings() 

elif mode[0] == 'AUTOm3u':
    import pvr_m3u as pvr
    fname = my_addon.getSetting('fname')
    path =  my_addon.getSetting('path')
    service = my_addon.getSetting('service')
    ret = pvr.build_m3u(fname,path,M3USERVICES.get(service))
    if ret:
        epgTimeShift = my_addon.getSetting('epgTimeShift')  
        epgUrl = my_addon.getSetting('epgUrl')
        pvr.update_iptv(fname,path,epgTimeShift,epgUrl)

elif mode[0] == 'UPDATE_CRON':
    import pvr_m3u as pvr
    auto_update_hour = my_addon.getSetting('auto_update_hour')
    auto_update_active =  my_addon.getSetting('auto_update_active')
    pvr.cron_update(auto_update_hour,auto_update_active)
    
elif mode[0] =='site':
    params = eval(params)
    service = params.get('_service')
    act = params.get('_act')
    mod = __import__(service)
    if act == 'ListChannels':
        params.update({'_act':'play'})
        items = mod.getChannels(ex_link)
        for one in items:
            addLinkItem(one.get('title',''), one['url'], params=params, mode='site', IsPlayable=True,infoLabels=one, iconimage=one.get('img','icon.gif'%(RESOURCES+service))) 
    elif act == 'play':
        streams = mod.getChannelVideo(ex_link)
        if isinstance(streams,list):
            print streams
            if len(streams)>1:
                label = [x.get('title') for x in streams]
                s = xbmcgui.Dialog().select('[COLOR gold]*^Fuentes^*[/COLOR]',label)
                stream_url = streams[s]
            elif streams:
                stream_url = streams[0]
            else: stream_url=''
        else:
            stream_url = streams
                  
        if stream_url:
            link = stream_url.get('url','')
            msg = stream_url.get('msg','')
            if link: xbmcplugin.setResolvedUrl(addon_handle, True,  xbmcgui.ListItem(path=link))
            else: 
                if msg: xbmcgui.Dialog().ok('Problema',msg)
                xbmcplugin.setResolvedUrl(addon_handle, False, xbmcgui.ListItem(path=''))
        else:
             xbmcplugin.setResolvedUrl(addon_handle, False, xbmcgui.ListItem(path=''))   


elif mode[0] =='site2':
    params = eval(params)
    service = params.get('_service')
    act = params.get('_act')
    mod = __import__(service)
    if act == 'ListChannels':
        params.update({'_act':'get_streams_play'})
        items = mod.getChannels(ex_link)
        img_service ='%s.gif'%(RESOURCES+service)
        print img_service
        for one in items:
            addLinkItem(one.get('title',''), one['url'], params=params, mode='site2', IsPlayable=True,infoLabels=one, iconimage=one.get('img',img_service)) 
    if act == 'get_streams_play':
        streams = mod.getStreams(ex_link)
        if streams:
            t = [stream.get('title') for stream in streams]
            s = xbmcgui.Dialog().select("[COLOR gold]*^Enlaces^*[/COLOR]", t)
            if s>-1: stream_url,url,header = mod.getChannelVideo(streams[s])
            else: stream_url=''
            if stream_url: 
                thread = threading.Thread(name='Deportes247Thread', target = Deportes247Thread2, args=[url,header])
                thread.start()
                xbmcplugin.setResolvedUrl(addon_handle, True, xbmcgui.ListItem(path=stream_url))
            else: xbmcplugin.setResolvedUrl(addon_handle, False, xbmcgui.ListItem(path=stream_url))
        else:
            xbmcgui.Dialog().textviewer('[COLOR aqua]DEPORTES 247[/COLOR]', '[COLOR white]Recomendaciones Deportes247:[/COLOR]\n\n[COLOR lightskyblue]-[COLOR red]Este enlace TODAVIA NO está activo PRUEBE entre 5  y 15 minutos antes del comienzo.[/COLOR]\n\n[COLOR lightskyblue]-[COLOR white]Los eventos estarán activos cuando tengan delante èste símbolo  "[COLOR lightgreen][B]*[/B][COLOR white]" .[/COLOR]\n\n[COLOR lightskyblue]-[COLOR white]Si tiene este addon a traves de un wizards y le piden donar, [COLOR red]NO DONEN[COLOR white].[/COLOR]\n[COLOR white]Éste proyecto es gratuito y RECHAZA las donaciones.[/COLOR]\n\n[COLOR lightskyblue]-[COLOR white]Consejo: Si no le funciona en un idioma, pruebe en otro.[/COLOR]\n\n[COLOR lightskyblue]-[COLOR white]¿Fuente oficial del addon?[/COLOR]\n    [COLOR gold]http://kodileia.xyz[/COLOR]\n\n[COLOR lightskyblue]-[COLOR white]Que ésto no me funciona:[/COLOR]\n[COLOR white]Estamos en telegram: [COLOR gold]https://t.me/addonfestaycristal [COLOR white]y en [COLOR gold]https://t.me/kodi18[/COLOR]\n\n\n\n\n\n\n\n\n                                                                                                                                                        [COLOR aqua]By Cristal Azul[/COLOR]')  
        
elif mode[0] == 'folder':
    pass

else:
    xbmcplugin.setResolvedUrl(addon_handle, False, xbmcgui.ListItem(path=''))        


xbmcplugin.endOfDirectory(addon_handle)

