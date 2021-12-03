#!/usr/bin/env python3
import sys

students = sys.argv[2].split(',')
universityOf = dict()
with open(sys.argv[1], 'r') as f:
	for line in f:
		universityOf[line.split(':')[0]] = line.split(':')[1].strip()

for student in students:
	try:
		print(f"Name: {student}, University: {universityOf[student]}")
	except:
		print(f"No record of {student} was found!")
