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
        
        self.assertEqual(c.Code, "SCEE09002")
        
        self.assertEqual(c.Name, "Control and Instrumentation Engineering 3")
        
        keywords = ["Control Systems", "Control Engineering", "Instrumentation"]
        
        self.assertEqual(c.Keywords, keywords)
        
        self.assertEqual(c.School,"School of Engineering")
        
        self.assertEqual(c.College, 'College of Science and Engineering')
        
        self.assertEqual(c.Credit_level, 'SCQF Level 9 (Year 3 Undergraduate)')
        
        self.assertEqual(c.Availability, 'Available to all students')
        
        self.assertEqual(c.SCQF_credits, 10)
        
        self.assertEqual(c.ECTS_credits, 5)
        
        summary = 'This is a first course in the design and analysis of instrumentation and control systems. The course starts with an introduction to instrumentation, covering the basics of sensor technology and measurement techniques, including the characteristics and real-world limitations of transducers as well as their interfacing with the control system. It then goes on to introduce Control Theory, providing a basic understanding and building the mathematical background for the modelling, design and analysis of linear single-input single-output feedback systems. It then introduces the concept of stability as well as the available methods for its assessment. It develops the analytical tools for the design of appropriate controllers to improve system performance. It allows students to appreciate the interdisciplinary nature and universal application of control engineering. Finally it introduces modern approaches including application of artificial intelligence to control systems. \n\nThe course also has a an interactive lab component which allows the students to get practical experience in working with a dynamic system and designing a simple controller.'
        
        self.assertEqual(c.Summary, summary)
        
        description = 'Topics covered (and indicative no. of lectures for each):\nInstrumentation (3 lectures): main types of transducers including flow, pressure, temperature, position, force, velocity and acceleration transducers; signal conditioning and interfacing.\n\nMathematical Models of Dynamic Systems (5 lectures): \nopen and closed-loop systems; static and dynamic response; modelling of linear systems; linearisation; Laplace transform; transfer functions; block diagrams.\n\nFeedback Systems (5 lectures): \nerror signals; sensitivity; disturbance rejection; steady-state and transient response; performance of 1st and 2nd order systems; stability; Routh-Hurwitz stability criterion. \n\nControl Systems in Frequency Domain (5 lectures): Bode plots; gain and phase margins; frequency domain performance specifications; relative stability; controller design using frequency response methods.\n\nController Design (4 lectures):\nProportional-Integral-Derivative controllers; Phase-lead and lag compensators; introduction to Artificial Intelligence for Control (Neural Networks, Fuzzy Controllers).'
        
        self.assertEqual(c.Description, description)
        
        self.assertEqual(c.Start, "Semester 2")
        

        activities_text = 'Total Hours: 100  (  Lecture Hours 22,  Seminar/Tutorial Hours 11,   Supervised Practical/Workshop/Studio Hours 3,      Formative Assessment Hours 1,  Summative Assessment Hours 4,    Programme Level Learning and Teaching Hours 2,  Directed Learning and Independent Learning Hours 57 )'
        
        self.assertEqual(c.ActivitiesText,activities_text)
        
        self.assertEqual(c.Hours, 100)
        
        activities = {
              'Directed Learning and Independent Learning Hours': 57,
              'Formative Assessment Hours': 1,
              'Lecture Hours': 22,
              'Programme Level Learning and Teaching Hours': 2,
              'Seminar/Tutorial Hours': 11,
              'Summative Assessment Hours': 4,
              'Supervised Practical/Workshop/Studio Hours': 3
        }
        
        self.assertEqual(c.Activities,activities)
        
        
        
if __name__ == "__main__":
    unittest.main()