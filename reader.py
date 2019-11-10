import serial

# assume factory settings, from Data Interface Description
# we changed from 7 data bits to 8 data bits to get this to work, on the scale itself.
with serial.Serial("/dev/ttyUSB0", 1200
        , timeout=100
        , parity=serial.PARITY_ODD
        , stopbits=1
        , xonxoff=0
        , rtscts=1) as ser:

    while True:
        print(ser.read().decode('ascii', errors='replace'), end="")



