#!/usr/bin/python3

from sqlalchemy import (create_engine)
from os import getenv
from sqlalchemy import MetaData
from logging import info

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
        """ Creates a new instance """
        # pool_pre_ping=True, Boolean, test liveness connections each checkout
        self.__engine = create_engine(sql.format(user, pssw, host, db),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            # bind is used to access the given database
            Base.metadata.drop_all(bind=self.__engine, checkfirst=True)

    def all(self, cls=None):
        """all objects"""
        dic = {}
        if cls:
                objs = self.__session.query(cls).all()
            for obj in objs:
                key = type(obj).__name__ + "." + str(obj.id)
                dic[key] = obj
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem        
        return dic






 
        dic = {}
        if cls is None:
            objs = []
            classes = ['User', 'State', 'City', 'Place', 'Review', 'Amenity']
            for _class in classes:
                results = self.__session.query(eval(_class))
                for result in results:
                    objs.append(result)
        else:
            objs = self.__session.query(cls).all()
        for obj in objs:
            key = type(obj).__name__ + "." + str(obj.id)
            dic[key] = obj
        return dic     