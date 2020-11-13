# import xmind2testlink
from xmind2testlink.xmind_parser import *
from xmind2testlink.testlink_parser import *
inputXmindPath='/Users/zhongcheng/Documents/TestCase/xmind/'
outputXmlPath='/Users/zhongcheng/Documents/TestCase/xml/'
CaseName='司机版242.xmind'
xmlName='司机版242.xml'
f=xmind_to_suite (inputXmindPath+CaseName)
to_testlink_xml_file(f,outputXmlPath+xmlName)



# output json is also supported
# xmind2testlink / path / to /testcase.xmind - json
# Generated: testcase.json