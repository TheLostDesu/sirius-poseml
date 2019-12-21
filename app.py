from flask import Flask, request

app = Flask("mahalovo")

@app.route("/api/recognize")
def recognize():
    print(request.data)
    return "test"

app.run(port=8080)