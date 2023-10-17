
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

# We have to show the Input Data for our model Input So we have to create a file which will call all the input data
import util # Importing data.py file which contains all info regardnig model and input data
util.read_data()


@app.route("/")
def home():
    return render_template('app.html')

@app.route('/City_names')  # Getting City names to populate it into the HTML select tag with help of JS
def get_city_names():
    response = jsonify({'Cities' : util.get_city_names()}) # <-- This will call and stores the city names from function inside data.py file
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route('/Property_types')
def get_property_types():
    reslt = jsonify({'Property_types': util.get_property_types()})  # <-- This will call and stores the types from function inside data.py file
    reslt.headers.add("Access-Control-Allow-Origin", "*")
    return reslt


@app.route('/reslt',methods = ['POST'])
def prediction():
    if request.method=="POST":
        Total_Area = float(request.form['Total_Area'])
        Baths = int(request.form['Bathrooms'])
        Balcony = int(request.form['Balcony'])
        BHK = float(request.form['BHK'])
        BH =  0 #float(request.form['BH'])
        RK = 0  #float(request.form['RK'])
        R = 0 #float(request.form['R'])
        City = request.form['City_names']
        Type = request.form['Property_types']

        reslt = util.prediction(Total_Area, Baths, Balcony, BHK, BH, RK, R, City, Type)
        return render_template("reslt.html",outpt=reslt)


if __name__ =="__main__":
    app.run(debug=True , port=5000)