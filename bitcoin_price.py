#!/usr/bin/python

import urllib2
import plotly
import plotly.plotly as py
import plotly.graph_objs as go



class GetData():

    def __init__(self):
        pass

    def get_real_time(self):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
        response = opener.open('https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD')
        the_answer = response.read()

        return the_answer

    def analyze_answer(self, what_analyze):
        self.what_analyze = what_analyze


class DrawGraph():

    def __init__(self):
        pass

    def do_the_drawing(self, time, price):
        price = go.Scatter(
        x=time,
        y=price
        )
        trace1 = go.Scatter(
        x=[1, 2, 3, 4],
        y=[16, 5, 11, 9]
        )
        data = [price, trace1]

        py.plot(data, filename = 'basic-line', auto_open=True)


        #return fig

the_data = GetData()
dump_of_data = the_data.get_real_time()
clean_data = the_data.analyze_answer(dump_of_data)

the_graph = DrawGraph()
plot_url = py.plot(the_graph.do_the_drawing())
print (plot_url)
#opener = urllib2.build_opener()
#opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
#response = opener.open('https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD')
#        the_answer = response.read()
#print response.read()
##
