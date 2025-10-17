# Image Packing to PDF Take-Home Task

This project is a Python program that automatically arranges a collection of images of various sizes into a multi-page PDF. It optimizes the placement to minimize wasted space while preserving each image's original aspect ratio. The script is designed to handle images with transparent backgrounds by cropping them to their visible content before packing.

---

## Features

-   **Automatic Cropping**: Intelligently removes empty transparent space around image content.
-   **Efficient Packing**: Uses a guillotine-based rectangle packing algorithm to minimize wasted space on each page.
-   **PDF Generation**: Outputs a clean, multi-page PDF with all images properly placed.
-   **Robust Handling**: Gracefully handles and processes empty or fully transparent images without crashing.
-   **Dependency Management**: All required libraries are listed in `requirements.txt`.

---

## Requirements

-   Python 3.7+

---

## 🚀 How to Run

Follow these steps to set up and run the project on your local machine.

### 1. Clone the Repository

First, clone the repository to your local machine using git.

```bash
git clone <your-repository-url>
cd python_hiring_task_1
```
### 2. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```
### 3. Install Dependencies
Install all the required libraries using the ```requirements.txt``` file.

```bash
pip install -r requirements.txt
```
### 4. Generate Sample Data
The project comes with a script to generate sample images for testing. Run the following command to create 50 sample images in the ```input_images/``` directory.

```bash 
python sample_data_generation.py
```

### 5. Run the Main Program
Execute the main script to start the image processing and PDF generation.

```bash 
python task_1_starter_code.py
```
