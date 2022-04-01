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
            
def sum_activities(courses):
    activities = {}

    count =0
   
    for c in courses:
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
            
    return activities

def other_activities(activities, threshold=0.02, keep=[]):
        total = 0
        summed = {}
        for k, v in activities.items():
            sv = sum(v)
            summed[k] = sv
            total = total + sv
    
        # convert percentage threshold to absolute value    
        threshold_abs = total * threshold    
        
        other = 0
        
        delete = []

        
        for k, sv in summed.items():
            # override keep if zero value
            if (sv < threshold_abs and not k in keep) or sv == 0:
                delete.append(k)
                other = other + sv
                
                
        for k in delete:
            summed.pop(k)
            
        summed["Other"] = other

        return summed
                    
           
if __name__ == "__main__":
    showContactOnly = False
    cp = 'courses.pickle'
    
    courses = load(cp)
    
    eng_courses = [] 
    eng_1 = []
    eng_2 = []
    eng_3 = []
    eng_4 = []
    eng_5 = []
    eng_pg = []
    
    for c in courses:
        if c.School == "School of Engineering":
            eng_courses.append(c)
            #print(f"{c.Year}")
            if c.Year == '1':
                eng_1.append(c)
            elif c.Year == '2':
                eng_2.append(c)
            elif c.Year == '3':
                eng_3.append(c)
            elif c.Year == '4':
                eng_4.append(c)
            elif c.Year == '5':
                eng_5.append(c)
            elif c.Year == 'pg':
                eng_pg.append(c)
                
            #print(f"{c.Code}: {c.Name} ({c.SCQF_credits} cr, {c.Hours} hrs)")
            
    activities = other_activities(sum_activities(eng_courses))
    
    
    if showContactOnly:
        labels = []
        sizes = []
        for key, value in activities.items():
            if key == "Directed Learning and Independent Learning Hours":
                continue
            labels.append(key)
            sizes.append(value)
            print(f"{key}: {value}")
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
        
    clist = [
        eng_1,
        eng_2,
        eng_3,
        eng_4,
        eng_5,
        eng_pg     
        ]
    
    levels = [
        "Year 1",
        "Year 2",
        "Year 3",
        "Year 4",        
        "Year 5",
        "Post Graduate"
        ] 
    
    #fix colours per category
    categories = sum_activities(eng_courses).items()
    
    short_keys = {'Lecture Hours': 'Lectures',
                  'Seminar/Tutorial Hours': 'Tutorials',
                  'Supervised Practical/Workshop/Studio Hours': 'Practicals',
                  'Feedback/Feedforward Hours': 'Feedback',
                  'Programme Level Learning and Teaching Hours': 'Programme',
                  'Directed Learning and Independent Learning Hours': 'Independent',
                  'Formative Assessment Hours': 'Formative',
                  'Summative Assessment Hours': 'Summative',
                  'Online Activities': 'Online', 
                  'Other Study Hours': 'Other study',
                  'Dissertation/Project Supervision Hours': 'Project Supervisions',
                  'Revision Session Hours': 'Revision',
                  'Placement Study Abroad Hours': 'Abroad',
                  'External Visit Hours': 'External Visits',
                  'Fieldwork Hours': 'Fieldwork'
                  }

    color_keys = { 'Other': 'lightgrey',
                   'Lecture Hours': 'firebrick',
                   'Seminar/Tutorial Hours': 'dodgerblue',
                   'Supervised Practical/Workshop/Studio Hours': 'forestgreen',
                   'Feedback/Feedforward Hours': 'blueviolet',
                   'Programme Level Learning and Teaching Hours': 'wheat',
                   'Directed Learning and Independent Learning Hours': 'orange',
                   'Formative Assessment Hours': 'darkmagenta',
                   'Summative Assessment Hours': 'navy',
                   'Online Activities': 'seagreen', 
                   'Other Study Hours': 'darkgrey',
                   'Dissertation/Project Supervision Hours': 'orange',
                   'Revision Session Hours': 'cornsilk',
                   'Placement Study Abroad Hours': 'chocolate',
                   'External Visit Hours': 'saddlebrown',
                   'Fieldwork Hours': 'peru'
                   }
    explode_keys = ['Supervised Practical/Workshop/Studio Hours'] 
    
    for c, l in zip(clist, levels):
            
        activities = other_activities(sum_activities(c), threshold=0.03, keep=["Supervised Practical/Workshop/Studio Hours"])
        labels = []
        sizes = []
        explode = []
        colors = []
        print(l)
        for key, value in activities.items():
            #replace key if known to have a short_key
            short = key
            if key in short_keys:
                short = short_keys[key]
            if key in explode_keys:
                explode.append(0.1)
            else:
                explode.append(0)
                
            if key in color_keys:    
                colors.append(color_keys[key])
            else:
                colors.append("beige")
                
            labels.append(short)
            sizes.append(value)
            print(f"{key}: {value}")
       
        
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, explode=explode, colors = colors, autopct='%1.0f%%',
        shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
   
        plt.title(l)
        plt.show() 
        l = l.replace(" ","_")
        plt.savefig(f"{l}_all_activities.png", dpi=300)
    
    
            
            
            
                
 