import os
from io import BytesIO
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import cm
import rectpack

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
    try:
        image= Image.open(image_path)
        # Get the bounding box of the non-transparent area
        bbox = image.getbbox()
        if bbox:
            image = image.crop(bbox)
            return image
        return None  # Return None for empty or fully transparent images
    except Exception as e:
        print(f"❌ Error preprocessing {os.path.basename(image_path)}: {e}")
        return None


def generate_pdf(input_dir: str, output_pdf_path : str, page_size):
    """This is the main function to generate the PDF

    Args:
        input_dir (str): The input directory containing the images
        output_pdf_path (str): The path to save the generated PDF
        page_size (_type_): The page size of the PDF (A4, Letter, etc.)
    """
 # --- 1. Preprocess all images ---
    print(f"🔍 Starting preprocessing from '{input_dir}'...")
    image_data = []
    if not os.path.isdir(input_dir):
        print(f"Error: Input directory '{input_dir}' not found.")
        print("Please run 'python sample_data_generation.py' first.")
        return

    for filename in sorted(os.listdir(input_dir)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(input_dir, filename)
            preprocessed_img = preprocess_image(filepath)
            if preprocessed_img:
                width, height = preprocessed_img.size
                image_data.append({'width': width, 'height': height, 'image': preprocessed_img})

    if not image_data:
        print("No valid images found to process.")
        return
    print(f"✅ Preprocessed {len(image_data)} images.")

    # --- 2. Pack images into bins (pages) ---
    print("📦 Packing images onto pages...")
    # Configure page dimensions with margins
    MARGIN = 1 * cm
    PAGE_WIDTH, PAGE_HEIGHT = page_size
    USABLE_PAGE_WIDTH = PAGE_WIDTH - (2 * MARGIN)
    USABLE_PAGE_HEIGHT = PAGE_HEIGHT - (2 * MARGIN)

    # ------------------ THIS IS THE CORRECTED LINE ------------------
    packer = rectpack.newPacker(sort_algo=rectpack.SORT_AREA, pack_algo=rectpack.GuillotineBssfSas)
    # ----------------------------------------------------------------

    for i, data in enumerate(image_data):
        packer.add_rect(data['width'], data['height'], rid=i)

    packer.add_bin(USABLE_PAGE_WIDTH, USABLE_PAGE_HEIGHT)
    packer.pack()
    print(f"✅ Packing complete. Images fit on {len(packer)} page(s).")

    # --- 3. Generate the PDF with packed images ---
    print(f"📄 Creating PDF at '{output_pdf_path}'...")
    c = canvas.Canvas(output_pdf_path, pagesize=page_size)

    for i, page in enumerate(packer):
        print(f"   -> Drawing page {i + 1}...")
        for rect in page:
            img_index = rect.rid
            img_info = image_data[img_index]
            img_obj = img_info['image']

            # Convert rectpack's top-left coordinates to reportlab's bottom-left
            x = rect.x + MARGIN
            y = USABLE_PAGE_HEIGHT - rect.y - rect.height + MARGIN

            # Save the image to an in-memory buffer with compression
            temp_buffer = BytesIO()
            img_obj.save(temp_buffer, format='PNG', optimize=True)
            temp_buffer.seek(0)
            
            # Draw the image from the in-memory buffer
            c.drawImage(
                ImageReader(temp_buffer),
                x, y,
                width=rect.width,
                height=rect.height,
                mask='auto'  # Handles transparency
            )
        c.showPage()  # Finish the current page

    c.save()
    print(f"🎉 PDF generated successfully!")


def compress_images(input_image_path: str, output_image_path: str, compression_level: int=5):
    """This function should compress the images to make the PDF size as minimun 

    Args:
        input_image_path (str): The path of the input image
        output_image_path (str): The path to save the compressed image
        compression_level (int) default 5: The compression level Ex: 0-9 where 0 is no compression and 9 is maximum compression

    Returns:
        _type_: The path of the compressed image
    """
    try:
        with Image.open(input_image_path) as img:
            print(f"Compressing {os.path.basename(input_image_path)}...")
            img.save(output_image_path, optimize=True, quality=quality)
        return output_image_path
    except Exception as e:
        print(f"❌ Error compressing {os.path.basename(input_image_path)}: {e}")
        return None




if __name__ == "__main__":
    
    generate_pdf(INPUT_DIR, OUTPUT_PDF, PAGE_SIZE)