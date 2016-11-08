#! /usr/bin/env pythons
import sys
from urllib.request import urlopen
import re

def getErrorLog(url):
    """
    Get's the error log from the url that is entered
    Args:
        url: url for the error log
    Returns:
        List of errors
    """
    errorLog = dict()
    message = urlopen(url)
    log = message.read().decode()
    splitLog = log.splitlines()
    for line in splitLog:
        try:
            splitLine = line.split(']')
            if splitLine[1] == ' [error':
                line = splitLine[3]
                #print(line)
                file = re.findall('/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
                #file = re.match(r"(/.)+?(\.[a-z]+)",line)
                #print(file.group(0))
                try:
                    if(file[0] in errorLog):
                        errorLog[file[0]] += 1
                    else:
                        errorLog[file[0]] = 1
                except:
                    pass
        except:
            pass

    errors = sorted(errorLog, key=errorLog.get, reverse=True)
    occures = sorted(errorLog.values(), reverse=True)
    i = 0
    print("*** Top 25 page errors ***")
    while i < 25:
        print("Count: ", occures[i], "  Page: ", errors[i])
        i += 1
    #print(errorLog)

def main():
    """
    Test Function
    """
    getErrorLog('http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.full')
    return

if __name__=="__main__":
    main()
    exit(0)
