from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}-->{subject}-->{message}')


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)

        return redirect('thankyou.html')
    else:
        return 'something went wrong. Try again :('










# Here we by writing def function for each html pages it will become complicate.
# So to overcome it we write a def function which goes to html page dynamically
'''
@app.route('/index.html')
def my_home1():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/components.html')
def components():
    return render_template('components.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/work.html')
def work():
    return render_template('work.html')


@app.route('/works.html')
def works():
    return render_template('works.html')
'''