#!python3

import frontmatter
import os
from pathlib import Path
import simplekml

sites = simplekml.Kml()

p = Path('_sites')
for d in p.iterdir():
	with open(d) as f:
		site = frontmatter.load(f)
		coordinates = site['Coordinates'].split(',')
		sites.newpoint(name=site['Name'], coords=[coordinates])

sites.save("sites.kml")