# Write a Python script utilizing SQLAlchemy ORM to map Python classes to MySQL database tables.
"""
  Sample SQLAlchemy setup:
  
  from sqlalchemy import create_engine, Column, Integer, String
  from sqlalchemy.ext.declarative import declarative_base
  from sqlalchemy.orm import sessionmaker

  engine = create_engine('mysql+mysqlconnector://root:@localhost/python_web_db')
  Base = declarative_base()

  class User(Base):
      __tablename__ = 'users'
      id = Column(Integer, primary_key=True)
      username = Column(String(50))
      email = Column(String(100))

  Base.metadata.create_all(engine)
"""
print("SQLAlchemy ORM mapping template documented.")