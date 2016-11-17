DATETIME_FORMAT = '%Y%m%d%H%M%S'
SIGNAL_COLUMNS = ["device_id", "date_arrival_porto", "date_device", "date_connection_gps", "speed", "prow", "type_signal", "signal_quality", "manufacturer", "latitude", "longitude", "origin"]

class GPSSignal(object):

    def __init__(self, device_id='', date_arrival_porto=None, date_device=None, date_connection_gps=None, speed=0, prow=0, type_signal='', signal_quality= '', manufacturer='', latitude=0., longitude=0., origin=0):
        self.device_id = device_id
        self.date_arrival_porto = date_arrival_porto
        self.date_device = date_device
        self.date_connection_gps = date_connection_gps
        self.speed = speed
        self.prow = prow
        self.type_signal = type_signal
        self.signal_quality = signal_quality
        self.manufacturer = manufacturer
        self.latitude = latitude
        self.longitude = longitude
        self.origin = origin

    def __str__(self):
     return self.device_id + ";" + self.date_arrival_porto.strftime(DATETIME_FORMAT) + ";" + self.date_device.strftime(DATETIME_FORMAT) + ";" + self.date_connection_gps.strftime(DATETIME_FORMAT) + ";" + str(self.speed) + ";" + str(self.prow) + ";" + self.type_signal + ";" + self.signal_quality + ";" + self.manufacturer + ";" + str(self.latitude) + ";" + str(self.longitude) + ";" + str(self.origin)