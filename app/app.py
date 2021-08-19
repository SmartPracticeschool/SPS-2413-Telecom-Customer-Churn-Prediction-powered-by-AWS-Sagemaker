from flask import Flask, render_template, request, redirect, jsonify
import json
import requests
app = Flask(__name__)
s = ""
j = {"data": ""}

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":

        return render_template("index.html")
    else:

        x = request.form.get("creditscore")
        s = str(x)
        x = request.form.get("geography")
        s = s+","+str(x)
        x = request.form.get("gender")
        s = s+","+str(x)
        x = request.form.get("age")
        s = s+","+str(x)
        x = request.form.get("tenure")
        s = s+","+str(x)
        x = request.form.get("balance")
        s = s+","+str(x)
        x = request.form.get("products")
        s = s+","+str(x)
        x = request.form.get("hascredit")
        s = s+","+str(x)
        x = request.form.get("activemember")
        s = s+","+str(x)
        x = request.form.get("salary")
        s = s+","+str(x)

        print(s)
        j = {"data": s}
        print(type(j))
        print(j)

        j = json.dumps(j, indent=4)
        headers = {
            'Content-Type': 'application/json',
            'X-Amz-Date': '20201011T202720Z',
            'Authorization': 'AWS4-HMAC-SHA256 Credential=AKIAXDU6UJCNJCSRKBEY/20201011/us-east-2/execute-api/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=40f3b62bf12576141e4055f3b9163f0122c0b6ab46099b9b64d9fca7763267bb'

        }
        r = requests.post(
            'https://worky9pl9a.execute-api.us-east-2.amazonaws.com/test/telecom-churn', headers=headers, data=j)
        print(r)
        if r.text == '1':
            res = "Yes, the customer is likely to leave"
        else:
            res = "No, the customer is unlikely to leave"
        print(r.text)
        return render_template("predict.html", res=res)


if __name__ == '__main__':
    app.run(debug=True)
