from flask import Flask, request
import pyrebase
import hashlib
import json

#set data to talk to firebase
with open('config.json') as f:
    config = json.load(f)


firebase = pyrebase.initialize_app(config) #initalize security
db = firebase.database() #reference to the database

app = Flask(__name__)

@app.route('/query')
def index():
    #get needed information from URL query
    discordName = request.args.get('discordName')
    valRank = request.args.get('valRank')
    email = request.args.get('email')
    method = request.args.get('Method') #method should either be 'get' or 'post'

    #if we want to post to the database
    if method == 'post':
        #store user info in json format
        userToSend = {
                'discordName': discordName,
                'vRank' : valRank,
                'email' : email
            }
        #before we add to the database, check to see if that username is already stored.  Don't want to write over data
        userCheck = db.child("users").child(discordName).get()
        if userCheck.val() != None:
            return "<h1>USER ALREADY IN DATABASE</h1>"

        #send data to google firebase to store and display what we stored to screen
        db.child("users").child(discordName).set(userToSend) #post
        return userToSend

    #if we want to retrieve data about someone from their discord name
    elif method == 'get':
        userGet = db.child("users").child(discordName).get()
        #if nothing comes back with the name we looked for, return error
        if userGet.val() == None:
            return "<h1>Name not found in database</h1>"
        else:
            return userGet.val()

    else:
        #method (post/get) was not specified in URL query. Don't know what to do
        return "<h1>post/get method not specified</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=9000)



# source env/bin/activate to start the env back up
#post: http://localhost:9000/query?Method=post&discordName=Big ChungusHTAG1234&email=HG@gmail.com&valRank=immortal3
#get:http://localhost:9000/query?Method=gefdfd&discordName=DavidShoehashtag1775
