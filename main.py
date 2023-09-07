import os
import docx

def convert_doc_to_docx(input_dir, output_dir):
    if not os.path.exists(output_dir):
        cmd = f'lowriter --convert-to docx --outdir {output_dir} {input_dir}*.doc'
        os.system(cmd)
    else:
        return

def read_docx_to_text(input_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith(".docx"):  # Check if the file is a DOC file
            doc = docx.Document(os.path.join(input_dir, filename))

            text = ''

            for paragraph in doc.paragraphs:
                text += paragraph.text + '\n'

            print(text)
            print('__________________________________________________________________________')
        else:
            return


        


if __name__ == '__main__':
    doc_input_dir = 'paintext/documents/'
    doc_output_dir = 'paintext/docx_documents/'
    convert_doc_to_docx(doc_input_dir, doc_output_dir)
    read_docx_to_text(doc_output_dir)
