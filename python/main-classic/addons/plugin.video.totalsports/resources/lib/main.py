# -*- coding: utf-8 -*-

import sys
import time
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

# Compatibilidad Py2 / Py3
try:
    import urllib.request as urllib_request
except ImportError:
    import urllib2 as urllib_request

addon = xbmcaddon.Addon()
HANDLE = int(sys.argv[1])

LIST_URL = "https://dl.dropboxusercontent.com/scl/fi/ua0k1zunodoeulerkysf4/lista1AAA_IPTV.m3u?rlkey=4h35nwc7nm78m93yh5bke0pjg&st=7wrpyc23&dl=0"

ADDON_ICON = addon.getAddonInfo("icon")
ADDON_FANART = addon.getAddonInfo("fanart")


# ------------------------------------------------------------
# DESCARGA FORZADA (sin cache)
# ------------------------------------------------------------
def get_remote_data(url):
    try:
        sep = '&' if '?' in url else '?'
        url = "%s%st=%d" % (url, sep, int(time.time()))
        response = urllib_request.urlopen(url, timeout=10)
        data = response.read()
        response.close()
        if isinstance(data, bytes):
            data = data.decode("utf-8", "ignore")
        return data
    except:
        return None


# ------------------------------------------------------------
# PARSER M3U (solo lo necesario)
# ------------------------------------------------------------
def parse_m3u(data):
    items = []
    current = {}

    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue

        if line.startswith("#EXTINF"):
            current = {"title": "", "logo": "", "url": ""}

            if "," in line:
                current["title"] = line.split(",", 1)[1].strip()

            if 'tvg-logo="' in line:
                current["logo"] = line.split('tvg-logo="', 1)[1].split('"', 1)[0]

        elif not line.startswith("#") and current:
            current["url"] = line
            items.append(current)
            current = {}

    return items


# ------------------------------------------------------------
# LISTADO DE CANALES
# ------------------------------------------------------------
def list_videos():
    xbmcplugin.setContent(HANDLE, "videos")

    data = get_remote_data(LIST_URL)
    if not data:
        xbmcgui.Dialog().ok("Error", "No se pudo descargar la lista.")
        return

    items = parse_m3u(data)

    for ch in items:
        li = xbmcgui.ListItem(label=ch["title"])

        li.setProperty("IsPlayable", "true")

        li.setArt({
            "icon": ch["logo"] or ADDON_ICON,
            "thumb": ch["logo"] or ADDON_ICON,
            "fanart": ADDON_FANART
        })

        play_url = (
            sys.argv[0]
            + "?play=1"
            + "&url=" + urllib_request.quote(ch["url"], safe="")
            + "&title=" + urllib_request.quote(ch["title"], safe="")
        )

        xbmcplugin.addDirectoryItem(
            handle=HANDLE,
            url=play_url,
            listitem=li,
            isFolder=False
        )

    xbmcplugin.endOfDirectory(
        HANDLE,
        succeeded=True,
        updateListing=True,
        cacheToDisc=False
    )


# ------------------------------------------------------------
# REPRODUCCIÓN (PATRÓN CORRECTO)
# ------------------------------------------------------------
def play(params):
    url = params.get("url", "")
    title = params.get("title", "Canal")

    li = xbmcgui.ListItem(label=title, path=url)
    li.setProperty("IsPlayable", "true")

    xbmcplugin.setResolvedUrl(HANDLE, True, li)


# ------------------------------------------------------------
# ROUTER
# ------------------------------------------------------------
def get_params():
    params = {}
    if len(sys.argv) > 2 and sys.argv[2]:
        for p in sys.argv[2][1:].split("&"):
            if "=" in p:
                k, v = p.split("=", 1)
                params[k] = urllib_request.unquote(v)
    return params


if __name__ == "__main__":
    params = get_params()
    if params.get("play"):
        play(params)
    else:
        list_videos()