# -*- coding: utf-8 -*-
import urllib2,urllib
import re,time
import time,json,base64
import cookielib,aes,os
import binascii


BASEURL='http://bit.ly/CristalAzulDeportes247'
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'

def fixForEPG(item):
    return(item)

def getUrl(url,data=None,header={},useCookies=True):
    if useCookies:
        cj = cookielib.LWPCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
    if not header:
        header = {'User-Agent':UA}
    req = urllib2.Request(url,data,headers=header)
    try:
        response = urllib2.urlopen(req, timeout=10)
        link = response.read()
        response.close()
    except:
        link=''
    return link

def getUrlc(url,data=None,header={},useCookies=True):
    cj = cookielib.LWPCookieJar()
    if useCookies:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
    if not header:
        header = {'User-Agent':UA}
    req = urllib2.Request(url,data,headers=header)
    try:
        response = urllib2.urlopen(req, timeout=10)
        link = response.read()
        response.close()
    except:
        link=''
    c = ''.join(['%s=%s'%(c.name,c.value) for c in cj]) if cj else ''
    return link,c

def getChannels(addheader=False):
	ret=''
	content = getUrl(BASEURL)
	wrapper = re.compile('(http[^"]+/advertisement.js\?\d+)').findall(content)
	wrappers = re.compile('<script type="text/javascript" src="(http://s1.medianetworkinternational.com/js/\w+.js)"').findall(content)
	for wrapper in wrappers:
		wc = getUrl(wrapper)
		content=JsUnwiser().unwiseAll(wc)
		ret = content
		ret = re.compile('return "(.*?)"').findall(content)
		if ret:
			ret = ret[0]
			print 'key %s'%ret
			break
	url='http://www.sport247.live/es/events/-/1/-/-/120'
	content = getUrl(url)
	ids = [(a.start(), a.end()) for a in re.finditer('onClick=', content)]
	ids.append( (-1,-1) )
	out=[]

	for i in range(len(ids[:-1])):
		subset = content[ ids[i][1]:ids[i+1][0] ]
		links=re.compile('\("([^"]+)", "([^"]+)", "[^"]+", 1\)').findall(subset)
		title2=re.compile('<img alt="(.*?)"').findall(subset)
		
		t=re.compile('>([^<]+)<').findall(subset)
		online = '[COLOR lightgreen][B]*[/B][/COLOR] ' if subset.find('/images/types/dot-green-big.png')>0 else '[COLOR gold]info [/COLOR]'
		if links and title2:
			event,urlenc=links[0]
			url = 'http://www.sport247.live/es/links/%s/1@%s'%(event.split('_')[-1],ret)
			etime,title1= t[:2]
			
			time = re.findall('(\d+:\d+)',etime)[0].replace('00:','23:').replace('01:','00:').replace('02:','01:').replace('03:','02:').replace('04:','03:').replace('05:','04:').replace('06:','05:').replace('07:','06:').replace('08:','07:').replace('09:','08:').replace('10:','09:').replace('11:','10:').replace('12:','11:').replace('13:','12:').replace('14:','13:').replace('15:','14:').replace('16:','15:').replace('17:','16:').replace('18:','17:').replace('19:','18:').replace('20:','19:').replace('21:','20:').replace('22:','21:').replace('23:','22:')
			li = time.split(':')
			hour,minute=li[0],li[1]
			hour=int(li[0])
			hour=('{:02}'.format(hour))
			etime=hour+':'+minute			
			
			
			
			lenguaje = t[-1].replace('Español','[COLOR gold]*^Esp[COLOR gold]^*[/COLOR][COLOR lightskyblue]').replace('Inglés','[COLOR gold]*^[COLOR white]Ing[COLOR gold]^*[/COLOR]').replace('Árabe','[COLOR gold]*^[COLOR white]Ára[COLOR gold]^*[/COLOR]').replace('Hebreo','[COLOR gold]*^[COLOR white]Heb[COLOR gold]^*[/COLOR]').replace('Turkish','[COLOR gold]*^[COLOR white]Tur[COLOR gold]^*[/COLOR]').replace('Ruso','[COLOR gold]*^[COLOR white]Rus[COLOR gold]^*[/COLOR]').replace('Checa','[COLOR gold]*^[COLOR white]Che[COLOR gold]^*[/COLOR]   ').replace('Francés','[COLOR gold]*^[COLOR white]Fra[COLOR gold]^*[/COLOR]').replace('Húngaro','[COLOR gold]*^[COLOR white]Hún[COLOR gold]^*[/COLOR]').replace('Rumano','[COLOR gold]*^[COLOR white]Rum[COLOR gold]^*[/COLOR]').replace('Alemán','[COLOR gold]*^[COLOR white]Ale[COLOR gold]^*[/COLOR]').replace('Ucranio','[COLOR gold]*^[COLOR white]Ucr[COLOR gold]^*[/COLOR]').replace('Dutch','[COLOR gold]*^[COLOR white]Dut[COLOR gold]^*[/COLOR]').replace('Portugués','[COLOR gold]*^[COLOR white]Por[COLOR gold]^*[/COLOR]').replace('Polaco','[COLOR gold]*^[COLOR white]Pol[COLOR gold]^*[/COLOR]')
			lenguaje2 = t[-1]
			calidad =  t[-2].replace('HQ&nbsp;','[COLOR white]HD[COLOR lightskyblue],') if len(t)==4 else '[COLOR white]SD[COLOR lightskyblue],'
			code=calidad+lenguaje2
			title = '[COLOR white]%s%s [/COLOR][COLOR white]%s [COLOR lightskyblue]%s [COLOR white]%s[/COLOR]'%(online,etime,lenguaje,title1,title2[0])
			plot='%s: [COLOR lightskyblue]%s[/COLOR] %s'%(etime,title1,title2[0])
			out.append({'title':title,'url':url,'image':title2[0],'code':'[COLOR gold]*^[COLOR white][COLOR lightskyblue]'+code+'[COLOR gold]^*[/COLOR]','plot':plot})	
	return out

