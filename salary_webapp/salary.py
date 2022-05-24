#import modules
from  flask  import Flask ,render_template, request
from os  import system
import  joblib  as  jb
import  pandas  as  pd
import  numpy  as  np
from  sklearn.linear_model  import  LinearRegression

app=Flask("myml_app")
@app.route("/")
def home():
    return render_template("model.html")
@app.route("/salary", methods=["GET"])
def model():
    exp_data=request.args.get("x")

    #filter dat
    data = pd.read_csv("Salary_Data.csv")
    #print(data.head(5))
    #print(data.shape)
    X = data["YearsExperience"]
    y = data["Salary"]
    X = X.values.reshape(30,1)
    #model creatio
    mind = LinearRegression() 
    mind.fit(X, y)
    #while True:
        #print("-------------------------------------------------------------------------------------")
        #print("\t\t\t *********Salary Predictor Program********* ")
        #exp = float(input("\nEnter your Experience:  "))
    
    exp=float(exp_data)
    a=mind.predict( [[ exp ]] )
    
    jb.dump( mind, "salary.pkl")
    a=str(a)        
    return a
app.run(debug=True,port="1231")

