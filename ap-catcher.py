'''
Code by Cougar - Do not copy without credits
www.guiadohacker.com.br
Written using Python 3.4.4 - For Windows
Release 1.7.5 (February 18, 2016)

Wordlist generator based on keywords
Copyright (C) 2016  Cougar

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
	
# Imports

import os, sys, math, timeit

# Functions

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def space(n):
	return '\n' * n

def toBin(num):
	if num == 0:
		return ""
	return toBin(num//2) + str(num%2)

def res(nstrings):
	pos = 1
	for i in range(nstrings):
		pos = pos * 2
	return pos

def wordcount(nstrings):
	words = 0
	for i in range(1, nstrings + 1):
		words = words + (math.factorial(nstrings) / math.factorial(nstrings - i))
	return int(words)

def convertBytes(size, is_memory):
	if (size == 0):
		return '0b'
	notation = ('b', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
	i = int(math.floor(math.log(size, 1024)))
	p = math.pow(1024, i)
	s = round(size/p, 2)
	warning_handler = ''
	if i >= 3 and s >= 2 and is_memory == True:
		print (space(1))
		warning_handler = '\n\n!Warning! 32-bit systems (x86) can store only 2GB of memory, exceeding the limit will leave the wordlist incomplete!'
	return '%s %s %s' % (s, notation[i], warning_handler)
	
def convertTime(time):
	floor = 0
	for i in range(2):
		if time >= 60:
			time = time / 60
			floor = floor + 1
	notation = ('seconds', 'minutes', 'hours')
	return '%.2f %s' % (time, notation[floor])
	

def filesize(strings, nstrings):
	nchar = 0
	for i in range(nstrings):
		nchar = nchar + len(strings[i])
	nchar = nchar * wordcount(nstrings)
	return convertBytes(nchar, False)

def memorysize(strings, nstrings):
	memory = (sys.getsizeof(strings) * wordcount(nstrings)) / 2
	return convertBytes(memory, True)

def zeros(val, nstrings):
	while len(val) < nstrings:
		val = "0" + val
	return val

def swap(result, l, r):
	t = result[l]
	result[l] = result[r]
	result[r] = t
	return result

def toString(List):
	return ''.join(List)

def permute(result, l, r):
	if l==r:
		if toString(result) not in lines_seen:
			wordlist.write(toString(result) + "\n")
			lines_seen.add(toString(result))
	else:
		for i in range(l, r + 1):
			result = swap(result, l, i)
			permute(result, l + 1, r)
			result = swap(result, l, i)

def checkint():
	while True:
		nkeywords = input('Number of keywords: ')
		try:
			nkeywords = int(nkeywords)
		except ValueError:
			print ('Invalid value!')
		if type(nkeywords) == int:
			return nkeywords

def parameters():
	print (space(1))
	print ('Building early structure, %s results.' % (pos))
	print (space(1))
	print ('Parameters\nNumber of keywords: %s \nKeywords: %s \nTotal number of words: %s \nApproximate file size: at least %s \nApproximate memory usage: at least %s' % (nkeywords, strings, "{:,}".format(wordcount(nstrings)), filesize(strings, nstrings), memorysize(strings, nstrings)))
	print (space(1))

# Code start and reload point

while True:

# Call clear

	cls()			

# Global Variables

	error_handler = 0
	strings = []
	parlist = []
	result = []
	lines_seen = set()
	wordlist = open('wordlist.txt', "w")

# For user input only

	nkeywords = checkint()
	print (space(1))
	for i in range(nkeywords):
		strings.append(input('Keyword %s: ' % (i + 1)))

# Resume Global Variables

	nstrings = len(strings)
	pos = res(nstrings)

# Wordlist

	parameters()
	
	while True:
		response = input('Are you sure you want to continue? [y/n]: ')
		answers = ['y', 'Y', 'n', 'N']
		if not(response in answers):
			print ('Invalid answer!')
		else:
			break
	
	if response in ('y', 'Y'):
		break

print (space(1))
print ('Writing wordlist...')
print (space(1))

start = timeit.default_timer()

for i in range(pos):
	par = zeros((toBin(i)), nstrings)

	for letter in par:
		parlist.append(letter)	

	for i in range(len(parlist)):
		if parlist[i] != "0":
			result.append(strings[i])

	if (len(result) - 1) != -1:
		permute(result, 0, len(result) - 1)
		
	parlist = []
	result = []

wordlist.close()

stop = timeit.default_timer()

print ('Finished with %s results in %s.\nTotal file size: %s \n' % ("{:,}".format(wordcount(nstrings)), convertTime(stop - start), convertBytes(os.path.getsize('wordlist.txt'), False)))