def getStreams(url):
	myurl,ret=url.split('@')
	
	content = getUrl(myurl)
	sources=re.compile('<span id=["\']span_link_links[\'"] onClick="\w+\(\'(.*?)\'').findall(content)
	out=[]
	for i, s in enumerate(sources):
		enc_data=json.loads(base64.b64decode(s))
		ciphertext = 'Salted__' + enc_data['s'].decode('hex') + base64.b64decode(enc_data['ct'])
		src=aes.decrypt(ret,base64.b64encode(ciphertext))
		src=src.strip('"').replace('\\','')
		title = '[COLOR lightskyblue]Enlace .m3u8 número [/COLOR][COLOR white]%d [/COLOR]'%(i+1)
		out.append({'title':title,'tvid':title,'key':ret,'url':src,'refurl':myurl,'urlepg':''})
	return out

def getChannelVideo(item):
	ran= binascii.b2a_hex(os.urandom(16))
	headers = {
    'User-Agent': UA,
    'Referer': 'http://www.sport247.live/',}
	content,c = getUrlc(item.get('url'),header=headers,useCookies=True)
	link1=re.compile("(http://www.[^\.]+.pw/.+?)'\s+", re.IGNORECASE + re.DOTALL + re.MULTILINE + re.UNICODE).findall(content)
	if link1:
		nxturl='%s%s'%(link1[0],ran)
		
		headers2 = {
				'User-Agent': UA,
				'Referer': item.get('url'),
				'Cookie':c,}
		content,c = getUrlc(nxturl,header=headers2,useCookies=True)
	links=re.compile('(http://www.[^\.]+.pw/(?!&#)[^"]+)', re.IGNORECASE + re.DOTALL + re.MULTILINE + re.UNICODE).findall(content)
	link = [x for x in links if '&#' in x] 
	if link:
		
		link=re.sub(r'&#(\d+);', lambda x: chr(int(x.group(1))), link[0])
		header = {'User-Agent':UA,'Referer':item.get('url')}
		data = getUrl(link,header=header,useCookies=True)
		b=re.compile('.*?name="b"\s*value=["\']([^"\']+)["\']').findall(data)
		f=re.compile('.*?name="f"\s*value=["\']([^"\']+)["\']').findall(data)
		d=re.compile('.*?name="d"\s*value=["\']([^"\']+)["\']').findall(data)
		r=re.compile('.*?name="r"\s*value=["\']([^"\']+)["\']').findall(data)
		action=re.compile('[\'"]action[\'"][,\s]*[\'"](http.*?)[\'"]').findall(data)
		srcs=re.compile('src=[\'"](.*?)[\'"]').findall(data)
		if f and r and d and action:
			payload=urllib.urlencode({'d':d[0],'f':f[0],'r':r[0],'b':b[0]})	
			header2 = {'User-Agent':UA,'Referer':link}
			data2,c= getUrlc(action[0],payload,header=header2,useCookies=True)
			link=re.compile('\([\'"][^"\']+[\'"], [\'"][^"\']+[\'"], [\'"]([^"\']+)[\'"], 1\)').findall(data2)	
			enc_data=json.loads(base64.b64decode(link[0]))
			ciphertext = 'Salted__' + enc_data['s'].decode('hex') + base64.b64decode(enc_data['ct'])
			src=aes.decrypt(item.get('key'),base64.b64encode(ciphertext))
			src=src.replace('"','').replace('\\','').encode('utf-8')
			a,c=getUrlc(srcs[-1],header=header2,useCookies=True) if srcs else '',''
			a,c=getUrlc(src,header=header2,useCookies=True)
			if src.startswith('http'):
				href =src+'|Referer=%s&User-Agent=%s&X-Requested-With=ShockwaveFlash/31.0.0.108'%(urllib.quote(action[0]),UA)
				print href
				return href,srcs[-1],header2
			else:
				href=aes.decode_hls(src)
				if href:
					href +='|Referer=%s&User-Agent=%s&X-Requested-With=ShockwaveFlash/31.0.0.108'%(urllib.quote(r[0]),UA)
					return href,srcs[-1],header2
	return ''

