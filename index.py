# import aspose.words as aw

# # Load the PDF file
# doc = aw.Document("how_to_complete_a_prf.pdf")

# # Save the document as HTML
# doc.save("done1.html")





# from pdfminer.high_level import extract_text

# def convert_pdf_to_html(pdf_path, output_html_path):
#     with open(output_html_path, 'w', encoding='utf-8') as html_file:
#         text = extract_text(pdf_path)
#         html_file.write("<html><body><p>\n")
#         html_file.write(text)
#         html_file.write("\n</p></body></html>")

# if __name__ == "__main__":
#     pdf_path = 'how_to_complete_a_prf.pdf'  # Укажите путь к вашему PDF-файлу
#     output_html_path = 'file.html'  # Укажите путь для сохранения результата

#     convert_pdf_to_html(pdf_path, output_html_path)




import subprocess

def convert_pdf_to_html(pdf_path, output_path):
    try:
        subprocess.run(['pdftohtml', '-noframes', '-enc', 'UTF-8', '-c', '-q', pdf_path, output_path])
        print(f'Successfully converted {pdf_path} to {output_path}')
    except Exception as e:
        print(f'Error converting {pdf_path} to HTML: {e}')

if __name__ == '__main__':
    pdf_file_path = 'Purchase & Sales Agreement .pdf'
    html_output_path = 'done1.html'

    convert_pdf_to_html(pdf_file_path, html_output_path)
