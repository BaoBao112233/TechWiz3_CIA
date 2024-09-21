# Dự án Cảm biến Nhiệt độ, Độ ẩm và Áp suất

Dự án này sử dụng Raspberry Pi để đọc dữ liệu từ cảm biến nhiệt độ và độ ẩm DHT11 (hoặc DHT22) và cảm biến áp suất BMP180. Dữ liệu được hiển thị trên màn hình LCD và được gửi đến server FastAPI.

## Yêu cầu

- Raspberry Pi
- Cảm biến DHT11 hoặc DHT22
- Cảm biến BMP180
- Màn hình LCD hỗ trợ I2C
- Thư viện Python

## Cài đặt

1. Cập nhật hệ thống:
   ```bash
   sudo apt-get update
   ```

2. Cài đặt pip cho Python 3:
   ```bash
   sudo apt-get install python3-pip
   ```

3. Cài đặt các thư viện cần thiết:
   ```bash
   sudo pip3 install -r setup.txt
   ```

## Cấu hình phần cứng

- Kết nối cảm biến DHT11/DHT22 với GPIO pin 4.
- Kết nối cảm biến BMP180 qua giao thức I2C.
- Kết nối màn hình LCD qua giao thức I2C.

## Sử dụng

1. Chạy server FastAPI:
   ```bash  
   uvicorn main:app --reload
   ```

2. Chạy mã để đọc dữ liệu từ cảm biến và hiển thị lên màn hình LCD:
   ```bash
   python3 main.py
   ```

## Mô tả mã nguồn

- **main.py**: Đọc dữ liệu từ cảm biến DHT và BMP180, hiển thị lên màn hình LCD và gửi dữ liệu lên server FastAPI.
- **setup.txt**: Danh sách các thư viện cần thiết cho dự án.

## Lưu ý

- Đảm bảo rằng các cảm biến được kết nối đúng cách với Raspberry Pi.
- Kiểm tra địa chỉ server trong `main.py` để đảm bảo nó trỏ đến đúng địa chỉ IP và cổng của server FastAPI.

## Giấy phép

Dự án này được phát hành dưới giấy phép TechWiz5 và được lập trình bởi các thành viên trong nhóm CIA.