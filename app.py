from flask import Flask, redirect, render_template, request, url_for
from db import Database

db = Database()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')
   # return "<p>Hello to World!</p>"

@app.route("/ME-DEPT", methods=['GET', 'POST'])
def AddStuReg():
    if request.method=='POST':
        stu_roll=request.form['stu_roll']
        stu_name=request.form['stu_name']
        semester=request.form['semester']
        gender=request.form['gender']
        dob=request.form['dob']
        phone=request.form['phone']
        stu_email=request.form['stu_email']
        stu_addrs=request.form['stu_addrs']
        db.insert_me_reg(stu_roll, stu_name, semester, gender, dob, phone, stu_email,stu_addrs)
        return redirect("/ME-DEPT")
    # print(allTodo)
    allReg=db.fetch_all_me_reg()
    return render_template('me_reg.html',allReg=allReg) 


@app.route("/update-MEReg/<int:stu_roll>", methods=['GET', 'POST'])
def updateMEReg(stu_roll):
    if request.method=='POST':
        stu_name=request.form['stu_name']
        semester=request.form['semester']
        gender=request.form.get('gender')
        dob=request.form['dob']
        phone=request.form['phone']
        stu_email=request.form['stu_email']
        stu_addrs=request.form['stu_addrs']
        
        db.update_me_reg(stu_roll, stu_name, semester, gender, dob, phone, stu_email, stu_addrs)
        return redirect('/ME-DEPT')
    reg_details=db.fetch_one_me_reg(stu_roll)
    return render_template('update_me_reg.html',reg_details=reg_details) 

@app.route("/delete-MEReg/<int:stu_roll>", methods=['GET', 'POST'])
def deleteMEReg(stu_roll):
    # print(allTodo)
    db.delete_me_reg(stu_roll)
    return redirect('/ME-DEPT')


    
@app.route("/EE-DEPT", methods=['GET', 'POST'])
def AddEEReg():
    if request.method=='POST':
        stu_roll=request.form['stu_roll']
        stu_name=request.form['stu_name']
        semester=request.form['semester']
        gender=request.form['gender']
        dob=request.form['dob']
        phone=request.form['phone']
        stu_email=request.form['stu_email']
        stu_addrs=request.form['stu_addrs']
        db.insert_ee_reg(stu_roll, stu_name, semester, gender, dob, phone, stu_email,stu_addrs)
        return redirect("/EE-DEPT")
    # print(allTodo)
    allReg=db.fetch_all_ee_reg()
    return render_template('ee_reg.html',allReg=allReg)


@app.route("/update-EEReg/<int:stu_roll>", methods=['GET', 'POST'])
def updateEEReg(stu_roll):
    if request.method=='POST':
        stu_name=request.form['stu_name']
        semester=request.form['semester']
        gender=request.form.get('gender')
        dob=request.form['dob']
        phone=request.form['phone']
        stu_email=request.form['stu_email']
        stu_addrs=request.form['stu_addrs']
        
        db.update_ee_reg(stu_roll, stu_name, semester, gender, dob, phone, stu_email, stu_addrs)
        return redirect('/EE-DEPT')
    reg_EE_details=db.fetch_one_ee_reg(stu_roll)
    return render_template('update_ee_reg.html',reg_EE_details=reg_EE_details) 

@app.route("/delete-EEReg/<int:stu_roll>", methods=['GET', 'POST'])
def deleteEEReg(stu_roll):
    # print(allTodo)
    db.delete_ee_reg(stu_roll)
    return redirect('/EE-DEPT')
        

@app.route("/CSE-DEPT", methods=['GET', 'POST'])
def AddCSEReg():
    if request.method=='POST':
        stu_roll=request.form['stu_roll']
        stu_name=request.form['stu_name']
        semester=request.form['semester']
        gender=request.form['gender']
        dob=request.form['dob']
        phone=request.form['phone']
        stu_email=request.form['stu_email']
        stu_addrs=request.form['stu_addrs']
        db.insert_cse_reg(stu_roll, stu_name, semester, gender, dob, phone, stu_email,stu_addrs)
        return redirect("/CSE-DEPT")
    # print(allTodo)
    allReg=db.fetch_all_cse_reg()
    return render_template('cse_reg.html',allReg=allReg)


@app.route("/update-CSEReg/<int:stu_roll>", methods=['GET', 'POST'])
def updateCSEReg(stu_roll):
    if request.method=='POST':
        stu_name=request.form['stu_name']
        semester=request.form['semester']
        gender=request.form.get('gender')
        dob=request.form['dob']
        phone=request.form['phone']
        stu_email=request.form['stu_email']
        stu_addrs=request.form['stu_addrs']
        
        db.update_cse_reg(stu_roll, stu_name, semester, gender, dob, phone, stu_email, stu_addrs)
        return redirect('/CSE-DEPT')
    reg_details=db.fetch_one_cse_reg(stu_roll)
    return render_template('update_cse_reg.html',reg_details=reg_details) 

