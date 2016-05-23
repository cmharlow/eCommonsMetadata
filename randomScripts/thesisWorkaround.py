import csv
import requests
import xml.dom.pulldom
import sys
import re
from codecs import open


def grabFeed(filename):
    hdls = []
    with open(filename, 'rb') as fh:
        reader = csv.reader(fh)
        for row in reader:
            hdls.append(row[0])
    return(hdls)


def changeID(hdl):
    oaiID = hdl.replace('http://hdl.handle.net/', 'oai:ecommons.cornell.edu:')
    return(oaiID)


def cleanXML(respText):
    RE_XML_ILLEGAL = u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' + \
                     u'|' + \
                     u'([%s-%s][^%s-%s])|([^%s-%s][%s-%s])|([%s-%s]$)|(^[%s-%s])' % \
                      (unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),
                       unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),
                       unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff))
    dataClean = re.sub(RE_XML_ILLEGAL, "?", respText)
    return(dataClean)


def writeXML(oaiIDs):
    ofile = open('output.xml', 'w', "utf-8")
    ofile.write('<?xml version="1.0" encoding="UTF-8"?><OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd"><ListRecords>\n')
    base = "https://ecommons.cornell.edu/dspace-oai/request?verb=GetRecord&metadataPrefix=dim&identifier="
    recordCount = 0

    for oaiID in oaiIDs:
        resp = requests.get(base + oaiID).content
        #resp_clean = cleanXML(resp)
        events = xml.dom.pulldom.parseString(resp)
        for (event, node) in events:
            if event == 'START_ELEMENT' and node.tagName == 'record':
                events.expandNode(node)
                node.writexml(ofile)
                recordCount += 1

    ofile.write('\n</ListRecords></OAI-PMH>\n'), ofile.close()
    print(recordCount)


filename = sys.argv[1:]
handles = grabFeed(filename[0])
oaiIDs = []
for handle in handles:
    oaiIDs.append(changeID(handle))
writeXML(oaiIDs)
