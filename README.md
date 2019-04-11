# python3dygraph

* install
git clone https://github.com/josieric/python3dygraph.git  
cd python3dygraph/dygraph  
python setup.py sdist  
pip install sdist/dygraph-0.1.tar.gz  

* For Use in python 3 must have a DataFrame indexed by date column in character  
import pandas as pd  
datas = [{'Date':'2019-01-01 00:00', 'c2':100, 'c3':100}, {'Date':'2019-01-02 00:00','c2':110, 'c3':124},{'Date':'2019-01-02 12:00','c2':90, 'c3':105}, {'Date':'2019-01-03 00:00','c2':120, 'c3':90}]  
df = pd.DataFrame(datas).set_index('Date')  

* Graph Option (See dygraph.com for details)  
graph_opts = {'legend': 'always','title': 'SI conso', 'ylabel': 'Puissance','showRangeSelector': 'true','connectSeparatedPoints': 'true' }  

* import module in python & use it  
from dygraph import *  
print(dygraph(df,graph_opts))  

* others Examples :  
import dygraph as dg  
print(dg.dygraph(df,graph_opts))  
* With no graph option and not re-send all javascript (=in the same page)   
print(dg.dygraph(df,{}, divname='NewGraph', includejs=False))  
* With Serie Selector !!  
print(dg.dygraphSS(df,graph_opts,'mondiv',False))  

* simple export to a html autonomous file  
dg.to_html_file("t.html",df,{}, divname='NewGraph')  

* use with ipyton  
import Ipython  
display(HTML(dg.dygraph(df,graph_opts)))  

