basicHTMLCode = '<meta http-equiv="refresh" content="0; url='
secondPart =  '" />'
print "Make shure to paste the entire URL including HTTPS"
URLName = raw_input("Paste the URL here:")
URL = basicHTMLCode + URLName + secondPart
fileName = raw_input("Name the file:")
URL = basicHTMLCode + URLName + secondPart
webShortcut = open(fileName+".html", "w")
webShortcut.write(URL)
webShortcut.close
print "A web page linking directly to the address you put has been placed in the same directory as this script under the name " + fileName + ".html"