def getUrlrh(url,data=None,header={},useCookies=True):
    cj = cookielib.LWPCookieJar()
    if useCookies:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
    if not header:
        header = {'User-Agent':UA}
    rh={}
    req = urllib2.Request(url,data,headers=header)
    try:
        response = urllib2.urlopen(req, timeout=15)
        for k in response.headers.keys(): rh[k]=response.headers[k]
        link = response.read()
        response.close()
    except:
        link=''
    c = ''.join(['%s=%s'%(c.name,c.value) for c in cj]) if cj else ''
    return link,rh

class JsUnwiser:
    def unwiseAll(self, data):
        try:
            in_data=data
            sPattern = 'eval\\(function\\(w,i,s,e\\).*?}\\((.*?)\\)'
            wise_data=re.compile(sPattern).findall(in_data)
            for wise_val in wise_data:
                unpack_val=self.unwise(wise_val)
                in_data=in_data.replace(wise_val,unpack_val)
            return re.sub(re.compile("eval\(function\(w,i,s,e\).*?join\(''\);}", re.DOTALL), "", in_data, count=1)
        except: 
            traceback.print_exc(file=sys.stdout)
            return data
        
    def containsWise(self, data):
        return 'w,i,s,e' in data
        
    def unwise(self, sJavascript):
        page_value=""
        try:        
            ss="w,i,s,e=("+sJavascript+')' 
            exec (ss)
            page_value=self.__unpack(w,i,s,e)
        except: traceback.print_exc(file=sys.stdout)
        return page_value
        
    def __unpack( self,w, i, s, e):
        lIll = 0;
        ll1I = 0;
        Il1l = 0;
        ll1l = [];
        l1lI = [];
        while True:
            if (lIll < 5):
                l1lI.append(w[lIll])
            elif (lIll < len(w)):
                ll1l.append(w[lIll]);
            lIll+=1;
            if (ll1I < 5):
                l1lI.append(i[ll1I])
            elif (ll1I < len(i)):
                ll1l.append(i[ll1I])
            ll1I+=1;
            if (Il1l < 5):
                l1lI.append(s[Il1l])
            elif (Il1l < len(s)):
                ll1l.append(s[Il1l]);
            Il1l+=1;
            if (len(w) + len(i) + len(s) + len(e) == len(ll1l) + len(l1lI) + len(e)):
                break;
            
        lI1l = ''.join(ll1l)
        I1lI = ''.join(l1lI)
        ll1I = 0;
        l1ll = [];
        for lIll in range(0,len(ll1l),2):
            ll11 = -1;
            if ( ord(I1lI[ll1I]) % 2):
                ll11 = 1;
            l1ll.append(chr(    int(lI1l[lIll: lIll+2], 36) - ll11));
            ll1I+=1;
            if (ll1I >= len(l1lI)):
                ll1I = 0;
        ret=''.join(l1ll)
        if 'eval(function(w,i,s,e)' in ret:
            ret=re.compile('eval\(function\(w,i,s,e\).*}\((.*?)\)').findall(ret)[0] 
            return self.unwise(ret)
        else:
            return ret
