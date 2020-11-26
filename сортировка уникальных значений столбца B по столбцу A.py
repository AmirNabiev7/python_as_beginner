import pandas as pd
xlsx_1 = pd.read_excel('file.xlsx')
l = xlsx_1.groupby('UNIT')['SAFT'].apply(list)
l.to_excel('output_file.xlsx')


import pandas as pd, os
os.chdir('/home/user/Documents/mir')
xlsx_1 = pd.read_excel('PBS_System.xlsx')
l = xlsx_1.groupby(['UNIT', 'SAFT'])['SEISMT'].apply(set)
l.to_excel("output_list1.xlsx")
