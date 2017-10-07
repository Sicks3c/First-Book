from shutil import copyfile
from sys import exit
import os
import shutil

def introduction():
	print "Choose which one"
	choice = raw_input("> ")
	if choice == '1':
		fuction1()
	elif choice == '2':
		fucntion2()
	else:
		pass


def fuction1():

	source = raw_input("Enter source file with full path: ")
	target = raw_input("Enter target file with full path: ")

	# adding exception handling
	try:
	    copyfile(source, target)
	except IOError as e:
	    print("Unable to copy file. %s" % e)
	    exit(1)

	print("\nFile copy done!\n")

	while True:
	    print("Do you like to print the file ? (y/n): ")
	    check = raw_input("(y/n)> ")
	    if check == 'n':
	        break
	    elif check == 'y':
	        file = open(target, "r")
	        print("\nHere follows the file content:\n")
	        print(file.read())
	        file.close()
	        print()
	        break
	    else:
	        continue




def fucntion2():
		source_2 = raw_input('Full path of the file > ')
		target_2= raw_input('Path where to copy > ')

		target = os.path.join(target_2, os.path.dirname(source_2))
		try:
			shutil.copy(source_2, target_2)
		except IOError as e:
			print ("Unable to copy file. %s" % e)

introduction()
