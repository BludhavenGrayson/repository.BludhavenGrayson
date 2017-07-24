'''
	BoxPlus Network Add-on
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
fanart    = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.boxplus', 'fanart.jpg'))
logo       = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.boxplus/resources/logos', ''))

def main():
	addLink('4Music','http://csm-e.tm.yospace.com/csm/extlive/boxplus01,4music-desktop.m3u8?yo.up=http%3A%2F%2Fak-boxplus01-live.cds1.yospace.com%2F4music%2F&pageURL=http%3A%2F%2Fwww.boxplus.com%2F&width=950&height=940&yo.po=5&yo.ac=false&yopad=true.m3u8',1,logo+'4Music.png')
	addLink('The Box','http://csm-e.tm.yospace.com/csm/extlive/boxplus01,thebox-desktop.m3u8?yo.up=http%3A%2F%2Fak-boxplus01-live.cds1.yospace.com%2Fthebox%2F&pageURL=http%3A%2F%2Fwww.boxplus.com%2F&width=950&height=940&yo.po=5&yo.ac=false&yopad=true.m3u8',1,logo+'thebox.png')
	addLink('Box Hits','http://csm-e.tm.yospace.com/csm/extlive/boxplus01,boxhits-desktop.m3u8?yo.up=http%3A%2F%2Fak-boxplus01-live.cds1.yospace.com%2Fboxhits%2F&pageURL=http%3A%2F%2Fwww.boxplus.com%2F&width=950&height=940&yo.po=5&yo.ac=false&yopad=true.m3u8',1,logo+'boxhits.png')
	addLink('Box Upfront','http://csm-e.tm.yospace.com/csm/extlive/boxplus01,boxupfront-desktop.m3u8?yo.up=http%3A%2F%2Fak-boxplus01-live.cds1.yospace.com%2Fboxupfront%2F&pageURL=http%3A%2F%2Fwww.boxplus.com%2F&width=950&height=940&yo.po=5&yo.ac=false&yopad=true.m3u8',1,logo+'boxupfront.png')
	addLink('Kerrang!','http://csm-e.tm.yospace.com/csm/extlive/boxplus01,kerrang-desktop.m3u8?yo.up=http%3A%2F%2Fak-boxplus01-live.cds1.yospace.com%2Fkerrang%2F&pageURL=http%3A%2F%2Fwww.boxplus.com%2F&width=950&height=940&yo.po=5&yo.ac=false&yopad=true.m3u8',1,logo+'kerrang.png')
	addLink('Kiss','http://csm-e.tm.yospace.com/csm/extlive/boxplus01,kiss-desktop.m3u8?yo.up=http%3A%2F%2Fak-boxplus01-live.cds1.yospace.com%2Fkiss%2F&pageURL=http%3A%2F%2Fwww.boxplus.com%2F&width=950&height=940&yo.po=5&yo.ac=false&yopad=true.m3u8',1,logo+'kiss.png')
	addLink('Magic','http://csm-e.tm.yospace.com/csm/extlive/boxplus01,magic-desktop.m3u8?yo.up=http%3A%2F%2Fak-boxplus01-live.cds1.yospace.com%2Fmagic%2F&pageURL=http%3A%2F%2Fwww.boxplus.com%2F&width=950&height=940&yo.po=5&yo.ac=false&yopad=true.m3u8',1,logo+'magic.png')
		
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
