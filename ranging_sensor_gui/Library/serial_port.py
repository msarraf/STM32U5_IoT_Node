import serial

# Open the serial port
ser = serial.Serial('COM4', baudrate=115200)  # Change 'COM1' to your serial port

# Read from the serial port until "START" is encountered
data = ""
while True:
    # Read a line from the serial port
    line = ser.readline().decode().strip()  # Decode bytes to string and remove whitespace
    print(line)
    # Check if "START" is encountered
    if line == "START!":
        break

    # Otherwise, append the line to the data
    data += line + "\n"

# Close the serial port
ser.close()

# Print the received data
print("Received data:")
print(data)