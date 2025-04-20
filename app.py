# from flask import Flask, render_template, request, session
from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
from utils.master_router import route_to_agent
import base64

app = Flask(__name__)
app.secret_key = "amit"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        user_text = request.form.get("user_text", "")
        image = request.files.get("image")

        image_base64 = None
        if image and image.filename != "":
            image_data = image.read()
            image_base64 = base64.b64encode(image_data).decode("utf-8")
            image.stream.seek(0)  # allow re-use by route_to_agent

        # Pass full history to route_to_agent (optional for LLM memory)
        history = session["chat_history"]
        response = route_to_agent(image, user_text, history=history)

        # Store latest interaction
        session["chat_history"].append({
            "user": user_text,
            "bot": response,
            "image": image_base64
        })
        session.modified = True

    return render_template("index.html", chat_history=session["chat_history"])

# @app.route("/clear", methods=['GET', 'POST'])
# def clear():
#     session.pop("chat_history", None)
#     return render_template("index.html", chat_history=[])

@app.route("/clear", methods=['GET', 'POST'])
def clear():
    print(f"[CLEAR] Method used: {request.method}")
    session.pop("chat_history", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)