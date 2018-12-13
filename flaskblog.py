from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

#Configure db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'fuel_system'

mysql = MySQL(app)


@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/table")
def table():
	cursor = mysql.connection.cursor()
	result = cursor.execute("SELECT * from driver")
	if result > 0:
		userDetails = cursor.fetchall()
	return render_template('tables.html',userDetails=userDetails)


@app.route("/", methods=['GET','POST'])
def home():
	if request.method == 'POST':
	    username = request.form['u']
	    password = request.form['p']
	    cursor = mysql.connection.cursor()
	    cursor.execute("SELECT * from Users where username='" + username +"' and password='" + password +"'")
	    data = cursor.fetchone()
	    if data is None:
	    	return "Username or Password is Incorrect"
	    else:
	    	return redirect(url_for('index'))
	return render_template('home.html')


@app.route("/driver", methods=['GET','POST'])
def driver():
   if request.method == 'POST':
   	   # fetch form data
	   userDetails = request.form
	   name = userDetails['name']
	   designation = userDetails['designation']
	   idNum = userDetails['idNum']
	   cursor = mysql.connection.cursor()
	   cursor.execute("INSERT INTO driver(driver_name, designation, idNum) VALUES(%s, %s, %s)",(name, designation, idNum))
	   cursor.connection.commit()
	   cursor.close
	   return 'Success'
   return render_template('driver.html')


@app.route("/vehicle", methods=['GET','POST'])
def vehicle():
   if request.method == 'POST':
   	   # fetch form data
	   userDetails = request.form
	   VehicleType = userDetails['VehicleType']
	   plateNum = userDetails['plateNum']
	   maxcap = userDetails['Maxcap']
	   cursor = mysql.connection.cursor()
	   cursor.execute("INSERT INTO vehicles(VehicleType, vehicle_plate_no, max_fuel_cap) VALUES(%s, %s, %s)",(VehicleType, plateNum, maxcap))
	   cursor.connection.commit()
	   cursor.close
	   return 'Success'
   return render_template('vehicle.html')
    

@app.route("/request", methods=['GET','POST'])
def fuelrequest():
   if request.method == 'POST':
   	   # fetch form data
	   userDetails = request.form
	   name = userDetails['name']
	   plateNum = userDetails['plateNum']
	   fuelRequest = userDetails['requested_fuel']
	   cursor = mysql.connection.cursor()
	   cursor.execute("INSERT INTO fuel_request(driver_name, vehicle_plate_no, requested_fuel) VALUES(%s, %s, %s)",(name, plateNum, fuelRequest))
	   cursor.connection.commit()
	   cursor.close
	   return 'Success'
   return render_template('request.html')

if __name__ == '__main__':
  	app.run(debug=True)