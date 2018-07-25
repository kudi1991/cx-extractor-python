# -*- coding: utf8 -*-

from CxExtractor import CxExtractor
cx = CxExtractor(threshold=186)
html = cx.getHtml("https://www.dianping.com/home-tuku/k3?utm_source=pc_shouye_smalltuku5")
content = cx.filter_tags(html)
s = cx.getText(content)
print(s)
