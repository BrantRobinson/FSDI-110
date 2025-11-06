from flask import Flask, jsonify, request
from flask_cors import CORS
from http import HTTPStatus

app = Flask(__name__) # instance of FLask
CORS(app, origins=["http://localhost:5173", "http://localhost:5174", "https://mayapp.com"])


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

# ------------PRODUCTS------------

products = [
     {
          "_id": 1,
          "title": "Nintendo Switch",
          "price": 29999,
          "category": "electronics",
          "image": "https://picsum.photos/seed/1/300/300"
     },
     {
          "_id": 2,
          "title": "Smart Refrigerator",
          "price": 99999,
          "category": "kitchen",
          "image": "https://picsum.photos/seed/2/300/300"
     },
     {
          "_id": 3,
          "title": "BLuetooth Speaker",
          "price": 7999,
          "category": "electronics",
          "image": "https://picsum.photos/seed/3/300/300"
     }
]



@app.get("/api/products")
def get_products():
     return jsonify({
          "success": True,
          "message": "Products retrieved successfully",
          "data": products
     }), HTTPStatus.OK # 200 - it would do this without this code, but we are overriding to always return code 200


@app.get("/api/products/<int:product_id>")
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

@app.delete("/api/products/<int:id>")
def delete_product(id):
     for index, product in enumerate(products):
          if product["_id"] == id:
               products.pop(index)
               return jsonify ({
                    "success": True,
                    "message": "Product Successfully Deleted",
                    "data": product
               }),HTTPStatus.OK
     return jsonify ({
          "success": False,
          "message": "Product not found",
          "data": product
          }),HTTPStatus.NOT_FOUND

@app.put("/api/products/<int:product_id>")
def update_product(product_id):
     data = request.get_json()
     for product in products:
          if product["_id"] == product_id:
               if "title" in data: #experimenting to see if i can keep the title and other paramenters the same if they aren't passed in the json
                    product["title"] = data["title"]
               if "price" in data:
                    product["price"] = data["price"]
               if "category" in data:
                    product["category"] = data["category"]
               if "image" in data:
                    product["image"] = data["image"]
               return jsonify ({
                    "success": True,
                    "message": "Product Updated Successfully",
                    "data": product
               }),HTTPStatus.OK
     return jsonify({
          "success": False,
          "message": "Product not found!"
     }),HTTPStatus.NOT_FOUND

#-----------COUPONS------------
coupons = [
        {"_id": 1, "code": "WELCOME10", "discount": 10},
        {"_id": 2, "code": "SPOOKY25", "discount": 25},
        {"_id": 3, "code": "VIP50", "discount": 50}
    ]


@app.get("/api/coupons")
def get_coupons():
     return jsonify({
                    "success": True,
                    "message": "Coupons retrieved successfully",
                    "data": coupons
     })


@app.get("/api/coupon/<int:_id>")
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

@app.put("/api/coupons/<int:coupon_id>")
def update_coupon(coupon_id):
     data = request.get_json()
     for coupon in coupons:
          if coupon["_id"] == coupon_id:
               coupon["code"] = data["code"]
               coupon["discount"] = data["discount"]
               return jsonify ({
                    "success": True,
                    "message": "Coupon Updated Successfully",
                    "data": coupon
               }),HTTPStatus.OK
     return jsonify({
          "success": False,
          "message": "Coupon not found!"
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
    return jsonify({
          "success": True,
          "message": "Number of Coupons retrieved successfully",
          "data": num_coupons
     })

@app.delete("/api/coupons/<int:id>")
def delete_coupon(id):
     for index, coupon in enumerate(coupons):
          if coupon["_id"] == id:
               coupons.pop(index)
               return jsonify ({
                    "success": True,
                    "message": "Coupon Successfully Deleted",
                    "data": coupon
               }),HTTPStatus.OK
     return jsonify ({
          "success": False,
          "message": "Coupon not found",
          "data": coupon
          }),HTTPStatus.NOT_FOUND


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

