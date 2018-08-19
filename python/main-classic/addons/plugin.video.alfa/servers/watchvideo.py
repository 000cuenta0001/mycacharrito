# -*- coding: utf-8 -*-

from core import httptools
from core import scrapertools
from lib import jsunpack
from platformcode import logger


def test_video_exists(page_url):
    logger.info("(page_url='%s')" % page_url)
    data = httptools.downloadpage(page_url).data
    if "Not Found" in data or "File was deleted" in data:
        return False, "[Watchvideo] El fichero no existe o ha sido borrado"
    return True, ""


def get_video_url(page_url, premium=False, user="", password="", video_password=""):
    logger.info("url=" + page_url)
    video_urls = []
    data = httptools.downloadpage(page_url).data
    media_urls = scrapertools.find_multiple_matches(data, 'file:"([^"]+)"')
    for media_url in media_urls:
        ext = "mp4"
        if "m3u8" in media_url:
            ext = "m3u8"
        video_urls.append(["%s [watchvideo]" % (ext), media_url])
    video_urls.reverse()
    for video_url in video_urls:
        logger.info("%s - %s" % (video_url[0], video_url[1]))
    return video_urls