@app.route("/delete-CSEReg/<int:stu_roll>", methods=['GET', 'POST'])
def deleteCSEReg(stu_roll):
    # print(allTodo)
    db.delete_cse_reg(stu_roll)
    return redirect('/CSE-DEPT')    
  
@app.route("/CIVIL-DEPT", methods=['GET', 'POST'])
def AddCIVILReg():
    if request.method=='POST':
        stu_roll=request.form['stu_roll']
        stu_name=request.form['stu_name']
        semester=request.form['semester']
        gender=request.form['gender']
        dob=request.form['dob']
        phone=request.form['phone']
        stu_email=request.form['stu_email']
        stu_addrs=request.form['stu_addrs']
        db.insert_civil_reg(stu_roll, stu_name, semester, gender, dob, phone, stu_email,stu_addrs)
        return redirect("/CIVIL-DEPT")
    # print(allTodo)
    allReg=db.fetch_all_civil_reg()
    return render_template('civil_reg.html',allReg=allReg)

@app.route("/update-CIVILReg/<int:stu_roll>", methods=['GET', 'POST'])
def updateCIVILReg(stu_roll):
    if request.method=='POST':
        stu_name=request.form['stu_name']
        semester=request.form['semester']
        gender=request.form.get('gender')
        dob=request.form['dob']
        phone=request.form['phone']
        stu_email=request.form['stu_email']
        stu_addrs=request.form['stu_addrs']
        
        db.update_civil_reg(stu_roll, stu_name, semester, gender, dob, phone, stu_email, stu_addrs)
        return redirect('/CIVIL-DEPT')
    reg_details=db.fetch_one_civil_reg(stu_roll)
    return render_template('update_civil_reg.html',reg_details=reg_details) 

@app.route("/delete-CIVILReg/<int:stu_roll>", methods=['GET', 'POST'])
def deleteCIVILReg(stu_roll):
    # print(allTodo)
    db.delete_civil_reg(stu_roll)
    return redirect('/CIVIL-DEPT')  


@app.route("/MTECH-DEPT", methods=['GET', 'POST'])
def AddMTECHReg():
    if request.method=='POST':
        stu_roll=request.form['stu_roll']
        stu_name=request.form['stu_name']
        semester=request.form['semester']
        gender=request.form['gender']
        dob=request.form['dob']
        phone=request.form['phone']
        stu_email=request.form['stu_email']
        stu_addrs=request.form['stu_addrs']
        db.insert_mtech_reg(stu_roll, stu_name, semester, gender, dob, phone, stu_email,stu_addrs)
        return redirect("/MTECH-DEPT")
    # print(allTodo)
    allReg=db.fetch_all_mtech_reg()
    return render_template('mtech_reg.html',allReg=allReg)

@app.route("/update-MTECHReg/<int:stu_roll>", methods=['GET', 'POST'])
def updateMTECHReg(stu_roll):
    if request.method=='POST':
        stu_name=request.form['stu_name']
        semester=request.form['semester']
        gender=request.form.get('gender')
        dob=request.form['dob']
        phone=request.form['phone']
        stu_email=request.form['stu_email']
        stu_addrs=request.form['stu_addrs']
        
        db.update_mtech_reg(stu_roll, stu_name, semester, gender, dob, phone, stu_email, stu_addrs)
        return redirect('/MTECH-DEPT')
    reg_details=db.fetch_one_mtech_reg(stu_roll)
    return render_template('update_mtech_reg.html',reg_details=reg_details) 

@app.route("/delete-MTECHReg/<int:stu_roll>", methods=['GET', 'POST'])
def deleteMTECHReg(stu_roll):
    # print(allTodo)
    db.delete_mtech_reg(stu_roll)
    return redirect('/MTECH-DEPT')     

@app.route("/MCA-DEPT", methods=['GET', 'POST'])
def AddMCAReg():
    if request.method=='POST':
        stu_roll=request.form['stu_roll']
        stu_name=request.form['stu_name']
        semester=request.form['semester']
        gender=request.form['gender']
        dob=request.form['dob']
        phone=request.form['phone']
        stu_email=request.form['stu_email']
        stu_addrs=request.form['stu_addrs']
        db.insert_mca_reg(stu_roll, stu_name, semester, gender, dob, phone, stu_email,stu_addrs)
        return redirect("/MCA-DEPT")
    # print(allTodo)
    allReg=db.fetch_all_mca_reg()
    return render_template('mca_reg.html',allReg=allReg)

