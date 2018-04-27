#All commented out code is redundant. Please ignore it.

#Imports PyMCLevel Library
from pymclevel import *
import numpy as np
import time

#Sets the display name for the filter.
displayName = "Parity Filter V3"

#Sets the inputs for the filter.
inputs = [
		(("Mode:", ("X&Y&Z", "X&Y", "X&Z", "Y&Z", "X", "Y", "Z", "Count*")),
		("Parity:", ("Even", "Odd")),
		#("Include X Blocks?", True),
		#("Include Y Blocks?", True),
		#("Include Z Blocks?", True),
		("Material:", alphaMaterials.Air),
		("Replace?", False),
		("VVVVVVVV", alphaMaterials.Air),
		("Output Log?*", False),
		("*See Notes tab for details.", "label"),
		("Perform", "title")), 
		
		(("Filter By T54", "label"),
		("Filter Info can be found here: ", "label"),
		(" ", ("string","value=https://goo.gl/myjGct")), #Insert link to filter info here
		("Info on me and usage of my filters", "label"),
		("as well as info on bug reporting ", "label"),
		("can be found here: ", "label"), 
		(" ", ("string","value=https://goo.gl/qwUiAE")),
		("Enabling \'Output Log?\' will slow down the filter and write a lot of text to the console.", "label"),
		("Count mode works best when the height  of the selection box is odd.", "label"),
		("Notes","title")),
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
	
#Defines the start of the algorithm
def perform(level, box, options):

	mode = options["Mode:"]
	parity = options["Parity:"]
	#incx = options["Include X Blocks?"]
	#incy = options["Include Y Blocks?"]
	#incz = options["Include Z Blocks?"]
	material = getBlockFromOptions(options, "Material:")
	log = options["Output Log?*"]
	replace =options["Replace?"]
	rMaterial = getBlockFromOptions(options, "VVVVVVVV")
	
	count = 1
	
	# Prints a message to the MCEdit console saying when the filter started.
	print '%s: Started at %s' % (displayName, time.ctime())
	if log:
		print("Output format is as follows: X, Y, Z")
	
	if parity == "Even":
		for x in xrange(box.minx, box.maxx):
			for z in xrange(box.minz, box.maxz):
				for y in xrange(box.miny, box.maxy):
					if mode == "X&Y&Z":
						if x % 2 == 0:
							if y % 2 == 0:
								if z % 2 == 0:
									if replace:
										replaceBlock(level, material, rMaterial, x, y, z)
									else:
										setBlockForced(level, material, x, y, z)
									if log:
										print("Even block replaced at: ", x, " ", y, " ", z)
					elif mode == "X&Y":
						if x % 2 == 0:
							if y % 2 == 0:
								if replace:
									replaceBlock(level, material, rMaterial, x, y, z)
								else:
									setBlockForced(level, material, x, y, z)
								if log:
									print("Even block replaced at: ", x, " ", y, " ", z)
					elif mode == "Y&Z":
						if y % 2 == 0:
							if z % 2 == 0:
								if replace:
									replaceBlock(level, material, rMaterial, x, y, z)
								else:
									setBlockForced(level, material, x, y, z)
								if log:
									print("Even block replaced at: ", x, " ", y, " ", z)
					elif mode == "X&Z":
						if x % 2 == 0:
							if z % 2 == 0:
								if replace:
									replaceBlock(level, material, rMaterial, x, y, z)
								else:
									setBlockForced(level, material, x, y, z)
								if log:
									print("Even block replaced at: ", x, " ", y, " ", z)
					elif mode == "X":
						if x % 2 == 0:
							if replace:
								replaceBlock(level, material, rMaterial, x, y, z)
							else:
								setBlockForced(level, material, x, y, z)
							if log:
								print("Even block replaced at: ", x, " ", y, " ", z)
					elif mode == "Y":
						if y % 2 == 0:
							if replace:
								replaceBlock(level, material, rMaterial, x, y, z)
							else:
								setBlockForced(level, material, x, y, z)
							if log:
								print("Even block replaced at: ", x, " ", y, " ", z)
					elif mode == "Z":
						if z % 2 == 0:
							if replace:
								replaceBlock(level, material, rMaterial, x, y, z)
							else:
								setBlockForced(level, material, x, y, z)
							if log:
								print("Even block replaced at: ", x, " ", y, " ", z)
					elif mode == "Count*":
						if count % 2 == 0:
							if replace:
								replaceBlock(level, material, rMaterial, x, y, z)
							else:
								setBlockForced(level, material, x, y, z)
							if log:
								print("Even block replaced at: ", x, " ", y, " ", z)
						count = count + 1
					else:
						if log:
							print("Program error. Deleting block at: ", x, " ", y, " ", z)
						setBlockForced(level, material, x, y, z)

	elif parity == "Odd":
		for x in xrange(box.minx, box.maxx):
			for z in xrange(box.minz, box.maxz):
				for y in xrange(box.miny, box.maxy):
					if mode == "X&Y&Z":
						if x % 2 != 0:
							if y % 2 != 0:
								if z % 2 != 0:
									if replace:
										replaceBlock(level, material, rMaterial, x, y, z)
									else:
										setBlockForced(level, material, x, y, z)
									if log:
										print("Odd block replaced at: ", x, " ", y, " ", z)
					elif mode == "X&Y":
						if x % 2 != 0:
							if y % 2 != 0:
								if replace:
									replaceBlock(level, material, rMaterial, x, y, z)
								else:
									setBlockForced(level, material, x, y, z)
								if log:
									print("Odd block replaced at: ", x, " ", y, " ", z)
					elif mode == "Y&Z":
						if y % 2 != 0:
							if z % 2 != 0:
								if replace:
									replaceBlock(level, material, rMaterial, x, y, z)
								else:
									setBlockForced(level, material, x, y, z)
								if log:
									print("Odd block replaced at: ", x, " ", y, " ", z)
					elif mode == "X&Z":
						if x % 2 != 0:
							if z % 2 != 0:
								if replace:
									replaceBlock(level, material, rMaterial, x, y, z)
								else:
									setBlockForced(level, material, x, y, z)
								if log:
									print("Odd block replaced at: ", x, " ", y, " ", z)
					elif mode == "X":
						if x % 2 != 0:
							if replace:
								replaceBlock(level, material, rMaterial, x, y, z)
							else:
								setBlockForced(level, material, x, y, z)
							if log:
								print("Odd block replaced at: ", x, " ", y, " ", z)
					elif mode == "Y":
						if y % 2 != 0:
							if replace:
								replaceBlock(level, material, rMaterial, x, y, z)
							else:
								setBlockForced(level, material, x, y, z)
							if log:
								print("Odd block replaced at: ", x, " ", y, " ", z)
					elif mode == "Z":
						if z % 2 != 0:
							if replace:
								replaceBlock(level, material, rMaterial, x, y, z)
							else:
								setBlockForced(level, material, x, y, z)
							if log:
								print("Odd block replaced at: ", x, " ", y, " ", z)
					elif mode == "Count*":
						if count % 2 != 0:
							if replace:
								replaceBlock(level, material, rMaterial, x, y, z)
							else:
								setBlockForced(level, material, x, y, z)
							if log:
								print("Odd block replaced at: ", x, " ", y, " ", z)
						count = count + 1
					else:
						if log:
							print("Program error. Deleting block at: ", x, " ", y, " ", z)
						if replace:
							replaceBlock(level, material, rMaterial, x, y, z)
						else:
							setBlockForced(level, material, x, y, z)
	
	# Prints a message to the MCEdit console saying when the filter ended.
	print '%s: Ended at %s' % (displayName, time.ctime())