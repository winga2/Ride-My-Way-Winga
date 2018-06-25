import unittest
import apiFunc

class KnownValues(unittest.TestCase):
    # Formula for unittest method nameis..
    # test_functionName_testDescription
    # 
     def test_get_Allrides(self):
         # The epectedresult of the fuction 
         result = apiFunc.get_Allrides()
         expected = [{'id':'01','name':'Winga O','offer':'10%'},
            {'id':'02','name':'Edwin W','offer':'20%'},
            {'id':'03','name':'chizi E','offer':'30%'}]
         # Checking for expected output
         self.assertEqual(expected,result)


#runing the test
 
if __name__ == '__main__':
    unittest.main() 