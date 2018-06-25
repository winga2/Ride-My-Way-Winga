#Getting a rider by id
import unittest
import apiFunc2

class KnownValues(unittest.TestCase):
    # Formula for unittest method nameis..
    # test_functionName_testDescription
    # 
     def test_get_ride(self):
         # The epectedresult of the fuction 
         result = apiFunc2.get_ride(ride_id)
         expected = [1]
         # Checking for expected output
         self.assertEqual(expected,result)


#runing the test
 
if __name__ == '__main__':
    unittest.main() 