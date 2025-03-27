#!/usr/bin/env python
# coding=utf-8

import inkex
from inkex import Rectangle

# General fills
color_ocean = '#396B70'
color_deep = '#325B68'
color_impass = '#0A3542'
color_text = '#FFFFFF'
color_base = '#B7AB80'

# Region and Unit fill colors to find and replace - note that Russia and Guarani have no recolor
ru_fills = {
	'#C6B7AB': color_base,  # Base
	'#3C9553': '#23763F',   # Portugal
	'#F0CE48': '#DBB045',   # Spain
	'#FC9C23': '#DB7745',   # Netherlands
	'#F94455': '#E33544',   # England
	'#66A2E3': '#24A57B',   # France
	'#A03838': '#AB2136',   # Ottoman
	'#E390B3': '#E57BA8',   # Poland-Lithuania
	'#AFC5D8': '#95ADC2',   # Inuit
	'#CADD7E': '#B8DC5C',   # Ming
	'#AB9F26': '#999941',   # Mughal
	'#F36678': '#E04A5D',   # Qing
	'#5A887F': '#407167',   # Safavid
	'#CA7A59': '#B87052',   # Ute-Shoshone
	'#A88080': '#9D6767',   # Abyssinia
	'#587BA7': '#4A688D',   # Ajuuraan
	'#E95A94': '#BB4C79',   # Athapasca
	'#A17555': '#82644D',   # Austria
	'#9A2F56': '#AD295D',   # Aymara
	'#9D84AE': '#B875CE',   # Ayutthaya
	'#924CB3': '#944FA5',   # Kongo
	'#81889D': '#696E7F',   # Mapuche-Tehuelche
	'#4E51BA': '#534884',   # Sweden
	'#7CDBC3': '#4AB79B'    # Tokugawa
}

# High Sea and Tree fills
deep_fills = {
	'Indian Ocean': 'path53785',
	'North Atlantic': 'path56148',
	'South Atlantic A': 'path56264',
	'South Atlantic B': 'path3305',
	'South Atlantic C': 'path3466',
	'North Pacific L': 'path3468',
	'North Pacific R': 'path3473',
	'South Pacific LA': 'path3469',
	'South Pacific LB': 'path500799',
	'South Pacific R': 'path3472',
	'Siberian Tundra': 'path466'
}

# Impassable fills
impass_fills = {
	'Sierra Nevada A': 'path813',
	'Sierra Nevada B': 'path812',
	'Greenland': 'path1-9',
	'Sahara A': 'path1511',
	'Sahara B': 'path1483',
	'Himalayas': 'path309495'
}

# Strings which flag a region for needing a text recolor
text_fills = [
	"Sea",
	"Bay ",
	" Bay",
	"Ocean",
	"Gulf",
	"Shore",
	"Coast",
	"Basin",
	"Strait",
	"Channel",
	"Passage",
	"Trough",
	"Plateau",
	"Rise",
	"Ridge",
	"Current",
	"Banks",
	"Islands",
	"Estuary",
	"1",
	"2",
	"3",
	"4",
	"5",
	"Bangka",
	"Reunion",
	"Aleuts",
	"Hawai'i",
	"Galapagos",
	"Lawrence",
	"Meules",
	"Baie",
	"Bermuda",
	"Bahamas",
	"Juventud",
	"Jamaica",
	"Windward",
	"Rico",
	"Antigua",
	"Guadeloupe",
	"Barbados",
	"New Courland",
	"Plata",
	"Chiloe",
	"Golfo",
	"Islas",
	"Hoces",
	"Helena",
	"Tome",
	"Fernando",
	"Cabo",
	"Jacob",
	"Gambia",
	"Canaries",
	"Azores",
	"Southern",
	"Bight",
	"Skagerrak",
	"Copen.",
	"Sound",
	"Qeshm",
	"Socotra",
	"Zanzibar",
	"Fort-Dauphin",
	"Maldives",
	"Aotearoa",
	"Tenggara",
	"Flores",
	"Timor",
	"Mindoro",
	"Palawan",
	"Cebu",
	"Hainan",
	"Okinawa",
	"Amami",
	"Kyushu",
	"Tsushima",
	"Enticosty",
	"Zamboanga",
	"Haitien",
	"Domingo",
	"Baleares",
	"Corse",
	"Otranto",
	"Adriatic",
	"Bahia",
	"Lucia",
	"Maarten",
	"Madeira",
	"Tundra"
]

