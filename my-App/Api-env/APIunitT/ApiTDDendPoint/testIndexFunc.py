import unittest
import indextFunc

class KnownValues(unittest.TestCase):
    # Formula for unittest method nameis..
    # test_functionName_testDescription
    # 
     def test_indextFuction_forRides(self):
         # The epectedresult of the fuction 
         result = indextFunc.testIndexFunc(getAllrideOF)
         Exception = rideOF
         # Checking for expected output
         self.assertEqual(Exception,result)


#runing the test

if __name__ == '__main__':
    unittest.main() 