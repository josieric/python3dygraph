
import pkg_resources
jspath = pkg_resources.resource_filename(__name__, "dygraph.1.0.1.js")
f = open(jspath, "r")
jscode = "<script type=\"text/javascript\">"+f.read()+"</script>"
f.close()
jspath = pkg_resources.resource_filename(__name__, "dygraph.addon.js")
f = open(jspath, "r")
jscode += "<script type=\"text/javascript\">"+f.read()+"</script>"
f.close()

def get_jspath():
  return(jspath)

## renvoi un div et script dygraph autonome
## P1 => DataFrame indexed by Date (Cf test.py)
def dygraph(df, df_opts, divname = "graphdiv", includejs = True):
  dygraph="<div id=\"" +divname+ "\" style=\"margin: 0 auto; width:auto;\"></div>"
  if (includejs):
    dygraph += jscode
  dygraph += "<script type=\"text/javascript\">var  "+divname+" = new Dygraph(document.getElementById('" +divname+ "'),\"" + df.index.name
  for h in df.keys().values:
    dygraph += "\t" + h
  dygraph += "\\n"
  dygraph += df.to_csv(index=True,line_terminator="\\n",sep="\t",header=False) +"\""+ "," + str(df_opts) + ");\n"
  dygraph += "</script>"
  return dygraph

def dygraphSS(df, df_opts, divname = "graphdiv", includejs = True):
  dygraph="<div id=\"" +divname+ "\" style=\"margin: 0 auto; width:auto;\"></div><div id=\"" +divname+ "_sel\" align=\"center\"></div>"
  if (includejs):
    dygraph += jscode
  dygraph += "<script type=\"text/javascript\">var  "+divname+" = new Dygraph(document.getElementById('" +divname+ "'),\"" + df.index.name
  for h in df.keys().values:
    dygraph += "\t" + h
  dygraph += "\\n"
  dygraph += df.to_csv(index=True,line_terminator="\\n",sep="\t",header=False) +"\""+ "," + str(df_opts) + ");\n"
  dygraph += "graph_selector('" +divname+ "_sel','" +divname+ "',"+divname+");</script>"
  return dygraph

def to_html_file(filename, df, df_opts, divname = "graphdiv", includejs = True):
  f = open(filename, "a")
  f.write(  dygraph(df, df_opts, divname, includejs) )
  f.close()

