# -*- coding: utf-8 -*-

'''
    Specto Add-on
    Copyright (C) 2015 lambda

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import re,urllib,urlparse
from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import source_utils
from resources.lib.modules import directstream


class source:
    def __init__(self):
        self.priority = 0
        self.language = ['en']
        self.domains = ['flixtor.to']
        self.base_link = 'https://flixtor.to'
        self.search_link = '/ajax/popsearch?q=%s'
       

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return None

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None: return
            url = urlparse.parse_qs(url)
            url = dict([(i, url[i][0]) if url[i] else (i, '') for i in url])
            url['title'],  url['season'], url['episode'], url['premiered'] = title, season, episode, premiered
            url = urllib.urlencode(url)
            return url
        except:
            return

    def sources(self, url, hostDict, locDict):
        #sources.append({'source': host.split('.')[0], 'quality': 'SD', 'provider': 'Movie25', 'url': url})
        sources = []

        try:
            if url == None: return sources
            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])
            title = data['tvshowtitle'] if 'tvshowtitle' in data else data['title']
            query = self.search_link % (urllib.quote_plus(title))
            query = urlparse.urljoin(self.base_link, query)            
            result = client.request(query)
            r =  re.findall(r'href="([^"]+)".*?data-txt="([^"]+)"', result)
            r = [i for i in r if cleantitle.get(title) == cleantitle.get(i[1]) and data['year'] in i[1]]
            
            sources = []

            for i in r:                
                try:
                    if 'episode' in data:
                        s = '/season/%s/episode/%s'%(data['season'], data['episode'])
                        url = urlparse.urljoin(self.base_link, i[0]+s)
                    else:
                        url = urlparse.urljoin(self.base_link, i[0])

                    valid, hoster = source_utils.is_host_valid(url, hostDict)
                    if valid:
                        sources.append({'source': 'CDN', 'quality': 'SD', 'language': 'en', 'url': url, 'direct': False, 'debridonly': False})                
                except:
                    pass

            return sources
        except Exception as e:
            return sources

    def resolve(self, url):
        return url
