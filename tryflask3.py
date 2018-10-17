from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


messages = [
    {
     'text': "Hi",
     'author': 'richard'
    },
    {
     'text': "Hi you too.",
     'author': 'tony'
    }
    ]

@app.route("/")
def login():
    return render_template("login3.html")


@app.route("/login", methods=["POST"])
def do_login():
    result = request.form["username"]
    # return "You have logged in as " + result
    return redirect("/chat/" + result)
    

@app.route("/chat/<result>")
def show_chat(result):
    return render_template("chat3.html", messages=messages, banana=result)


@app.route("/chat/<result>/add", methods=["POST"])
def add_message(result):
    message = request.form["msg"]
    message_dict = {
        'text': message,
        'author': result
    }
    messages.append(message_dict)
    return redirect("/chat/" + result)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)