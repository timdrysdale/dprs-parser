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
            
            
    def Code(self):
        # return course code    
        tag = self.Soup.find("meta",attrs={"name":"modcode"})            
        return tag["content"] if tag else "No course code found"
    
    def Name(self):
        #return course name
        tag = self.Soup.find("meta",attrs={"name":"modname"})            
        return tag["content"] if tag else "No course name found"
    
    def Keywords(self):
        #return keywords
        tag = self.Soup.find("meta",attrs={"name":"modkeywords"})  
        content = tag["content"] if tag else ""
        kw = []
        for k in content.split(","):
            kw.append(k.strip())
            
        return kw    





