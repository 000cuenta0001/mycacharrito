# -*- coding: utf-8 -*-
import re
from core import httptools
from core import scrapertools
from platformcode import logger


def test_video_exists(page_url):
    logger.info("(page_url='%s')" % page_url)
    global data
    data = httptools.downloadpage(page_url).data
    if "<h2>WE ARE SORRY</h2>" in data or '<title>404 Not Found</title>' in data:
        return False, "[milffox] El fichero no existe o ha sido borrado"
    return True, ""


def get_video_url(page_url, video_password):
    logger.info("(page_url='%s')" % page_url)
    video_urls = []
    # data = httptools.downloadpage(page_url).data
    # patron = '"video(?:_alt|)_url":\s*"([^"]+)"'
    patron = "video(?:_alt|)_url:\s*'([^']+)'"
    matches = re.compile(patron,re.DOTALL).findall(data)
    for url in matches:
        url = url.replace("\/", "/")
        if "sd" in url: quality="SD"
        if "hd" in url: quality="HD"
        video_urls.append(["[milffox] %s" %quality, url])
    return video_urls

