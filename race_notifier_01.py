'''
http://stackoverflow.com/questions/9697901/python-saving-xml-from-webservice
http://stackoverflow.com/questions/2792650/python3-error-import-error-no-module-name-urllib
http://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python

'''

from urllib.request import urlopen
import datetime as DT
from datetime import datetime
from datetime import timedelta
import xml.etree.ElementTree as ET



def is_xml_today(race_number):
	'''check an xml file to confirm it is for the correct date'''
	tree = ET.parse("VR%s.xml" % (str(race_number)))
	root = tree.getroot()
	xml_racetime = root.findall("./Meeting/Race")[0].attrib["RaceTime"]
	xml_racetime_dto = datetime.strptime(xml_racetime, '%Y-%m-%dT%H:%M:%S')
	datetime_now = DT.datetime.now()
	if xml_racetime_dto.date() == datetime_now.date():
		return(True)
	else:
		return(False)

def get_xml(race_number):
	today_year = DT.datetime.now().year
	today_month = DT.datetime.now().month
	today_day = DT.datetime.now().day
	url = "https://tatts.com/pagedata/racing/%s/%s/%s/VR%s.xml" % (today_year,today_month,today_day,str(race_number))
	s = urlopen(url)
	contents = s.read()
	file = open("VR%s.xml" % (str(race_number)), 'wb')
	file.write(contents)
	file.close()


def how_long_till_race(race_number):
	tree = ET.parse("VR%s.xml" % (str(race_number)))
	root = tree.getroot()
	xml_racetime = root.findall("./Meeting/Race")[0].attrib["RaceTime"]
	xml_racetime_dto = datetime.strptime(xml_racetime, '%Y-%m-%dT%H:%M:%S')
	datetime_now = DT.datetime.now()
	delta = xml_racetime_dto - DT.datetime.now()
	return(delta.total_seconds()/60)

def notify(race_number):

https://www.google.com/settings/security/lesssecureapps


for i in [4,5,6]:
	if DT.datetime.now().weekday() >= 2 and DT.datetime.now().weekday() <= 6:
		if is_xml_today(i) == False:
			print("Getting updated XML...")
			get_xml(i)
		if how_long_till_race(i) < 10 and how_long_till_race(i) > 0:
			notify(i)



DT.datetime.now().weekday()


delta = xml_racetime_dto - DT.datetime.now()
mintes_till_race = delta.total_seconds()/60

date_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

DT.datetime.now()

xml_racetime_dto
DT.datetime.now()
xml_racetime_dto - DT.datetime.now()

delta.total_seconds()/60

root.tag
root.attrib
root[0][1].text

root[0][0][4].tag

root.findall("./Meeting/Race")[0].tag
root.findall("./Meeting/Race")[0].attrib
root.findall("./Meeting/Race")[0].attrib
root.findall("./Meeting/Race")[0].attrib.Element("RaceTime")
root.findall("./Meeting/Race")[0].attrib["RaceTime"]

