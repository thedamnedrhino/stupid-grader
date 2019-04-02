import os
import sys
import math

def has(string, keywords):
	for w in keywords:
		if w in string:
			return True
	return False

def check_grades(folder):
	f = None	
	try:
		f = open("{}/TestDriver.c".format(folder), 'r')
	except FileNotFoundError:
		print("{}/TestDriver.c not found".format(folder))
	
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
	print(grades)

if __name__ == '__main__':
	folder = sys.argv[1]
	check_grades(folder)
		

	
