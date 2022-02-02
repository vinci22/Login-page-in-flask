from logging import debug
from typing import List
from flask import Flask as fk 
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = fk(__name__)
#
@app.route('/')
def Register()-> str :
   return render_template ('Loggin.html',Tittlepage='Loggin')

if __name__ == '__main__':
   
   app.run(debug=True)
