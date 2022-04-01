"""Course

A course object is initiliased by parsing the relevant HTML page from DRPS
Methods provide information about the course, extracted from the page.

"""

from bs4 import BeautifulSoup
import regex

class Course(): # pylint: disable=too-few-public-methods
    """Courses are initialised from an HTML page in a string
    The optional version string is in case the format changes in future
    or varies
    """
    def __init__(self, markup, parser="lxml", format="default"):
        # we only know about the default format for now
        if format != "default":
            raise ValueError(f'Format {format} not known; available formats are ["default"]')
            
        self.Soup = BeautifulSoup(markup, parser)
        
        #check format
        page_type = self.Soup.find("meta",attrs={"name":"type"})            
        
        if (not page_type) or page_type["content"] != "DPT":
           raise ValueError('Page type is not DPT') 
           
        self.ParseCode()
        self.ParseName()
        self.ParseKeywords()
        self.ParseOutline() 
        self.ParseDelivery()
        
        self.Soup = None #save memory
            
            
    def ParseCode(self):
        # return course code    
        tag = self.Soup.find("meta",attrs={"name":"modcode"})            
        self.Code = tag["content"] if tag else "No course code found"
    
    def ParseName(self):
        #return course name
        tag = self.Soup.find("meta",attrs={"name":"modname"})            
        self.Name = tag["content"] if tag else "No course name found"
    
    def ParseKeywords(self):
        #return keywords
        tag = self.Soup.find("meta",attrs={"name":"modkeywords"})  
        content = tag["content"] if tag else ""
        kw = []
        for k in content.split(","):
            kw.append(k.strip())
            
        self.Keywords = kw    
        
    def GetTableData(self, caption_text):
       # get data from a table with a given caption 
       for caption in self.Soup.find_all('caption'):
           if caption.get_text() == caption_text:
               table = caption.find_parent('table', {'class': 'sitstablegrid'})
       
       data = []
       try: #we might not have found a table with the caption
           rows = table.find_all('tr')
           for row in rows:
               cols = row.find_all('td')
               cols = [ele.text.strip() for ele in cols]
               data.append([ele for ele in cols if ele]) # Get rid of empty values   
       except:
           pass
       
       return data
    
    def ParseOutline(self):
        
        #TODO switch on first string in each row to assign values
               
        data = self.GetTableData("Course Outline")
        self.Outline = data
        
        if data == []:
            return
        
        for row in data:
            
            try:    
                label = row[0].strip()
            
                if label == "School":
                    try:
                        self.School = row[1]
                        self.College = row[3]
                    except:
                        pass
                          
                elif label == "Credit level (Normal year taken)":
                    try:
                        self.Credit_level = row[1]
                        self.Availability = row[3]
                    except:
                        pass
                    
                elif label == "SCQF Credits":
                    try:
                        self.SCQF_credits = float(row[1])
                        self.ECTS_credits = float(row[3])
                    except:
                        pass           
                elif label == "Summary":
                   self.Summary = row[1]
                   
                elif label == "Course description":
                   self.Description = row[1]
               
            except IndexError:
                pass
       
    def ParseDelivery(self):   
        
        data = self.GetTableData("Course Delivery Information")
        self.ActivitiesText = ""
        self.Hours = ""
        
        if data == []:
            return
        
        for row in data:
           try:
               
               label = row[0].strip()
               
               if label == "Course Start":
                   self.Start = row[1]
               elif label.startswith("Learning"):
                   self.ActivitiesText = row[1].replace("\n", " ")
           except IndexError:
               pass
        
          
        pattern = regex.compile(r'^Total\s*Hours:\s*([0-9]+).*')
        m = pattern.match(self.ActivitiesText)
        if m.groups():
            self.Hours = float(m.groups()[0])
            
        pattern = regex.compile(r'(([a-zA-Z\/\s]+)([0-9]+))')
        m = pattern.findall(self.ActivitiesText)
        self.Activities = {}
        for element in m:
            what = element[1].strip()
            hours = int(element[2])
            if not (what == ""):
                self.Activities[what] = hours
        
                    

    
