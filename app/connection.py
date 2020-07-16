from app import *
import pymysql as sql

def getConnection(app):
    connect = sql.connect(host=app.config['DATABASE_HOST'],
                            user=app.config['DATABASE_USER'], 
                            password=app.config['DATABASE_PASS'], 
                            db=app.config['DATABASE_NAME'],
                            cursorclass=sql.cursors.DictCursor)

    return (connect)