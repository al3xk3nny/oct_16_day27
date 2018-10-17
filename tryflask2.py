from flask import Flask, render_template, request, redirect

app = Flask(__name__)

messages = [
        {
        "author": "Alex",
        "text": "The Best Of"
        },
        {
        "author": "Brian",
        "text": "The Worst Of"
        }
    ]

@app.route("/", methods=["GET"])
def show_index():
    return render_template("index2.html", data=messages) 
   

@app.route("/add", methods=["POST"])
def add_message():
    result = request.form["msg"]
    
    message_dict = {
        "author": "Bugs Bunny",
        "text": result
    }    
   
    messages.append(message_dict)
    return redirect("/")


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)