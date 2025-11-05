from flask import Flask, jsonify, request
from http import HTTPStatus

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





# Session #3
# Path Parameters
# Is a dynamic part of the URL used to identify a specific item or resource
@app.route("/greet/<string:name>")
def greet(name):
     return f"Hey {name}"

student_names = ["Micah", "Brant", "Jeuan", "Mat", "Eric"]

@app.route("/students", methods=["POST"])
def add_student():
     student_names.append("Leo")
     print("Hello Cohort 61")
     return student_names

products = [
     {
          "_id": 1,
          "title": "Nintendo Switch",
          "price": 299.99,
          "category": "electronics",
          "image": "https://picsum.photos/seed/1/300/300"
     },
     {
          "_id": 2,
          "title": "Smart Refrigerator",
          "price": 999.99,
          "category": "kitchen",
          "image": "https://picsum.photos/seed/2/300/300"
     },
     {
          "_id": 3,
          "title": "BLuetooth Speaker",
          "price": 79.99,
          "category": "electronics",
          "image": "https://picsum.photos/seed/3/300/300"
     }
]



@app.route("/api/products")
def get_products():
     return jsonify({
          "success": True,
          "message": "Products retrieved successfully",
          "data": products
     }), HTTPStatus.OK # 200 - it would do this without this code, but we are overriding to always return code 200


@app.route("/api/products/<int:product_id>", methods=["GET"])
def  get_product_by_id(product_id):
     print(product_id)
     for product in products:
          if product["_id"] == product_id:
               return jsonify({
                    "success": True,
                    "message": "Products retrieved successfully",
                    "data": product
     })
     return jsonify({
          "success": False,
          "message": "Product not found"
     }),HTTPStatus.NOT_FOUND
          

@app.post("/api/products")
def add_product():
     new_product = request.get_json()
     new_product["_id"] = len(products) + 1
     products.append(new_product)
     return jsonify ({
          "success": True,
          "message": "Product Successfully Added",
          "data": new_product
     }), HTTPStatus.CREATED




#-----------COUPONS------------
coupons = [
        {"_id": 1, "code": "WELCOME10", "discount": 10},
        {"_id": 2, "code": "SPOOKY25", "discount": 25},
        {"_id": 3, "code": "VIP50", "discount": 50}
    ]


@app.route("/api/coupons", methods=["GET"])
def get_coupons():
     return jsonify({
                    "success": True,
                    "message": "Coupons retrieved successfully",
                    "data": coupons
     })

@app.route("/api/coupon/<int:_id>", methods=["GET"])
def get_one_coupon(_id):
     for coupon in coupons:
          if coupon["_id"] == _id:
               return jsonify({
                    "success": True,
                    "message": "Coupon retrieved successfully",
                    "data": coupon
     })
     return jsonify({
          "success": False,
          "message": "Coupon not found"
     }),HTTPStatus.NOT_FOUND


@app.post("/api/coupons")
def add_coupon():
     new_coupon = request.get_json()
     new_coupon["_id"] = len(coupons) + 1
     coupons.append(new_coupon)
     return jsonify ({
          "success": True,
          "message": "Coupon Successfully Added",
          "data": new_coupon
     }), HTTPStatus.CREATED


@app.route("/api/coupons/count", methods=["GET"])
def get_coupon_count():
    num_coupons = len(coupons)
    return jsonify({"coupon-count ": num_coupons})




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

