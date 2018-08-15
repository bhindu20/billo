import pyrebase
config = {
  "apiKey": "AIzaSyAnOtm-BBGemaE6zVuHdAsGPv74jAja8HE",
  "authDomain": "billo-dc14a.firebaseapp.com",
  "databaseURL": "https://billo-dc14a.firebaseio.com",
  "projectId": "billo-dc14a",
  "storageBucket": "billo-dc14a.appspot.com",
  "messagingSenderId": "958595540779"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
#authenticate a user
user = auth.sign_in_with_email_and_password("bhindu20@gmail.com", "test1234")

# Create data in the realtime database
# db = firebase.database()
# archer = {"email": "bhindu20@yahoo.com", "password": "test1234"}
# db.child("agents").push(archer, user['idToken'])

# New user account to sign in
auth.create_user_with_email_and_password("bhindu20@yahoo.com", "test1234")