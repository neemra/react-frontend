from flask import Flask, request

app = Flask(__name__)

storage = []

@app.route("/employee/add", methods=['POST'])
def add_emp():
    print(request.form)
    #storage["employee"].append("")
    emp = {
        "id" : request.form.get("id"),
        "name" : request.form.get("name"),
        "email" : request.form.get("email")
    }
    storage.append(emp)
    return "emp sucessully added"

@app.route("/employee/<idd>", methods=['GET'])
def add_emp_by_get(idd):
    print("id", idd)
    return "get method"

@app.route("/employees",methods=['GET'])
def get_employee():
    return storage
    

@app.route("/employee?id=1",methods=['GET'])
def emp_with_id_1():
    return "get"

@app.route("/employee/<idd>", methods=['DELETE'])
def delete_emp(idd):
    print("id", idd)
    return "emp deleted"

@app.route("/employee/<idd>",methods=['PUT'])
def put_method(idd):
    print("id",idd)
    return "updated"
    
app.run(
    port=3001,
    debug = True
)
