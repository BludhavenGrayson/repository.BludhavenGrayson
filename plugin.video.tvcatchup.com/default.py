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
import xbmcvfs
import os
import sys
import datetime
import string
import hashlib
import net
import xbmc
import xbmcaddon
from resources.lib.modules.common import *
from resources.lib.modules.plugintools import *

icon   = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.tvcatchup.com', 'icon.jpg'))
fanart = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.tvcatchup.com', 'fanart.jpg'))

def main():
    listings()
    addLink('Blaze - EPG Unavailable','http://tvcatchup.com/watch/blaze',2,'https://www.tvcatchup.com/channel-images/blaze.png')
    addLink('CITV - EPG Unavailable','http://tvcatchup.com/watch/citv',2,'https://www.tvcatchup.com/channel-images/citv.png')
    addLink('E4 - EPG Unavailable','http://tvcatchup.com/watch/e4',2,'https://www.tvcatchup.com/channel-images/e4.png')
    addLink('Film4 - EPG Unavailable','http://tvcatchup.com/watch/film4',2,'https://www.tvcatchup.com/channel-images/film4.png')
    addLink('Food Network - EPG Unavailable','http://tvcatchup.com/watch/foodnetwork',2,'https://www.tvcatchup.com/channel-images/foodnetwork.png')
    addLink('ITV2 - EPG Unavailable','http://tvcatchup.com/watch/itv2',2,'https://www.tvcatchup.com/channel-images/itv2.png')
    addLink('ITV3 - EPG Unavailable','http://tvcatchup.com/watch/itv3',2,'https://www.tvcatchup.com/channel-images/itv3.png')
    addLink('Pick - EPG Unavailable','http://tvcatchup.com/watch/pick',2,'https://www.tvcatchup.com/channel-images/pick.png')
    addLink('Spike - EPG Unavailable','http://tvcatchup.com/watch/spike',2,'https://www.tvcatchup.com/channel-images/spike.png')
    addLink('Sky News - EPG Unavailable','http://tvcatchup.com/watch/skynews',2,'https://www.tvcatchup.com/channel-images/skynews.png')
    addLink('Travel Channel - EPG Unavailable','http://tvcatchup.com/watch/travelchannel',2,'https://www.tvcatchup.com/channel-images/travelchannel.png')
    addLink('True Crime - EPG Unavailable','http://tvcatchup.com/watch/truecrime',2,'https://www.tvcatchup.com/channel-images/truecrime.png')
    addLink('truTV - EPG Unavailable','http://tvcatchup.com/watch/trutv',2,'https://www.tvcatchup.com/channel-images/trutv.png')
    addLink('YourTV - EPG Unavailable','http://tvcatchup.com/watch/yourtv',2,'https://www.tvcatchup.com/channel-images/yourtv.png')
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)

def listings():
    url       = 'https://tvcatchup.com/'
    iconimage = ""
    req       = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response  = urllib2.urlopen(req)
    link      = response.read()
    response.close()

    pattern = ""
    matches = plugintools.find_multiple_matches(link,'<p class="channelsicon" style.+?>(.*?)</div>')
    
    for entry in matches:
       
        getchannel = plugintools.find_single_match(entry,'alt="Watch (.+?)"')
        gettitle   = plugintools.find_single_match(entry,'<br/> (.+?) </a>').replace("&#039;","'")
        name       = getchannel+' - '+gettitle
        geturl     = plugintools.find_single_match(entry,'<a href="(.+?)">')
        url        = 'http://tvcatchup.com' + geturl
        iconimage  = plugintools.find_single_match(entry,'src="(.+?)"')

        addLink(name,url,2,iconimage)
		
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
elif mode==2: tvcatchup(url)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
