#!/usr/bin/python

import re
import urllib2
import datetime
import plotly
import plotly.plotly as py
import plotly.graph_objs as go



class GetData():

    def __init__(self):
        pass

    def get_real_time(self):
        """
        Reading data from API.

        :return: whole dump oof data
        
        """
        opener = urllib2.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
        response = opener.open('https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit=48')
        the_answer = response.read()

        return the_answer

    def analyze_answer(self, what_analyze):
        """
        Analyzing recived data.

        :time_index: Gets index for timestamps
        :real_time: List of date and time in readable format
        :price_index: Gets index for prices
        :price_end: End index for price
        :real_price: List of prices
        :return: real_price, real_time
        
        """
        self.what_analyze = what_analyze
        real_time = []
        real_price = []
        
        i = 0

        self.time_index = [m.start() for m in re.finditer('"time":', what_analyze)]
        for xtm in self.time_index:
            real_time.append(datetime.datetime.fromtimestamp(int(what_analyze[xtm+7:xtm+17])).strftime("%Y-%m-%d %H-%M-%S"))

        self.price_index = [m.start() for m in re.finditer('"close":', what_analyze)]
        self.price_end = [m.start() for m in re.finditer(',"high":', what_analyze)]
        for xpr in self.price_index:
            real_price.append(what_analyze[xpr+8:self.price_end[i]])
            i += 1
        
        return real_price, real_time
        
            


class DrawGraph():

    def __init__(self):
        pass

    def do_the_drawing(self, use_data):
        """
        Drawing a graph, based on sended data. 'x' represents Time line, 'y' represents Price line

        :use_data: param: List of two items Price and Time
        
        """
        price = go.Scatter(
        x=use_data[1],
        y=use_data[0]
        )
##        trace1 = go.Scatter(
##        x=[1, 2, 3, 4],
##        y=[16, 5, 11, 9]
##        )
        data = [price,] #trace1]

        py.plot(data, filename = 'basic-line', auto_open=True)


        #return fig

the_data = GetData()
dump_of_data = the_data.get_real_time()
clean_data = the_data.analyze_answer(dump_of_data)

the_graph = DrawGraph()
plot_url = py.plot(the_graph.do_the_drawing(clean_data))
#print (plot_url)


