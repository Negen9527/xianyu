USERNAME = 'root'
USERPASS = '123456'
IP = '127.0.0.1'
PORT = '3306'
DBNAME = 'xianyu'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, USERPASS, IP, PORT, DBNAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False