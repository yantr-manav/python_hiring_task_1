import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

INPUT_DIR = "input_images"
OUTPUT_PDF = "output.pdf"
PAGE_SIZE = A4  # width, height in points (1 pt = 1/72 inch) 

def preprocess_image(image_path: str):
    """This function should do all preprocessing of the images 

    Args:
        image_path (str): The Input path of the image

    Returns:
        _type_: The preprocessed image
    """
    # Remove transparent background and crop to visible area or any other preprocessing steps

    image = Image.open(image_path)
 
    return image


def generate_pdf(input_dir: str, output_pdf_path : str, page_size):
    """This is the main function to generate the PDF

    Args:
        input_dir (str): The input directory containing the images
        output_pdf_path (str): The path to save the generated PDF
        page_size (_type_): The page size of the PDF (A4, Letter, etc.)
    """

    # Write the logic to pack the images into the PDF here

    c = canvas.Canvas(output_pdf_path, pagesize=page_size)
    
    c.save()


def compress_images(input_image_path: str, output_image_path: str, compression_level: int=5):
    """This function should compress the images to make the PDF size as minimun 

    Args:
        input_image_path (str): The path of the input image
        output_image_path (str): The path to save the compressed image
        compression_level (int) default 5: The compression level Ex: 0-9 where 0 is no compression and 9 is maximum compression

    Returns:
        _type_: The path of the compressed image
    """
    # Write the logic to compress the images here

    return output_image_path


if __name__ == "__main__":
    
    generate_pdf(INPUT_DIR, OUTPUT_PDF, PAGE_SIZE)