
from flask import Flask, render_template, request, json, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

# import NLP as nlp

# # from requests_html import HTMLSession
# import urllib2
# from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/2018/10/19/world/middleeast/jamal-khashoggi-dead-saudi-arabia.html?action=click&module=Top%20Stories&pgtype=Homepage'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/richardjiang/desktop/ga/hack/hack/db.db'
db = SQLAlchemy(app)

class FileContents(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)
@app.route('/')
def index():
    # return {"status": "OK"}
    return render_template('index.html')

@app.route('/data',methods=['POST'])
# @app.route('/api/data')
def urlOrtext():
    temp = json.loads(request.data.decode('utf-8'))

    # textContent = temp["content"] if 



    # temp = json.dumps(request.data)
    # print(json.dumps(request.data))
    # print(temp["content"])

    # temp = []
    # page = urllib2.urlopen(url)
    # soup = BeautifulSoup(page, 'html.parser')
    # temp = " ".join(ele.text for ele in soup.find_all('p'))

    # return getResponse(temp)

    # session = HTMLSession()
    # r = session.get(url)
    # soup = BeautifulSoup(r.html.raw_html,features = "lxml")
    # # print(soup.prettify())
    # # print(soup.title.string)


    # for para in soup.find_all('p'):
    #     print(para.text)
    #     print type(para.text)

    return getResponse(temp["content"])

@app.route('/api/upload', methods = ['POST'])
def upload():
    file = request.files['fileToUpload']
    newFile = FileContents(name=file.filename, data=file.read())
    db.session().add(newFile)
    db.session().commit()
    
    # file_data = FileContents.query.filter_by(id = 1).first()
    # print(file_data)
    # return json.dumps({'status':'OK'})
    return "asdf"

def getResponse(text):
    processor = nlp.NLP(text)
    return processor.getInsight()

if __name__=="__main__":
    app.run(host='127.0.0.1', port=3000)

