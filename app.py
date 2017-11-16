from flask import Flask,render_template,request,redirect
import csv

app=Flask("__name__")

a = 0

@app.route("/",methods=['POST','GET'])
def goto():
    return render_template("form.html")

@app.route("/submit",methods=['POST','GET'])
def submit():
    global a
    a = a + 1
    row = list()
    
#    return redirect("https://thunderrlogistics.com/index1.html")
#    fname = request.form["first_name"]
#    lname = request.form["last_name"]
#    email = request.form["email"]
#
#    pno = request.form["phone"]
#    add = request.form["address"]
#    zipc = request.form["zip"]
#    age = request.form["age"]
#    bg = request.form["Bloodg"]
#    fullt = request.form["full-time"]
#    emp = request.form["employed-y"]
#    lisc = request.form["license-y"]
#    bnk = request.form["bank-y"]
#    cmp = request.form["comp-y"]
#    smtph = request.form["smartphone-y"]
#    sal = request.form["Salary"]
#    lang = request.form["languages"]
    row=[   a,  request.form["first_name"]
    , request.form["last_name"]
    , request.form["email"]
    , request.form["phone"]
    , request.form["address"]
    , request.form["zip"]
    , request.form["age"]
    , request.form["Bloodg"]
    , request.form["full-time"]
    , request.form["employed-y"]
    , request.form["license-y"]
    , request.form["bank-y"]
    , request.form["comp-y"]
    , request.form["smartphone-y"]
    , request.form["Salary"]
    , request.form["languages"]
    ]
    with open("log_data.csv","w+") as f:
        writer = csv.writer(f)
        writer.writerow(row)
        
    return redirect("https://thunderrlogistics.com/index1.html")
    
    

if __name__ == "__main__":
    app.run()