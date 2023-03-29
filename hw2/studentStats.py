"""
A program that reads the file roster2.dat that has this format:
    name,age,major,gpa
    
Convert this to a numpy array as shown above. Then use that array to com-
pute and print each of the following:
    (a) The average GPA of all students
    (b) The maximum GPA of students majoring in CS
    (c) The number of students with a GPA over 3.5
    (d) The average GPA of students who are at least 25 years old
    (e) The major that has the highest average GPA among 
    students at most 22 years old.

Usage: studentStats.py
Dependencies: roster2.dat
"""
import numpy as np

data_type = {
    "names": ("name", "age", "major", "gpa"),
    "formats": ("U50", "i4", "U4", "f8"),
}

data = np.genfromtxt(
    fname="roster2.dat", 
    delimiter=",", 
    dtype=data_type, 
    encoding="utf-8"
)

"""
According to the example in the homework instructions, 
we could initialize the array as follows, however
to reduce redundancy, I've used the array generated
by genfromtxt directly.

    arr = np.zeros(len(data), dtype=data_type)

    arr['name'] = data['name']
    arr['age'] = data['age']
    arr['major'] = data['major']
    arr['gpa'] = data['gpa']

I would like to reiterate that whether we used
data or arr for the upcoming code, the output would
still be the same.
"""

# (a) The average GPA of all students
avg_gpa = np.mean(data["gpa"])
print(f"{avg_gpa}")

# (b) The maximum GPA of students majoring in CS
if np.any(data["major"] == "CS"):
    max_gpa_cs = np.max(data["gpa"][data["major"] == "CS"])
else:
    max_gpa_cs = None
print(f"{max_gpa_cs}")

# (c) The number of students with a GPA over 3.5
if np.any(data["gpa"] > 3.5):
    total_students = np.sum(data["gpa"] > 3.5)
else:
    total_students = None
print(f"{total_students}")

# (d) The average GPA of students who are at least 25 years old
follow_age_restriction = data["age"] >= 25
if np.any(follow_age_restriction):
    avg_gpa = np.mean(data["gpa"][follow_age_restriction])
else:
    avg_gpa = None
print(f"{avg_gpa}")

# (e) The major that has the highest average GPA among students at most 22 years old
follow_age_restriction = data["age"] <= 22
if np.any(follow_age_restriction):
    majors = np.unique(data["major"][follow_age_restriction])
    avg_gpa = np.zeros(len(majors))
    for i in range(len(majors)):
        avg_gpa[i] = np.mean(
            data["gpa"][(follow_age_restriction) & (data["major"] == majors[i])]
        )

    major = majors[np.argmax(avg_gpa)]
else:
    major = None
print(major)