"""Test Course"""

import unittest
from course import Course

class TestCourse(unittest.TestCase):
    """TestCourse"""
    
    def test_init(self):
        """Parse markup"""
        
        #open text file in read mode
        file = open("./example/cxscee09002.html", "r")
        
        #read whole file into a string
        markup = file.read()
 
        #close file
        file.close()
    
        #parse markup
        c = Course(markup)
        
        self.assertEqual(c.Code(), "SCEE09002")
        
        self.assertEqual(c.Name(), "Control and Instrumentation Engineering 3")
        
        keywords = ["Control Systems", "Control Engineering", "Instrumentation"]
        self.assertEqual(c.Keywords(), keywords)



if __name__ == "__main__":
    unittest.main()