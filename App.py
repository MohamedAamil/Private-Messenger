from flask import Flask, render_template, request, redirect, url_for
from DB_Opr import add_data, get_chat, delete_chat

app = Flask(
    __name__, template_folder='client/template',
    static_folder='client/static'
)


@app.route('/')
def home():
    names, chats, images = get_chat()
    return render_template("home.html", length=len(names), names=names, chats=chats, images=images)


@app.route('/insert', methods=["POST"])
def insert():
    name = request.form["name"]
    message = request.form["message"]
    image = request.form["image"]
    if name == "":
        pass
    else:
        add_data(name, message, image)
    return redirect(url_for('home'))


@app.route('/delete', methods=["POST"])
def delete():
    delete_chat()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)