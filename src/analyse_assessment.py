"""
Summarise assessments in School of Engineering courses
"""
import os
import pandas as pd
import pickle

def load(cp):
    
    isExist = os.path.exists(os.path.join(".",cp))
    
    if not isExist:
        print("Data has not been processed - run parse_dpt.py")
    else:
        
        with open(cp, 'rb') as f:
            courses = pickle.load(f)
            return courses
            
               
if __name__ == "__main__":
    showContactOnly = False
    cp = 'courses.pickle'
    
    courses = load(cp)
    
    eng_courses = [] 
     
    for c in courses:
        if c.School == "School of Engineering":
            eng_courses.append(c)
          
            #print(f"{c.Code}: {c.Assessments}")
            
    code = []
    name = []
    organiser = []
    year = []
    credit = []
    semester = []
    we = []
    cw = []
    pe = []
    
    sorted_eng_courses = sorted(eng_courses, key=lambda x: (x.Code[0:3], x.Year))
 
    for c in sorted_eng_courses:
        code.append(c.Code)
        name.append(c.Name)
        organiser.append(c.CourseOrganiser)
        year.append(c.Year)
        semester.append(c.Start)
        credit.append(c.SCQF_credits)
        
        try:
            we.append(c.Assessments["Written Exam"])
        except KeyError:
            we.append("-")
        
        try:
           cw.append(c.Assessments["Coursework"])
        except KeyError:
           cw.append("-")
           
        try:
           pe.append(c.Assessments["Practical Exam"])
        except KeyError:
           pe.append("-")
      
      
        
    df = pd.DataFrame({
        'Code': code,
        'Name': name,
        'Organiser': organiser,
        'Year': year,
        'Credits': credit,
        'Semester': semester,
        'Written Exam %': we,
        'Coursework %': cw,
        'Practical Exam %': pe,
        })
    
    df.to_csv('SOE_assessment.csv', index=False)
  
                
 
