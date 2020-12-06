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
        if (data_dict['preffered_major'] != ""):
            cur.execute('UPDATE student SET preffered_major = \'%s\' WHERE username = \'%s\'' % (data_dict['preffered_major'], data_dict['username']))
        if (data_dict['sat'] != ""):
            cur.execute('UPDATE student SET sat_score = \'%s\' WHERE username = \'%s\'' % (data_dict['sat'], data_dict['username']))
        if (data_dict['act'] != ""):
            cur.execute('UPDATE student SET act_score = \'%s\' WHERE username = \'%s\'' % (data_dict['act'], data_dict['username']))
        if (data_dict['gpa'] != ""):
            cur.execute('UPDATE student SET gpa = \'%s\' WHERE username = \'%s\'' % (data_dict['gpa'], data_dict['username']))
        if (data_dict['school_size'] != ""):
            cur.execute('UPDATE student SET school_size = \'%s\' WHERE username = \'%s\'' % (data_dict['school_size'], data_dict['username']))
        if (data_dict['location'] != ""):
            cur.execute('UPDATE student SET location_ = \'%s\' WHERE username = \'%s\'' % (data_dict['location'], data_dict['username']))
        if (data_dict['pub_or_priv'] != ""):
            cur.execute('UPDATE student SET pub_or_priv = \'%s\' WHERE username = \'%s\'' % (data_dict['pub_or_priv'], data_dict['username']))
        if (data_dict['wtp'] != ""):
            cur.execute('UPDATE student SET willingness_topay = \'%s\' WHERE username = \'%s\'' % (data_dict['wtp'], data_dict['username']))
        conn.commit()
        return jsonify(data_dict), 201

    @app.route('/ct_get', methods = ['POST'])
    def get():
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        data_json = request.data
        #print(data_json)
        data_dict = json.loads(data_json)
        #print(data_dict)
        cur.execute('SELECT * FROM College WHERE collegename = \'%s\'' % data_dict['lookUp'])
        result = cur.fetchone()
        print(result)
        cur.close()
        return jsonify(result)

    @app.route('/ct_location', methods = ['POST'])
    def locateQ():
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        data_json = request.data
        #print(data_json)
        data_dict = json.loads(data_json)
        #print(data_dict)
        cur.execute('SELECT collegeName FROM student INNER JOIN college ON student.location_ = college.location_ WHERE username = \'%s\'' % data_dict['username'])
        result = cur.fetchall()
        print(result)
        cur.close()
        return jsonify(result)

    @app.route('/ct_cost', methods = ['POST'])
    def CostComp():
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        data_json = request.data
        #print(data_json)
        data_dict = json.loads(data_json)
        #print(data_dict)
        cur.execute('SELECT collegeName FROM student INNER JOIN college ON CAST(student.willingness_topay AS int)>= CAST(college.tuition_cost AS int)WHERE username = \'%s\'' % data_dict['username'])
        result = cur.fetchall()
        print(result)
        cur.close()
        return jsonify(result)    

        #JoinedTable = ('SELECT * FROM student INNER JOIN college ON location_ = location_')
        #cur.execute('SELECT * FROM JoinedTable WHERE username = \'%s\'' % data_dict['username'])

    @app.route('/at_insert', methods = ['POST'])
    def insert_pref():
        print('INSERTING PREFERENCES')
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

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

        q2 = 'SELECT (student_id) FROM student WHERE username = \'%s\'' % username
        cur.execute(q2)
        sid = cur.fetchone()[0]
        print(sid)
        print(type(sid))

        print(sid)
        
        record_to_insert = [sid, major, sat, act, gpa, size, location, pub_or_priv, wtp]

        query = "INSERT INTO application (student_id, preferences) VALUES (%s, ARRAY[%s, %s, %s, %s, %s, %s, %s, %s])"

        cur.execute(query,record_to_insert)
        conn.commit()
        
        return jsonify(data_dict), 201


    # major is at index 0
    # sat is at index 1
    # act is at index 2
    # gpa is at index 3
    # size is at index 4
    # location is at index 5
    # pub_or_priv is at index 6
    # wtp is at index 7
    

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)



    
