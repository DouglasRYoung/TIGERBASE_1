from flask import Flask,json, g, jsonify, request
import werkzeug, os
from werkzeug.utils import secure_filename
from flask_cors import CORS


import psycopg2
from config import config


def create_app():
    app = Flask(__name__, static_folder='../frontend/build')
    CORS(app)


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
        print(request)
        print(result)
        cur.close()
        return jsonify(result)

    @app.route('/st_insert', methods = ['POST'])
    def insert_student():
        print('INSERTING STUDENT')
        conn = None
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        stuff = request.method
        print(stuff)
        print(request)
        print ("HERE")

        data_json = request.data
        data_dict = json.loads(data_json)
        print(data_dict)
        major = data_dict['preffered_major']
        sat = data_dict['sat_score']
        act = data_dict['act_score']
        gpa = data_dict['gpa']
        size = data_dict['school_size']
        location = data_dict['location_']
        pub_or_priv = data_dict['pub_or_priv']
        wtp = data_dict['willingness_topay']
        username = data_dict['username']
        record_to_insert = (major, sat, act, gpa, size, location, pub_or_priv, wtp, username)

        query = "INSERT INTO student (preffered_major, sat_score, act_score, gpa, school_size, location_, pub_or_priv, willingness_topay, username) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query,record_to_insert)
        conn.commit()
        # bad request
        if "gpa" not in data_dict:
            return jsonify({"errorMsg": "bad request"}), 400
        # succeed
        return jsonify(data_dict), 201

        #record_to_insert = ('Chemistry','1500', '32', '3.9', '10000', 'San Antonio', 'Private', '30000', 'steph')

    @app.route('/st_delete', methods = ['DELETE'])
    def delete_student():
        print('DELETING STUDENT')
        conn = None
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        data_json = request.data
        data_dict = json.loads(data_json)
    
        cur.execute('DELETE FROM student WHERE username = \'%s\'' % data_dict['username'])
       
        conn.commit()
        return jsonify(data_dict), 201
    
    @app.route('/st_update', methods = ['POST'])
    def update_student():
        print('UPDATING STUDENT')
        conn = None
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        data_json = request.data
        data_dict = json.loads(data_json)
      
        cur.execute('UPDATE student SET gpa = \'%s\' , act = \'%s\', sat = \'%s\', school_size = \'%s\', location_ = \'%s\', pub_or_priv = \'%s\', wtp = \'%s\' WHERE username = \'%s\'' % (data_dict['gpa'], data_dict['act'], data_dict['sat'], data_dict['school_size'], data_dict['location_'], data_dict['pub_or_priv'], data_dict['wpa'],data_dict['username']))
        conn.commit()
        return jsonify(data_dict), 201



        
    

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)



    
