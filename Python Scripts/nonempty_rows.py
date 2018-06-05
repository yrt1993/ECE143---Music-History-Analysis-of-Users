import os
import pandas as pd

main = os.getcwd()
path = os.getcwd() + '\UserHisNonEmptyRows'
new_path = os.getcwd() + '\UserHistory2011'

os.chdir(path)

assert os.path.exists(path), "Warning! Directory must contain 'UserHisNonEmpty' folder!' 

if not os.path.exists(new_path):
    os.makedirs(new_path)
#UTC Time
begin_year = 1293840000 #Jan 1, 2011
end_year =   1325376000 #Jan 1, 2012
    
for filename in os.listdir(path):
    user_data = pd.read_csv(filename, delimiter = '\t', index_col = '0')
    user_2011 = user_data.loc[begin_year:end_year]
    user_2011.reset_index(inplace=True) #Resets the row names to integer names again.
    new_filename = filename[:-4] + '_2011.csv'
    user_2011.to_csv(new_path + '\\'+ new_filename, sep = '\t', index = False)
    
os.chdir(main)
