from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

#Configure db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'fuel_system'

mysql = MySQL(app)

@app.route("/")
def hello():
    return render_template('home.html')


@app.route("/", methods=['POST'])
def Authenticate():

    username = request.form['u']
    password = request.form['p']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from Users where username='" + username +"' and password='" + password +"'")
    data = cursor.fetchone()
    if data is None:
    	return "Username or Password is Incorrect"
    else:
    	return "Logged In successfully"


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
    



if __name__ == '__main__':
  	app.run(debug=True)