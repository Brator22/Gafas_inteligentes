import bluetooth
import time
from ble_advertising import advertising_payload

_ENV_SENSE_UUID = bluetooth.UUID(0x181A)
_TEMP_CHAR = (
    bluetooth.UUID(0x2A6E), 0x0002 | 0x0010 | 0x0020,)

_ENV_SENSE_SERVICE = (_ENV_SENSE_UUID,(_TEMP_CHAR,),)

class BLETemperature:
    def __init__(self, ble, name="mpy-temp"):
        self._ble = ble
        
        self._ble.active(True)
        
        self._ble.irq(self._irq)
        self.connections = set()
        
        ((self._handle,),) = self._ble.gatts_register_services((_ENV_SENSE_SERVICE,))
        self._payload = advertising_payload(name=name, services=[bluetooth.UUID(0x181A)], appearance=768)
        
        self._advertise()
    
    def _irq(self, event, data):
        if event == 1:
            conn_handle, _, _=data
            self.connections.add(conn_handle)
            
        elif event == 2:
            conn_handle, _, _ = data
            self.connections.remove(conn_handle)
        
        elif event == 20:
            conn_handle, value_handle, status = data
        
    def _advertise(self, interval_us=500000):
        self._ble.gap_advertise(interval_us,adv_data=self._payload)
        

if __name__ == "__main__":
    ble = bluetooth.BLE()
    temp = BLETemperature(ble, "Potter")
    
    while True:
        time.sleep_ms(1000)