class DarkMode (inkex.EffectExtension):
	
	def effect (self):
		
		# Loop over all groups
		groups = self.document.xpath('//svg:g', namespaces={'svg': inkex.NSS['svg']})
		for group in groups:
			
			# Grab the Other Fills group
			if group.get('id') == "layer14":
				
				# Recolor all text in the Other Fills group
				for text in group:
					text.style.set_color(color_text, 'fill')
				
				# Recolor the paths defined in deep_fills and impass_fills for layers in the Other Fills group
				for path in group:
					if path.get('id') in deep_fills.values():
						path.style.set_color(color_deep, 'fill')
						
					if path.get('id') in impass_fills.values():
						path.style.set_color(color_impass, 'fill')
				
				# Do the same for subgroups of the Other Fills group
				for child in group.getchildren():
					for path in child:
						if path.get('id') in deep_fills.values():
							path.style.set_color(color_deep, 'fill')
		
			# Grab the Sidebar group
			if group.get('id') == "layer7":
				for path in group:
					
					# Hide map edge
					if path.get('id') == "rect14569":
						path.style.set_color(color_base, 'fill')
					
					# Recolor Sidebar background
					if path.get('id') == "rect37478":
						path.style.set_color(color_base, 'fill')
			
			# Grab the Titles group
			if group.get('id') == "layer1":
				
				# Recolor the texts defined in text_fills for layers in the Titles group
				for text in group:
					if any(substring in text.get_text() for substring in text_fills):
						text.style.set_color(color_text, 'fill')
			
			# Grab the Background group
			if group.get('id') == "g407997":
				
				# Style a dark rectangle
				rect_style = {'stroke': '#000000', 'stroke-width': 0, 'fill': color_ocean}
				rect_attribs = {'style': str(inkex.Style(rect_style)),
						inkex.addNS('label', 'inkscape'): "rect1",
						'left': '0', 'top': '0',
						'width': '4464', 'height': '2200'}
				
				# Draw a rectangle
				darkrect_layer = inkex.etree.SubElement(group, 'g', {
					inkex.addNS('label', 'inkscape'): 'Dark Rectangle'
				})
				darkrect_layer.add(Rectangle (**rect_attribs))
			
			# Grab the Region Colors group or the Unit Output group or the Island Fills group
			if group.get('id') == "layer6" or group.get('id') == "layer16" or group.get('id') == "layer11":
				for path in group:
					
					# Recolor the path matching keys of the ru_fills dictionary
					path_color = str(path.style.get_color().to_rgb()).upper()
					if path_color in ru_fills:
						path.style.set_color(ru_fills.get(path_color), 'fill')
					
				# Do the same for children of this group
				for child in group.getchildren():
					for path in child:
						path_color = str(path.style.get_color().to_rgb()).upper()
						if path_color in ru_fills:
							path.style.set_color(ru_fills.get(path_color), 'fill')
						
			# Grab the SC Markers group
			if group.get('id') == "layer3":
				for child in group.getchildren():
					for path in child:
						
						# Recolor the path matching keys of the ru_fills dictionary
						path_color = str(path.style.get("fill")).upper()
						if path_color != "NONE":
							if path_color in ru_fills:
								path.style.set_color(ru_fills.get(path_color), 'fill')

if __name__ == '__main__':
	DarkMode ().run ()