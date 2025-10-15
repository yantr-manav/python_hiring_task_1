import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

INPUT_DIR = "input_images"
OUTPUT_PDF = "output.pdf"
PAGE_SIZE = A4  # width, height in points (1 pt = 1/72 inch)

def preprocess_image(image_path):
    # Remove transparent background and crop to visible area or any other preprocessing steps

    image = Image.open(image_path)
 
    return image


def generate_pdf(input_dir, output_pdf_path, page_size):
    # Write the logic to pack the images into the PDF here

    c = canvas.Canvas(output_pdf_path, pagesize=page_size)
    
    c.save()


if __name__ == "__main__":
    generate_pdf(INPUT_DIR, OUTPUT_PDF, PAGE_SIZE)