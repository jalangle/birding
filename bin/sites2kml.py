#!python3

from datetime import date
import frontmatter
import os
from pathlib import Path
import simplekml

sites = simplekml.Kml(name="Washington Birding Site Impressions, " + date.today().strftime("%Y/%m/%d"))

p = Path('_sites')
for d in p.iterdir():
	with open(d) as f:
		site = frontmatter.load(f)
		coordinates = site['Coordinates'].split(',')
		sites.newpoint(name=site['Title'], coords=[coordinates])

sites.save("sites.kml")