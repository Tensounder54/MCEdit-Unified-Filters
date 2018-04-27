#imports key librarys
import time
from pymclevel import *

#sets the name of the filter as it will appear in mcedit
displayName = "Make Honey Pots Filter V1"

#sets the imputs for the filter
inputs = [
		(("Filter By T54", "label"),
		("Filter Info can be found here: ", "label"),
		(" ", ("string","value=https://goo.gl/5hKdWB")), #Insert link to filter info here
		("Info on me and usage of my filters", "label"),
		("as well as info on bug reporting ", "label"),
		("can be found here: ", "label"), 
		(" ", ("string","value=https://goo.gl/qwUiAE")),
		("Perform", "title")),
	]

#function sets the given block and data at the given coordinates marked by x, y and z
def setBlockForced(level, (block, data), x, y, z):
	level.setBlockAt(int(x), int(y), int(z), block)
	level.setBlockDataAt(int(x), int(y), int(z), data)
	
#Defines the start of the algorithm
def perform(level, box, options):
	
	# Prints a message to the MCEdit console saying when the filter started.
	print '%s: Started at %s' % (displayName, time.ctime())
	
	# Iterates through the selection box.
	for (chunk, slices, _) in level.getChunkSlices(box):
		# Indexes blocks using slices.
		blocks = chunk.Blocks[slices]
		#Itterates through the list of blocks
		for i in range(1,256):
			#replces the existing block with air
			blocks[blocks == i] = 0
	
	#sets variable y equal to the lowest value of y in the selection box
	y = box.miny
	#defines grass withing minecraft
	grass = (2, 0)
	#itterates throught the x and z of the selection box
	for x in xrange(box.minx, box.maxx):
		for z in xrange(box.minz, box.maxz):
			# calls the 'setBlockForced(level, (block, data), x, y, z)' 
			# function with identical parameters except for (block, data)
			# where the values are passed in as part of the tupal grass
			setBlockForced(level, grass, x, y, z)
	
	# Prints a message to the MCEdit console saying when the filter ended.
	print '%s: Ended at %s' % (displayName, time.ctime())
	
#END