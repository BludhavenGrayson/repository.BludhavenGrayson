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
	
	name = 'BBC One'
	url  = '89'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'BBC Two'
	url  = '90'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'ITV'
	url  = '204'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Channel 4'
	url  = '92'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Five'
	#url  = '93'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Dave'
	url  = '300'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Really'
	url  = '306'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Yesterday'
	url  = '308'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Drama'
	url  = '346'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Home'
	url  = '512'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Quest'
	url  = '327'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Quest Red'
	url  = '577'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'ITV2'
	url  = '556'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'ITV3'
	url  = '558'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'More4'
	url  = '563'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'ITV4'
	url  = '559'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'ITVBe'
	url  = '557'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = '5Star'
	#url  = '566'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Spike'
	#url  = '568'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Food Network'
	url  = '125'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Travel Channel'
	url  = '126'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = '4seven'
	url  = '565'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'CNN International'
	url  = '286'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'BBC Four'
	url  = '110'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'QVC'
	url  = '247'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'BET'
	url  = '572'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Lifetime'
	#url  = '281'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'TLC'
	#url  = '330'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Universal'
	#url  = '597'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Syfy'
	#url  = '594'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'E!'
	#url  = '596'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'W'
	#url  = '307'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'GOLD'
	#url  = '303'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Alibi'
	#url  = '299'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Comedy Central'
	#url  = '282'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'MTV'
	#url  = '288'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Comedy Central Extra'
	#url  = '323'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Sony Entertainment'
	#url  = '298'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Movies24'
	#url  = '595'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'History'
	#url  = '283'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Discovery'
	#url  = '328'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Investigation Discovery'
	#url  = '334'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Discovery Turbo'
	#url  = '335'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Animal Planet'
	#url  = '331'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'H2'
	#url  = '284'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Crime + Investigation'
	#url  = '285'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Viceland'
	#url  = '588'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Good Food'
	#url  = '304'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Eden'
	#url  = '302'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'National Geographic'
	#url  = '507'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'NatGeo Wild'
	#url  = '505'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Eurosport 1'
	#url  = '332'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Eurosport 2'
	#url  = '333'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'BoxNation'
	#url  = '591'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Ginx'
	#url  = '309'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'CBeebies'
	url  = '114'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'CBBC'
	url  = '113'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'CITV'
	url  = '560'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Nickelodeon'
	#url  = '222'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Nick Jr'
	#url  = '223'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Nick Jr Too'
	#url  = '516'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Cartoon Network'
	#url  = '278'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Boomerang'
	#url  = '280'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'Cartoonito'
	#url  = '179'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	#name = 'BabyTV'
	#url  = '506'
	#addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Heart'
	url  = '153'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Capital TV'
	url  = '157'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Clubland'
	url  = '225'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Chilled'
	url  = '226'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Channel AKA'
	url  = '227'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'NOW Music'
	url  = '228'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Dave ja vu'
	url  = '317'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Yesterday+1'
	url  = '318'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Food Network+1'
	url  = '254'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Travel Channel+1'
	url  = '255'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'QVC Plus'
	url  = '344'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Fashion TV'
	url  = '193'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Revelation TV'
	url  = '262'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'GOD TV'
	url  = '573'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'S4C'
	url  = '251'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'BBC Alba'
	url  = '236'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Community Channel'
	url  = '259'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Notts TV'
	url  = '590'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'BBC News'
	url  = '111'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Bloomberg'
	url  = '514'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'France 24'
	url  = '199'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'NHK World'
	url  = '301'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Euronews'
	url  = '287'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Newsy'
	url  = '575'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Fascination TV'
	url  = '576'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'TRT World'
	url  = '580'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'BBC Parliament'
	url  = '345'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Al Jazeera'
	url  = '146'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'Russia Today'
	url  = '156'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'QVC Extra'
	url  = '248'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'QVC Style'
	url  = '249'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'QVC Beauty'
	url  = '250'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
	name = 'TV Warehouse'
	url  = '584'
	addLink(name,url,1,'https://assets.tvplayer.com/common/logos-square/256/Inverted/%s.png' % url)
	
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
	header    = {'Token':plugin.getSetting('token'),'Token-Expiry': plugin.getSetting('expiry'),'Referer':plugin.getSetting('referer'),'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
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
	return re.compile('stream":"(.+?)"').findall(LINK)[0]

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
