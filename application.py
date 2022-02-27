from logging import debug
from typing import List
from flask import Flask as fk, request 
from flask import Flask, render_template
import urllib 


<<<<<<< HEAD:application.py
application = fk(__name__)
@application.route('/')
def Register()-> str :
   return render_template ('Loggin.html',Tittlepage='Loggin')

if __name__ == '__main__':
   
   application.run(debug=True)
=======
app = fk(__name__)
@app.route('/')
def Register()-> str :
   return render_template ('Loggin.html',Tittlepage='Loggin')
>>>>>>> dev:app.py
