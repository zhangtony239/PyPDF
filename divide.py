from pypdf import PdfReader, PdfWriter
import math

def split_pdf(input_path, output_path, start_page, end_page):
    """
    Splits a PDF file from start_page to end_page.

    :param input_path: Path to the source PDF file.
    :param output_path: Path to save the new PDF file.
    :param start_page: The first page to include in the new PDF (1-based).
    :param end_page: The last page to include in the new PDF.
    """
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    # Page numbers in pypdf are 0-based, so we adjust
    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])
        
    with open(output_path, "wb") as f:
        writer.write(f)

def split_into(file, n):
    """
    Splits a PDF file into n equal parts.

    :param file: Path to the source PDF file.
    :param n: Number of parts to split the PDF into.
    """
    try:
        reader = PdfReader(file)
        total_pages = len(reader.pages)
        
        if total_pages < n:
            print(f"The PDF has fewer than {n} pages and cannot be split into {n} parts.")
        else:
            pages_per_part = math.ceil(total_pages / n)
            
            for i in range(n):
                start = i * pages_per_part + 1
                end = min((i + 1) * pages_per_part, total_pages)
                output_file = f"{file.split('.')[0]}_part{i+1}.pdf"
                
                if start > total_pages:
                    break
                
                print(f"Creating {output_file} from page {start} to {end}...")
                split_pdf(file, output_file, start, end)
            
            print("PDF splitting complete.")

    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")

if __name__ == "__main__":
    split_into(
        input("Enter the path to the PDF file: ").strip('"'),
        int(input("Enter the number of parts to split the PDF into: "))
        )