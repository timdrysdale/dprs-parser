"""Test Course"""
import sys
import unittest
import analyse


class TestAnalyse(unittest.TestCase):
    """TestAnalyse"""
    
   
    def test_other_activities(self):
        
        a  = {
              'Directed Learning and Independent Learning Hours': [57,123],
              'Formative Assessment Hours': [1,4],
              'Lecture Hours': [22,12],
              'Programme Level Learning and Teaching Hours': [2,0],
              'Seminar/Tutorial Hours': [11,45],
              'Summative Assessment Hours': [4,3],
              'Supervised Practical/Workshop/Studio Hours': [1,1]
              
        }
        exp  = {
      'Directed Learning and Independent Learning Hours': 180,
      'Other': 7,
      'Lecture Hours': 34,
      'Seminar/Tutorial Hours': 56,
      'Summative Assessment Hours': 7,
      'Supervised Practical/Workshop/Studio Hours': 2
}
        
        actual = analyse.other_activities(a, keep=["Supervised Practical/Workshop/Studio Hours"])
        print(actual)
        for key, value in exp.items():
            self.assertEqual(value, actual[key])

        
        
if __name__ == "__main__":
    unittest.main()