@app.route("/update-MCAReg/<int:stu_roll>", methods=['GET', 'POST'])
def updateMCAReg(stu_roll):
    if request.method=='POST':
        stu_name=request.form['stu_name']
        semester=request.form['semester']
        gender=request.form.get('gender')
        dob=request.form['dob']
        phone=request.form['phone']
        stu_email=request.form['stu_email']
        stu_addrs=request.form['stu_addrs']
        
        db.update_mca_reg(stu_roll, stu_name, semester, gender, dob, phone, stu_email, stu_addrs)
        return redirect('/MCA-DEPT')
    reg_details=db.fetch_one_mca_reg(stu_roll)
    return render_template('update_mca_reg.html',reg_details=reg_details) 

@app.route("/delete-MCAReg/<int:stu_roll>", methods=['GET', 'POST'])
def deleteMCAReg(stu_roll):
    # print(allTodo)
    db.delete_mca_reg(stu_roll)
    return redirect('/MCA-DEPT') 

@app.route("/ECE-DEPT", methods=['GET', 'POST'])
def AddECEReg():
    if request.method=='POST':
        stu_roll=request.form['stu_roll']
        stu_name=request.form['stu_name']
        semester=request.form['semester']
        gender=request.form['gender']
        dob=request.form['dob']
        phone=request.form['phone']
        stu_email=request.form['stu_email']
        stu_addrs=request.form['stu_addrs']
        db.insert_ece_reg(stu_roll, stu_name, semester, gender, dob, phone, stu_email,stu_addrs)
        return redirect("/ECE-DEPT")
    # print(allTodo)
    allReg=db.fetch_all_ece_reg()
    return render_template('ece_reg.html',allReg=allReg)

@app.route("/update-ECEReg/<int:stu_roll>", methods=['GET', 'POST'])
def updateECEReg(stu_roll):
    if request.method=='POST':
        stu_name=request.form['stu_name']
        semester=request.form['semester']
        gender=request.form.get('gender')
        dob=request.form['dob']
        phone=request.form['phone']
        stu_email=request.form['stu_email']
        stu_addrs=request.form['stu_addrs']
        
        db.update_ece_reg(stu_roll, stu_name, semester, gender, dob, phone, stu_email, stu_addrs)
        return redirect('/ECE-DEPT')
    reg_details=db.fetch_one_ece_reg(stu_roll)
    return render_template('update_ece_reg.html',reg_details=reg_details) 

@app.route("/delete-ECEReg/<int:stu_roll>", methods=['GET', 'POST'])
def deleteECEReg(stu_roll):
    # print(allTodo)
    db.delete_ece_reg(stu_roll)
    return redirect('/ECE-DEPT') 

@app.route("/CHEM-DEPT", methods=['GET', 'POST'])
def AddCHEMReg():
    if request.method=='POST':
        stu_roll=request.form['stu_roll']
        stu_name=request.form['stu_name']
        semester=request.form['semester']
        gender=request.form['gender']
        dob=request.form['dob']
        phone=request.form['phone']
        stu_email=request.form['stu_email']
        stu_addrs=request.form['stu_addrs']
        db.insert_chem_reg(stu_roll, stu_name, semester, gender, dob, phone, stu_email,stu_addrs)
        return redirect("/CHEM-DEPT")
    # print(allTodo)
    allReg=db.fetch_all_chem_reg()
    return render_template('chem_reg.html',allReg=allReg)

@app.route("/update-CHEMICALReg/<int:stu_roll>", methods=['GET', 'POST'])
def updateCHEMICALReg(stu_roll):
    if request.method=='POST':
        stu_name=request.form['stu_name']
        semester=request.form['semester']
        gender=request.form.get('gender')
        dob=request.form['dob']
        phone=request.form['phone']
        stu_email=request.form['stu_email']
        stu_addrs=request.form['stu_addrs']
        
        db.update_chem_reg(stu_roll, stu_name, semester, gender, dob, phone, stu_email, stu_addrs)
        return redirect('/CHEM-DEPT')
    reg_details=db.fetch_one_chem_reg(stu_roll)
    return render_template('update_chemical_reg.html',reg_details=reg_details) 

@app.route("/delete-CHEMICALReg/<int:stu_roll>", methods=['GET', 'POST'])
def deleteCHEMICALReg(stu_roll):
    # print(allTodo)
    db.delete_chem_reg(stu_roll)
    return redirect('/CHEM-DEPT')     


if __name__ == "__main__":
    app.run(debug=True)
