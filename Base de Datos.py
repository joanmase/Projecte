import pandas as pd
'''
instal·lar pandas i openpyxl
'''

path = 'Pelis_series.xlsx'
df=pd.read_excel(path)
'''
pd.read_excel(  on esta a l'ordinador, 
                sheet_name = 'nom de la fulla excel',
                usecols = ['primera columna que volem usar','...','...']
                )
Més a : https://pandas.pydata.org/docs/user_guide/io.html#excel-files
'''

new_dict = df.to_dict()

print(new_dict)

