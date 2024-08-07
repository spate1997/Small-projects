#
import PyPDF2
import os

def merge_pdfs(pdf_list, output):
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        with open(pdf, 'rb') as f:
            merger.append(f)

    with open(output, 'wb') as f:
        merger.write(f)
        merger.close()

def get_pdf_paths():
    pdf_list = []
    print("Enter the path of each PDF file you want to merge. Type 'done' when you are finished:")
    while True:
        path = input("PDF path: ")
        if path.lower() == 'done':
            break
        elif os.path.isfile(path):
            pdf_list.append(path)
        else:
            print("File not found. Please enter a valid path.")

    return pdf_list

if __name__ == "__main__":
    pdfs = get_pdf_paths()
    if pdfs:
        output_path = input("Enter the output file path (including the file name, e.g., merged.pdf): ")
        merge_pdfs(pdfs, output_path)
        print(f"PDFs merged successfully into {output_path}")
    else:
        print("No PDF files to merge.")
