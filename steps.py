#step 1
from flask import Flask, request

app = Flask(__name__)

storage = {
    "employee" : [
        
    ]
}

# step 3 making APIs with decorator
# @app.route("/")
# def home():
#     return "hello"

# @app.route("/profile", methods=['GET'])
# def test():
#     return "hello"

@app.route("/input", methods=['GET'])
def input():
    print(request.args)
    print("query string 1 ",request.args.get("Keys1"))
    print("query string 2 ",request.args.get("Keys2"))
    return "query string"

# <id> path parameter used for geting input by GET Method
@app.route("/input/get/path_parameter/<idd>")
def input_get_path_parameter(idd):
    print("id",idd)
    return "path parameter"

@app.route("/input/post/add_employee", methods=['POST'])
def input_post_add_emp():
    return "added" 

#step 2
app.run(
    port=3001,
    debug = True
)
