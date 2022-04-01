"""
Analyse courses
"""
import course 
import os
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
    
    cp = 'courses.pickle'
    
    courses = load(cp)
    
        
    for c in courses:
        if c.School == "School of Engineering":
            print(f"{c.Code}: {c.Name} ({c.SCQF_credits} cr, {c.Hours} hrs)")
                
 