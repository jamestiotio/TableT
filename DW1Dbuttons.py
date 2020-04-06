import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class TabletGrid(App):
    
    
    def build(self):
    
        self.layout = GridLayout(cols = 2)
        
        self.Assistancelst = []
        self.Toiletlst = []
        
        self.b1 = Button(text="Request Assistance")
        self.b2 = Button(text="Cancel")
        self.b3 = Button(text="Toilet")
        self.b4 = Button(text="Cancel")
        self.layout.add_widget(self.b1)
        self.layout.add_widget(self.b2)
        self.layout.add_widget(self.b3)
        self.layout.add_widget(self.b4)
        
        self.b1.bind(on_press=self.pressRA)
        self.b2.bind(on_press=self.pressCA)
        self.b3.bind(on_press=self.pressT)
        self.b4.bind(on_press=self.pressCT)
        
        return self.layout    
    
    def pressRA(self, instance):
        self.Assistancelst.append("Inputname")
        print (self.Assistancelst)
        db.child("Assistancelst").set(Assistancelst, user['idToken'])
        
    def pressCA(self, instance):    
        self.Assistancelst.remove("Inputname")
        print (self.Toiletlst)
        db.child("Assistancelst").set(Assistancelst, user['idToken'])
        
    def pressT(self, instance):    
        self.Toiletlst.append("Inputname")
        print (self.Toiletlst)
        db.child("Toiletlst").set(Toiletlst, user['idToken'])
        
    def pressCT(self, instance):    
        self.Toiletlst.remove("Inputname")
        print (self.Toiletlst)
        db.child("Toiletlst").set(Toiletlst, user['idToken'])
        
        
    
if __name__ == "__main__":
    TabletGrid().run()
    
    
from libdw import pyrebase

projectid = "tablet-de2e6"
dburl = "https://" + projectid + ".firebaseio.com"
authdomain = projectid + ".firebaseapp.com"
apikey = "AIzaSyCNLlrAOASA68BbmgYwKbNoPforjAoF8n8"
email = "imjw1998@gmail.com"
password = "Alialididi"

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)   

db = firebase.database()
root = db.child("/").get(user['idToken'])
print(root.key(), root.val())

Assistancelst = db.child("Assistancelst").get(user['idToken'])
print(Assistancelst.key(), Assistancelst.val()) 

Toiletlst = db.child("Toiletlst").get(user['idToken'])
print(Toiletlst.key(), Toiletlst.val())     
    
