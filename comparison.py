import pandas as pd
import numpy as np
import os

def compare_values():
    athena = pd.read_csv(os.path.join(file_loc['compare_dir'], athena_file), float_precision='round_trip')
    redshift = pd.read_excel(os.path.join(file_loc['compare_dir'], redshift_file))

    athena.columns = map(str.lower, athena.columns)
    redshift.columns = map(str.lower, redshift.columns)

    if athena.shape == redshift.shape:
        print('File is match in rows / columns')
        print("Athena:" + str(athena.shape))
        print("Redshift:" + str(redshift.shape))

        compare_results = athena

        comparison_values = athena.values == redshift.values

        rows,cols=np.where(comparison_values==False)
        rows1,cols1=np.where(comparison_values==True)

        for item in zip(rows,cols):
            compare_results.iloc[item[0], item[1]] = '{} --> {}'.format(athena.iloc[item[0], item[1]],redshift.iloc[item[0], item[1]])

        for item in zip(rows1,cols1):
            compare_results.iloc[item[0], item[1]] = 'TRUE'

        final_compare_results = compare_results

        rows2,cols2=np.where(final_compare_results== 'varchar --> character varying')
        for item in zip(rows2,cols2):
            final_compare_results.iloc[item[0], item[1]] = 'TRUE'

        rows3,cols3=np.where(final_compare_results== 'decimal(38,6) --> numeric')
        for item in zip(rows3,cols3):
            final_compare_results.iloc[item[0], item[1]] = 'TRUE'

        rows4,cols4=np.where(final_compare_results== 'timestamp --> timestamp without time zone')
        for item in zip(rows4,cols4):
            final_compare_results.iloc[item[0], item[1]] = 'TRUE'

        final_compare_results.to_csv(os.path.join(file_loc['target_dir'], file_loc['target_fname']),index=False,header=True)
    else:
        print('File does not match in rows / columns')
        print("Athena:" + str(athena.shape))
        print("Redshift:" + str(redshift.shape))