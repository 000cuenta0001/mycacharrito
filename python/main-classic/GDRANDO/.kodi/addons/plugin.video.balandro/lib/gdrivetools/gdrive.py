# -*- coding: utf-8 -*-
'''
    gdrive (Google Drive ) for KODI / XBMC Plugin
    Copyright (C) 2013-2016 ddurdle

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

# cloudservice - required python modules
import os, re, sys
import urllib, urllib2
import socket
import json
import cookielib

from authorization import authorization

from platformcode import config, logger #, platformtools


#
# Google Drive API implementation of Google Drive
#
class gdrive(object):

    AUDIO = 1
    VIDEO = 2
    PICTURE = 3

    # magic numbers
    MEDIA_TYPE_MUSIC = 1
    MEDIA_TYPE_VIDEO = 2
    MEDIA_TYPE_PICTURE = 3
    MEDIA_TYPE_UNKNOWN = 4

    MEDIA_TYPE_FOLDER = 0


    API_VERSION = '3.0'

    PROTOCOL = 'https://'

    # ~ API_URL = PROTOCOL+'www.googleapis.com/drive/v2/'
    API_URL = PROTOCOL+'www.googleapis.com/drive/v3/'

    ##
    # initialize (save addon, instance name, user agent)
    ##
    def __init__(self, instanceName, authenticate=True):
        self.instanceName = instanceName

        username = self.getInstanceSetting('username', default='')
        self.authorization = authorization(username)

        self.cookiejar = cookielib.CookieJar()

        self.user_agent = '' #user_agent

        # load the OAUTH2 tokens or force fetch if not set
        if (authenticate == True and (not self.authorization.loadToken(self.instanceName, 'auth_access_token') or not self.authorization.loadToken(self.instanceName, 'auth_refresh_token'))):
            if self.getInstanceSetting('code'):
                self.getToken(self.getInstanceSetting('code'))
            else:
                # ~ xbmcgui.Dialog().ok(self.addon.getLocalizedString(30000), self.addon.getLocalizedString(30017), self.addon.getLocalizedString(30018))
                logger.error('Faltan datos para conectar con GDrive!')


    ##
    # get OAUTH2 access and refresh token for provided code
    #   parameters: OAUTH2 code
    #   returns: none
    ##
    def getToken(self,code):

            header = { 'User-Agent' : self.user_agent }
            # ~ logger.debug('getToken User-Agent: ' + self.user_agent)

            url = 'https://accounts.google.com/o/oauth2/token'
            clientID = self.getInstanceSetting('client_id')
            clientSecret = self.getInstanceSetting('client_secret')
            header = { 'User-Agent' : self.user_agent , 'Content-Type': 'application/x-www-form-urlencoded'}

            req = urllib2.Request(url, 'code='+str(code)+'&client_id='+str(clientID)+'&client_secret='+str(clientSecret)+'&redirect_uri=urn:ietf:wg:oauth:2.0:oob&grant_type=authorization_code', header)

            # try login
            try:
                response = urllib2.urlopen(req)
            except urllib2.URLError, e:
                if e.code == 403:
                    logger.error('Login information is incorrect or permission is denied (403)')
                else:
                    logger.error('Login information is incorrect or permission is denied')
                return

            response_data = response.read()
            response.close()

            # retrieve authorization token
            for r in re.finditer('\"access_token\"\s?\:\s?\"([^\"]+)\".+?' +
                             '\"refresh_token\"\s?\:\s?\"([^\"]+)\".+?' ,
                             response_data, re.DOTALL):
                accessToken,refreshToken = r.groups()
                self.authorization.setToken('auth_access_token',accessToken)
                self.authorization.setToken('auth_refresh_token',refreshToken)
                self.updateAuthorization()
                # ~ xbmcgui.Dialog().ok(self.addon.getLocalizedString(30000), self.addon.getLocalizedString(30142))
                logger.info('Account activated successfully')

            for r in re.finditer('\"error_description\"\s?\:\s?\"([^\"]+)\"',
                             response_data, re.DOTALL):
                errorMessage = r.group(1)
                # ~ xbmcgui.Dialog().ok(self.addon.getLocalizedString(30000), self.addon.getLocalizedString(30119), errorMessage)
                # ~ xbmc.log(errorMessage)
                logger.error('The following login error was encountered:')
                logger.error(errorMessage)

            return


    ##
    # refresh OAUTH2 access given refresh token
    #   parameters: none
    #   returns: none
    ##
    def refreshToken(self):

            header = { 'User-Agent' : self.user_agent }
            # ~ logger.debug('refreshToken User-Agent: ' + self.user_agent)

            url = 'https://accounts.google.com/o/oauth2/token'
            clientID = self.getInstanceSetting('client_id')
            clientSecret = self.getInstanceSetting('client_secret')
            header = { 'User-Agent' : self.user_agent , 'Content-Type': 'application/x-www-form-urlencoded'}

            req = urllib2.Request(url, 'client_id='+clientID+'&client_secret='+clientSecret+'&refresh_token='+self.authorization.getToken('auth_refresh_token')+'&grant_type=refresh_token', header)

            # try login
            try:
                response = urllib2.urlopen(req)
            except urllib2.URLError, e:
                if e.code == 403:
                    logger.error('Login information is incorrect or permission is denied (403)')
                else:
                    logger.error('Login information is incorrect or permission is denied')
                return

            response_data = response.read()
            response.close()

            # retrieve authorization token
            for r in re.finditer('\"access_token\"\s?\:\s?\"([^\"]+)\".+?' ,
                             response_data, re.DOTALL):
                accessToken = r.group(1)
                self.authorization.setToken('auth_access_token',accessToken)
                self.updateAuthorization()
                logger.debug('refreshToken updateAuthorization ' + accessToken)

            for r in re.finditer('\"error_description\"\s?\:\s?\"([^\"]+)\"',
                             response_data, re.DOTALL):
                errorMessage = r.group(1)
                # ~ xbmcgui.Dialog().ok(self.addon.getLocalizedString(30000), self.addon.getLocalizedString(30119), errorMessage)
                # ~ xbmc.log(errorMessage)
                logger.error('The following login error was encountered:')
                logger.error(errorMessage)

            return

    ##
    # return the appropriate "headers" for Google Drive requests that include 1) user agent, 2) authorization token
    #   returns: list containing the header
    ##
    def getHeadersList(self, isPOST=False, additionalHeader=None, additionalValue=None, isJSON=False):
        if self.authorization.isToken(self.instanceName, 'auth_access_token') and not isPOST:
#            return { 'User-Agent' : self.user_agent, 'Authorization' : 'Bearer ' + self.authorization.getToken('auth_access_token') }
            if additionalHeader is not None:
                return { 'Cookie' : 'DRIVE_STREAM='+ self.authorization.getToken('DRIVE_STREAM'), 'Authorization' : 'Bearer ' + self.authorization.getToken('auth_access_token'), additionalHeader : additionalValue }
            else:
                return {  'Cookie' : 'DRIVE_STREAM='+ self.authorization.getToken('DRIVE_STREAM'), 'Authorization' : 'Bearer ' + self.authorization.getToken('auth_access_token') }
        elif isJSON and self.authorization.isToken(self.instanceName, 'auth_access_token'):
#            return { 'User-Agent' : self.user_agent, 'Authorization' : 'Bearer ' + self.authorization.getToken('auth_access_token') }
            return { 'Content-Type': 'application/json', 'Cookie' : 'DRIVE_STREAM='+ self.authorization.getToken('DRIVE_STREAM'), 'Authorization' : 'Bearer ' + self.authorization.getToken('auth_access_token') }
        elif self.authorization.isToken(self.instanceName, 'auth_access_token'):
#            return { 'User-Agent' : self.user_agent, 'Authorization' : 'Bearer ' + self.authorization.getToken('auth_access_token') }
            return { "If-Match" : '*', 'Content-Type': 'application/atom+xml', 'Cookie' : 'DRIVE_STREAM='+ self.authorization.getToken('DRIVE_STREAM'), 'Authorization' : 'Bearer ' + self.authorization.getToken('auth_access_token') }
            #return {  'Content-Type': 'application/atom+xml', 'Authorization' : 'Bearer ' + self.authorization.getToken('auth_access_token') }
        elif self.authorization.isToken(self.instanceName, 'DRIVE_STREAM') and not isPOST:
            if additionalHeader is not None:
                return { 'Cookie' : 'DRIVE_STREAM='+ self.authorization.getToken('DRIVE_STREAM'), additionalHeader : additionalValue }
            else:
                return {  'Cookie' : 'DRIVE_STREAM='+ self.authorization.getToken('DRIVE_STREAM') }

        else:
            return { 'User-Agent' : self.user_agent}


    ##
    # return the appropriate "headers" for Google Drive requests that include 1) user agent, 2) authorization token, 3) api version
    #   returns: URL-encoded header string
    ##
    def getHeadersEncoded(self):
        return urllib.urlencode(self.getHeadersList())


    ##
    # retrieve the list of team drives
    #   parameters: none
    #   returns: array of team drives
    ##
    def getTeamDrives(self):

        # retrieve all items
        url = self.API_URL +'teamdrives?pageSize=100'
        # ~ url = self.API_URL +'drives?pageSize=10'
        drives = []

        while True:
            req = urllib2.Request(url, None, self.getHeadersList())

            # if action fails, validate login
            try:
              response = urllib2.urlopen(req)
            except urllib2.URLError, e:
              if e.code == 403 or e.code == 401:
                self.refreshToken()
                req = urllib2.Request(url, None, self.getHeadersList())
                try:
                  response = urllib2.urlopen(req)
                except urllib2.URLError, e:
                  # ~ xbmc.log('getTeamDrives '+str(e))
                  logger.error(str(e))
                  return
              else:
                # ~ xbmc.log('getTeamDrives '+str(e))
                logger.error(str(e))
                return

            response_data = response.read()
            response.close()

            for r1 in re.finditer('\{[^\"]+"kind": "drive#teamDrive"(.*?)\}' ,response_data, re.DOTALL):
                entry = r1.group(1)

                resourceID=''
                name=''
                for r in re.finditer('\"id\"\:\s+\"([^\"]+)\"' , entry, re.DOTALL):
                  resourceID = r.group(1)
                for r in re.finditer('\"name\"\:\s+\"([^\"]+)\"' , entry, re.DOTALL):
                  name = r.group(1)

                # ~ drives.append(teamdrive.teamdrive(resourceID,name));
                drives.append((resourceID,name));
                logger.debug('getTeamDrives %s %s' % (resourceID,name))


            # look for more pages of videos
            nextPageToken = ''
            for r in re.finditer('\"nextPageToken\"\:\s+\"([^\"]+)\"' , response_data, re.DOTALL):
                nextPageToken = r.group(1)


            # are there more pages to process?
            if nextPageToken == '':
                break
            else:
                url = self.API_URL +'teamdrives?pageSize=100&pageToken=' + str(nextPageToken)

        return drives


    ##
    # retrieve the list of drive files
    #   parameters: none
    #   returns: array of drive files
    ##
    def getFiles(self, drive_id=None, q=None, nextPageToken=None, perpage=10, orden='modifiedTime+desc'):
        if not drive_id: return None

        # retrieve all items
        url = self.API_URL +'files?corpora=drive&driveId='+drive_id+'&includeItemsFromAllDrives=true&supportsAllDrives=true'
        url += '&pageSize=' + str(perpage)
        if q: url += "&q=" + q #TODO? encode/quote ?
        if orden: url += '&orderBy=' + orden
        if nextPageToken: url += "&pageToken=" + nextPageToken
        # ~ url += '&fields=id%2Cname'
        logger.debug(url)

        req = urllib2.Request(url, None, self.getHeadersList())

        # if action fails, validate login
        try:
          response = urllib2.urlopen(req)
        except urllib2.URLError, e:
          if e.code == 403 or e.code == 401:
            self.refreshToken()
            req = urllib2.Request(url, None, self.getHeadersList())
            try:
              response = urllib2.urlopen(req)
            except urllib2.URLError, e:
              logger.error(str(e))
              return
          else:
            logger.error(str(e))
            return

        response_data = response.read()
        response.close()
        
        try:
            datos = json.loads(response_data)
        except:
            logger.debug(response_data)
            logger.error('No se puede cargar la respuesta de google!')
            datos = None

        return datos


    def getFileUrl(self, file_id=None):
        if not file_id: return None

        url = self.API_URL +'files/'+file_id+'?includeTeamDriveItems=true&supportsTeamDrives=true&alt=media'

        headers = self.getHeadersList()
        for i, h in enumerate(headers):
            url += '|' if i == 0 else '&'
            url += h + '=' + str(headers[h])

        return url


    def getFileInfo(self, file_id=None):
        if not file_id: return None

        url = self.API_URL +'files/'+file_id+'?includeTeamDriveItems=true&supportsTeamDrives=true'
        url += '&fields=id%2Cname%2Csize%2CvideoMediaMetadata'

        req = urllib2.Request(url, None, self.getHeadersList())

        # if action fails, validate login
        try:
          response = urllib2.urlopen(req)
        except urllib2.URLError, e:
          if e.code == 403 or e.code == 401:
            self.refreshToken()
            req = urllib2.Request(url, None, self.getHeadersList())
            try:
              response = urllib2.urlopen(req)
            except urllib2.URLError, e:
              logger.error(str(e))
              return None
          else:
            logger.error(str(e))
            return None

        response_data = response.read()
        response.close()
        
        try:
            datos = json.loads(response_data)
            datos['url_directo'] = self.getFileUrl(file_id)
        except:
            logger.debug(response_data)
            logger.error('No se puede cargar la respuesta de google!')
            datos = None

        try:
            datos['extra'] = self.getFileInfo_extra(file_id)
        except:
            datos['extra'] = None

        return datos


    def getFileInfo_extra(self, file_id=None):
        if not file_id: return None

        url = 'https://drive.google.com/get_video_info?docid='+file_id
        # ~ logger.debug(url)

        req = urllib2.Request(url, None, self.getHeadersList())

        # if action fails, validate login
        try:
          response = urllib2.urlopen(req)
        except urllib2.URLError, e:
          if e.code == 403 or e.code == 401:
            self.refreshToken()
            req = urllib2.Request(url, None, self.getHeadersList())
            try:
              response = urllib2.urlopen(req)
            except urllib2.URLError, e:
              logger.error(str(e))
              return None
          else:
            logger.error(str(e))
            return None

        response_data = response.read()

        cookies = ""
        cookie = response.headers["set-cookie"].split("HttpOnly, ")
        for c in cookie:
            cookies += c.split(";", 1)[0] + "; "
        headers_string = "|Cookie=" + cookies

        response.close()

        from core import scrapertools
        video_urls = []; urls = []
        data = response_data.decode('unicode-escape')
        data = urllib.unquote_plus(urllib.unquote_plus(data))
        logger.debug(data)
        url_streams = scrapertools.find_single_match(data, 'url_encoded_fmt_stream_map=(.*)')
        streams = scrapertools.find_multiple_matches(url_streams,
                                                     'itag=(\d+)&url=(.*?)(?:;.*?quality=.*?(?:,|&)|&quality=.*?(?:,|&))')

        itags = {'18': '360p', '22': '720p', '34': '360p', '35': '480p', '37': '1080p', '43': '360p', '59': '480p'}
        for itag, video_url in streams:
            if not video_url in urls:
                video_url += headers_string
                video_urls.append([itags[itag], video_url])
                urls.append(video_url)
            video_urls.sort(key=lambda video_urls: int(video_urls[0].replace("p", "")), reverse=True)

        return video_urls




    def getInstanceSetting(self,setting, default=None):
        try:
            # ~ return self.addon.getSetting(self.instanceName+'_'+setting)
            return config.get_setting(self.instanceName + '_'+setting, default=default)
        except:
            return default


    ##
    # if we don't have an authorization token set for the plugin, set it with the recent login.
    #   auth_token will permit "quicker" login in future executions by reusing the existing login session (less HTTPS calls = quicker video transitions between clips)
    ##
    def updateAuthorization(self):
        if self.authorization.isUpdated :#and addon.getSetting(self.instanceName+'_save_auth_token') == 'true':
            self.authorization.saveTokens(self.instanceName)

