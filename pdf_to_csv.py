import fitz
import csv

def pdf_to_csv(input_path, output_path):
    doc = fitz.open(input_path)
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        headers_written = False  
        for page in doc:
            tables = page.find_tables()
            if tables:
                for idx, table in enumerate(tables):
                    table_data = table.extract()
                    if not headers_written:
                        csv_writer.writerows(table_data)
                        headers_written = True
                    else:
                        csv_writer.writerows(table_data[1:])

    print("Conversion successful!")
# Attach your file here
pdf_to_csv(r"file_name.pdf",'csv1.csv')