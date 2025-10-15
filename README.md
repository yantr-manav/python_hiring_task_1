# Learn Basics Take-Home Task: Image Packing on PDF

## 📝 Task Overview

Your goal is to implement a **Python program** that arranges a set of images of **random sizes and shapes** into a PDF in a way that **minimizes the total space used**, while preserving each image's **original aspect ratio**.

This task tests your understanding of:

- **Bin packing / rectangle packing algorithms**
- **Image processing**
- **PDF generation**
- **Efficient code design**

---

## 🎯 Objectives

1. **Read images** from a folder (`input_images/`).  
   Images may contain **transparent backgrounds** and **random shapes**.

2. **Preprocess images**:
   - Remove transparent background (optional for packing optimization)
   - Crop images to the **bounding box of the visible area**
   - Preserve **original aspect ratio**

3. **Pack images optimally** into pages of a PDF:
   - Each page can have a **fixed size** (A4, Letter, or configurable)
   - **Minimize wasted space**

4. **Generate a PDF** (`output.pdf`) with all images properly packed.

---

## 🛠 Starter Files

| File | Description |
|------|-------------|
| `input_images/` | Folder containing generated images |
| `bin_packing_task.py` | Starter template for implementing the bin packing algorithm |
| `README.md` | This file |

---

## 📦 Usage

1. Install dependencies:

```bash
pip install pillow reportlab
