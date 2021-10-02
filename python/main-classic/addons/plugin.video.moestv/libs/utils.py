# -*- coding: utf-8 -*-

import sys, os, re
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import xbmcvfs
import base64
import hashlib
import json
import glob
import copy
import time

from threading import Lock
from threading import Thread

from six.moves import urllib_parse
from six.moves import reload_module
from six.moves import urllib_request
from six.moves import reduce
import six

if six.PY3:
    import types, importlib
    long = int
else:
    import imp

try:
    translatePath = xbmcvfs.translatePath
except:
    translatePath =  xbmc.translatePath


ADDON = xbmcaddon.Addon()
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_VERSION = ADDON.getAddonInfo('version')
HEADING = "%s (%s)" %(ADDON_NAME, ADDON_VERSION)
RUNTIME_PATH = translatePath(ADDON.getAddonInfo('Path'))
DATA_PATH = translatePath(ADDON.getAddonInfo('Profile'))
IMAGE_PATH = os.path.join(RUNTIME_PATH, 'resources', 'media')


# Clases auxiliares
class Item(object):
    defaults = {}

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __contains__(self, item):
        return item in self.__dict__

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        if item.startswith("__"):
            return object.__getattribute__(self, item)
        else:
            return self.defaults.get(item, '')

    def __eq__(self, other):
        return isinstance(other, Item) and self.action == other.action and self.content == other.content and \
               self.tmdb == other.tmdb and self.season == other.season and self.episode == other.episode

    def __str__(self):
        return '{%s}' % (', '.join(['\'%s\': %s' % (k, repr(self.__dict__[k])) for k in sorted(self.__dict__.keys())]))

    def pop(self, attr):
        return self.__dict__.pop(attr, None)

    def getart(self):
        if 'fanart' not in self.__dict__:
            self.__dict__['fanart'] = os.path.join(RUNTIME_PATH, 'fanart.gif')
        d = {k: self.__dict__.get(k) for k in ['poster', 'icon', 'fanart', 'thumb'] if k in self.__dict__}
        if not d.get('thumb'):
            d['thumb'] = d.get('poster') or d.get('icon')
        if not d.get('icon'):
            d['icon'] = d.get('poster', '')

        return d

    def tourl(self):
        value = self.__str__()
        if not isinstance(value, six.binary_type):
            value = six.binary_type(value, 'utf8')
        return six.ensure_str(urllib_parse.quote(base64.b64encode(value)))

    def fromurl(self, url):
        str_item = base64.b64decode(urllib_parse.unquote(url))
        self.__dict__.update(eval(str_item))
        return self

    def tojson(self, path=""):
        if path:
            open(path, "wb").write(six.ensure_binary(dump_json(self.__dict__)))
        else:
            return six.ensure_str(dump_json(self.__dict__))

    def fromjson(self, json_item=None, path=""):
        if path:
            json_item = six.ensure_str(open(path, "rb").read())

        if isinstance(json_item, dict):
            item = json_item
        else:
            item = load_json(json_item)
        self.__dict__.update(item)
        return self

    def is_label(self):
        return not self.__dict__.get('action')

    def clone(self, **kwargs):
        newitem = copy.deepcopy(self)
        for k in ['label', 'html', 'type', 'contextMenu', 'limitResults_index']:
            if k in newitem.__dict__:
                newitem.__dict__.pop(k)

        for k, v in kwargs.items():
            setattr(newitem, k, v)
        return newitem


