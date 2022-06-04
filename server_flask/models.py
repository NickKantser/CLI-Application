from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class File(Base):
    """"""
    __tablename__ = 'file'
    # __table_args__ = {'autoload':True}
    UUID = Column(Integer, primary_key=True)
    name = Column(String(50))
    create_datetime = Column(DateTime)
    size = Column(String(10))
    mimetype = Column(String(25))
    path = Column(String(100))

    def __init__(self, uuid, name, create_datetime, size, mimetype, path):
        self.UUID = uuid
        self.name = name
        self.create_datetime = create_datetime
        self.size = size
        self.mimetype = mimetype
        self.path = path
