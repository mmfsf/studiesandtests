from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import mapper

from gpssignal import GPSSignal

metadata = MetaData()

signals = Table('dt_signal', metadata, 
    Column('device_id', String, primary_key=True),
    Column('date_arrival_porto', DateTime),
    Column('date_device', DateTime, primary_key=True),
    Column('date_connection_gps', DateTime),
    Column('speed', Integer),
    Column('prow', Integer),
    Column('type_signal', String),
    Column('signal_quality', String),
    Column('manufacturer', String),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('origin', String)
)

mapper(GPSSignal, signals)