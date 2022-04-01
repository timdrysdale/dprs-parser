"""
Analyse courses
"""
import course 
import matplotlib.pyplot as plt
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
    
    eng_courses = []     
    for c in courses:
        if c.School == "School of Engineering":
            eng_courses.append(c)
            #print(f"{c.Code}: {c.Name} ({c.SCQF_credits} cr, {c.Hours} hrs)")
            
            
    activities = {}

    count =0
    
    for c in eng_courses:
        count = count + 1
        
        # add placeholder for activities we're tracking
        # that are not in this course
        for key in activities:
            if not key in c.Activities:
                c.Activities[key] = 0
        
        for key, value in c.Activities.items():
        
            if key in activities:
                a = activities[key]
            else:
                # keep all values in sequence
                # even when adding new type of activity
                a = [0] * count
                    
            a.append(value)
            activities[key]=a
    
    labels = []
    sizes = []
    for key, value in activities.items():
        if key == "Directed Learning and Independent Learning Hours":
            continue
        labels.append(key)
        sizes.append(sum(value))
        print(f"{key}: {sum(value)}")
        #plt.figure()
        #plt.plot(value)
        #plt.title(key)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    #plt.tight_layout()
    plt.show()    
    plt.savefig("contact_activities.png", dpi=300)
    
    labels = []
    sizes = []
    for key, value in activities.items():
        labels.append(key)
        sizes.append(sum(value))
        print(f"{key}: {sum(value)}")
        #plt.figure()
        #plt.plot(value)
        #plt.title(key)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    #plt.tight_layout()
    plt.show()    
    plt.savefig("all_activities.png", dpi=300)
            
            
            
                
 