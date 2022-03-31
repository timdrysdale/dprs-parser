"""Course

A course object is initiliased by parsing the relevant HTML page from DRPS
Methods provide information about the course, extracted from the page.

"""

from bs4 import BeautifulSoup

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
       rows = table.find_all('tr')
       for row in rows:
           cols = row.find_all('td')
           cols = [ele.text.strip() for ele in cols]
           data.append([ele for ele in cols if ele]) # Get rid of empty values   
       return data
    
    def ParseOutline(self):
        
        data = self.GetTableData("Course Outline")
        self.Outline = data
        self.School = data[0][1]
        self.College = data[0][3]
        self.Credit_level = data[1][1]
        self.Availability = data[1][3]
        self.SCQF_credits = int(data[2][1])
        self.ECTS_credits = int(data[2][3])
        self.Summary = data[4][1]
        self.Description = data[5][1]
        
       
    def ParseDelivery(self):   
        
        data = self.GetTableData("Course Delivery Information")
        self.Start = data[2][1]
    
    def Activities(self):
        #return activities and hours
        return None

    
