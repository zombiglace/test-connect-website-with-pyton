import urllib.request

link = 'you-link-website'

def connect():
    try:
        urllib.request.urlopen(link)
        return True
    except:
        return False
if connect ():
    print ("Connected")
else:
    print ("Failed to connect")
