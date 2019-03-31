#! /usr/bin/env python3

## DataFrame
import pandas as pd
datas = [{'Date':'2019-01-01 00:00', 'c2':100}, {'Date':'2019-01-02 00:00','c2':110},{'Date':'2019-01-02 12:00','c2':90}, {'Date':'2019-01-03 00:00','c2':120}]
df = pd.DataFrame(datas).set_index('Date')

## Graph Option
graph_opts = {'legend': 'always','title': 'SI conso', 'ylabel': 'Puissance','showRangeSelector': 'true','connectSeparatedPoints': 'true' }

#from dygraph import *
#print(dygraph(df,graph_opts))

import dygraph as dg

print(dg.dygraph(df,graph_opts))
print(dg.dygraph(df,graph_opts,'mondiv',False))
print(dg.dygraph(df,{}, divname='NewGraph', includejs=False))

#dg.to_html_file("t.html",df,{}, divname='NewGraph')


# import Ipython
# display(HTML(dg.dygraph(df,graph_opts)))

