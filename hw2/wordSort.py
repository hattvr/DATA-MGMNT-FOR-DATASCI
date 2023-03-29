"""
A program that reads words from a file (filename 
given as a command-line argument) and prints them 
in (case insensitive) sorted order.

Usage: wordSort.py filename
"""
import sys
import os

if not os.path.isfile(sys.argv[1]):
    print("[Error] File does not exist!")
    exit()

file = open(sys.argv[1], 'r')
words = file.read().split()

for word in sorted(words, key=str.lower):
    print(word)
    
file.close()