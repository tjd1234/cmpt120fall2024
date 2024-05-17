# read_web_page.py

import urllib.request

def get_web_page_text(url):
    """ Retrieve the contents of a web page.
    """
    socket = urllib.request.urlopen(url)
    return socket.read()

page = get_web_page_text('https://www.sfu.ca/')
print(page)
