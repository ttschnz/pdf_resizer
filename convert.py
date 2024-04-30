#!/usr/bin/env python3
import pypdf as pdf

def convert_pdf(file_name: str)->bool:
    try:
        reader = pdf.PdfReader(file_name)
    except:
        print("could not open file. maybe not a pdf?")
        return False
        # exit()
    
    writer = pdf.PdfWriter()

    for page in reader.pages:
        
        print("processing page %d" % page.page_number)
        width = page.mediabox[2]
        height = page.mediabox[3]
        rotation = page.get("/Rotate", 0)

        if rotation in [90, 270]:
            width, height = height, width
        if not rotation == 0:
            print(f"rotating page {page.page_number} by {rotation} degrees")
            rotation = pdf.Transformation().scale(1,1).rotate(rotation)
            page.add_transformation(rotation, expand=True)

        new_page = writer.add_blank_page(width*2, height)

        # add the original page to the new page
        new_page.merge_page(page)

    writer.write(file_name)
    return True