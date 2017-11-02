'''
	TVCatchup.com Add-on
	Copyright (C) 2017 BludhavenGrayson

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

import urllib
import urllib2
import re
import xbmcplugin
import xbmcgui
import os
import sys
import datetime
import string
import plugintools
import xbmcaddon
import base64
import xbmc

fanart    = 'special://home/addons/plugin.video.tvcatchup.com/fanart.jpg'

def play(url):
	resolved = url+'|User-Agent=TVCatchup/1.0.1 (samsung/SM-J7008; Android 4.4.2/KOT49H)'
	item     = xbmcgui.ListItem(path=resolved)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	
def open_url(url):
	req      = urllib2.Request(url)
	#req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
	response = urllib2.urlopen(req)
	link     = response.read()
	link     = cleanHex(link)
	response.close()
	return link
	
def addLink(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', iconimage)
        liz.setProperty("IsPlayable","true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', iconimage)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    try :return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))
    except:return re.sub("(?i)&#\w+;", fixup, text.encode("ascii", "ignore").encode('utf-8'))
	
def tvcatchup_base64(url):
	link = open_url(url)
	link = link
	b64  = re.compile('=  "(.+?)";').findall(link)
	for base64str in b64:
		decodedstr = base64.b64decode(base64str)
		play(decodedstr)
		
def tvcatchup(url):
	link  = open_url(url)
	link  = link
	match = re.compile('<source src="(.+?)" type="application/x-mpegURL">').findall(link)
	for url in match:
		play(url)
	
def	tvcatchup2(url):
    url       = url
    iconimage = ""
    req       = urllib2.Request(url)
    #req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    #req.add_header('User-Agent', 'Magic Browser')
    response  = urllib2.urlopen(req)
    link      = response.read()
    response.close()

    pattern = ""
    matches = plugintools.find_multiple_matches(link,">jwplayer(.*?)</script>")
    
    for entry in matches:
       
        #url = plugintools.find_single_match(entry,'var.+?"(.+?)";')
        url = plugintools.find_single_match(entry,'=  "(.+?)";')
        decrypt = base64.urlsafe_b64decode(url)
        #url = url
        xbmc.log('[plugin.video.tvcatchup.com] Attempting to play: %s' % url,  xbmc.LOGDEBUG)
        print url
        #decrypted = unpad(cipher.decrypt(decodestr))

        play(decrypt)
	
def	tvcatchup_old(url):
    url       = url
    iconimage = ""
    req       = urllib2.Request(url)
    #req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    response  = urllib2.urlopen(req)
    link      = response.read()
    response.close()

    pattern = ""
    matches = plugintools.find_multiple_matches(link,"jwplayer(.*?)</script>")
    
    for entry in matches:
       
        url = plugintools.find_single_match(entry,"file: '(.+?)'")
        xbmc.log('[plugin.video.tvcatchup.com] Attempting to play: %s' % url,  xbmc.LOGDEBUG)

        play(url)