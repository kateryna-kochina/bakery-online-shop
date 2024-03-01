from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from ..database import db


category_option_association_table = Table('category_option', db.Model.metadata,
                                          Column('category_id', Integer,
                                                 ForeignKey('categories.id')),
                                          Column('option_id', Integer,
                                                 ForeignKey('options.id'))
                                          )


class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False)

    options = relationship(
        'Option', secondary=category_option_association_table, back_populates='categories')


class Product(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    img_path = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)

    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)


class Option(db.Model):
    __tablename__ = 'options'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False)
    coefficient = Column(Float, nullable=False)

    categories = relationship(
        'Category', secondary=category_option_association_table, back_populates='options')
