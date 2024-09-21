import smbus
import time

# Địa chỉ I2C của cảm biến BMP180
BMP180_I2C_ADDRESS = 0x77

# Khởi tạo bus I2C
bus = smbus.SMBus(1)

# Hàm để đọc dữ liệu từ cảm biến BMP180
def read_bmp180():
    # Đọc dữ liệu áp suất
    bus.write_byte_data(BMP180_I2C_ADDRESS, 0xF4, 0x34)
    time.sleep(0.5)
    msb = bus.read_byte_data(BMP180_I2C_ADDRESS, 0xF6)
    lsb = bus.read_byte_data(BMP180_I2C_ADDRESS, 0xF7)
    pressure = ((msb << 8) + lsb) / 256.0  # Chuyển đổi dữ liệu

    return pressure

while True:
    pressure = read_bmp180()
    print(f"Áp suất không khí: {pressure:.2f} hPa")
    time.sleep(2)  # Đợi 2 giây trước khi đọc tiếp