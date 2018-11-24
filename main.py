# -*- coding: utf-8 -*-

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin
import xbmc

xbmc.Player().play("http://kanlive.bynetcdn.com/kan11/smil:kan11_mp4.smil/playlist.m3u8")
