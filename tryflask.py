from flask import Flask, render_template, request, redirect

app = Flask(__name__)

messages = ["Hello", "Happy birthday", "What's up?"]

people = ["John", "Paul", "George", "Ringo"]

@app.route("/", methods=["GET"])
def show_index():
    return render_template("index.html", data=messages, beatles=people) 
   
    # Render, in other words means, open "index.html" read it and return it, but while you're doing that, consider data, "messages". # Also, word "data" is not reserves. It could be anything (i.e. more typically, messages - see for loop in index.html, could read; for message in messages).

# Realated to "action" in form on "index.html".
@app.route("/add", methods=["POST"])
def add_message():
    result = request.form["msg"] # Takes string from form on "index.html" and stores it in variable called "result".
    messages.append(result) # Appends value stored in "result" variable and appends it to "messages" list.
    return redirect("/")


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)