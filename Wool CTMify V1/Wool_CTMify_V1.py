from pymclevel import *
import time as t
import numpy as np

displayName = "Wool CTMify V1"

inputs = [
		(("Concrete", ("Normal", "Powder")),
		("Output Log?", False),
		("(Enabling \'Output Log?\' will slow down the filter and write a lot of text to the console.)", "label"),
		("Perform", "title")),

		(("Filter By T54", "label"),
		("Filter Info can be found here: ", "label"),
		(" ", ("string","value=https://goo.gl/dpqoGQ")), #Insert link to filter info here
		("Info on me and usage of my filters", "label"),
		("as well as info on bug reporting ", "label"),
		("can be found here: ", "label"), 
		(" ", ("string","value=https://goo.gl/qwUiAE")),
		("Notes","title"))
		]

def getBlockFromOptions(options, block):
	return (options[block].ID, options[block].blockData)
	
def getBlock(level,x,y,z):
	return (level.blockAt(int(x),int(y),int(z)), level.blockDataAt(int(x),int(y),int(z)))

def setBlock(level, (block, data), x, y, z):
	if getBlock(level, x,y,z) == AIR:
		level.setBlockAt(int(x), int(y), int(z), block)
		level.setBlockDataAt(int(x), int(y), int(z), data)

def setBlockForced(level, (block, data), x, y, z):
	level.setBlockAt(int(x), int(y), int(z), block)
	level.setBlockDataAt(int(x), int(y), int(z), data)
	
def replaceBlock(level, material, rMaterial, x, y, z):
	if getBlock(level,x,y,z) == rMaterial:
		setBlockForced(level, material, x, y, z)

def perform(level, box, options):
	
	wool = ((35,0),(35,1),(35,2),(35,3),(35,4),(35,5),(35,6),(35,7),(35,8),(35,9),(35,10),(35,11),(35,12),(35,13),(35,14),(35,15))
	
	concrete = ((251,0),(251,1),(251,2),(251,3),(251,4),(251,5),(251,6),(251,7),(251,8),(251,9),(251,10),(251,11),(251,12),(251,13),(251,14),(251,15))
	
	powder = ((252,0),(252,1),(252,2),(252,3),(252,4),(252,5),(252,6),(252,7),(252,8),(252,9),(252,10),(252,11),(252,12),(252,13),(252,14),(252,15))
	
	type = options["Concrete"]
	log = options["Output Log?"]
	
	for x in xrange(box.minx, box.maxx):
		for y in xrange(box.miny, box.maxy):
			for z in xrange(box.minz, box.maxz):
				for i in range(0,16):
					if type == "Normal":
						replaceBlock(level, concrete[i], wool[i], x, y, z)
					elif type == "Powder":
						replaceBlock(level, powder[i], wool[i], x, y, z)
					if log:
						print (type, " replaced at: ", x, y, z)
