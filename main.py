import Adafruit_DHT
import smbus
import time
import I2C_LCD_driver  # Thư viện cho màn hình LCD
import httpx
from datetime import datetime  # Thư viện để lấy thời gian

# Khởi tạo màn hình LCD
lcd = I2C_LCD_driver.lcd()

# Chọn loại cảm biến: DHT11 hoặc DHT22
sensor = Adafruit_DHT.DHT11  # Hoặc DHT22
# Chọn GPIO pin kết nối với cảm biến
pin = 4  # Ví dụ pin 4

# Địa chỉ I2C của cảm biến BMP180
BMP180_I2C_ADDRESS = 0x77
bus = smbus.SMBus(1)

# Địa chỉ server FastAPI
server_url = "http://localhost:8000/tech5_cia"

# Hàm để đọc dữ liệu từ cảm biến BMP180
def read_bmp180():
    bus.write_byte_data(BMP180_I2C_ADDRESS, 0xF4, 0x34)
    time.sleep(0.5)
    msb = bus.read_byte_data(BMP180_I2C_ADDRESS, 0xF6)
    lsb = bus.read_byte_data(BMP180_I2C_ADDRESS, 0xF7)
    pressure = ((msb << 8) + lsb) / 256.0  # Chuyển đổi dữ liệu
    return pressure

while True:
    # Đọc giá trị nhiệt độ và độ ẩm
    humidity, temperature = Adafruit_DHT.read(sensor, pin)
    
    # Đọc áp suất từ BMP180
    pressure = read_bmp180()
    
    # Lấy thời gian hiện tại
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if humidity is not None and temperature is not None:
        # Hiển thị dữ liệu lên màn hình LCD
        lcd.lcd_clear()
        lcd.lcd_display_string(f"Thời gian: {current_time}", 1)
        lcd.lcd_display_string(f"Nhiệt độ: {temperature:.1f}°C", 2)
        lcd.lcd_display_string(f"Độ ẩm: {humidity:.1f}%", 3)
        lcd.lcd_display_string(f"Áp suất: {pressure:.2f} hPa", 4)

        # Gửi dữ liệu lên server
        data = {
            "temperature": temperature,
            "humidity": humidity,
            "pressure": pressure,
            "timestamp": current_time  # Thêm thời gian vào dữ liệu gửi
        }
        response = httpx.post(server_url, json=data)
        print(f"Đã gửi dữ liệu: {data}, Phản hồi: {response.status_code}")
    else:
        lcd.lcd_clear()
        lcd.lcd_display_string("Lỗi đọc cảm biến", 1)
    
    # Đợi 2 giây trước khi đọc tiếp
    time.sleep(2)