import os
import sys
import math

def has(string, keywords):
	for w in keywords:
		if w in string:
			return True
	return False

def check_grades(folder, p=True):
	f = None	
	try:
		f = open("{}/TestDriver.c".format(folder), 'r')
	except FileNotFoundError:
		print("{}/TestDriver.c not found".format(folder))
		return {'sum': 0, 'not_found': True}
	
	grades = {'add': 0, 'compute': 0, 'print': 0, 'destroy': 0}
	for line in f:
		add_keywords = ['insert_course', 'add_course']
		if has(line, add_keywords):
			grades['add'] = 1
		if has(line, ['compute_course']):
			grades['compute'] = 1
		if has(line, ['print_course']):
			grades['print'] = 1
		if has(line, ['destroy_course']):
			grades['destroy'] = 1

	grades['sum'] = sum(grades.values())
	grades['name'] = folder
	if p:
		print(grades)
	return grades

def read_json(fname):
	import json
	with open(fname) as f:
		data = json.load(f)
	return data

def dump_json(data, f):
	import json
	with open(f, 'w') as file:
		json.dump(data, file, indent=4)
		print("data written to {}".format(file))	

if __name__ == '__main__':
	folder = sys.argv[1]
	if 'json' in folder:
		data = read_json(folder)
		d = sys.argv[2]
		grades = {}
		for name in os.listdir(d):
			if not os.path.isdir("{}/{}".format(d, name)):
				continue
			g = check_grades("{}/{}".format(d, name), p=False)
			grades[name] = g['sum']
			print(g['sum'])
		for l, e in enumerate(data["marks"]):
			name = e["userid"]
			if name in grades:
				e["testing"]["mark"] += grades[name]
			data["marks"][l] = e
			print("{}, {}, {}".format(name, e["testing"]["mark"], grades[name]))
		dump_json(data, 'new_marks.json')
				
		# base = sys.argv[2]
		# for name in os	
	else:
		check_grades("{}/{}", base, folder)
		

	
