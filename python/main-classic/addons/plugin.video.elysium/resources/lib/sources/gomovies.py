# -*- coding: utf-8 -*-

'''

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


import re,urllib,urlparse,json,base64

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import directstream
from resources.lib.modules import jsunfuck
from resources.lib.modules import cache
from BeautifulSoup import BeautifulSoup
CODE = '''def retA():
    class Infix:
        def __init__(self, function):
            self.function = function
        def __ror__(self, other):
            return Infix(lambda x, self=self, other=other: self.function(other, x))
        def __or__(self, other):
            return self.function(other)
        def __rlshift__(self, other):
            return Infix(lambda x, self=self, other=other: self.function(other, x))
        def __rshift__(self, other):
            return self.function(other)
        def __call__(self, value1, value2):
            return self.function(value1, value2)
    def my_add(x, y):
        try: return x + y
        except Exception: return str(x) + str(y)
    x = Infix(my_add)
    return %s
param = retA()'''


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['123movies.to', '123movies.ru', '123movies.is', '123movies.gs', '123-movie.ru', '123movies-proxy.ru', '123movies.moscow', '123movies.msk.ru', '123movies.msk.ru', '123movies.unblckd.me', 'gomovies.to']
        self.base_link = 'https://gomovies.to'
        self.search_link = '/ajax/suggest_search'
        self.search_link_2 = '/movie/search/%s'
        self.info_link = '/ajax/movie_load_info/%s'
        self.server_link = '/ajax/movie_episodes/%s'
        self.embed_link = '/ajax/load_embed/'
        self.token_link = '/ajax/movie_token?eid=%s&mid=%s'
        self.sourcelink = '/ajax/movie_sources/%s?x=%s&y=%s'

    def getOriginalTitle(self, imdb):
        try:
            tmdb_link = base64.b64decode(
                'aHR0cHM6Ly9hcGkudGhlbW92aWVkYi5vcmcvMy9maW5kLyVzP2FwaV9rZXk9MTBiYWIxZWZmNzZkM2NlM2EyMzQ5ZWIxMDQ4OTRhNmEmbGFuZ3VhZ2U9ZW4tVVMmZXh0ZXJuYWxfc291cmNlPWltZGJfaWQ=')
            t = client.request(tmdb_link % imdb, timeout='10')
            try: title = json.loads(t)['movie_results'][0]['original_title']
            except: pass
            try: title = json.loads(t)['tv_results'][0]['original_name']
            except: pass
            title = cleantitle.normalize(title)
            return title
        except:
            return

    def movie(self, imdb, title, year):
        try:
            self.elysium = []
            cleaned_title = cleantitle.get(title)
            title = cleantitle.getsearch(title)
            q = self.search_link_2 % (urllib.quote_plus(title))
            r = urlparse.urljoin(self.base_link, q)
            html = BeautifulSoup(client.request(r))
            containers = html.findAll('div', attrs={'class': 'ml-item'})
            for result in containers:
                links = result.findAll('a')
                for link in links:
                    link_title = link['title'].encode('utf-8')
                    href = link['href'].encode('utf-8')
                    info = link['data-url'].encode('utf-8')
                    if cleantitle.get(link_title) == cleaned_title:
                        info = urlparse.urljoin(self.base_link, info)
                        html = client.request(info)
                        pattern = '<div class="jt-info">(.+?)</div>'
                        match = re.compile(pattern).findall(html)
                        for check in match:
							if not check == year: raise Exception()
							url = client.replaceHTMLCodes(href)
							url = urlparse.urljoin(self.base_link, url)
							return urllib.urlencode({'url': url, 'episode': 0})
        except:
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, year):
        try:
            url = {'tvshowtitle': tvshowtitle, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return


    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])
            title = cleantitle.getsearch(data['tvshowtitle'])
            season = '%01d' % int(season)
            episode = '%01d' % int(episode)
            query = (urllib.quote_plus(title)) + "+season+" + season
            checkseason = cleantitle.get(title) + "season" + season
			
            q = self.search_link_2 % (query)
            r = urlparse.urljoin(self.base_link, q)

            html = BeautifulSoup(client.request(r))
            containers = html.findAll('div', attrs={'class': 'ml-item'})
            for result in containers:
                links = result.findAll('a')
                for link in links:
                    link_title = link['title'].encode('utf-8')
                    href = link['href'].encode('utf-8')
                    href = client.replaceHTMLCodes(href)
                    href = urlparse.urljoin(self.base_link, href)
                    if cleantitle.get(link_title) == checkseason:
                        return urllib.urlencode({'url': href, 'episode': episode})
            
        except:
            return

    def onemovies_info(self, url):
        try:
            u = urlparse.urljoin(self.base_link, self.info_link)
            u = client.request(u % url)

            q = client.parseDOM(u, 'div', attrs = {'class': 'jtip-quality'})[0]

            y = client.parseDOM(u, 'div', attrs = {'class': 'jt-info'})
            y = [i.strip() for i in y if i.strip().isdigit() and len(i.strip()) == 4][0]

            return (y, q)
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []
            if url is None:
                return sources

            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])
            url = data['url']
            episode = int(data['episode'])

            url = urlparse.urljoin(self.base_link, url)
            url = url.replace('/watching.html', '')

            mid = re.findall('-(\d+)', url)[-1]

            try:
                headers = {'Referer': url}
                u = urlparse.urljoin(self.base_link, self.server_link % mid)
                r = client.request(u, headers=headers, XHR=True)
                r = json.loads(r)
                r = client.parseDOM(r['html'], 'div', attrs = {'class': 'les-content'})
                ids = client.parseDOM(r, 'a', ret='data-id')
                servers = client.parseDOM(r, 'a', ret='data-server')
                labels = client.parseDOM(r, 'a', ret='title')
                r = zip(ids, servers, labels)

                for eid in r:
                    try:
                        try:
                            ep = re.findall('episode.*?(\d+):.*?',eid[2].lower())[0]
                        except:
                            ep = 0
                        if (episode == 0) or (int(ep) == int(episode)):
                            url = urlparse.urljoin(self.base_link, self.token_link % (eid[0], mid))
                            script = client.request(url)

                            if '$_$' in script:
                                params = self.uncensored1(script)
                            elif script.startswith('[]') and script.endswith('()'):
                                params = self.uncensored2(script)
                            elif '_x=' in script:
                                x = re.search('''_x=['"]([^"']+)''', script).group(1)
                                y = re.search('''_y=['"]([^"']+)''', script).group(1)

                                params = {'x': x, 'y': y}
                            else:
                                raise Exception()
                            u = urlparse.urljoin(self.base_link, self.sourcelink % (eid[0], params['x'], params['y']))
                            r = client.request(u)
                            url = json.loads(r)['playlist'][0]['sources']
                            url = [i['file'] for i in url if 'file' in i]
                            url = [directstream.googletag(i) for i in url]
                            url = [i[0] for i in url if i]
                            for s in url:
                                sources.append({'source': 'gvideo', 'quality': s['quality'], 'provider': 'Gomovies',
                                                'url': s['url'], 'direct': True, 'debridonly': False})
                    except:
                        pass
            except:
                pass

            return sources
        except:
            return sources

    def resolve(self, url):
        try:
            if self.embed_link in url:
                result = client.request(url, XHR=True)
                url = json.loads(result)['embed_url']
                return url

            try:
                if not url.startswith('http'):
                    url = 'http:' + url

                for i in range(3):
                    u = directstream.googlepass(url)
                    if not u == None: break

                return u
            except:
                return
        except:
            return

    def uncensored(a, b):
        x = '' ; i = 0
        for i, y in enumerate(a):
            z = b[i % len(b) - 1]
            y = int(ord(str(y)[0])) + int(ord(str(z)[0]))
            x += chr(y)
        x = base64.b64encode(x)
        return x

    def uncensored1(self, script):
        try:
            script = '(' + script.split("(_$$)) ('_');")[0].split("/* `$$` */")[-1].strip()
            script = script.replace('(__$)[$$$]', '\'"\'')
            script = script.replace('(__$)[_$]', '"\\\\"')
            script = script.replace('(o^_^o)', '3')
            script = script.replace('(c^_^o)', '0')
            script = script.replace('(_$$)', '1')
            script = script.replace('($$_)', '4')

            vGlobals = {"__builtins__": None, '__name__': __name__, 'str': str, 'Exception': Exception}
            vLocals = {'param': None}
            exec (CODE % script.replace('+', '|x|'), vGlobals, vLocals)
            data = vLocals['param'].decode('string_escape')
            x = re.search('''_x=['"]([^"']+)''', data).group(1)
            y = re.search('''_y=['"]([^"']+)''', data).group(1)
            return {'x': x, 'y': y}
        except:
            pass

    def uncensored2(self, script):
        try:
            js = jsunfuck.JSUnfuck(script).decode()
            x = re.search('''_x=['"]([^"']+)''', js).group(1)
            y = re.search('''_y=['"]([^"']+)''', js).group(1)
            return {'x': x, 'y': y}
        except:
            pass
