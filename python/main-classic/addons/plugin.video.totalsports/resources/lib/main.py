# -*- coding: utf-8 -*-

import sys
import time
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

# -----------------------------
# Compatibilidad Py2 / Py3
# -----------------------------
try:
    import urllib.request as urllib_request
    from urllib.parse import quote, unquote
except ImportError:
    import urllib2 as urllib_request
    from urllib import quote, unquote

addon = xbmcaddon.Addon()
HANDLE = int(sys.argv[1])

LIST_URL = "https://dl.dropboxusercontent.com/scl/fi/0khvwyoah0xbosfcc85p7/lista1AAA_IPTV.m3u?rlkey=ytvn2dprcdzrpgl5797elm43l&st=o2jaa1ge&dl=0"

ADDON_ICON = addon.getAddonInfo("icon")
ADDON_FANART = addon.getAddonInfo("fanart")


# ------------------------------------------------------------
# UTILIDADES UNICODE SEGURAS (Py2 / Py3)
# ------------------------------------------------------------
def safe_quote(value):
    try:
        # Python 2
        if isinstance(value, unicode):
            value = value.encode("utf-8")
    except NameError:
        # Python 3
        if isinstance(value, str):
            value = value.encode("utf-8")
    return quote(value, safe="")


def safe_unquote(value):
    value = unquote(value)
    try:
        return value.decode("utf-8")
    except:
        return value


# ------------------------------------------------------------
# DESCARGA FORZADA (SIN CACHE)
# ------------------------------------------------------------
def get_remote_data(url):
    try:
        sep = "&" if "?" in url else "?"
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
# PARSER M3U (MÍNIMO NECESARIO)
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
        title = ch["title"]
        url = ch["url"]

        li = xbmcgui.ListItem(label=title)

        # NO forzar info técnica (codec, resolución, etc.)
        try:
            tag = li.getVideoInfoTag()
            tag.setTitle(title)
            tag.setMediaType("video")
        except:
            pass

        li.setArt({
            "icon": ch["logo"] or ADDON_ICON,
            "thumb": ch["logo"] or ADDON_ICON,
            "fanart": ADDON_FANART
        })

        play_url = (
            sys.argv[0]
            + "?play="
            + safe_quote(url)
            + "&title="
            + safe_quote(title)
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
# REPRODUCCIÓN (NOMBRE CORRECTO DEL CANAL)
# ------------------------------------------------------------
def play(params):
    url = params.get("play")
    title = params.get("title", "")

    li = xbmcgui.ListItem(label=title)

    try:
        tag = li.getVideoInfoTag()
        tag.setTitle(title)
        tag.setMediaType("video")
    except:
        pass

    xbmc.Player().play(url, li)


# ------------------------------------------------------------
# ROUTER
# ------------------------------------------------------------
def router(paramstring):
    params = {}

    if paramstring:
        for p in paramstring[1:].split("&"):
            if "=" in p:
                k, v = p.split("=", 1)
                params[k] = safe_unquote(v)

    if "play" in params:
        play(params)
    else:
        list_videos()


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------
if __name__ == "__main__":
    router(sys.argv[2])