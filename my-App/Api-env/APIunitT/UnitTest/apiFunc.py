# UnitTest for Getting all list of riders
# Equate return to a figure
# This fails the tesat
# When the expected = [] in the TestApi.py 

def get_Allrides():
    """return a list of all rides with their id, name,offer"""
    return 0

# To pass the test
# giving it content of a [] list
# This pass the test
Allriders =[{'id':'01','name':'Winga O','offer':'10%'},
            {'id':'02','name':'Edwin W','offer':'20%'},
            {'id':'03','name':'chizi E','offer':'30%'}]

def get_Allrides():
    """return a list of all rides with their id, name,offer"""
    return Allriders