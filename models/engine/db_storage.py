#!/usr/bin/python3
""" module define a class to manage db storage for hbnb clone """
from sqlalchemy import (create_engine)
from os import getenv
from sqlalchemy import MetaData

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base

sql = 'mysql+mysqldb://{}:{}@{}:3306/{}'
user = getenv('HBNB_MYSQL_USER')
pssw = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')


class DBStorage:
    """ Manages storage in the database"""

    __engine = None
    __session = None

    def __init__(self):
        """ Creates a new engine instance """
        # pool_pre_ping=True
        self.__engine = create_engine(sql.format(user, pssw, host, db),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            # used to access the given database
            Base.metadata.drop_all(bind=self.__engine, checkfirst=True)

    def all(self, cls=None):
        """ Queries a database for objects """
        dic = {}
        if cls:
            # query on self.__session all objs depending of the class name
            query_list = self.__session.query(cls).all()
            for elem in query_list:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            # query all type of objects if class (cls) not exists
            objs = [State, City, User, Place, Review]
            for i in objs:
                print(i)
            for obj in objs:
                quer = self.__session.query(obj)
                for elem in quer:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return dic

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables and database session"""
        # create all tables in the database
        self.__session = Base.metadata.create_all(self.__engine)
        # generate new session object
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # to make sure your Session is thread-safe
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def close(self):
        """ close session """
        self.__session.close()
