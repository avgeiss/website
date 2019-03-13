#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 01:35:07 2019

@author: andrew
"""

#propagates changes made to the header of the index.html page accross all pages in the site.
#looks for <div class="content"></div> tag and retains only info within this tag for pages that
#aren't index.html. If there is no such tag no changes are made.

from glob import glob
from BeautifulSoup import BeautifulSoup


#get the html for the index page:
f = open('./index.html')
template = BeautifulSoup(f.read())
content_template = template.find(name="div",attrs={"class" : "content"})
f.close()

files = glob('./*.html')
for i in range(len(files)):
    #get html for page to update
    f = open(files[i],"r")
    page = BeautifulSoup(f.read())
    f.close()
    #isolate the content section of the page and change it
    content_section = page.find(name="div",attrs={"class" : "content"})
    if content_section:
        content_template.contents = content_section.contents
        #save the new html
        f = open(files[i],"w")
        f.write(str(template))
        f.close()