import Adafruit_DHT
import time

# Chọn loại cảm biến: DHT11 hoặc DHT22
sensor = Adafruit_DHT.DHT11  # Hoặc DHT22
# Chọn GPIO pin kết nối với cảm biến
pin = 4  # Ví dụ pin 4

while True:
    # Đọc giá trị nhiệt độ và độ ẩm
    humidity, temperature = Adafruit_DHT.read(sensor, pin)
    
    if humidity is not None and temperature is not None:
        print(f"Nhiệt độ: {temperature:.1f}°C, Độ ẩm: {humidity:.1f}%")
    else:
        print("Lỗi khi đọc từ cảm biến. Đang thử lại...")
    
    # Đợi 2 giây trước khi đọc tiếp
    time.sleep(2)
