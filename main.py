## Python 2

import scraperwiki
import urllib2
from lxml import etree

# Opens the URL for the .PDF
u = urllib2.urlopen("http://images.derstandard.at/2013/08/12/VN2p_2012.pdf")
# Interperate it as XML
x = scraperwiki.pdftoxml(u.read())
#print x[:1024]

r = etree.fromstring(x)
print r
#r.xpath('//page[@number="1"]')