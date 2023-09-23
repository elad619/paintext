import pandas as pd

from parser_columns.anesthetics_sensitivity import AnestheticsSensitivity
from parser_columns.contrast_materials_sensitivity import ContrastMaterialsSensitivity

if __name__ == '__main__':
    file_path = 'pain_data.csv'
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    anesthetics = AnestheticsSensitivity()
    contrast = ContrastMaterialsSensitivity()

    for index, row in df.iterrows():
        document_content = row['Content']
        res = anesthetics.parse_document(document_content)
        # print(res)

# from parser_columns.blood_thinners import BloodThinners
#
#
# def convert_doc_to_docx(input_dir, output_dir):
#     cmd = f'lowriter --convert-to docx --outdir {output_dir} {input_dir}*.doc'
#     os.system(cmd)
#
# CONTENT = 'Content'
# BLOOD_THINNERS_TYPES = ['אספירין', 'מיקרופירין', 'קרטיה', 'פלביקס', 'קלופידרוגל', 'קסרלטו', 'אליקוויס', 'קומדין', 'קלקסל'] # TODO two typos found קסלטו, אפסירין
# BLOOD_THINNERS = 'מדללי דם'
# NOT_FOUND = 'ללא'
#
# def transform_value(content):
#     for bt in BLOOD_THINNERS_TYPES:
#         if bt in content:
#             return bt
#     if BLOOD_THINNERS in content:
#         return BLOOD_THINNERS
#     return NOT_FOUND
#
# def blood_thinners():
#
#     file_path = 'pain_data.csv'
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv(file_path)
#     for index, row in df.iterrows():
#         df.at[index, 'blood_thinners'] = str(transform_value(row[CONTENT]))
#     # print(df)
#     # print(df[CONTENT][10])
#     special = df[df['blood_thinners'] == 'מדללי דם']
#     print(special)

# if __name__ == '__main__':
#     file_path = 'pain_data.csv'
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv(file_path)
#     no_sens = 0
#     other_no_sense = 0
#     no_sensetivity_sentences = ['וכי אין רגישות לחומר ניגוד ואין רגישות לחומרי הרדמה',
#                                 'אין רגישות לחומר ניגוד וחומרי הרדמה', ]
#     for index, row in df.iterrows():
#         document_content = row['Content']
#         if 'אין רגישות לחומר ניגוד וחומרי הרדמה' in document_content:
#             no_sens += 1
#         else:
#             print(document_content)
#             print('_____________________________________________________________________________________________')
#             other_no_sense += 1
#     print(no_sens)
#     print(other_no_sense)
#     print(df)
#     # special = df[df['blood_thinners'] == 'מדללי דם']
#     # print(special)
#     # convert_doc_to_docx('/home/arcuser/team/bruriah/paintext/documents/', '/home/arcuser/team/bruriah/paintext/docx_documents/')
