from flask import Flask, render_template,request, redirect
import csv

app =Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/<string:page>')
def redirect2page(page):
    redirect2=page+'.html'
    # print(redirect2)
    return render_template(redirect2)

def save2txt(data):
    with open('db.txt','a') as txt:
        email=data['email']
        subject=data['subject']
        message=data['message']
        txt.write(f'\n{email},{subject},{message}')

def save2csv(data):
    with open('db.csv','a',newline='') as csvfile:
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer=csv.writer(csvfile,delimiter=',',quotechar=' ',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            save2txt(data)
            save2csv(data)
            return redirect('thankyou')
        except:
            return 'error occured'
    else:
        return 'method not post, something happened'

# @app.route('/index')
# def index():
#     return render_template('index.html')

# @app.route('/blog')
# def blog():
#     return 'thhis is blog'

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/work')
# def work():
#     return render_template('work.html')

# @app.route('/works')
# def works():
#     return render_template('works.html')

# @app.route('/thankyou')
# def thankyou():
#     return render_template('thankyou.html')

# @app.route('/components')
# def components():
#     return render_template('components.html')