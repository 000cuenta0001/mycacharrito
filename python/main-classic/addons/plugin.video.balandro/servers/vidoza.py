# -*- coding: utf-8 -*-

from core import httptools, scrapertools, jsontools
from platformcode import logger


def get_video_url(page_url, url_referer=''):
    logger.info("(page_url='%s')" % page_url)
    video_urls = []

    data = httptools.downloadpage(page_url).data
    # ~ logger.debug(data)

    if "Page not found" in data or "File was deleted" in data:
        return 'El archivo no existe o ha sido borrado'
    elif "processing" in data:
        return 'El archivo no está disponible'

    s = scrapertools.find_single_match(data, 'sourcesCode\s*:\s*(\[\{.*?\}\])')
    s = s.replace('src:', '"src":').replace('file:', '"file":').replace('type:', '"type":').replace('label:', '"label":').replace('res:', '"res":')
    try:
        data = jsontools.load(s)
        # ~ logger.debug(data)
        for enlace in data:
            if 'src' in enlace or 'file' in enlace:
                url = enlace['src'] if 'src' in enlace else enlace['file']
                tit = ''
                if 'label' in enlace: tit += '[%s]' % enlace['label']
                if 'res' in enlace: tit += '[%s]' % enlace['res']
                if tit == '' and 'type' in enlace: tit = enlace['type']
                if tit == '': tit = '.mp4'
                
                video_urls.append([tit, url])
    except:
        logger.debug('No se detecta json %s' % s)
        pass

    video_urls.reverse()

    return video_urls