# Chu_ky_so
cài openssl.exe
![z7167731285738_969f0760b9f9101ff22e60b31d88c5c0](https://github.com/user-attachments/assets/8cfb13d6-7754-437b-9433-2a03ce264b9a)
cài signer.key trong cmd chạy với quyền admin nhập đường dẫn đến openssl 
![z7168067902891_909cd6da7e8c4e1188650b6fb4d5e2c6](https://github.com/user-attachments/assets/c4bf9e85-1c7f-4431-bf61-56fb32927533)
tải python 
pip install cryptography pyPDF2
![z7168104449195_60d822f4e8a531b0dda1a4fc82849b46](https://github.com/user-attachments/assets/8756c3ce-4463-4751-8a0a-2237ad77896c)
khi cài xong sẽ sinh ra 2 file
<img width="796" height="168" alt="image" src="https://github.com/user-attachments/assets/2a5ca3a2-9662-43c2-9a42-b294980c9cc6" />
code python
import fitz  # PyMuPDF
from datetime import datetime

# --- Cấu hình ---
pdf_path = "Phan_1_Cau_truc_PDF_Chu_ky_so_signed.pdf"  # file gốc
signature_img = r"c:\Users\nguye\Downloads\chu-ky-ten-kien.jpg"
output_pdf = "bai_tap_02_ChuKiSo_signed_by_Kien.pdf"

name = "Nguyen Trung Kiên"
date = datetime.now().strftime("%d/%m/%Y")

# --- Mở file PDF ---
doc = fitz.open(pdf_path)

# --- Xác định các trang cần chèn ---
pages = [0, len(doc) - 1]  # trang đầu và trang cuối

for page_num in pages:
    page = doc[page_num]
    # Lấy kích thước trang
    rect = page.rect
    # Vị trí chèn ảnh (phía dưới cùng, giữa trang)
    x = rect.width / 2 - 100
    y = rect.height - 150
    # Chèn ảnh chữ ký
    page.insert_image(fitz.Rect(x, y, x + 200, y + 100), filename=signature_img)

    # Thêm tên, ngày ký, SĐT bên cạnh
    page.insert_text((x + 80, y + 105), f"Ngày ký: {date}", fontsize=10)
    page.insert_text((x + 40, y + 135), name, fontsize=11, color=(0, 0, 0))

# --- Lưu file mới ---
doc.save(output_pdf)
doc.close()

print(f"✅ Đã ký và lưu file: {output_pdf}")

file gốc
<img width="1228" height="744" alt="image" src="https://github.com/user-attachments/assets/e0b28acf-a85c-4519-ad37-c7d0a0099a1f" />

file sau khi ký tên
<img width="1226" height="778" alt="image" src="https://github.com/user-attachments/assets/482e3242-48ff-494c-b249-30c6f7b593ec" />


