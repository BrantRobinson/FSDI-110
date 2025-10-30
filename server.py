from flask import Flask, jsonify

app = Flask(__name__) # instance of FLask


@app.route("/", methods=["GET"])
def index():
     return "Welcome to Flask framework"


@app.route("/cohort61", methods=["GET"])
def cohort61():
     return "Eric, Jeuan, Brant, Micah, Mat"


@app.route("/cohort100", methods=["GET"])
def cohort100():
     students_list = ["Pam", "John", "Dwight", "Michael", "Oscar"]
     return students_list


@app.route("/contact", methods=["GET"])
def contact():
     information = {
          "email": "jenny@TommyTutone.com", 
          "phone": "867-5309"
          }
     return information


@app.route("/course", methods=["GET"])
def course_information():
     information = {
          "title": "Introduction to Web API Flask", 
          "duration": "4 sessions",
          "level": "beginner"
     }
     return information


@app.route("/user", methods=["GET"])
def get_user():
     user = {
          "name": "Brant",
          "role": "Super Dad",
          "is_active": True,
          "favorite_tech": ["React", "JQuery", "PHP", "Nintendo Entertainment System"]
     }
     return user


coupons = [
        {"_id": 1, "code": "WELCOME10", "discount": 10},
        {"_id": 2, "code": "SPOOKY25", "discount": 25},
        {"_id": 3, "code": "VIP50", "discount": 50}
    ]


@app.route("/api/coupons", methods=["GET"])
def get_coupons():
     return jsonify(coupons)


@app.route("/api/coupons/count", methods=["GET"])
def get_coupon_count():
    num_coupons = len(coupons)
    return jsonify(num_coupons)


@app.route("/cohort/<id>", methods=["GET"])
def get_cohort_names(id):
    if id == "100":
        students_list = ["Pam", "John", "Dwight", "Michael", "Oscar"]
    elif id == "61":
        students_list = ["Eric", "Jeuan", "Brant", "Micah", "Mat"]
    else:
        students_list = ["No Students in that cohort"]

    return students_list


if __name__ == "__main__":
     app.run(debug=True)

# WHen this file is run directly: __name__ == "__main__"
# When this file is imported as a module __name__ == "server"

