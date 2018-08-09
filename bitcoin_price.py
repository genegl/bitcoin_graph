#!/usr/bin/python

import urllib2

class GetData:

    def __init__(self):
        pass

    def getRealTime(self):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
        response = opener.open('https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD')
        the_answer = response.read()
        #print response.read()

        return the_answer

    def analyze_answer(self, what_analyze):
        self.what_analyze = what_analyze


class DrawGraph:

    def __init__(self):
        pass

    def doTheDrowing(self):
        pass


#opener = urllib2.build_opener()
#opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
#response = opener.open('https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD')
#        the_answer = response.read()
print response.read()
##
