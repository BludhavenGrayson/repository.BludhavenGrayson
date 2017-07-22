'''
    UKTV Play Add-on
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
import xbmcvfs
import os
import sys
import datetime
import string
import hashlib
import xbmc
import xbmcaddon
import json
from resources.lib.modules.common import *
from resources.lib.modules.plugintools import *
from resources.lib.modules.uktv_play import *

icon   = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.bhg.uktvplay', 'icon.jpg'))
fanart = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.bhg.uktvplay', 'fanart.jpg'))
logos  = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.bhg.uktvplay/resources/logos', ''))

def main():
	addDir('Dave','http://uktvplay.uktv.co.uk/shows/channel/dave/',10,logos+'dave.png')
	addDir('Drama','http://uktvplay.uktv.co.uk/shows/channel/drama/',10,logos+'drama.png')
	addDir('Really','http://uktvplay.uktv.co.uk/shows/channel/really/',10,logos+'really.png')
	addDir('Yesterday','http://uktvplay.uktv.co.uk/shows/channel/yesterday/',10,logos+'yesterday.png')
		
def get_params():
        param=[]
        paramstring = sys.argv[2]
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
        
              
params=get_params()
url=None
name=None
mode=None

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

print "Mode: "+str(mode)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        main()
	
elif mode==1: play(url)
elif mode==4: vod_play(url)
elif mode==10: vod_uktv(url)
elif mode==11: vod_uktvEp(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
