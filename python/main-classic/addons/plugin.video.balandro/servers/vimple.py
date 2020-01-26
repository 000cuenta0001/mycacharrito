# -*- coding: utf-8 -*-

from core import httptools, scrapertools
from platformcode import logger


def get_video_url(page_url, url_referer=''):
    logger.info("url=" + page_url)
    video_urls = []
    
    resp = httptools.downloadpage(page_url, cookies=False)
    # ~ logger.debug(resp.data)
    
    if '<title>Video Not Found</title>' in resp.data:
        return 'El archivo ha sido eliminado o no existe'
    
    url = scrapertools.find_single_match(resp.data, ',"url":"([^"]+)').replace('\\', '')
    if url.startswith('http'):
        cks = httptools.get_cookies_from_headers(resp.headers)
        # ~ logger.debug(cks)
        if cks:
            url += '|Cookie=' + '; '.join([ck_name + '=' + ck_value for ck_name, ck_value in cks.items()])

        video_urls.append(['mp4', url])

    return video_urls
