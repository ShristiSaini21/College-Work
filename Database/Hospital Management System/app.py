from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://shristisaini589_db_user:suhani9368@cluster0.npydojz.mongodb.net/HospitalDB?retryWrites=true&w=majority")
db = client["HospitalDB"]
medicines = db["medicines"]

@app.route("/")
def home():
    total = medicines.count_documents({})
    return render_template("index.html", total=total)

@app.route("/add", methods=["GET", "POST"])
def add_medicine():
    msg = None
    if request.method == "POST":
        med_id = int(request.form["medicine_id"])
        if medicines.find_one({"medicine_id": med_id}):
            msg = "Medicine ID already exists!"
        else:
            medicines.insert_one({
                "medicine_id": med_id,
                "name": request.form["name"],
                "category": request.form["category"],
                "price": float(request.form["price"]),
                "stock": int(request.form["stock"]),
                "manufacturer": request.form["manufacturer"]
            })
            msg = "Medicine added successfully!"
    return render_template("add_medicine.html", msg=msg)

@app.route("/medicines")
def view_medicines():
    all_meds = list(medicines.find({}, {"_id": 0}))
    return render_template("medicines.html", meds=all_meds)

@app.route("/search", methods=["GET", "POST"])
def search_medicine():
    medicine = None
    error = None
    if request.method == "POST":
        val = request.form["query"]
        query_filter = {"$or": [{"name": val}]}
        if val.isdigit():
            query_filter["$or"].append({"medicine_id": int(val)})
        medicine = medicines.find_one(query_filter, {"_id": 0})
        if not medicine:
            error = "No medicine found."
    return render_template("search_med.html", medicine=medicine, error=error)

@app.route("/update", methods=["GET", "POST"])
def update_stock():
    msg = None
    if request.method == "POST":
        mid = int(request.form["medicine_id"])
        new_stock = int(request.form["stock"])
        res = medicines.update_one({"medicine_id": mid}, {"$set": {"stock": new_stock}})
        if res.matched_count > 0:
            msg = "Stock updated successfully!"
        else:
            msg = "Medicine ID not found."
    return render_template("update_stock.html", msg=msg)

@app.route("/delete", methods=["GET", "POST"])
def delete_medicine():
    msg = None
    if request.method == "POST":
        mid = int(request.form["medicine_id"])
        res = medicines.delete_one({"medicine_id": mid})
        if res.deleted_count > 0:
            msg = "Medicine deleted successfully!"
        else:
            msg = "Medicine ID not found."
    return render_template("delete_med.html", msg=msg)

@app.route("/report")
def report():
    total_count = medicines.count_documents({})
    all_m = list(medicines.find({}, {"_id": 0}))
    total_stock = sum(m.get("stock", 0) for m in all_m)
    low_stock = [m for m in all_m if m.get("stock", 0) < 30]
    expensive = max(all_m, key=lambda x: x.get("price", 0)) if all_m else None
    cheapest = min(all_m, key=lambda x: x.get("price", 0)) if all_m else None
    return render_template("report.html", total_count=total_count, total_stock=total_stock, low_stock=low_stock, expensive=expensive, cheapest=cheapest)

if __name__ == "__main__":
    app.run(debug=True)