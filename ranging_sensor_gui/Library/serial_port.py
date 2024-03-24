import serial
from Settings.GUI_settings import ERROR_MESSAGE

def ranging_sensor_data(port: str, baudrate: int) -> str:
    """
    Read ranging sensor data based on the port data. START indicate each pack of data.


    """
    try:
        ser = serial.Serial(port=port, baudrate=baudrate)  

        data = ""

        while True:
            
            line = ser.readline().decode().strip()  
            if line == "START!":
                break
            data += line + "\n"

        ser.close()

        return data
    
    except serial.serialutil.SerialException:
        return ERROR_MESSAGE.SERIAL_ERROR_MESSSAGE