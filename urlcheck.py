import getopt
import sys
import urllib.request

## checks if url is working and returns response status code
def check_url(url,time):
   try:
      if(urllib.request.urlopen(url,timeout=time)):
         status=urllib.request.urlopen(url).getcode()
         return status
   except:
      print("Error: "+url)

## function to open input url list
def open_file(file_name):
   with open(file_name) as f:
      return list(f)

## function to write output to file
def write_file(text):
   with open('output.txt',"a") as myfile:
      myfile.write(text+"\n")

## main function
def main(argv):

   # variable declaration
   url = None
   urlList = None
   output = False
   protocol = None
   fullCheck = False
   time = 10  # set default timeout to 10

   # get variable values from terminal
   try:
      opts, args = getopt.getopt(argv,"hu:l:op:f",["url=","urllist=","output","protocol=","fullcheck"])
   except getopt.GetoptError:
      print("python urlcheck.py -u <url> -p http -o")
      sys.exit(2)
   
   for opt,arg in opts:
      if opt in ('-h','--help'):
         print("python urlcheck.py -u <url> -p http -o")
         sys.exit()
      elif opt in ('-u','--url'):
         url = arg
      elif opt in ('-l','--urllist'):
         urlList = arg
      elif opt in ('-o','--output'):
         output = True
      elif opt in ('-p','--protocol'):
         protocol = arg
      elif opt in ('-f','--fullcheck'):
         fullCheck = True
   
   # if user has not entered any url prompt error message
   if(url == None and urlList == None):
      print("Error: You have to enter either url or a list of urls")
      print("python urlcheck.py -u <url> -p http -o")
      sys.exit()
   
   if(url != None):
      # if user opted for a full-check, scan urls with all protocols
      if(fullCheck):
         protocols = ['https','http','ftp']
         
         for protocol in protocols:
            status = check_url(str(protocol)+"://"+str(url),time)

            if status is not None:
               print('Success: ',str(protocol)+"://"+str(url))
               if output:
                  write_file(str(protocol)+"://"+str(url))

      else:
         # if user has not opted for full-check and has not mentioned any protocol, set default protocol to https
         if(protocol == None):
            protocol = 'https'
         url = str(protocol)+"://"+str(url)
         url = url.strip()
         status = check_url(url,time)

         if status is not None:
            print('Success: ',url)
            if output:
               write_file(url)

   else:
      for url in open_file(urlList):
         # if user opted for a-full check, scan urls with all protocols
         if(fullCheck):
            protocols = ['https','http','ftp']
            
            for protocol in protocols:
               status = check_url(str(protocol)+"://"+str(url),time)

               if status is not None:
                  print('Success: ',str(protocol)+"://"+str(url))
                  if output:
                     write_file(str(protocol)+"://"+str(url))

         else:
            # if user has not opted for full-check and has not mentioned any protocol, set default protocol to https
            if(protocol == None):
               protocol = 'https'
            url = str(protocol)+"://"+str(url)
            print(url)
            url = url.strip()
            status = check_url(url,time)

            if status is not None:
               print('Success: ',url)
               if output:
                  write_file(url)


if __name__ == "__main__":
   main(sys.argv[1:])
