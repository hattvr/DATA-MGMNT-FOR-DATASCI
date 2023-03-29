"""
A program that reads words from a file (file-
name given as a command-line argument) and 
prints the number of distinct words. Words that 
differ only in case should be considered to be 
equivalent.

Usage: wordCountDistinct.py filename
"""
import sys
import os

if not os.path.isfile(sys.argv[1]):
    print("[Error] File does not exist!")
    exit()
    
file = open(sys.argv[1], 'r')
words = file.read().split()

distinct = []
for word in sorted(words, key=str.lower):
    if word.lower() not in distinct:
        distinct.append(word.lower())

print(len(distinct))