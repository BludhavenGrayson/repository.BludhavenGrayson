'''
	ROH Wrestling Add-on
	Copyright (C) 2017 BludhavenGrayson
	Copyright (C) 2016 rw86

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

addon     = xbmcaddon.Addon('plugin.video.rohwrestling')
enableVOD = addon.getSetting('ringside')
fanart    = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.rohwrestling', 'fanart.jpg'))
icon      = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.rohwrestling', 'icon.png'))


def main():
	addLink('[B]Watch the Latest Episode[/B]','http://rohwrestling.com/tv/current',2,icon)
	addDir('[B]ROH TV:[/B] 2017','17',4,icon)
	addDir('[B]ROH TV:[/B] 2016','16',4,icon)
	addDir('[B]ROH TV:[/B] 2015','15',4,icon)
	addDir('[B]ROH TV:[/B] 2014','14',4,icon)
	if enableVOD == "true":
		addDir('[B]Ringside:[/B] Video-On-Demand','url',5,icon)
	else:
		pass
		
def getRingside():
	addDir('[B]VOD:[/B] 2016','16',3,icon)
	addDir('[B]VOD:[/B] 2015','15',3,icon)
	addDir('[B]VOD:[/B] 2014','14',3,icon)
	addDir('[B]VOD:[/B] 2013','13',3,icon)
	addDir('[B]VOD:[/B] 2012','12',3,icon)
	addDir('[B]VOD:[/B] 2011','11',3,icon)
	addDir('[B]VOD:[/B] 2010','10',3,icon)
	addDir('[B]VOD:[/B] 2009','09',3,icon)
	addDir('[B]VOD:[/B] 2008','08',3,icon)
	addDir('[B]VOD:[/B] 2007','07',3,icon)
	addDir('[B]VOD:[/B] 2006','06',3,icon)
	addDir('[B]VOD:[/B] 2005','05',3,icon)
	addDir('[B]VOD:[/B] 2004','04',3,icon)
	addDir('[B]VOD:[/B] 2003','03',3,icon)
	addDir('[B]VOD:[/B] 2002','02',3,icon)
	
def getEpisode(url):
	link = open_url(url)
	link = link
	match=re.compile('.c.ooyala.com/(.+?)/').findall(link)
	for url in match:
		url = 'http://player.ooyala.com/player/ipad/'+url+'.m3u8'
		#name = 'Ring of Honor TV'
		play(name,url)
		
def getVOD(url):
	link = open_url('http://rohwrestling.com/vod')
	link = link
	match=re.compile('<span class="field-content"><a href="(.+?)" class="ppv-product-load">(.+?)/'+url+' (.+?)</a></span>').findall(link)
	#match=list(reversed(match))
	for url2,date,name in match:
		url2      = 'http://rohwrestling.com'+url2
		name      = name.replace("&#039;","'")
		name      = date+'/'+url+' '+name
		iconimage = icon
		addLink(name,url2,2,iconimage)
	match2=re.compile('<span class="field-content"><a href="(.+?)" class="ppv-product-load">(.+?).'+url+' (.+?)</a></span>').findall(link)
	#match=list(reversed(match))
	for url2,date,name in match2:
		url2      = 'http://rohwrestling.com'+url2
		name      = name.replace("&#039;","'")
		name      = date+'.'+url+' '+name
		iconimage = icon
		addLink(name,url2,2,iconimage)
	
def getTV(url):
	link = open_url('http://rohwrestling.com/tv/current')
	link = link
	match=re.compile('<span class="field-content"><a href="(.+?)" class="ppv-product-load">(.+?)/'+url+'</a></span>').findall(link)
	#match=list(reversed(match))
	for url2, name in match:
		url2      = 'http://rohwrestling.com'+url2
		name      = name+'/'+url
		iconimage = icon
		addLink(name,url2,2,iconimage)
						
def play(name,url):
		stream_url = url
		liz = xbmcgui.ListItem(name, path=stream_url)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
		
def open_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link
		
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

def addDir(name,url,mode,iconimage):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name} )
		liz.setProperty('fanart_image', fanart)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
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


print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
		print ""
		main()

elif mode==1: play(name,url)
elif mode==2: getEpisode(url)
elif mode==3: getVOD(url)
elif mode==4: getTV(url)
elif mode==5: getRingside()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
