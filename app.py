from logging import debug
from typing import List
from flask import Flask as fk, request 
from flask import Flask, render_template
import urllib 


app = fk(__name__)
@app.route('/')
def Register()-> str :
   return render_template ('Loggin.html',Tittlepage='Loggin')