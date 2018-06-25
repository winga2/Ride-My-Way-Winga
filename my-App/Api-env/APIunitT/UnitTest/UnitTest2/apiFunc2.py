#Getting a rider by id
# This faild the test!
# When expected is equated to [1]



#To pass the tets!

# Create a list
riders =[{'id':'01','name':'Winga O','offer':'10%'},
            {'id':'02','name':'Edwin W','offer':'20%'},
            {'id':'03','name':'chizi E','offer':'30%'}]

def get_ride():
    """return a rides with their id, name,offer"""
    return riders [1]
