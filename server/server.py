import database as db
from models import File
import flask
from flask import Flask, send_file, g

app = Flask(__name__)

# Common part in the URL of read and stat commands
# Get request of corresponding uuid
@app.url_value_preprocessor
def pull_file_uuid(endpoint, values):
    if values and 'uuid' in values:
        uuid = values.pop('uuid', None)
        g.response = db.session.query(File).filter(File.UUID == uuid).first()

@app.route('/file/<int:uuid>/stat', methods=['GET'])
def stat():
    try:
        response = g.response
        data =  { 'create_datetime': response.create_datetime,
                  'size': response.size,
                  'mimetype': response.mimetype,
                  'name': response.name }
        return data
    except:
        return 'The file not found', 404



@app.route('/file/<int:uuid>/read', methods=['GET'])
def read():
    try:
        response = g.response
        return send_file(response.path)

    except:
        return 'The file not found', 404



if __name__ == '__main__':
    app.run(debug=True)
