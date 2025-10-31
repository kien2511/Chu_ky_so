from pyhanko.sign import signers, fields
from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign.fields import SigFieldSpec
from pyhanko.sign.appearance import PdfAppearance, stamp

# File PDF gốc và PDF ký xong
input_pdf = r"Phan_1_Cau_truc_PDF_Chu_ky_so.pdf"
output_pdf = r"C:\Users\nguye\OneDrive\Desktop\BTATBMTT\bai_tap_02_ChuKiSo_signed.pdf"

# Khóa và chứng chỉ
private_key_file = r"C:\Users\nguye\OneDrive\Desktop\BTATBMTT\signer.key"
certificate_file = r"C:\Users\nguye\OneDrive\Desktop\BTATBMTT\signer.crt"
signature_img = r"C:\Users\nguye\Downloads\chu-ky-ten-kien.jpg"

# Đọc khóa và chứng chỉ
with open(private_key_file, "rb") as kf:
    key_data = kf.read()
with open(certificate_file, "rb") as cf:
    cert_data = cf.read()

# Tạo signer
signer = signers.SimpleSigner.load(key_data, cert_data, key_passphrase=None)

# Ký PDF
with open(input_pdf, "rb") as inf, open(output_pdf, "wb") as outf:
    writer = IncrementalPdfFileWriter(inf)

    # Tạo vùng chữ ký hiển thị ở góc dưới phải
    fields.append_signature_field(
        writer,
        SigFieldSpec(sig_field_name="Signature1", box=(400, 50, 550, 150))
    )

    # Metadata chữ ký
    meta = signers.PdfSignatureMetadata(
        field_name="Nguyen Trung Kien",
        reason="Tôi là tác giả của tài liệu này",
        location="Bắc Giang",
    )

    # Thêm ảnh chữ ký
    appearance = PdfAppearance(
        stamp_style=stamp.StaticStampStyle(
            background=signature_img,  # ảnh chữ ký tay
            text_box_style=stamp.TextBoxStyle(
                text_params=stamp.DEFAULT_SIGNATURE_TEXT_PARAMS
            ),
        )
    )

    # Tiến hành ký
    signers.sign_pdf(
        writer,
        meta,
        signer=signer,
        appearance=appearance,
        output=outf
    )

print(f"✅ Đã ký thành công! File mới: {output_pdf}")
