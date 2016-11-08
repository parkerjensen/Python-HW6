#! /usr/bin/env pythons
import sys
from urllib.request import urlopen

def getErrorLog(url):
    """
    Get's the error log from the url that is entered
    Args:
        url: url for the error log
    Returns:
        List of errors
    """
    message = urlopen(url)
    log = message.read().decode()
    splitLog = log.splitlines()
    for line in splitLog:
        splitLine = line.split(']')
        if splitLine[1] == ' [error':
            print(splitLine[3])

        
    #splitLog = splitLog.split('[')
    #splitLog = splitLog.split(']')
    #print(splitLog)
    #print(log)



def main():
    """
    Test Function
    """
    getErrorLog('http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test')
    return

if __name__=="__main__":
    main()
    exit(0)
