"""
Analyse
"""

import course
import os


def directory(directory_in_str):
    
    courses = []
    
    directory = os.fsencode(directory_in_str)
    total = len(os.listdir(directory))
    count = 0
    for file in os.listdir(directory):
        count = count + 1
        try:
            filename = os.fsdecode(file)
            if filename.endswith(".html"):
            
                name = os.path.join(str(directory, 'utf-8'), filename)
                file = open(name, "r")
                #read whole file into a string
                markup = file.read()
                #close file
                file.close()
                #parse markup
 
                c = course.Course(markup)
                print(f"{count}/{total}: {filename} -> {c.Name}\n")
                courses.append(c)
                
        except Exception as e:
            #ignore any problems
            print(f"{count}/{total}: {filename} -X- {e}\n")

    return courses        