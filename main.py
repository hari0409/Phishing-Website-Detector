# Required Imports
import re
import urllib

# Basic Data Initialisation
URL="http://197.248.5.23/"
data=[]

# If the URL contains a IP
containsIP=re.match("^(http|https)://\d+\.\d+\.\d+\.\d+\.*", URL)
if containsIP:
    data.append(1)
else:
    data.append(0)

# If the URL is long
urlLength=len(URL)
if urlLength<54:
    data.append(-1)
if urlLength>54 and urlLength<75:
    data.append(0)
if urlLength>=75:
    data.append(1)

# If its a tiny url
resp=urllib.request.urlopen(URL)
print(resp.url)

print(data)
