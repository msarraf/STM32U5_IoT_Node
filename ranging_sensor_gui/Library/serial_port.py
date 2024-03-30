import serial
from Settings.GUI_settings import ERROR_MESSAGE
import logging
def ranging_sensor_data(port: str, baudrate: int) -> str:
    """
    Read ranging sensor data based on the port data. START indicate each pack of data.


    """
    try:
        ser = serial.Serial(port=port, baudrate=baudrate, timeout=0.2)  

        data = ""
        while True:
            line = ser.readline().decode().strip() 
            if line:
                if line == "START!":
                    break
                data += line + "\n"
            else:
                break
        ser.close()

        return data
    
    except serial.serialutil.SerialException as e:
        logging.error(ERROR_MESSAGE.SERIAL_ERROR_MESSSAGE)
        logging.error(e)
        return ERROR_MESSAGE.SERIAL_ERROR_MESSSAGE