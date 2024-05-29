import datetime
from flask import Flask, render_template, request, redirect, url_for, session ,flash,jsonify
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt,check_password_hash
import MySQLdb.cursors
import re
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
app.secret_key = 'your secret key'
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sairam21'
app.config['MYSQL_DB'] = 'accom'
 
mysql = MySQL(app)

@app.route('/')
@app.route('/login',methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username'].upper()
        password = request.form['password'].upper()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = % s ', (username, ))
        account = cursor.fetchone()
        if account and check_password_hash(account['password'], password):
            session['loggedin'] = True
            session['username'] = account['username']
            return redirect('home')
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html',msg=msg)

@app.route('/register', methods =['GET', 'POST'])
def register():
     msg = ''
     if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'cpassword' in request.form:
        username = request.form['username'].upper()
        password = request.form['password'].upper()
        cpassword = request.form['cpassword'].upper()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = % s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Username already exists !'
        elif not re.match(r'[A-Za-z]+', username):
            msg = 'Username must contain only characters!'
        elif not username or not password or not cpassword:
            msg = 'Please fill out the form !'
        elif password != cpassword:
            msg = 'Password and Confirm Password do not match!'
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            cursor.execute('INSERT INTO users VALUES (NULL, % s, % s)', (username, hashed_password ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
            return redirect("/login")
     elif request.method == 'POST':
        msg = 'Please fill out the form !'
     return render_template('register.html', msg = msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route('/home/allotment', methods=['GET', 'POST'])
def allotment():
    clicked_link_text = "Allotment"
    id_card = request.args.get('id_card')
    if id_card is None:  # If id_card is None, initialize it with an empty string
        id_card = ""
    if request.method == 'POST':
        lead_name = request.form['leadName'].upper()
        mobile_number = request.form['mobileNumber']
        nation_code = request.form['nation_code'].upper()
        id_card = request.form['idCard']
        i_f=request.form['i_f'].upper()
        gender = request.form['gender']
        g_f_s = request.form['g_f_s']
        d_a = request.form['d_a']
        maleno = int(request.form['maleno'])
        femaleno = int(request.form['femaleno'])
        child = int(request.form['child']) 
        total = maleno + femaleno + child
        room_number = request.form['roomNumber'].upper()
        from_date = request.form['fromDate']
        number_of_days = request.form['numberOfDays']
        to_date = request.form['toDate']
        amount_due = request.form['amountDue']
        amount_collected = request.form['amountCollected']
        pay_mode = request.form['payMode'].upper()
        remarks = request.form['remarks'].upper()
        bill_type = request.form['billTypeInput'].upper()

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) # To get the result as dictionary.
        cursor.execute("select * from person_master WHERE person_id = %s",(id_card,)) # Used for executing sql queries
        result = cursor.fetchone()
        if result is None:
            cursor.execute("INSERT INTO Person_Master (person_id, Name, mobile_num,gender,place_name,I_F) VALUES (%s, %s, %s, %s, %s, %s)",
                           (id_card, lead_name, mobile_number,gender,nation_code,i_f))
            mysql.connection.commit()
        else:
            if result['person_id'] == id_card:
                cursor.execute("UPDATE person_master SET mobile_num = %s WHERE person_id = %s", (mobile_number,id_card,))
                mysql.connection.commit()
                pass
            else:
                cursor.execute("INSERT INTO Person_Master (person_id, Name, mobile_num,gender,place_name,I_F) VALUES (%s, %s, %s, %s, %s, %s)",
                               (id_card, lead_name, mobile_number,gender,nation_code,i_f))
                mysql.connection.commit()
        
        cursor.execute("INSERT INTO Visit_Master (person_id,room_number, from_date, to_date, no_of_days, male_num, female_num, child_num, total, A_D, remark,I_F) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (id_card,room_number, from_date, to_date, number_of_days, maleno, femaleno, child, total, d_a, remarks,i_f))
        
        mysql.connection.commit()
        visit_num = cursor.lastrowid
        visit_id = str(i_f) + str(visit_num)

        cursor.execute("UPDATE Visit_Master SET visit_id = %s WHERE visit_num = %s", (visit_id,visit_num,))
        mysql.connection.commit()

        cursor.execute("INSERT INTO Bill_master (bill_id,room_number, G_F_S, Amt_collected, paymode,bill_type,visit_num,amt_due) VALUES (NULL,%s, %s, %s, %s, %s, %s, %s)", (room_number, g_f_s, amount_collected, pay_mode, bill_type,visit_num,amount_due))
        mysql.connection.commit()

        bill_id = cursor.lastrowid

        cursor.execute("UPDATE Visit_Master SET bill_id = %s WHERE visit_num = %s", (bill_id, visit_num))
        mysql.connection.commit()

        cursor.execute("UPDATE flat_manager SET room_occupancy = 'o', visit_num = %s WHERE room_number = %s", (visit_num, room_number))
        mysql.connection.commit()
        cursor.close()
        flash("Alloted Successfully!")
        return redirect('/home/allotment')
    
    return render_template('allotment.html',id_card=id_card,clicked_link_text=clicked_link_text)

@app.route('/home/extension', methods = ['GET', 'POST'])
def extension():
     clicked_link_text = "Extension"
     if request.method == 'POST':
         flatNoToExtend = request.form['flatNoToExtend'].upper()
         billNumber=request.form['billNumber']
         idCard=request.form['idCard'].upper()
         IF = request.form['IF'].upper()
         GFS = request.form['GFS'].upper()
         DA = request.form['DA'].upper()
         maleNumber = request.form['maleNumber']
         femaleNumber = request.form['femaleNumber']
         childrenNumber = request.form['childrenNumber']
         total = request.form['total']
         fromDate = request.form['fromDate']
         numberOfDays = request.form['numberOfDays']
         toDate = request.form['toDate']
         amountDue = request.form['amountDue']
         amountCollected = request.form['amountCollected']
         payMode=request.form['payMode'].upper()
         billTypeInput=request.form['billTypeInput'].upper()

         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

         cursor.execute("UPDATE bill_Master SET closed_on = %s WHERE bill_id = %s", (fromDate,billNumber,))
         mysql.connection.commit()

         cursor.execute("UPDATE visit_Master SET vacated_date = %s WHERE bill_id = %s", (fromDate,billNumber,))
         mysql.connection.commit()

         cursor.execute("INSERT INTO visit_Master (I_F, room_number, person_id,from_date,to_date,no_of_days,male_num,female_num,child_num,total,A_D) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)", (IF, flatNoToExtend, idCard,fromDate,toDate,numberOfDays,maleNumber,femaleNumber,childrenNumber,total,DA))
         mysql.connection.commit()

         visit_num = cursor.lastrowid

        # Now you can concatenate i_f and visit_num to form visit_id
         visit_id = str(IF) + str(visit_num)

        # Update the record with the generated visit_id
         cursor.execute("UPDATE Visit_Master SET visit_id = %s WHERE visit_num = %s", (visit_id,visit_num,))
         mysql.connection.commit()
        # Inserting data into Bill_master
         cursor.execute("INSERT INTO Bill_master (bill_id,room_number, G_F_S, Amt_collected, paymode,bill_type,visit_num,amt_due) VALUES (NULL,%s, %s, %s, %s, %s, %s,%s)", (flatNoToExtend, GFS, amountCollected, payMode, billTypeInput,visit_num,amountDue))
         mysql.connection.commit()

         bill_id = cursor.lastrowid

        # Update the visit_master table with the generated bill_id
         cursor.execute("UPDATE Visit_Master SET bill_id = %s WHERE visit_num = %s", (bill_id, visit_num))
         mysql.connection.commit()
         
         cursor.execute("UPDATE flat_manager SET room_occupancy = 'o', visit_num = %s WHERE room_number = %s", (visit_num,flatNoToExtend))
         mysql.connection.commit()
         cursor.close()
         
         flash("Extended Successfully!")
         return redirect('/home/extension')
         
     return render_template('extension.html', clicked_link_text=clicked_link_text)

@app.route('/home/modifybill', methods = ['GET', 'POST'])
def modifybill():
    clicked_link_text = "ModifyBill"
    if request.method == 'POST':
        bill_number = request.form.get('billNumber')
        name = request.form.get('name').upper()
        nation_state = request.form.get('nationState').upper()
        i_f = request.form.get('iF').upper()
        gender = request.form.get('gender').upper()
        gfs = request.form.get('gFS').upper()
        da = request.form.get('dA').upper()
        male_number = request.form.get('maleNumber')
        female_number = request.form.get('femaleNumber')
        children_number = request.form.get('childrenNumber')
        total = request.form.get('total')
        room_number = request.form.get('roomNumber').upper()
        from_date = request.form.get('fromDate')
        number_of_days = request.form.get('numberOfDays')
        to_date = request.form.get('toDate')
        amount_due = request.form.get('amountDue')
        amount_collected = request.form.get('amountCollected')
        paymode = request.form.get('paymode').upper()
        remarks = request.form.get('remarks').upper()
        mobile_number = request.form.get('mobileNumber')
        id_card = request.form.get('idCard').upper()
        bill_type = request.form.get('billType')

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("update Person_Master set Name=%s ,mobile_num=%s,gender=%s,place_name=%s,I_F=%s where person_id=%s", (name, mobile_number,gender,nation_state,i_f,id_card))
        mysql.connection.commit()

        # Inserting data into Visit_Master
        cursor.execute("update visit_Master set room_number=%s ,from_date=%s,to_date=%s,no_of_days=%s,male_num=%s,female_num=%s,child_num=%s,total=%s,A_D=%s,I_F=%s where bill_id=%s", (room_number, from_date,to_date,number_of_days,male_number,female_number,children_number,total,da,i_f,bill_number))
        mysql.connection.commit()

        cursor.execute("update bill_master set room_number=%s, G_F_S=%s, Amt_collected=%s, paymode=%s,bill_type=%s,amt_due=%s,remark=%s where bill_id=%s", (room_number, gfs, amount_collected, paymode, bill_type,amount_due,remarks,bill_number))
        mysql.connection.commit()
        cursor.close()

        flash("Bill Modified Successfully!")
        return redirect('/home/modifybill')
    
    return render_template('modifybill.html', clicked_link_text=clicked_link_text)

@app.route('/home/shift', methods = ['GET','POST'])
def shift():
    clicked_link_text = "Shifting"
    if request.method =='POST':
        bill_number = request.form.get('billNumber')
        name = request.form.get('name').upper()
        nation_state = request.form.get('nationState').upper()
        i_f = request.form.get('iF').upper()
        gender = request.form.get('gender').upper()
        gfs = request.form.get('gFS').upper()
        da = request.form.get('dA').upper()
        male_number = request.form.get('maleNumber')
        female_number = request.form.get('femaleNumber')
        children_number = request.form.get('childrenNumber')
        total = request.form.get('total')
        room_number = request.form.get('roomNumber').upper()
        room_tariff = request.form.get('roomTariff')
        from_date = request.form.get('fromDate')
        number_of_days = request.form.get('numberOfDays')
        to_date = request.form.get('toDate')
        amount_due = request.form.get('amountDue')
        amount_collected = request.form.get('amountCollected')
        paymode = request.form.get('paymode').upper()
        remarks = request.form.get('remarks').upper()
        mobile_number = request.form.get('mobileNumber')
        id_card = request.form.get('idCard').upper()
        bill_type = request.form.get('billType').upper()

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute("select visit_num from visit_master where bill_id=%s",(bill_number,))
        visits = cursor.fetchone()['visit_num']

        cursor.execute("UPDATE flat_manager SET room_occupancy = 'v',visit_num = NULL where visit_num = %s", (visits,))
        mysql.connection.commit()

        cursor.execute("UPDATE bill_Master SET closed_on = %s WHERE bill_id = %s", (from_date,bill_number,))
        mysql.connection.commit()

        cursor.execute("UPDATE visit_Master SET vacated_date = %s WHERE bill_id = %s", (from_date,bill_number,))
        mysql.connection.commit()

        cursor.execute("INSERT INTO visit_Master (I_F, room_number, person_id,from_date,to_date,no_of_days,male_num,female_num,child_num,total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)", (i_f, room_number, id_card,from_date,to_date,number_of_days,male_number,female_number,children_number,total))
        mysql.connection.commit()

        visit_num = cursor.lastrowid

        # Now you can concatenate i_f and visit_num to form visit_id
        visit_id = str(i_f) + str(visit_num)

        # Update the record with the generated visit_id
        cursor.execute("UPDATE Visit_Master SET visit_id = %s WHERE visit_num = %s", (visit_id,visit_num,))
        mysql.connection.commit()
        # Inserting data into Bill_master
        cursor.execute("INSERT INTO Bill_master (bill_id,room_number, G_F_S, Amt_collected, paymode,bill_type,visit_num,amt_due,remark) VALUES (NULL,%s, %s, %s, %s, %s, %s,%s,%s)", (room_number, gfs, amount_collected, paymode, bill_type,visit_num,amount_due,remarks))
        mysql.connection.commit()

        bill_id = cursor.lastrowid

        # Update the visit_master table with the generated bill_id
        cursor.execute("UPDATE Visit_Master SET bill_id = %s WHERE visit_num = %s", (bill_id, visit_num))
        mysql.connection.commit()

        

        cursor.execute("UPDATE flat_manager SET room_occupancy = 'o', visit_num = %s WHERE room_number = %s", (visit_num,room_number))
        mysql.connection.commit()
        cursor.close()

        flash("Room is shifted successfully!")

        return redirect('/home/shift')
    return render_template('shift.html', clicked_link_text=clicked_link_text)

@app.route('/home/vacation', methods = ['GET', 'POST'])
def vacation():
    clicked_link_text = "Vacation"
    if request.method == 'POST':
        room_number = request.form['roomNumber']
        bill_number = request.form['billNumber']
        date_of_vacation = request.form['dateOfVacation']
        remarks = request.form['remarks']
        print(bill_number)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #for flat_manager
        cursor.execute("UPDATE flat_manager SET room_occupancy = 'v', visit_num = NULL WHERE room_number = %s", (room_number,))
        mysql.connection.commit()
        #for bill_master
        cursor.execute("UPDATE bill_master SET closed_on = %s WHERE bill_id = %s", (date_of_vacation,bill_number))
        mysql.connection.commit()
        #for visit_master 
        cursor.execute("UPDATE visit_master SET vacated_date = %s WHERE bill_id = %s", (date_of_vacation,bill_number))
        mysql.connection.commit()


        mysql.connection.commit()

        cursor.close()

        flash("Vacated successfully and recorded")
        return redirect('/home/vacation')
    
    return render_template('vacation.html', clicked_link_text=clicked_link_text)

@app.route('/home/guestdiary',methods=[ 'GET','POST' ])
def guestdiary():
    clicked_link_text = "GuestDairy"
    if request.method == 'POST':
        guest_name = request.form['guestname'].upper()
        name_of_dept = request.form['name_of_dept']
        onpayment = request.form['onpayment']
        dateofissue = request.form['dateofissue']
        roomNumber = request.form['roomNumber'].upper()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("INSERT INTO guest_diary (name, department, on_payment, from_date, room_number) VALUES (%s, %s, %s, %s, %s)",
                           (guest_name, name_of_dept, onpayment, dateofissue, roomNumber))
        cursor.execute("UPDATE flat_manager SET room_occupancy= %s WHERE room_number = %s", ('o', roomNumber))
        mysql.connection.commit()
        cursor.close()
        
        flash("Guest entered Successfully!")
        return redirect('/home/guestdiary')
    
    return render_template('guestdiary.html', clicked_link_text=clicked_link_text)
    
@app.route('/home/overseas', methods=['GET', 'POST'])
def overseas():
    clicked_link_text = "Overseas Registration"
    if request.method == 'POST':
        passport_nos = request.form.getlist('passport_no')
        names = request.form.getlist('name')
        nation_codes = request.form.getlist('nation_code')
        genders = request.form.getlist('gender')
        dobs = request.form.getlist('dob')
        visa_numbers = request.form.getlist('visa_number')
        visa_expiry_dates = request.form.getlist('visa_expiry')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        for i in range(len(passport_nos)):
            cursor.execute("INSERT INTO person_master (person_id,name,gender,dob,place_name,I_F,visa_number,visa_expiry) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                           (passport_nos[i],names[i], genders[i], dobs[i], nation_codes[i],'F', visa_numbers[i],visa_expiry_dates[i]))
            mysql.connection.commit()
            cursor.execute("SELECT visit_num FROM visit_master ORDER BY visit_num DESC LIMIT 1")
            last_visit_num = cursor.fetchone()['visit_num']
            cursor.execute("INSERT INTO person_visit (person_id,visit_num) VALUES (%s, %s)",
                           (passport_nos[i],last_visit_num))
            mysql.connection.commit()
        return redirect(url_for('allotment',id_card=passport_nos[0]))
    return render_template('overseas.html', clicked_link_text=clicked_link_text)

@app.get( '/room_tariff/<string:roomNumber>/<string:d_a>')
def allotment_room_tarrif(roomNumber:str, d_a:str):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT room_occupancy FROM flat_manager WHERE room_number = %s"
    cursor.execute(query, (roomNumber,))
    result = cursor.fetchone()
    if result ['room_occupancy'] == 'o' or result['room_occupancy'] == 'g':
        query_occupied = """SELECT pm.Name, vm.to_date FROM Person_Master pm JOIN Visit_Master vm ON pm.person_id = vm.person_id JOIN 
                            Bill_master bm ON vm.Visit_num = bm.Visit_num WHERE bm.Room_number = %s"""
        cursor.execute(query_occupied, (roomNumber,))
        occupant_details = cursor.fetchone()
        return {
            'status': False,
            'message': 'Occupied',
            'occupant_details': occupant_details
        }
    if d_a  == 'A':
        query_allotee="""SELECT tm.allottee_tariff FROM Flat_Master fm JOIN Tariff_Master tm ON fm.Category_id = tm.Category_id
                         WHERE fm.room_number = %s"""
        cursor.execute(query_allotee, (roomNumber,))
        result = cursor.fetchone()
        if result:
            room_tariff = result['allottee_tariff']
        else:
            room_tariff = None
        return  {"status":True,"Tariff":room_tariff}
    elif d_a=='D':
        query_donor="""SELECT tm.donor_tariff FROM Flat_Master fm JOIN Tariff_Master tm ON fm.Category_id = tm.Category_id 
                    WHERE fm.room_number = %s"""
        cursor.execute(query_donor, (roomNumber,))
        result = cursor.fetchone()
        if result:
            room_tariff = result['donor_tariff']
        else:
            room_tariff = None
        return  {"status":True,"Tariff":room_tariff}
    elif d_a == "None":
        query = "SELECT tm.tariff FROM Flat_Master fm JOIN Tariff_Master tm ON fm.Category_id = tm.Category_id WHERE fm.room_number = %s"
        cursor.execute(query, (roomNumber,))
        result = cursor.fetchone()
        if result:
            room_tariff = result['tariff']
        else:
            room_tariff = None    
        return  {"status":True,"Tariff":room_tariff}

# this code is to make full form of the entered code and if wrong it will make alert and if correct it will display i_F
@app.get('/nation_code/<string:nation_code>')
def allotment_nation_code(nation_code: str):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM country_state WHERE code = %s"
    cursor.execute(query, (nation_code,))
    result = cursor.fetchone()
    
    if result:
        place = result['place_name']
        category = result["I_F"]
        return {"status":True,"Place": place, "Category": category}
    else:
        query_starting_with_letter = "SELECT code, place_name FROM country_state WHERE code LIKE %s"
        cursor.execute(query_starting_with_letter, (nation_code[0] + "%",))
        available_codes = cursor.fetchall()
        return jsonify({"status": False, 'Message': 'Invalid Nation Code', 'Available_Codes': available_codes})

@app.get('/allotment_id/<string:idCard>')
def allotment_id(idCard: str):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT * FROM person_master WHERE person_id = %s"
    cursor.execute(query, (idCard,))
    result = cursor.fetchone()
    return result

@app.get( '/extension_room/<string:roomNumber>')
def extension_room(roomNumber:str):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT room_occupancy FROM flat_manager WHERE room_number = %s"
    cursor.execute(query, (roomNumber,))
    result = cursor.fetchone()
    if result ['room_occupancy'] == 'o' or result['room_occupancy'] == 'g':
        query = """SELECT bm.bill_id,pm.name,vm.person_id,pm.place_name,pm.gender,bm.G_F_S,vm.A_D,vm.male_num,vm.female_num,vm.child_num,
                vm.total,vm.I_F,bm.bill_type
                FROM visit_master vm
                JOIN person_master pm ON vm.person_id = pm.person_id
                JOIN bill_master bm ON vm.visit_num = bm.visit_num
                WHERE bm.room_number = %s
                ORDER BY bm.bill_id DESC
                LIMIT 1"""
        cursor.execute(query, (roomNumber,))
        result = cursor.fetchone()
        return {'status':True , 'result' : result }
    else:
        return{'status': False}

@app.get( '/extension_bill/<bill_id>')
def extension_room_bill(bill_id:int):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT closed_on FROM bill_master WHERE bill_id = %s"
    cursor.execute(query, (bill_id,))
    result = cursor.fetchone()
    if result ['closed_on'] is None:
        query = """select bill_master.room_number,name,visit_master.person_id,visit_master.I_F,person_master.place_name,
          person_master.gender, bill_master.G_F_S ,visit_master.A_D , visit_master.male_num, visit_master.female_num,
            visit_master.child_num,visit_master.total,bill_master.bill_type
            from visit_master
            join person_master ON visit_master.person_id = person_master.person_id
            join bill_master  on visit_master.visit_num = bill_master.visit_num
            where bill_master.bill_id = %s"""
        cursor.execute(query, (bill_id,))
        result = cursor.fetchone()
        return {'status':True , 'result' : result }
    else:
        return{'status': False}

@app.get( '/extension_room_tariff/<string:flatNoToExtend>/<string:DA>')
def extension_room_tarrif_ad(flatNoToExtend:str, DA:str):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT room_occupancy FROM flat_manager WHERE room_number = %s"
    cursor.execute(query, (flatNoToExtend,))
    result = cursor.fetchone()
    if DA  == 'A':
        query_allotee="""SELECT tm.allottee_tariff FROM Flat_Master fm JOIN Tariff_Master tm ON fm.Category_id = tm.Category_id
                         WHERE fm.room_number = %s"""
        cursor.execute(query_allotee, (flatNoToExtend,))
        result = cursor.fetchone()
        if result:
            room_tariff = result['allottee_tariff']
        else:
            room_tariff = None
        return  {"status":True,"Tariff":room_tariff}
    elif DA=='D':
        query_donor="""SELECT tm.donor_tariff FROM Flat_Master fm JOIN Tariff_Master tm ON fm.Category_id = tm.Category_id 
                    WHERE fm.room_number = %s"""
        cursor.execute(query_donor, (flatNoToExtend,))
        result = cursor.fetchone()
        if result:
            room_tariff = result['donor_tariff']
        else:
            room_tariff = None
        return  {"status":True,"Tariff":room_tariff}
    elif DA == "None":
        query = "SELECT tm.tariff FROM Flat_Master fm JOIN Tariff_Master tm ON fm.Category_id = tm.Category_id WHERE fm.room_number = %s"
        cursor.execute(query, (flatNoToExtend,))
        result = cursor.fetchone()
        if result:
            room_tariff = result['tariff']
        else:
            room_tariff = None    
        return  {"status":True,"Tariff":room_tariff}

@app.get( '/modify_bill/<bill_id>')
def modify_bill(bill_id:int):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT closed_on FROM bill_master WHERE bill_id = %s"
    cursor.execute(query, (bill_id,))
    result = cursor.fetchone()
    if result ['closed_on'] is None:
        query = """select bill_master.room_number, name,visit_master.person_id,visit_master.I_F,person_master.place_name,
          person_master.gender, bill_master.G_F_S ,visit_master.A_D , visit_master.male_num, visit_master.female_num, 
          visit_master.child_num,visit_master.total,bill_master.bill_type,person_master.mobile_num,visit_master.from_date,
          visit_master.to_date,visit_master.no_of_days,bill_master.amt_collected,bill_master.amt_due
        from visit_master
        join person_master ON visit_master.person_id = person_master.person_id
        join bill_master  on visit_master.visit_num = bill_master.visit_num
        where bill_master.bill_id = %s"""
        cursor.execute(query, (bill_id,))
        result = cursor.fetchone()
        result['from_date'] = str(result['from_date'])
        result['to_date'] = str(result['to_date'])
        return { 'status': True,'result': result }
    else:
        return{'status': False}

@app.get( '/shifting_room/<string:roomNumber>/<string:dA>')
def shifting_room(roomNumber:str,dA:str):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT room_occupancy from flat_manager where room_number=%s"
    cursor.execute(query, (roomNumber,))
    result = cursor.fetchone()
    if result['room_occupancy'] == 'o':
        message="Room occupied"
        return { 'status': False,'message':message }
    if dA  == 'A':
        query_allotee="""SELECT tm.allottee_tariff FROM Flat_Master fm JOIN Tariff_Master tm ON fm.Category_id = tm.Category_id
                         WHERE fm.room_number = %s"""
        cursor.execute(query_allotee, (roomNumber,))
        result = cursor.fetchone()
        if result:
            room_tariff = result['allottee_tariff']
        else:
            room_tariff = None
        return  {"status":True,"Tariff":room_tariff}
    elif dA=='D':
        query_donor="""SELECT tm.donor_tariff FROM Flat_Master fm JOIN Tariff_Master tm ON fm.Category_id = tm.Category_id 
                    WHERE fm.room_number = %s"""
        cursor.execute(query_donor, (roomNumber,))
        result = cursor.fetchone()
        if result:
            room_tariff = result['donor_tariff']
        else:
            room_tariff = None
        return  {"status":True,"Tariff":room_tariff}
    elif dA == "None":
        query = "SELECT tm.tariff FROM Flat_Master fm JOIN Tariff_Master tm ON fm.Category_id = tm.Category_id WHERE fm.room_number = %s"
        cursor.execute(query, (roomNumber,))
        result = cursor.fetchone()
        if result:
            room_tariff = result['tariff']
        else:
            room_tariff = None    
        return  {"status":True,"Tariff":room_tariff}
@app.get( '/vacation_room/<string:roomNumber>')
def vacation_room(roomNumber:str):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT room_occupancy from flat_manager where room_number=%s"
    cursor.execute(query, (roomNumber,))
    result = cursor.fetchone()
    if result['room_occupancy'] == 'o' or result['room_occupancy'] == 'g':
        query = "select bill_id from bill_master where room_number=%s ORDER BY bill_id DESC LIMIT 1 "
        cursor.execute(query, (roomNumber,))
        result = cursor.fetchone()
        return {'status':True ,'result':result}
    else:
        return{'status':False}

@app.get( '/vacation_bill/<billNumber>')
def vacation_room_bill(billNumber:int):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT closed_on FROM bill_master WHERE bill_id = %s"
    cursor.execute(query, (billNumber,))
    result = cursor.fetchone()
    if result ['closed_on'] is None:
        query = "select room_number from bill_master where bill_id=%s"
        cursor.execute(query, (billNumber,))
        result = cursor.fetchone()
        return { 'status': True,'result': result }
    else:
        result['closed_on'] = str(result['closed_on'])
        closed=result['closed_on']
        return{'status': False,'closed':closed}

@app.get( '/guest_diary/<string:roomNumber>')
def guest_diary(roomNumber:str):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT room_occupancy from flat_manager where room_number=%s"
    cursor.execute(query, (roomNumber,))
    result = cursor.fetchone()
    if result['room_occupancy'] == 'o':
        message="Room occupied"
        return { 'status': False,'message':message }
    
@app.route('/get_amt_collected/<string:Acc_Date_Input>')
def get_amt_collected(Acc_Date_Input:str):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT SUM(bm.amt_collected) AS amt_collected FROM Visit_Master vm JOIN Bill_Master bm ON vm.visit_num = bm.visit_num WHERE vm.from_date = %s"
    cursor.execute(query,(Acc_Date_Input,) )
    result = cursor.fetchone()
    if result['amt_collected'] is None:
        amt_collected= 0
        return {'status':False, 'result': amt_collected}
    else:
        amt_collected=result['amt_collected']
        return {'status':True,'result': amt_collected}

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)