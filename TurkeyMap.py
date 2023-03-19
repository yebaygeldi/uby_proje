import folium
from AutomaticView import AutomaticView


class TurkeyMap:
	def mapopen(lat, lon, ethq_province):
		auto_view = AutomaticView
		auto_view.view(ethq_province)
		myMap = folium.Map(location=[lat, lon], zoom_start=10)
		folium.CircleMarker(location=(lat, lon), radius=100, fill_color='red').add_to(myMap)
		folium.Marker(location=[lat, lon], popup=ethq_province).add_to(myMap)
		myMap.show_in_browser()
		
