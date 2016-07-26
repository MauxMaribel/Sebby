import sys
import spells_data

all = spells_data.all

def find_by_name(name):
	name = name.lower()
	for s in all:
		if s['name'].lower() == name:
			return s
	return None

def find_by_class(classname, classlevel=None):
	results = []
	classname = classname.lower()
	for s in all:
		if classname in s['classes'] and (classlevel == None or s['classes'][classname] == classlevel):
			results.append(s)
	return results

def find_class_spells(classname, classlevel):
	results = []
	classname = classname.lower()
	for s in all:
		if classname in s['classes'] and (classlevel == None or s['classes'][classname] == classlevel):
			spell_name = s['name']
			results.append(spell_name)
	results.sort()
	return results
