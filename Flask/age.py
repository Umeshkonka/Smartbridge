from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__) #your application
rfr=pickle.load(open('age.pkl','rb'))


@app.route('/') # default route
def home():
    return render_template("age.html")


@app.route('/predict',methods=['post'])
def predict():
    Sex=float(request.form['Sex'])
    Length=float(request.form['Length'])
    Diameter=float(request.form['Diameter'])
    Height=float(request.form['Height'])
    Whole_weight=float(request.form['Whole Weight'])
    Shucked_weight=float(request.form['Shucked Weight'])
    Viscera_weight=float(request.form['Viscera Weight'])
    Shell_weight=float(request.form['Shell Weight'])
    #Rings=float(request.form['Rings'])
    
    print(Sex,Length,Diameter,Height,Whole_weight,Shucked_weight,Viscera_weight,Shell_weight)
    a=np.array([[Sex,Length,Diameter,Height,Whole_weight,Shucked_weight,Viscera_weight,Shell_weight]])
    
    result=rfr.predict(a)
    x=result
    return render_template('age.html',x='Abalone age is {} '.format(*x))

if __name__ == '__main__':
    app.run(port=8000) # you are running your app