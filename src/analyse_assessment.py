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
    year = []
    credit = []
    we = []
    cw = []
    pe = []
    ai= []
    fb = []
    
    sorted_eng_courses = sorted(eng_courses, key=lambda x: (x.Code[0:3], x.Year))
        
    for c in sorted_eng_courses:
        code.append(c.Code)
        name.append(c.Name)
        year.append(c.Year)
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
        'Year': year,
        'Credits': credit,
        'Written Exam': we,
        'Coursework': cw,
        'Practical Exam': pe,
        })
    
    writer = pd.ExcelWriter('SOE_assessment.xlsx') 
    
    df.to_excel(writer, sheet_name='Courses', index=False)     
            
    writer.close()      
                
 
