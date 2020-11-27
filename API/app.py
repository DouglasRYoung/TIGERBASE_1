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

    @app.route('/st_insert')
    def insert_student():
        print('INSERTING STUDENT')
        conn = None
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        #record_to_insert = ('Chemistry','1500', '32', '3.9', '10000', 'San Antonio', 'Private', '30000', 'steph')
        query = "INSERT INTO student (preffered_major, sat_score, act_score, gpa, school_size, location_, pub_or_priv, willingness_topay, username) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query)#, record_to_insert)
        conn.commit()

    

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)



    
