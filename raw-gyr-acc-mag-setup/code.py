import time
import board
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33
from adafruit_lis3mdl import LIS3MDL

# Initialize LSM6DS33 for gyro and accelerometer
sensor_gyro = LSM6DS33(board.I2C())

# Initialize LIS3MDL for magnetometer
sensor_mag = LIS3MDL(board.I2C())

while True:
    # Read acceleration, gyro, and magnetometer data
    accel_x, accel_y, accel_z = sensor_gyro.acceleration
    gyro_x, gyro_y, gyro_z = sensor_gyro.gyro
    mag_x, mag_y, mag_z = sensor_mag.magnetic

    # Print the sensor readings
    print("Acceleration (m/s^2):       x={:.2f}, y={:.2f}, z={:.2f}".format(accel_x, accel_y, accel_z))
    print("Gyro (degrees/sec):         x={:.2f}, y={:.2f}, z={:.2f}".format(gyro_x, gyro_y, gyro_z))
    print("Magnetometer (microteslas): x={:.2f}, y={:.2f}, z={:.2f}".format(mag_x, mag_y, mag_z))

    # Delay for a second
    time.sleep(.5)
