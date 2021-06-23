import urllib.request

## function open file

def open_file(file_name):
    with open(file_name) as f:
        mylist = list(f)
        return mylist


## function to append to file

def write_file(text):
    with open('output.txt', "a") as myfile:
        myfile.write(text+"\n")


## function to check url and return status

def check_url(url):
    try:
        if(urllib.request.urlopen(url, timeout=10)):
            status = urllib.request.urlopen(url).getcode()
            return status
    except:
        # catch the exception if the url returns an error
        print('Error: '+url)


## path of input file
input = '/home/thehackermonk/Bug Bounty/bitdefender/domains.txt'

for url in open_file(input):
    # strip the url for unwanted characters
    url = url.strip()

    # complete the url by adding protocol to it, if needed
    if not url.startswith('https://') or not url.startswith('http://'):

        status = check_url('https://'+url)
        if status is not None:
            write_file('https://'+url)
            print('Success: '+'https://'+url)

        status = check_url('http://'+url)
        if status is not None:
            write_file('http://'+url)
            print('Success: '+'http://'+url)
    else:
        status = check_url(url)
        if status is not None:
            write_file(url)
            print('Success: '+url)
