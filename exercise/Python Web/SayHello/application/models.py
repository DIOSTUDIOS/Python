from datetime import datetime
from application import db
from sqlalchemy import Column, Integer, String, DateTime


class Message(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(24))
    body = Column(String(240))
    timestamp = Column(DateTime, default=datetime.now, index=True)

    pass