"""
A program that reads words from a file (filename given
as a command-line argument) and prints the number of words.

Usage: wordCount.py filename
"""
import sys
import os

if not os.path.isfile(sys.argv[1]):
    print("[Error] File does not exist!")
    exit()
    
file = open(sys.argv[1], 'r')
words = file.read().split()

print(len(words))