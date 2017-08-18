'''
	PAC-12 Network Add-on
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
import xbmcaddon

addon_id  = xbmcaddon.Addon().getAddonInfo('id')
selfAddon = xbmcaddon.Addon(id=addon_id)
fanart    = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.pac12.network', 'fanart.jpg'))
logo       = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.pac12.network/resources/logos', ''))

def main():
	addLink('PAC-12 Network','http://p12n-lh.akamaihd.net/i/network_delivery@428818/master.m3u8',1,logo+'1.png')
	#addLink('PAC-12 Plus','http://p12x-lh.akamaihd.net/i/pac12plus_delivery@198236/master.m3u8',1,logo+'2.png')
	addLink('PAC-12 Arizona','http://p12a-lh.akamaihd.net/i/arizona_delivery@199730/master.m3u8',1,logo+'3.png')
	addLink('PAC-12 Bay Area','http://p12b-lh.akamaihd.net/i/bayarea_delivery@429334/master.m3u8',1,logo+'4.png')
	addLink('PAC-12 Los Angeles','http://p12l-lh.akamaihd.net/i/la_delivery@425541/master.m3u8',1,logo+'5.png')
	addLink('PAC-12 Mountain','http://p12m-lh.akamaihd.net/i/mountain_delivery@428912/master.m3u8',1,logo+'6.png')
	addLink('PAC-12 Oregon','http://p12o-lh.akamaihd.net/i/oregon_delivery@103261/master.m3u8',1,logo+'7.png')
	addLink('PAC-12 Washington','http://p12w-lh.akamaihd.net/i/washington_delivery@426584/master.m3u8',1,logo+'8.png')
	
		
def play(name,url):
		stream_url = url
		liz        = xbmcgui.ListItem(name, path=stream_url)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
		
def open_url(url):
	req      = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link     = response.read()
	link     = cleanHex(link)
	response.close()
	return link
	
def cleanHex(text):
	def fixup(m):
		text        = m.group(0)
		if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
		else: return unichr(int(text[2:-1])).encode('utf-8')
	try: return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))
	except: return re.sub("(?i)&#\w+;", fixup, text.encode("ascii", "ignore").encode('utf-8'))
		
def get_params():
		param=[]
		paramstring=sys.argv[2]
		if len(paramstring)>=2:
				params=sys.argv[2]
				cleanedparams=params.replace('?','')
				if (params[len(params)-1]=='/'):
						params=params[0:len(params)-2]
				pairsofparams=cleanedparams.split('&')
				param={}
				for i in range(len(pairsofparams)):
						splitparams={}
						splitparams=pairsofparams[i].split('=')
						if (len(splitparams))==2:
								param[splitparams[0]]=splitparams[1]
								
		return param
		
def addLink(name,url,mode,iconimage):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name} )
		liz.setProperty('fanart_image', fanart)
		liz.setProperty("IsPlayable","true")
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		return ok
		
params=get_params()
url=None
name=None
mode=None
iconimage=None

try:
		url=urllib.unquote_plus(params["url"])
except:
		pass
try:
		name=urllib.unquote_plus(params["name"])
except:
		pass
try:
		mode=int(params["mode"])
except:
		pass
try:
		iconimage=urllib.unquote_plus(params["iconimage"])
except:
		pass
try:
		iconimage=urllib.unquote_plus(params["fanart"])
except:
		pass


print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Fanart: "+str(fanart)

if mode==None or url==None or len(url)<1:
		print ""
		main()

elif mode==1: play(name,url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
