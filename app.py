from flask import Flask, jsonify


app = Flask(__name__)


employees = [
    {"id": 1, "name": "Rahul", "department": "IT"},
    {"id": 2, "name": "Priya", "department": "HR"},
    {"id": 3, "name": "Amit", "department": "Finance"}
]




@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Employee Management API",
        "status": "Running"
    })




@app.route("/employees")
def get_employees():
    return jsonify(employees)




@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
