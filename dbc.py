class DatabaseConfig:
    SECRET_KEY='secretkey'
    DEBUG=True
    TESTING=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:root@localhost/bvsite'