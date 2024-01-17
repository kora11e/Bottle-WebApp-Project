from sqlite3 import create_engine, ForeignKey, Column, String, Integer, CHAR



Base = declarative_base()

class Person(Base):
    __tablename__ = 'persons'

    ssn = Column('ssn', Integer, primary_key = True)
    furstname = []