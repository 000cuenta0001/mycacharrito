#encoding=utf-8
import sys
import xbmcgui
import xbmcplugin
import xbmc
import urllib
import urllib2
import urlparse
import xbmcaddon
import os
import unicodedata
import json
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
my_addon = xbmcaddon.Addon()
PATH = my_addon.getAddonInfo('path')
def build_url(query):
    return base_url + '?' + urllib.urlencode(query)
mode = args.get('mode', None)
if mode is None:
    keys = sorted(json.loads(urllib2.urlopen(urllib2.Request("https://pastebin.com/raw/gRkZGEhX"),timeout=60).read().replace('\r', '').replace('\n', '').replace('\t', '').replace(' ','').replace('},]','}]')),key=lambda i:i['n'],reverse=False)
    for key in keys:
        url = build_url({'mode': 'change_the_fucking_key', 'n': key['n'], 'key': key['key'], 'id': key['id'],'secret': key['secret']})
        li = xbmcgui.ListItem('API KEY ' + str(key['n']), iconImage = PATH + '/icon.png')
        li.setInfo(type="Video", infoLabels={"plot": 'Cambiar la API KEY de YouTube'})
        li.setArt({'fanart': PATH + '/fanart.jpg'})
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
    xbmcplugin.endOfDirectory(addon_handle)
elif mode[0] == 'change_the_fucking_key':
    HOME = xbmc.translatePath('special://home/')
    USERDATA = os.path.join(HOME, 'userdata')
    ADDON_DATA = os.path.join(USERDATA, 'addon_data')
    YOUTUBE = os.path.join(ADDON_DATA, 'plugin.video.youtube')
    SETTINGS_FILE = os.path.join(YOUTUBE, 'settings.xml')
    if os.path.isfile(SETTINGS_FILE) == True:
        f = open(SETTINGS_FILE, "r")
        contenido = f.read()
        f.close()
        funcionando = 0
        keys = sorted(json.loads(urllib2.urlopen(urllib2.Request("https://pastebin.com/raw/gRkZGEhX"),timeout=60).read().replace('\r', '').replace('\n', '').replace('\t', '').replace(' ','').replace('},]','}]')),key=lambda i:i['n'],reverse=False)
        key_num = int(args['n'][0])
        total_keys = len(keys)
        DIALOG_PROGRESS = xbmcgui.DialogProgress()
        DIALOG_PROGRESS.create("Probando Keys", "")
        WINDOW_PROGRESS = xbmcgui.Window(10101)
        xbmc.sleep(100)
        CANCEL_BUTTON = WINDOW_PROGRESS.getControl(10)
        for x in range(key_num, total_keys+1):
            if DIALOG_PROGRESS.iscanceled():
                DIALOG_PROGRESS.close()
                break
            xbmc.sleep(500)
            DIALOG_PROGRESS.update(int((x)*100/total_keys), "[B]PROBANDO SI LA KEY " + str(keys[x-1]['n']) + " FUNCIONA...[/B]")
            try:
                test = urllib2.urlopen(urllib2.Request("https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCUV33rOY6Cmu1OptrDYLr7w&maxResults=50&key=" + keys[x-1]['key']),timeout=60).read()
            except:
                test = ''
            if '"kind"' in test:
                funcionando = 1
                contenido = contenido.replace('<setting id="youtube.api.enable">false</setting>', '<setting id="youtube.api.enable">true</setting>')
                contenido = contenido.replace('<setting id="youtube.api.enable" value="false" />', '<setting id="youtube.api.enable" value="true" />')
                xml_tipo = 1
                piece_id = contenido.split('<setting id="youtube.api.id">')
                if len(piece_id) < 2:
                    piece_id = contenido.split('<setting id="youtube.api.id" default="true">')
                if len(piece_id) < 2:
                    piece_id = contenido.split('<setting id="youtube.api.id" value="')
                    xml_tipo = 2
                if xml_tipo == 1:
                    piece_id2 = piece_id[1].split('</setting>')
                    piece_id2[0] = args['id'][0]
                    contenido = piece_id[0] + '<setting id="youtube.api.id">' + '</setting>'.join(piece_id2)
                else:
                    piece_id2 = piece_id[1].split('"')
                    piece_id2[0] = args['id'][0]
                    contenido = piece_id[0] + '<setting id="youtube.api.id" value="' + '"'.join(piece_id2)
                xml_tipo = 1
                piece_key = contenido.split('<setting id="youtube.api.key">')
                if len(piece_key) < 2:
                    piece_key = contenido.split('<setting id="youtube.api.key" default="true">')
                if len(piece_key) < 2:
                    piece_key = contenido.split('<setting id="youtube.api.key" value="')
                    xml_tipo = 2
                if xml_tipo == 1:
                    piece_key2 = piece_key[1].split('</setting>')
                    piece_key2[0] = args['key'][0]
                    contenido = piece_key[0] + '<setting id="youtube.api.key">' + '</setting>'.join(piece_key2)
                else:
                    piece_key2 = piece_key[1].split('"')
                    piece_key2[0] = args['key'][0]
                    contenido = piece_key[0] + '<setting id="youtube.api.key" value="' + '"'.join(piece_key2)
                xml_tipo = 1
                piece_secret = contenido.split('<setting id="youtube.api.secret">')
                if len(piece_secret) < 2:
                    piece_secret = contenido.split('<setting id="youtube.api.secret" default="true">')
                if len(piece_secret) < 2:
                    piece_secret = contenido.split('<setting id="youtube.api.secret" value="')
                    xml_tipo = 2
                if xml_tipo == 1:
                    piece_secret2 = piece_secret[1].split('</setting>')
                    piece_secret2[0] = args['secret'][0]
                    contenido = piece_secret[0] + '<setting id="youtube.api.secret">' + '</setting>'.join(piece_secret2)
                else:
                    piece_secret2 = piece_secret[1].split('"')
                    piece_secret2[0] = args['secret'][0]
                    contenido = piece_secret[0] + '<setting id="youtube.api.secret" value="' + '"'.join(piece_secret2)
                f = open(SETTINGS_FILE, "w")
                f.write(contenido)
                f.close()
                DIALOG_PROGRESS.close()
                xbmc.executebuiltin('XBMC.Notification(%s, %s, %s, %s)' % ('Funcionando!', 'La KEY ha sido cambiada a la número ' + str(x), 4000, PATH + '/icon.png'))
                break
            else:
                xbmc.sleep(500)
        DIALOG_PROGRESS.close()
        if funcionando == 0:
            xbmc.executebuiltin('XBMC.Notification(%s, %s, %s, %s)' % ('Ups', 'Ninguna KEY está funcionando...', 4000, PATH + '/icon.png'))
    else:
        xbmc.executebuiltin('XBMC.Notification(%s, %s, %s, %s)' % ('Ups', 'No se ha podido cambiar la KEY', 4000, PATH + '/icon.png'))