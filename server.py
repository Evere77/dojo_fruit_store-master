from flask import Flask, render_template, request, redirect

app = Flask(__name__)  

@app.route('/')         
def index():
    print(request.form)
    
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    student_id = request.form["student_id"]
    strawberry = request.form["strawberry"]
    raspberry = request.form["raspberry"]
    apple = request.form["apple"]
    blackberry = request.form["blackberry"]
    total_count = int(strawberry) + int(raspberry) + int(apple) + int(blackberry)
    print(f"Charging {first_name} {last_name} for {total_count} fruits.")
    return render_template("checkout.html", first_name=first_name, last_name=last_name, student_id=student_id, strawberry=strawberry, raspberry=raspberry, apple=apple, blackberry=blackberry, total_count=total_count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    