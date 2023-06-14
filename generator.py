import qrcode
from PIL import Image
import csv
from io import BytesIO
from barcode import EAN13
from barcode.writer import ImageWriter
import barcode

def get_csv_file():
    # Path to the CSV file
    csv_file_path = "/Volumes/workspace/etiquetteGenerator/Sanitizedview.csv"
    out = []
    # Open the CSV file
    with open(csv_file_path, "r") as file:
        # Create a CSV reader object
        reader = csv.reader(file)
        for row in reader:
            out.append(row)
        return out

def generate_bar_code(data, file_path):
    barcode_value = data  # Replace with your barcode value
    ean = barcode.get('code128', barcode_value, writer=ImageWriter())
    ean.save(file_path)



def generate_qr_code(data, file_path):
    # Create a QR code instance
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=1)

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to the specified file path
    qr_img.save(file_path)

# Example usage
# data = "https://www.example.com"
# generate_qr_code(data, file_path)
# print(f"QR code generated and saved to {file_path}")
rows = get_csv_file()
for row in rows: 
    id = row[0]
    file_path = f"/Volumes/workspace/etiquetteGenerator/qr_code/{id}.png"
    generate_qr_code(f"https://csil.ca/products/{id}", file_path)
    file_path = f"/Volumes/workspace/etiquetteGenerator/barcode/{id}.png"
    barcode_id = row[2]
    if (barcode_id != "0"):
        generate_bar_code(barcode_id, file_path )