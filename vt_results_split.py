import pandas as pd
from pathlib import Path

my_dir = Path('C:\Python\Validation_Test_split\Input')

first_file = 'Adapt_Inno3-CE_650.xlsx'

all_data = pd.DataFrame()

for i in Path.iterdir(my_dir):
    df = pd.read_excel(i, header=None)

    if first_file not in str(i):
        df = df.iloc[3:,2:]
    else:
        df = df.iloc[:,2:]

    all_data = all_data.append(df)

output_file = Path('C:\Python\Validation_Test_split\Output' + 'Results_' + first_file)
all_data.to_excel(output_file, index=False, header=False)