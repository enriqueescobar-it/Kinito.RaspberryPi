import xbmc, xbmcaddon, xbmcgui, xbmcplugin, urllib2, urllib, re, string, sys, os, traceback, time, datetime,json,urlparse
__plugin__ = 'Pluralsight'
__author__ = 'Jon Flanders'
__date__ = '03-05-2013'
__version__ = '1.2.0'
id = 'pluralsight.plugin.xmbc'
VIDEO_URL = 'http://www.youtube.com/user/pluralsight/videos'


def open_url( url ):
	req = urllib2.Request( url )
	content = urllib2.urlopen( req )
	data = content.read()
	content.close()
	return data

def build_main_directory():
	response = urllib2.urlopen('http://gdata.youtube.com/feeds/api/videos?author=pluralsight&alt=json')
	tree = json.loads(response.read())
	feed = tree['feed']
	entries = feed['entry']
	ADDON = xbmcaddon.Addon(id = 'pluralsight.plugin.xmbc')
	HANDLE = int(sys.argv[1])
	icon = os.path.join(ADDON.getAddonInfo('path'), 'icon.png')
	for e in entries:
		title = e['title']['$t']
		url = e['id']['$t']
		item = xbmcgui.ListItem(title, iconImage = icon)
		#print 'title ==' + title + ' url ' + url
		u = sys.argv[0] + "?mode=0&name=" +  title  + "&url=" + url 
		xbmcplugin.addDirectoryItem(HANDLE, u, item, False)
	xbmcplugin.endOfDirectory(HANDLE)

def play_video( name, url ):
	parts = urlparse.urlsplit(url)
	ua = parts.path.split('/')
	vid = ua[len(ua)-1]
	item = xbmcgui.ListItem( label = name, iconImage = "DefaultVideo.png", thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ) )
	item.setInfo( type="Video", infoLabels={ "Title": name , "Director": "Pluralsight", "Studio": "Pluralsight" } )
	playback_url = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % vid
	print 'trying to play ' + playback_url
	
	xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(playback_url)

def get_params():
	param = []
	paramstring = sys.argv[2]
	if len( paramstring ) >= 2:
		params = sys.argv[2]
		cleanedparams = params.replace( '?', '' )
		if ( params[len( params ) - 1] == '/' ):
			params = params[0:len( params ) - 2]
		pairsofparams = cleanedparams.split( '&' )
		param = {}
		for i in range( len( pairsofparams ) ):
			splitparams = {}
			splitparams = pairsofparams[i].split( '=' )
			if ( len( splitparams ) ) == 2:
				param[splitparams[0]] = splitparams[1]					
	return param

params = get_params()
mode = None
name = None
url = None

try:
        url = urllib.unquote_plus(params["url"])
except:
        pass
try:
        name = urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode = int(params["mode"])
except:
        pass

if mode == None:
	build_main_directory()
elif mode == 0:
	play_video( name, url)


