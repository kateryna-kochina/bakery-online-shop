from sqlalchemy import Column, ForeignKey, Integer, String

from ..database import db


class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False)


class Product(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    img_path = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)

    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
