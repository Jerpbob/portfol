import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route("/<string:page_name>")
def works(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open("venv/database.csv", "a", newline='') as database2:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:  
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thanks.html')
        except:
            return 'nothing was stolen'
    else:
        return 'I could not steal it'

