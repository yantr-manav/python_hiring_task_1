# Learn Basics Take-Home Task: Image Packing on PDF

## 📝 Task Overview

Your goal is to implement a **Python program** that arranges a set of images of **random sizes and shapes** into a PDF in a way that **minimizes the total space used**, while preserving each image's **original aspect ratio**.

This task tests your understanding of:

- **Rectangle packing algorithms**
- **Image processing**
- **PDF generation**
- **Efficient code design**

---

## 🎯 Objectives
1. **Create a virtual environment** for the project.

2. **Install dependencies** from `requirements.txt`.

3. **Generate sample images** using `sample_data_generation.py`.

4. **Read images** from a folder (`input_images/`).  
   Images may contain **transparent backgrounds** and **random shapes**.

5. **Preprocess images**:
   - Remove transparent background (optional for packing optimization)
   - Crop images to the **bounding box of the visible area**
   - Preserve **original aspect ratio**

6. **Pack images optimally** into pages of a PDF:
   - Each page can have a **fixed size** (A4, Letter, or configurable)
   - **Minimize wasted space**

7. **Generate a PDF** (`output.pdf`) with all images properly packed.

8. **Update the requirements.txt file** with the necessary dependencies.

9. **Update README.md** with instructions for running the program.

---

## 🛠 Starter Files

| File | Description | Additional Notes |
|------|-------------| ---------|
| `sample_data_generation.py` | Script for generating sample images | Run `python sample_data_generation.py` to generate sample images |
| `input_images/` | Folder containing generated images | Folder will be created if it doesn't exist when the script is run |
| `task_1_starter_code.py` | Starter template for implementing the packing algorithm |
| `README.md` | This file | |
| `requirements.txt` | List of dependencies required to run the program | Install these in a virtual environment |
---

## 📦 Steps

Follow these steps to get started:

1. Create a virtual environment for the project.
2. Install dependencies from `requirements.txt`.
3. Run the `sample_data_generation.py` script to generate sample images.
4. Edit and implement the task in `task_1_starter_code.py`.
5. Run your solution to generate the output PDF.

## Bonus Points

1. **Optimize image compression** to reduce file size.
2. **Implement a command-line interface** for running the program.
3. **Add documentation** to explain the program's functionality.
4. **Implement error handling** for handling edge cases.
