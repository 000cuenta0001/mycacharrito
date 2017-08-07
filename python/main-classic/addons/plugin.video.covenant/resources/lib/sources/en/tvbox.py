# -*- coding: utf-8 -*-

'''
    Covenant Add-on

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


import re,urllib,urlparse,json,base64,hashlib,time

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import source_utils
from resources.lib.modules import dom_parser



class source:
    def __init__(self):       
        self.priority = 0
        self.language = ['en']
        self.domains = ['tvbox.ag']
        self.base_link = 'https://tvbox.ag'
        self.search_link = 'https://tvbox.ag/search?q=%s'

    
    def movie(self, imdb, title, localtitle, aliases, year):
        try:            
            query = self.search_link % urllib.quote_plus(cleantitle.query(title))           
            for i in range(3):
                result = client.request(query, timeout=10)
                if not result == None: break

            t = [title] + [localtitle] + source_utils.aliases_to_array(aliases)
            t = [cleantitle.get(i) for i in set(t) if i]
            items = dom_parser.parse_dom(result, 'div', attrs={'class':'result'})
            url = None
            for i in items:
                result = re.findall(r'href="([^"]+)">(.*)<', i.content)
                if re.sub('<[^<]+?>', '', cleantitle.get(cleantitle.normalize(result[0][1]))) in t and year in result[0][1]: url = result[0][0]
                if not url == None: break 

            url = url.encode('utf-8')
            return url
        except:
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:

            query = self.search_link % urllib.quote_plus(cleantitle.query(tvshowtitle))
            for i in range(3):
                result = client.request(query, timeout=10)
                if not result == None: break

            t = [tvshowtitle] + source_utils.aliases_to_array(aliases)
            t = [cleantitle.get(i) for i in set(t) if i]
            items = dom_parser.parse_dom(result, 'div', attrs={'class':'result'})
            url = None
            for i in items:
                result = re.findall(r'href="([^"]+)">(.*)<', i.content)
                if re.sub('<[^<]+?>', '', cleantitle.get(cleantitle.normalize(result[0][1]))) in t and year in result[0][1]: url = result[0][0]
                if not url == None: break 

            url = url.encode('utf-8')
            return url
        except:
            return


    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None: return

            url = urlparse.urljoin(self.base_link, url)
            for i in range(3):
                result = client.request(url, timeout=10)
                if not result == None: break  

            title = cleantitle.get(title)
            premiered = re.compile('(\d{4})-(\d{2})-(\d{2})').findall(premiered)[0]
            premiered = '%s/%s/%s' % (premiered[2], premiered[1], premiered[0])
            result = re.findall(r'<h\d>Season\s+%s<\/h\d>(.*?<\/table>)' % season, result)[0]
            result = dom_parser.parse_dom(result, 'a', attrs={'href': re.compile('.*?episode-%s/' % episode)}, req='href')[0]
            url = result.attrs['href']

            url = url.encode('utf-8')
            return url
        except:
            return


    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            if url == None: return sources
            url = urlparse.urljoin(self.base_link, url)
            for i in range(3):
                result = client.request(url)
                if not result == None: break
            
            links = re.compile('onclick="report\(\'([^\']+)').findall(result)         
            for link in links:
                try:                    
                    valid, hoster = source_utils.is_host_valid(link, hostDict)
                    if not valid: continue
                    urls, host, direct = source_utils.check_directstreams(link, hoster)
                    for x in urls:
                        # if x['quality'] == 'SD':
                        #     try:
                        #         result = client.request(x['url'], timeout=5)
                        #         if 'HDTV' in result or '720' in result: x['quality'] = 'HD'
                        #         if '1080' in result: x['quality'] = '1080p'
                        #     except:
                        #         pass
                        sources.append({'source': host, 'quality': x['quality'], 'language': 'en', 'url': x['url'], 'direct': direct, 'debridonly': False})
                except:
                    pass

            return sources
        except:
            return sources


    def resolve(self, url):
        return url
