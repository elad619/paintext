import os

def convert_doc_to_docx(input_dir, output_dir):
    cmd = f'lowriter --convert-to docx --outdir {output_dir} {input_dir}*.doc'
    os.system(cmd)

if __name__ == '__main__':
    convert_doc_to_docx('/home/arcuser/team/bruriah/paintext/documents/', '/home/arcuser/team/bruriah/paintext/docx_documents/')
