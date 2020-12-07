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
    
    @app.route('/adv_func', methods = ['POST'])
    def aF():
        print('AdvFunc beginning')
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        data_json = request.data
        data_dict = json.loads(data_json)
        username = data_dict['username']
        q1 = 'SELECT * FROM student WHERE username = \'%s\'' % username
        cur.execute(q1)
        studInfo = cur.fetchone()
        q2 = 'SELECT preferences FROM application WHERE student_id = \'%s\'' % studInfo[0]
        cur.execute(q2)
        prefs = cur.fetchall()[-1][0]
        studInfo = studInfo[1:9]
        rankList = list(zip(prefs, studInfo))
        #print(studInfo)
        #print(prefs)
        #print(tuple(rankList))
        #print(list(rankList))
        q3 = 'SELECT * FROM college'
        cur.execute(q3)
        collegeList = cur.fetchall()
        #print(collegeList)
        fScores = fitScore(rankList, collegeList)
        cur.close()
        return jsonify(fScores)

       # return []

    def fitScore(rl, cl):
        fScores = []
        for i in range(len(cl)):
            #[('5', 'Biology'), ('2', '5'), ('1', '20'), ('8', '4.0'), ('6', '10000'), ('4', 'panama'), ('7', 'public'), ('3', '30000')]
            #fitScore = majorScore + SATScore + ACTScore
            if(rl[0][1] in cl[i][2]): majorScore = (100 - (int(rl[0][0]) * 10)) 
            else: majorScore = 0
            if(float(rl[1][1]) >= float(cl[i][3])): satScore = (100 - (int(rl[1][0]) * 10)) 
            else: satScore = 0
            if (float(rl[2][1]) >= float(cl[i][4])): actScore = (100 - (int(rl[2][0]) * 10))  
            else: actScore = 0
            if (float(rl[3][1]) >= float(cl[i][5])): gpaScore = (100 - (int(rl[3][0]) * 10))  
            else: gpaScore = 0
            if (abs(float(rl[4][1]) - float(cl[i][6]) <= 2000)): sizeScore = (100 - (int(rl[4][0]) * 10)) 
            else: sizeScore = 0
            if (rl[5][1] == cl[i][7]): locationScore = (100 - (int(rl[5][0]) * 10))  
            else: locationScore = 0
            if (rl[6][1] == cl[i][8]): pubScore = (100 - (int(rl[6][0]) * 10)) 
            else: pubScore = 0
            if (float(rl[7][1]) >= float(cl[i][9])): tuitionScore = (100 - (int(rl[7][0]) * 10)) 
            else: tuitionScore = 0

            score = majorScore + satScore + actScore + gpaScore + sizeScore + locationScore + pubScore + tuitionScore
            fScores.append((score, cl[i][1]))

        fScores.sort(reverse=True)

        print(fScores)
        return fScores[0:3]



    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)



    
