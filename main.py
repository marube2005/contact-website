#Contains the endpoints of our website.
#irst thing you ask yourself what are the different endpoints you require for your website.
#We want a CRUD app an Operation for Creating,Reading,Uploading,Deleting.
#When we Create what do we need, We need :
# - first_name
# - last_name
# - email
# When we create aN API, we need an server which runs the API.
#An end point is something which comes after the local host.
#Example of a local host is :
#Local host: 5000 / create_contact
#Request - process of sending data to an API.(From an external source)
# TYPES : GET(FETCH DATA EG USER HISTORY) UPDATE(USED FOR UPDATION EG CONTACT), DELETE
#We can also send json data(info that comes alongside with our request data)

#Response - fetched back from API to the frontend. Contains the following:
#status : 200(success), 404(not found), 400(bad request), 403(forbidden)

from flask import request, jsonify #Allow us to turn to json data.
from config import app, db
from models import Contact

@app.route("/contacts", methods=["GET"])
def get_contacts():
  contacts = Contact.query.all() #Gives us a list of all contacts
  json_contacts = list(map(lambda x: x.to_json(), contacts))
  return jsonify({"contacts" : json_contacts}), 200

@app.route("/create_contact", methods=["POST"])
def create_contact():
                                                            #Getting the data associated with the contact we wanna create. Request should also be in json format.
 first_name = request.json.get("firstName")
 last_name = request.json.get("lastName")
 email = request.json.get("email")
                                                              # we wanna make sure these values exist coz if they don't exist we can't make a contact. 
 if not first_name or not last_name or not email :
   return jsonify({"Message":"You must provide a first name, last name and email address"}), 400
   
                                                               #Symbolising that a new contact was created and it was a success.
 new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
 try:
   db.session.add(new_contact)
   db.session.commit()                                         #Contact has been Fully added on the database through this statement.
 except Exception as e:
   db.session.rollback() #
   return jsonify({"Message":str(e)}), 400
 
 return jsonify({"Message":"Contact has been saved successfully"}), 201


@app.route("/update_contact/<int:user_id>", methods=["PATCH"] )                    # update in accordance to the user_id which was auto_increment.
def update_contact (user_id):
 contact = Contact.query.get(user_id)                                      # Look at the list of Contacts and find the user that has a specific user_id.

 if not contact:
   return jsonify({"Message":"User has not been found"}), 404
 
 data = request.json 
 contact.first_name = data.get("firstName", contact.first_name)          # A user can change either first_name or last_name or email or all from these code.
 contact.last_name = data.get("lastName", contact.last_name)
 contact.email = data.get("email", contact.email)

 db.session.commit()                                                    #Contact has been fully updated in the database.
 
 return jsonify({"Message" : "User Updated"}),200
                                                                         #tHE FILE WILL ONLY RUN DIRECTLY FROM HERE AND WHEN WE IMPORT IT THE CODE BELOW WONT BE EXECUTED>

@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
   contact = Contact.query.get(user_id)                                      # Look at the list of Contacts and find the user that has a specific user_id.

   if not contact:
    return jsonify({"Message":"User has not been found"}), 404
   db.session.delete(contact)
   db.session.commit()

   return jsonify({"Message":"User deleted"}), 200
        
if __name__  == '__main__':                                              # It says if you run the main.py file thrn execute the code below.
 with app.app_context():                                                 #does this if they are not created.
   db.create_all()
 app.run(debug = True)

 #postman allows you send specific request with json data to An API in an IDE.