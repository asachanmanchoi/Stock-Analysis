from bs4 import BeautifulSoup
import operator
import urllib.request
import os
import sys

folderPath = ''


def tryConnect(link):
    networkOK = False
    while networkOK == False:
        try:
            content = urllib.request.urlopen(link, timeout=10)
            networkOK = True
            return content
        except urllib.error.URLError:
            time.sleep(1)
        except socket.timeout:
            time.sleep(1)
            
def validCode(code):
    return (code <= 4000) or ((code >= 8000) and (code < 9000))

def get_stock_list():
    onlineList = []
    coRecords = []
    temp = ''
    listSoup = BeautifulSoup(tryConnect('http://www.hkexnews.hk/listedco/listconews/advancedsearch/stocklist_active_main.htm'), 'html.parser')
    for codeInfo in listSoup.find_all('td'):
        if (codeInfo['align'] == 'Center'):
            temp = codeInfo.get_text() if (validCode(int(codeInfo.get_text()))) else ''
        elif (codeInfo['align'] == 'left' and temp != ''):
            onlineList.append([temp, codeInfo.get_text()])

    onlineList = dict(zip([coRecord[0] for coRecord in onlineList], [coRecord[1] for coRecord in onlineList]))
    sortedList = sorted(onlineList.items(), key=operator.itemgetter(0))
    
    targetList = sorted(set(onlineList))
    
    print(sortedList)
    
if __name__ == "__main__":
    sys.exit(get_stock_list())
