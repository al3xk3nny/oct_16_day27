# Challenge
# 1. Get the Hello World Flask code working.
# 2. Create an index.html in templates
# 3. Render index.html
# 4. Create a list of strings (messages)
# 5. Render the list of strings dynamically in index.html
# 6. Add a form to index.html containing a text box
# 7. On submitting the form, add the text to messages and redirect to home.

from flask import Flask, render_template, redirect, request

app = Flask(__name__)

messages = ["I'm fine", "I'm grand"]

@app.route("/", methods=["GET"])
def show_myindex():
    return render_template("myindex.html", data=messages)
    
@app.route("/answer", methods=["POST"])
def add_answer():
    ans = request.form["question"]
    messages.append(ans)
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)