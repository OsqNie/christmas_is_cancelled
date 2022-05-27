#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Oskar / 2015
#
# Skripti paremman joulun puolesta
#
# Asenna ensin:
# https://github.com/hugosenari/mpris2
# https://github.com/hugosenari/pydbusdecorator
#

from mpris2.player import Player
from mpris2.utils import get_players_uri
from mpris2.some_players import Some_Players
import time, json, urllib2, urllib, hashlib, sys
  
SHARED_SECRET = 'askj5473::23'

class PlayerHandler: 

  def __init__(self):
    self.uri = get_players_uri()[0]
    if self.uri.find('spotify') == -1: 
      quit()
    self.data = self.getMetadata()
    self.mode = sys.argv
    self.banned_words = [
      'christ',
      'xmas',
      'jul'
      'christmas',
      'joulu',
      'valko',
      'snow',
      'joy',
      'bell'
    ]
    # Danger Zone
    self.replace_song = 'spotify:track:2CJtimCSGAn8x6RE3irZFV'
    # OR if you want to really tune into the Christmas spirit: The only real christmas song
    # self.replace_song = 'spotify:track:0QPYn15U8IQHKcH2LDfrek'
  def __self__(self):
    print self.data

  def getMetadata(self):
    mp2 = Player(dbus_interface_info={'dbus_uri': self.uri})
    return mp2.Metadata

  def last_xmas(self):
    mp2 = Player(dbus_interface_info={'dbus_uri': self.uri})
    for ban in self.banned_words:
      if ( self.data[self.data.TITLE].lower().find(ban) >= 0 and mp2.PlaybackStatus == 'Playing' ):
        if self.mode[-1] == "DANGER!":
          print('Vaarantava virhe!')
          mp2.OpenUri( self.replace_song )
        else:
          print('Stop')
          mp2.Stop()
        return

    print('Jatkuu')
    return

handler = PlayerHandler()
handler.last_xmas()
