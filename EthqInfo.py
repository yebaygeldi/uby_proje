from TurkeyMap import TurkeyMap
from urllib.request import urlopen
import json

class EthqInfo:
	def infoethq(start_date, end_date):
		ethq_province = str()
		
#		start_date = input("Başlangıç tarihini (yyyy-mm-dd) formatında giriniz: ")
#		end_date = input("Bitiş tarihini (yyyy-mm-dd) formatında giriniz: ")
		
		url = f"https://deprem.afad.gov.tr/apiv2/event/filter?start={start_date}%2010:00:00&end={end_date}%2011:00:00&filter?magtype=mb&minmag=4"
		
		response = urlopen(url)
		
		data_json = json.loads(response.read())
		
		# print(data_json)
		
		last_earthquake = data_json[-1]
		
		print(last_earthquake)
		
		if last_earthquake.get('province') == None:
			ethq_province = last_earthquake.get('location')
		else:
			ethq_province = last_earthquake.get('province')
		
		ethq_magnitude = last_earthquake.get('magnitude')
		ethq_time = last_earthquake.get('date')
		ethq_lat = float(last_earthquake.get('latitude'))
		ethq_lon = float(last_earthquake.get('longitude'))
		
		print(ethq_time + ethq_magnitude + ethq_province + str(ethq_lat) + str(ethq_lon))
		
		mapop = TurkeyMap
		mapop.mapopen(ethq_lat, ethq_lon, ethq_province)
	




