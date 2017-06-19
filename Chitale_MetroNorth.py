
#Author: Anand Chitale
import webbrowser
import urllib.request
import urllib.parse
import datetime

fName = 'firstwebpage.html'
f = open(fName, 'w', encoding='utf-8') # opens fName for writing and uses utf-8 encoding
def getDateStr():
    cur = datetime.datetime.now()
    date = str(cur.date())
    return date[5:7]  + "-" + date[8:10]+ "-" + date[0:4]
def getTimeStr():
    cur = datetime.datetime.now()
    time = str(cur.time())
    proper = time[0:5]
    curhour = int(proper[0:2])
    if(curhour > 12):
        return((str(curhour - 12) +  ":" + proper[3:6]),"PM")
    elif(curhour == 12):
        return((proper),"PM")
    elif(curhour == 0):
        return ((str(curhour + 12) + ":" + proper[3:6]),"AM")
    else:
        return((proper),"AM")

formValues = {'orig_id' : 71,
              'dest_id' : 1,
              'Filter_id' : 1,
              'traveldate' : getDateStr(),
              'Time_id' : getTimeStr()[0],
              'SelAMPM1' : getTimeStr()[1],
              'cmdschedule' : 'see schedule'}


data = urllib.parse.urlencode(formValues)  # encode out dictionary into a usable format
                                           # for submitting to the web server

data = data.encode('utf-8')
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain", "User-Agent" : user_agent}

url = 'http://as0.mta.info/mnr/schedules/sched_results.cfm?n=y'
req = urllib.request.Request(url, data, headers) # generated a Request object
response = urllib.request.urlopen(req)  # executed the request

resultsPage = response.read().decode('utf-8')
#print(resultsPage)
allLines = resultsPage.split("\n")  # split the string up into multiple elements of a list,
                                    # using \n as the delimiter. The split method returns a list

fName = 'scheduleResults.html'
f = open(fName, 'w', encoding='utf-8') # opens fName for writing and uses utf-8 encoding

# we want to loop through the results page line by line
condition = False
f.write("<HTML>\n")
f.write("<HEAD>\n")
f.write("\t<TITLE> Computer-Generated Webpage </TITLE>\n")
f.write("</HEAD>\n")
f.write("</body>\n")
for line in allLines:
    line = line.strip()
    # here is where you should add your code to process the file
    if(line == '<div id="navyheader"style="font-weight:bold;padding-left:25px;padding-bottom:25px;">'):
        condition = True
    if(line == '<body onLoad="MSG();">'):
        continue
    if(condition == True):
        f.write(line + '\n')
f.write("</HTML>\n")
##f.write(resultsPage)
f.close()

webbrowser.open(fName)

