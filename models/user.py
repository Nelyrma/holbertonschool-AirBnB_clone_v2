#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import column, string


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"

    email = column(string(128), nullable=False)
    password = column(string(128), nullable=False)
    first_name = column(string(128), nullable=True)
    last_name = column(string(128), nullable=True)
