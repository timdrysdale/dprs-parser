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
            
            
    def Code(self):
        
        code = self.Soup.find("meta",attrs={"name":"modcode"})            
        return code["content"] if code else "No course code found"




