import urllib.request

with open('path_url_url_list_as_txt_file') as f:
    mylist=list(f)

for url in mylist:

    # strip the url for unwanted characters
    url=url.strip()

    # complete the url by adding protocol to it, if needed
    if(url.startswith('https://')):
        url=url
    elif(url.startswith('www')):
        url='https://'+url
    else:
        url='https://www.'+url

    try:
        # check for the url
        if(urllib.request.urlopen(url)):
            status=urllib.request.urlopen(url).getcode()
            print(status,url)
    except:
        # catch the exception if the url returns an error
        print('Error: '+url)