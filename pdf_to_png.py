import os
from pdf2image import convert_from_path
from PIL import Image

def pdf_to_png(pdf_folder, output_base_folder):
    # Ensure the base output folder exists
    if not os.path.exists(output_base_folder):
        os.makedirs(output_base_folder)

    # Iterate through PDF files in the input folder
    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            pdf_name = os.path.splitext(pdf_file)[0]
            
            # Create output folder for this PDF
            output_folder = os.path.join(output_base_folder, pdf_name)
            
            # Check if the output folder already exists and contains images
            if os.path.exists(output_folder) and any(file.endswith('.png') for file in os.listdir(output_folder)):
                print(f"Skipping {pdf_file} as it has already been converted.")
                continue
            
            # If the folder doesn't exist or is empty, create it
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Convert PDF to images
            images = convert_from_path(pdf_path, poppler_path=r"C:\poppler-24.02.0\Library\bin") # Replace "C:\poppler-24.02.0\Library\bin" with the actual path to your Poppler bin directory.

            # Save each image as PNG
            for i, image in enumerate(images):
                image_path = os.path.join(output_folder, f'page_{i+1}.png')
                image.save(image_path, 'PNG')

            print(f"Converted {pdf_file} to PNG images in {output_folder}")

# Usage
pdf_folder = './pdf'
output_base_folder = './outputs'
pdf_to_png(pdf_folder, output_base_folder)

stop = 0