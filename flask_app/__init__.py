from flask import Flask, session
DATABASE = "car_pool_schema"

app = Flask(__name__)
app.secret_key = "Here is our flask project"