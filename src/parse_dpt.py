"""
Parse DPT
"""
import os
import parse
import pickle

if __name__ == "__main__":
    
    cp = 'courses.pickle'
    
    isExist = os.path.exists(os.path.join(".",cp))
    
    if isExist:
        print("Data already processeed")
    else:
        
        
        courses = parse.directory('../dpt')
        
        for c in courses:
            if c.School == "School of Engineering":
                print(f"{c.Code}: {c.Name} (level {c.Year}, {c.SCQF_credits} cr, {c.Hours} hrs)")
                
        with open(cp, 'wb') as f:
            pickle.dump(courses,f)    
        
    
