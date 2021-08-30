from zse.common import db
from zse.common.constants import DepartureType
from sqlalchemy import Column, String, Integer, Boolean, DateTime, Text, Enum


class Airport(db.Base):
    __tablename__ = 'airport'
    airport_icao = Column(String(4), primary_key=True)
    name = Column(String(240))
    facility = Column(String(20))


class Runway(db.Base):
    __tablename__ = 'airport_runway'
    airport_icao = Column(String(4), primary_key=True)
    code = Column(String(3), primary_key=True)
    length = Column(Integer)


class Departure(db.Base):
    __tablename__ = 'airport_departure'
    airport_icao = Column(String(4), primary_key=True)
    name = Column(String(6), primary_key=True)
    departure_type = Column(String(80))


class Arrival(db.Base):
    __tablename__ = 'airport_arrival'
    airport_icao = Column(String(4), primary_key=True)
    name = Column(String(6), primary_key=True)


class PreferredRoute(db.Base):
    __tablename__ = 'preferred_route'
    departure_airport = Column(String(4), primary_key=True)
    arrival_airport = Column(String(4), primary_key=True)
    route = Column(Text)
