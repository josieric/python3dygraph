
function graph_line(divid,title,filename) {
    var g = new Dygraph(
  	document.getElementById(divid),
           filename,
           { connectSeparatedPoints: true,
             title: title,
             legend: 'always',
             showRangeSelector: true
           });
    return g;
}

function graph_selector(sdivid,gdivid,g) {
    var labs = g.getLabels();
    var selector = document.getElementById(sdivid);
    if (selector != null) {
      myform = "<form>";
      for(var id= 1; id < labs.length; id++) {
        myform += "<input type=\"checkbox\" id=\""+(id-1)+"\" checked onClick=\"change(this,"+gdivid+")\" />"+labs[id]+"&nbsp;&nbsp;";
      };
      myform += "</form>";
      selector.innerHTML = myform;
      //alert(labs);
    }
}
function change(el,g) {
  g.setVisibility(parseInt(el.id), el.checked);
}
