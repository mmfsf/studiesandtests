from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker

from gpssignal import GPSSignal

import gpssignal_mapper

from datetime import datetime

engine = create_engine('postgresql://mmfsf:p2ssw0rd@localhost:5432/virtualalarm')
Session = sessionmaker(bind=engine)
session = Session()

our_user = session.query(GPSSignal).filter_by(device_id='001140294').first()

new_signal = GPSSignal()
new_signal.device_id = '001140294'
new_signal.date_arrival_porto = None
new_signal.date_device = datetime.now()
new_signal.date_connection_gps = None
new_signal.speed = 10
new_signal.prow = 5
new_signal.type_signal = 'I'
new_signal.signal_quality = 'V'
new_signal.manufacturer = 'KPS'
new_signal.latitude = -23.567
new_signal.longitude = -46.987
new_signal.origin = ''

session.add(new_signal)
session.commit()

# print our_user.device_id

# with engine.connect() as con:

#     rs = con.execute('SELECT * FROM dt_signal limit 10')

#     for row in rs:
#         print row