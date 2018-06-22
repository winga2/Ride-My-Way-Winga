from flask import Flask, jsonify, request,json

app = Flask(__name__)

# Creating a list of rider
rideOF=[{'id':'01','name':'Winga O','offer':'10%'},
            {'id':'02','name':'Edwin W','offer':'20%'},
            {'id':'03','name':'chizi E','offer':'30%'}]


#Getting all rides
@app.route('/index/v1/rides',methods=['GET'])
def get_All_ride():
    return jsonify({'rides':rideOF})


#Getting a rider by id
@app.route('/index/v1/rides/<ride_id>',methods=['GET'])
def get_ride(ride_id):
    usr = [ ride for ride in rideOF if (ride['id'] == ride_id) ] 
    return jsonify({'ride':usr})



@app.route('/index/v1/rides/<ride_id>/requests',methods=['GET'])
def request_ride(offer):
    ask = [ ride for ride in rideOF if (ride['id'] == offer) ] 
    return jsonify({'ride':ask})


@app.route('/index/v1/rides/<ride_Id>',methods=['PUT'])
def updateride(ride_Id):
    rid = [ ride for ride in rideOF if (ride['id'] == ride_Id) ]
    if 'name' in request.json : 
        rid[0]['name'] = request.json['name']
    if 'offer' in request.json:
        rid[0]['offer'] = request.json['offer']
    return jsonify({'ride':rid[0]})

#adding rider  
@app.route('/index/v1/rides',methods=['POST'])
def createride():
    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'offer':request.json['offer']
    }
    rideOF.append(dat)
    return jsonify(dat)

#deleting a ride
@app.route('/index/v1/rides/<ride_Id>',methods=['DELETE'])
def deleteride(ride_Id):
    em = [ ride for ride in rideOF if (ride['id'] == ride_Id) ]
    if len(em) == 0:
        return em, 200 #Success or OK
    rideOF.remove(em[0])
    return jsonify({'response':'Success'})
if __name__ == '__main__':
 app.run()


