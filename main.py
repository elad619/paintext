import os
import pandas as pd

def convert_doc_to_docx(input_dir, output_dir):
    cmd = f'lowriter --convert-to docx --outdir {output_dir} {input_dir}*.doc'
    os.system(cmd)

CONTENT = 'Content'
BLOOD_THINNERS_TYPES = ['אספירין', 'מיקרופירין', 'קרטיה', 'פלביקס', 'קלופידרוגל', 'קסרלטו', 'אליקוויס', 'קומדין', 'קלקסל'] # TODO two typos found קסלטו, אפסירין
BLOOD_THINNERS = 'מדללי דם'
NOT_FOUND = 'ללא'

def transform_value(content):
    for bt in BLOOD_THINNERS_TYPES:
        if bt in content:
            return bt
    if BLOOD_THINNERS in content:
        return BLOOD_THINNERS
    return NOT_FOUND

def blood_thinners():

    file_path = 'pain_data.csv'
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    for index, row in df.iterrows():
        df.at[index, 'blood_thinners'] = str(transform_value(row[CONTENT]))
    # print(df)
    # print(df[CONTENT][10])
    special = df[df['blood_thinners'] == 'מדללי דם']
    print(special)

if __name__ == '__main__':
    blood_thinners()
    # convert_doc_to_docx('/home/arcuser/team/bruriah/paintext/documents/', '/home/arcuser/team/bruriah/paintext/docx_documents/')
