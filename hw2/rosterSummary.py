"""
A student roster file roster1.dat has these fields:
    name,major,gpa,credits
    
Write a file roster1.out with these new fields:
    major,avgGpa,avgCredits,count

where avgGpa is the average GPA for students in that major, avgCredits is
the average number of credits for students in that major, and count is the
number of students in that major.

Usage: rosterSummary.py
Dependencies: roster1.dat
"""
import numpy as np

data_type = {
    'names': ('name', 'major', 'gpa', 'credits'),
    'formats': ('U50', 'U4', 'f8', 'i4')
}

data = np.genfromtxt(
    fname='roster1.dat', 
    delimiter=',', 
    dtype=data_type,
    encoding="utf-8"
)

majors = np.unique(data['major'])

avg_gpa = np.zeros(len(majors))
avg_credits = np.zeros(len(majors))
counts = np.zeros(len(majors), dtype=int)

for i, major in enumerate(majors):
    current_major = data['major'] == major
    avg_gpa[i] = np.mean(data['gpa'][current_major])
    avg_credits[i] = np.mean(data['credits'][current_major])
    counts[i] = np.sum(current_major)

np.savetxt(
    fname='roster1.out',
    X=np.column_stack((majors, avg_gpa, avg_credits, counts)),
    fmt='%s',
    delimiter=',',
    header='major,avgGpa,avgCredits,count',
)