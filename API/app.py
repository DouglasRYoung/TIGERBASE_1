from flask import Flask, g, jsonify
import werkzeug, os
from werkzeug.utils import secure_filename

import psycopg2
from config import config


def create_app():
    app = Flask(__name__)


    @app.route('/db_version')
    def index():
        print ('ROUTE')
        conn = None
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM student;")
        result = cur.fetchone()
        print(result)
        cur.close()
        return jsonify(result)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)



    
