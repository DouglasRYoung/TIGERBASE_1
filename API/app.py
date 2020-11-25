from flask import Flask, g, jsonify
import werkzeug, os
from werkzeug.utils import secure_filename

import psycopg2
from psycopg2 import pool

def get_db():
    print ('GETTING CONN')
    if 'db' not in g:
        g.db = app.config['postgreSQL_pool'].getconn()
    return g.db


def create_app():
    app = Flask(__name__)

    app.config['postgreSQL_pool'] = psycopg2.pool.SimpleConnectionPool(1, 20,user = "postgres",
                                                  password = "thisisTIGERBASE!",
                                                  host = "35.239.33.73",
                                                  port = "5432",
                                                  database = "postgres")

    @app.teardown_appcontext
    def close_conn(e):
        print('CLOSING CONN')
        db = g.pop('db', None)
        if db is not None:
            app.config['postgreSQL_pool'].putconn(db)


    @app.route('/')
    def index():
        print ('ROUTE')
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM student;")
        result = cursor.fetchall()
        print (result)

        cursor.close()
        return jsonify(result)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
