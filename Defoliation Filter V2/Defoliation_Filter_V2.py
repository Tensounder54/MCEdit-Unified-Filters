# Feel free to modify and use this filter however you wish. If you do,
# please give credit to T54.

#All commented out code is redundent. Please ignore it.

#Imports PyMCLevel Library
from pymclevel import materials
import numpy as np
import time

#BlockIDs = [

#Sets the display name for the filter.
displayName = "Defoliation Filter V2"

#Sets the inputs for the filter.
inputs = [
		(("Exclude:", ("Nothing","Leaves","Wood")),
		#("Exclude Saplings?", True),
		("Perform", "title")), 
		
		(("Filter By T54", "label"),
		("Filter Info can be found here: ", "label"),
		(" ", ("string","value=https://goo.gl/mmcqb3")), #Insert link to filter info here
		("Info on me and usage of my filters", "label"),
		("as well as info on bug reporting ", "label"),
		("can be found here: ", "label"), 
		(" ", ("string","value=https://goo.gl/qwUiAE")),
		("Notes","title")), #Insert link to my info here
	]

#Defines the start of the algorithm
def perform(level, box, options):

	# Prints a message to the MCEdit console saying when the filter started.
	method = "Defoliate"
	print '%s: Started at %s' % (method, time.ctime())

    #Assigns the input options to variables
	exclude = options["Exclude:"]
	
	#Assigns other variables
	
	# Iterates through the selection box.
	for (chunk, slices, _) in level.getChunkSlices(box):
		# Indexes blocks and Data using slices.
		blocks = chunk.Blocks[slices]
		data = chunk.Data[slices]
		#checks to see if user wants to exclude leaves.
		if exclude == "Leaves":
			#*Sets all instances of logs to air.
			data[np.logical_or(blocks == 17,blocks == 162)] = 0
			blocks[np.logical_or(blocks == 17,blocks == 162)] = 0
		#checks to see if user wants to exclude logs.
		elif exclude == "Wood":
			#**Sets all instances of oak, spruce, birch, jungle, acacia and dark oak leaves to air.
			data[np.logical_or(blocks == 18,blocks == 161)] = 0
			blocks[np.logical_or(blocks == 18,blocks == 161)] = 0
		#Default
		else:
			#*)  
			data[np.logical_or(blocks == 17,blocks == 162)] = 0
			blocks[np.logical_or(blocks == 17,blocks == 162)] = 0
			#**
			data[np.logical_or(blocks == 18,blocks == 161)] = 0
			blocks[np.logical_or(blocks == 18,blocks == 161)] = 0
		# Notify the world that the chunk changed.
		chunk.chunkChanged()
		
	# Prints a message to the MCEdit console saying when the filter ended.
	print '%s: Ended at %s' % (method, time.ctime())
	
#END