class Video(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return repr(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

    def __getattr__(self, name):
        if name.startswith("__"):
            return super(Video, self).__getattribute__(name)

        elif name == 'type':
            return self._get_type()

        elif name == 'is_InputStream':
            if self.type in ['mpd', 'rtmp']:
                return True
            return False

        elif name == 'player':
            if 'player' in self.__dict__:
                return self.player.lower()
            else:
                return 'default'

        elif name == 'label':
            if 'label' in self.__dict__:
                return self.label
            else:
                lng = {'es': u'Castellano', 'fr': u'Frances', 'en': u'Ingles', 'ru': u'Ruso', 'de': u'Aleman',
                       'it': u'Italiano', 'eu': u'Euskera', 'vo': u'Versión original'}  # ISO_639-1
                label = ''
                if self.lang:
                    label += lng.get(self.lang.lower(), self.lang)

                if self.res:
                    res_num = None
                    if isinstance(self.res, int):
                        res_num = self.res
                    elif not self.res.lower() in ['4k', '8k']:
                        res_num = re.findall(r'(\d+)', self.res)[0]
                    label += " [%s]" % ("%sp" % res_num) if res_num else self.res
                else:
                    label += (" (%s)" % self.type.upper())

                if self.bitrate:
                    try:
                        bitrate = int(self.bitrate)
                        if bitrate / 1000000.0 > 10:
                            l_bitrate = " - %dMbps" % (bitrate / 1000000)
                        elif bitrate / 1000000.0 > 1:
                            l_bitrate = " - %.2fMbps" % (bitrate / 1000000.0)
                        elif bitrate / 1000.0 > 2:
                            l_bitrate = " -  %dKbps" % (bitrate / 1000)
                        else:
                            l_bitrate = " - %dbps" % bitrate
                    except:
                        l_bitrate = " - %s" % self.bitrate
                    label = label[:-1] + l_bitrate + label[-1]

                return label

        else:
            # return self.__dict__.get(name, self.defaults.get(name, ''))
            return self.__dict__.get(name, '')

    def __deepcopy__(self, memo):
        new = Video(**self.__dict__)
        return new

    def _get_type(self):
        if self.url.startswith('rtmp'):
            return 'rtmp'
        else:
            ext = os.path.splitext(self.url.split('?')[0].split('|')[0])[1]
            if ext.startswith('.'): ext = ext[1:]
            return ext

    def clone(self, **kwargs):
        newvideo = copy.deepcopy(self)
        for k, v in kwargs.items():
            setattr(newvideo, k, v)
        return newvideo


class LimitResults:
    """
    Clase para limitar los resultados de una función debe usarse como decorator:
        @LimitResults()
        def contents(item):
            ---
    El decorador admite dos argumentos:
        limit: numero de items devueltos por pagina. (Por defecto limit = 50)
        deep_limit: numero maximo de iteracciones para obtener una pagina completa (Por defecto deep_limit = 15)
    La función debe tener el formato estandard con un solo parametro "item" y devolver un itemlist.
    Si la función devuelve mas items del limite, los limita cortando el itemlist y añadiendo un item para pasar a la si
    guiente parte.
    Si la función devuelve menos items del limite y el ultimo item es para pasar a siguiente pagina, va pasando paginas
    hasta llegar al limite.
    """

    def __init__(self, limit=100, deep_limit=15):
        self.limit = limit
        self.deep_limit = deep_limit
        self.deep = 0
        self.item = None
        self.next_item = None
        self.page_items = 0
        self.itemlist = []
        # self.fnc = fnc

    def get_itemlist(self):
        """
        Obtiene los items llamando a la función y elimina el item de página siguiente.
        :return:
        """
        # Llamamos a la función con el item como argumento
        itemlist = self.fnc(self.item)

        # Eliminamos el item para pagina siguiente en caso de existir y lo guarda para usarlo mas adelante
        if itemlist and itemlist[-1].type == 'next':
            self.next_item = itemlist[-1].clone(limitResults_index=None, type='next')
            itemlist = itemlist[:-1]
        else:
            #self.item.limitResults_index = None
            self.next_item = None

        # Numero de items de la ultima llamada, utilizado para saber el indice por donde cortar en la siguiente pagina
        self.page_items = len(itemlist)
        self.itemlist.extend(itemlist)

    def fill_itemlist(self):
        """
        Realiza llamadas a la función hasta que el itemlist tenga el tamaño adecuado.
        :return:
        """
        # Vamos pasando paginas mientras haya un item de 'Página siguiente' y el itemlist no llegue al tamaño indicado
        while True:
            # Contabilizamos la profundidad en el listado
            self.deep += 1

            # Llamamos a la función
            self.get_itemlist()

            # Si venimos de un itemlist cortado, eliminamos los primeros x elementos (los de las páginas anteriores)
            if self.item.type == 'next' and self.item.limitResults_index:
                logger("fill_itemlist %s" %self.item.limitResults_index)
                self.itemlist = self.itemlist[self.item.limitResults_index:]

            # Si el itemlist no esta lleno y hay mas paginas, continuamos con la siguiente
            if len(self.itemlist) < self.limit and self.next_item and self.deep < self.deep_limit:
                self.item = self.next_item
            else:
                break

    def limit_itemlist(self):
        """
        Corta el itemlist para no sobrepasar el limite de resultados, añade un item para pagina siguiente:
         - Si es una pagina siguiente real, pasa el item obtenido de la funcion (con una nueva url)
         - Si es una pagina siguiente virtual, pasa el ultimo item, con el index por donde cortar en la siguiente pagina
        :return:
        """

        # Si el itemlist es mayor que el limite:
        if len(self.itemlist) > self.limit:
            index = self.page_items - (len(self.itemlist) - self.limit)
            self.itemlist = self.itemlist[:self.limit]
            next_page = self.item.clone(type='next', limitResults_index=index)
        else:
            next_page = self.next_item

        # Añadimos el item para pasar de pagina
        if next_page:
            self.itemlist.append(next_page)

    def __call__(self, fnc):
        # Se ejecuta la función y limita el resultado
        self.fnc = fnc
        self.deep = 0

        def wrapped_f(arg):
            self.item = arg
            self.fill_itemlist()
            self.limit_itemlist()
            return self.itemlist

        return wrapped_f


# Funciones auxiliares

LOGINFO = xbmc.LOGINFO if six.PY3 else xbmc.LOGNOTICE


def logger(message, level=None):
    def format_message(data=""):
        try:
            value = str(data)
        except Exception:
            value = repr(data)

        if isinstance(value, six.binary_type):
            value = six.text_type(value, 'utf8', 'replace')

        """if isinstance(value, unicode):

            return [value]
        else:
            return value"""
        return value

    texto = '[%s] %s' % (xbmcaddon.Addon().getAddonInfo('id'), format_message(message))

    try:
        if level == 'info':
            xbmc.log(texto, LOGINFO)
        elif level == 'error':
            xbmc.log("######## ERROR #########", xbmc.LOGERROR)
            xbmc.log(texto, xbmc.LOGERROR)
        else:
            xbmc.log("######## DEBUG #########", LOGINFO)
            xbmc.log(texto, LOGINFO)
    except:
        # xbmc.log(six.ensure_str(texto, encoding='latin1', errors='strict'), LOGINFO)
        xbmc.log(str([texto]), LOGINFO)


locker = Lock()


def load_json_file(path):
    with locker:
        if os.path.isfile(path):
            data = open(path, 'rb').read()
            data = load_json(six.ensure_str(data))
        else:
            data = dict()

    return data


def dump_json_file(data, path):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    data = six.ensure_binary(dump_json(data))
    with locker:
        open(path, 'wb').write(data)


def load_json(*args, **kwargs):
    if "object_hook" not in kwargs:
        kwargs["object_hook"] = set_encoding

    try:
        value = json.loads(*args, **kwargs)
    except Exception as e:
        # logger(e)
        value = {}

    return value


def dump_json(*args, **kwargs):
    if not kwargs:
        kwargs = {
            'indent': 4,
            'skipkeys': True,
            'sort_keys': True,
            'ensure_ascii': False
        }

    try:
        value = json.dumps(*args, **kwargs)
    except Exception:
        logger("Error dump_json")
        value = ''

    return value


def set_encoding(dct):
    if isinstance(dct, dict):
        return dict((set_encoding(key), set_encoding(value)) for key, value in dct.items())

    elif isinstance(dct, list):
        return [set_encoding(element) for element in dct]

    elif isinstance(dct, six.string_types):
        return six.ensure_str(dct)

    else:
        return dct


def time_to_seconds(time_in):
    try:
        h, m, s = map(int, time_in.split(':'))
        return h * 3600 + m * 60 + s
    except:
        return 0


def get_videos_m3u8(url, video=Video(), fn_url=None):
    video_list = list()
    res_max = 0
    only_audio = False
    m3u8_code = 200

    if '.m3u8' in url:
        m3u8_data = httptools.downloadpage(url)
        m3u8_code = m3u8_data.code
        m3u8_data = m3u8_data.data

        try:
            if m3u8_code != 200:
                raise ()

            bitrate = re.findall(r'BANDWIDTH=(\d+)', m3u8_data, re.I)
            res_url = re.findall(r'RESOLUTION=\d+x(\d+).*?\s+(.*?)\s+', m3u8_data, re.I)

            if res_url:
                for i in range(len(res_url)):
                    file_uri = res_url[i][1]
                    res = int(res_url[i][0])
                    res_max = max(res_max, res)

                    if fn_url:
                        # logger(url)
                        # logger(file_uri)
                        file_uri = fn_url(file_uri, url)
                        # logger(file_uri)

                    new_video = video.clone(res=res, url=file_uri.strip())

                    if len(res_url) == len(bitrate):
                        new_video.bitrate = bitrate[i]

                    video_list.append(new_video)

            else:
                if r'#EXT-X-MEDIA:TYPE=AUDIO' in m3u8_data:
                    only_audio = True
                else:
                    raise ()
        except:
            # logger("Error get_videos_m3u8: url= %s" % url)
            # logger("Error get_videos_m3u8: data= %s" % (m3u8_data))
            pass

    if len(video_list) > 1:
        new_video = video.clone(res=res_max, url=url, bitrate='multi-bitrate')
        video_list.insert(0, new_video)

    elif m3u8_code == 200:
        new_video = video.clone(url=url)
        if res_max:
            new_video.res = res_max

        if only_audio:
            new_video.type = 'audio'

        video_list = [new_video]

    return video_list


def natural_sort_key(s):
    import unicodedata
    s = six.ensure_text(str(s).lower())
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('(\d+)', ''.join((c for c in unicodedata.normalize('NFD', s)
                                                   if unicodedata.category(c) not in ['Po', 'Mn', 'Pc', 'Pd', 'Pe',
                                                                                      'Ps'])))]


def sorted_itenlist(itemlist, key='label'):
    l_sort = list()
    next = None

    if itemlist:
        if key not in itemlist[0].__dict__:
            logger("Error sorted_itenlist: El item no tiene el artributo %s" % key)
            return []

        if itemlist[-1].type == 'next':
            next = itemlist.pop()

        l_sort = sorted(itemlist, key=lambda x: natural_sort_key(x.__dict__.get(key)))

        if next:
            l_sort.append(next)

    return l_sort


def sorted_videolist(videolist):
    videolist.sort(key=lambda x: natural_sort_key(x.bitrate), reverse=True)
    videolist.sort(key=lambda x: natural_sort_key(x.res), reverse=True)
    videolist.sort(key=lambda x: x.is_InputStream, reverse=True)

    return videolist


def remove_html_tags(string_in):
    patron = r'<[^>]+>'
    return re.sub(patron, '', string_in)


def remove_white_spaces(html):
    patron = r'\n|\r|\t|&nbsp;'
    return re.sub(r'\s+', ' ', re.sub(patron, '', html))


def get_setting(name, default=None):
    value = xbmcaddon.Addon().getSetting(name)

    if not value:
        return default

    elif value == 'true':
        return True

    elif value == 'false':
        return False

    else:
        try:
            value = int(value)
        except ValueError:
            try:
                value = long(value)
            except ValueError:
                try:
                    aux = load_json(value)
                    if aux: value = aux
                except ValueError:
                    pass

        return value


def set_setting(name, value):
    try:
        if isinstance(value, bool):
            if value:
                value = "true"
            else:
                value = "false"

        elif isinstance(value, (int, long)):
            value = str(value)

        elif not isinstance(value, str):
            value = dump_json(value)

        xbmcaddon.Addon().setSetting(name, value)

    except Exception as ex:
        logger("Error al convertir '%s' no se guarda el valor \n%s" % (name, ex), 'error')
        return None

    return value


# Main
from libs import httptools

httptools.load_cookies()
reload_module(httptools)

