'''
	TVPlayer.com Add-on
	Copyright (C) 2017 BludhavenGrayson
	Copyright (C) 2017 Mikey1234

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
import sys
import re
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmc
import os
import json
import base64
import net

net        = net.Net()
plugin     = xbmcaddon.Addon(id='plugin.video.tvplayer.com')
dataPath   = xbmc.translatePath(plugin.getAddonInfo('profile'))
cookiePath = os.path.join(dataPath, 'cookies')
cookieJar  = os.path.join(cookiePath, 'tvplayer.lwp')

if os.path.exists(cookiePath) == False:
		os.makedirs(cookiePath)

def main():
	link  = openURL('https://pastebin.com/raw/njE3Z76f')
	link  = link
	match = re.compile('<li data-name="(.+?)" class="online free"><a href=".+?" title=".+?"><img src="https://assets.tvplayer.com/common/logos-square/150/Inverted/(.+?).png" alt=.+?"></a></li>').findall(link)
	for name,url in match:
		iconimage = 'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url
		addLink(name,url,1,iconimage)
		xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)

def login():
	loginURL = 'https://tvplayer.com/account/login/'
	email    = plugin.getSetting('email')
	password = plugin.getSetting('password')
	UA       = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
	headers  = {'Host':'tvplayer.com','Connection':'keep-alive','Cache-Control':'max-age=0','Origin':'https://tvplayer.com','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36','Content-Type':'application/x-www-form-urlencoded','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Referer':'https://tvplayer.com/watch','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.8'}
	link     = net.http_GET(loginURL, headers).content
	net.saveCookies(cookieJar)
	token    = re.compile('name="token" value="(.+?)"').findall(link)[0]
	data     = {'email':email,'password':str(password),'token':token}
	net.setCookies(cookieJar)
	net.http_POST(loginURL, data, headers)
	net.saveCookies(cookieJar)

def openURL(url):								   
	req      = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link     = response.read()
	response.close()
	return link

def openStream(url):
	import time
	timestamp = int(time.time()) + 4 * 60 * 60
	header    = {'Token':plugin.getSetting('token'),'Token-Expiry': plugin.getSetting('expiry'),'Referer':plugin.getSetting('referer'),'User-Agent': 'iPhone/iOS 8.4 (iPhone; U; CPU iPhone OS 8_4 like Mac OS X;)'}
	req       = urllib2.Request(url,headers=header)
	response  = urllib2.urlopen(req)
	link      = response.read()
	response.close()
	cookie    = response.info()['Set-Cookie']			   
	return link,cookie

def tvplayer(url):
	if plugin.getSetting('premium')== 'true':
		login()
		net.setCookies(cookieJar)
	headers   = {'Host': 'tvplayer.com','Connection': 'keep-alive','Origin': 'http://tvplayer.com','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Accept': '*/*','Accept-Encoding': 'gzip, deflate','Accept-Language': 'en-US,en;q=0.8'}
	html      = net.http_GET('http://tvplayer.com/watch/', headers).content
	dataToken = re.compile('data-token="(.+?)"').findall(html)[0]
	getURL    = 'http://tvplayer.com/watch/context?resource=%s&gen=%s' % (url,dataToken)
	html      = net.http_GET(getURL, headers).content
	validate  = re.compile('"validate":"(.+?)"').findall(html)[0]
	if plugin.getSetting('premium') == 'true':
		token = re.compile('"token":"(.+?)"').findall(html)[0]
	else:
		token = 'null'
	data      = {'service':'1','platform':'chrome','id':url,'token':token,'validate':validate}
	postURL   = 'http://api.tvplayer.com/api/v2/stream/live'
	headers   = {'Host': 'api.tvplayer.com','Connection': 'keep-alive','Origin': 'http://api.tvplayer.com','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Accept': '*/*','Accept-Encoding': 'gzip, deflate','Accept-Language': 'en-US,en;q=0.8'}
	LINK      = net.http_POST(postURL, data,headers=headers).content
	net.saveCookies(cookieJar)
	return re.compile('stream": "(.+?)"').findall(LINK)[0]

def play(name,url,iconimage):
	stream  = tvplayer(url)
	host    = stream.split('//')[1]
	host    = host.split('/')[0]
	headers = {'Host': host,'Connection': 'keep-alive','Origin': 'http://'+host,'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
	token   = open(cookieJar).read()
	token   = 'AWSELB='+re.compile('AWSELB=(.+?);').findall (token)[0]
	liz     = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
	liz.setInfo(type='Video', infoLabels={'Title':name})
	liz.setProperty("IsPlayable","true")
	liz.setPath(stream+'|Cookies='+token)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

def addLink(name,url,mode,iconimage):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setProperty('fanart_image', iconimage)
		liz.setProperty("IsPlayable","true")
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		return ok					

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

params    = get_params()
url       = None
name      = None
mode      = None
iconimage = None


try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: mode=int(params["mode"])
except: pass

print "Mode: "      + str(mode)
print "URL: "       + str(url)
print "Name: "      + str(name)
print "IconImage: " + str(iconimage)
   
		
if mode==None or url==None or len(url)<1:
		main()
	   
elif mode==1: play(name,url,iconimage)
	   
xbmcplugin.endOfDirectory(int(sys.argv[1]))
