'''
	Fitness Blender Add-on
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

ADDON     = xbmcaddon.Addon(id='plugin.video.fitnessblender')
addon_id  = xbmcaddon.Addon().getAddonInfo('id')
selfAddon = xbmcaddon.Addon(id=addon_id)
fanart    = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.fitnessblender', 'fanart.jpg'))
icon      = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.fitnessblender', 'icon.png'))
baseurl   = 'https://www.fitnessblender.com/videos/'
vidurl    = 'https://www.fitnessblender.com/videos?keywords=&minlength=0&maxlength=0&minburn=0&maxburn=0&'

def CATEGORIES():
	addDir('All Videos','https://www.fitnessblender.com/videos',2,icon)
	addDir('[B]Body Focus:[/B] Core',vidurl+'focus%5B%5D=2',2,icon)
	addDir('[B]Body Focus:[/B] Lower Body',vidurl+'focus%5B%5D=3',2,icon)
	addDir('[B]Body Focus:[/B] Upper Body',vidurl+'focus%5B%5D=1',2,icon)
	addDir('[B]Body Focus:[/B] Total Body',vidurl+'focus%5B%5D=4',2,icon)
	addDir('[B]Training Type:[/B] Balance / Agility',vidurl+'trainingtype%5B%5D=5',2,icon)
	addDir('[B]Training Type:[/B] Barre',vidurl+'trainingtype%5B%5D=6',2,icon)
	addDir('[B]Training Type:[/B] Cardiovascular',vidurl+'trainingtype%5B%5D=7',2,icon)
	addDir('[B]Training Type:[/B] HIIT',vidurl+'trainingtype%5B%5D=8',2,icon)
	addDir('[B]Training Type:[/B] Kettlebell',vidurl+'trainingtype%5B%5D=9',2,icon)
	addDir('[B]Training Type:[/B] Low Impact',vidurl+'trainingtype%5B%5D=10',2,icon)
	addDir('[B]Training Type:[/B] Pilates',vidurl+'trainingtype%5B%5D=11',2,icon)
	addDir('[B]Training Type:[/B] Plyometric',vidurl+'trainingtype%5B%5D=12',2,icon)
	addDir('[B]Training Type:[/B] Strength Training',vidurl+'trainingtype%5B%5D=13',2,icon)
	addDir('[B]Training Type:[/B] Toning',vidurl+'trainingtype%5B%5D=14',2,icon)
	addDir('[B]Training Type:[/B] Warm Up / Cool Down',vidurl+'trainingtype%5B%5D=15',2,icon)
	addDir('[B]Training Type:[/B] Yoga / Stretching / Flexibility',vidurl+'trainingtype%5B%5D=16',2,icon)
	#addDir('[B]Training Type:[/B] ','',2,icon)

def getVideos(url):
	link = open_url(url)
	link = link
	match=re.compile('<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>\n				<div class=\'clear\'></div>\n			</a>\n		</div>\n		<p class=\'videogriddescription\'><a href="/videos/(.+?)">').findall(link)
	for iconimage, name, url in match:
		url = 'https://www.fitnessblender.com/videos/'+url
		iconimage = 'https://www.fitnessblender.com'+iconimage
		addLink(name,url,1,iconimage)
	next=re.compile("col-sm-2'><a href='(.+?)' class='paginationnext'>Next").findall(link)
	for url in next:
		url       = 'https://www.fitnessblender.com'+url
		name      = 'Next Page'
		iconimage = icon
		addDir(name,url,2,iconimage)
	next2=re.compile(" <a href='(.+?)' class='paginationnext'>Next").findall(link)
	for url in next2:
		url       = 'https://www.fitnessblender.com'+url
		name      = 'Next Page'
		iconimage = icon
		addDir(name,url,2,iconimage)
		
def play(name,url):
	link = open_url(url)
	link = link
	match=re.compile('<iframe.+?src=".+?/embed/(.+?)\?rel=.+?</iframe>').findall(link)
	for yt_id in match:
		name = name
		url  = 'plugin://plugin.video.youtube/play/?video_id='+yt_id
		playYT(name,url)

def playYT(name,url):
		stream_url = url
		liz = xbmcgui.ListItem(name, path=stream_url)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
		
def open_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	link=cleanHex(link)
	response.close()
	return link
	
def cleanHex(text):
	def fixup(m):
		text = m.group(0)
		if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
		else: return unichr(int(text[2:-1])).encode('utf-8')
	try :return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))
	except:return re.sub("(?i)&#\w+;", fixup, text.encode("ascii", "ignore").encode('utf-8'))
		
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
		CATEGORIES()

elif mode==1: play(name,url)
elif mode==2: getVideos(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
