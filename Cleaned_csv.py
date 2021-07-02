import pandas as pd
import numpy as np

url = 'data_100000.csv'

tree_row = pd.read_csv(url)


print(tree_row.head())

print(tree_row.shape)

print(tree_row.columns.tolist())

"""https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh
website data of NYC"""
"""to delete ONE column"""
del tree_row['created_at']

print(tree_row.head())

print(tree_row.columns.tolist())

print(tree_row.columns.tolist())

"""to delete several columns with pandas, the inplace change the original dataframe"""
tree_row.drop(columns=['stump_diam', 'block_id', 'curb_loc', 'spc_latin', 'steward', 'zip_city',
                       'borocode', 'cncldist', 'st_assem', 'st_senate', 'nta', 'state',
                       'latitude', 'longitude', 'address'], inplace=True)


print(tree_row.shape)

del tree_row['the_geom']

print(tree_row.shape)
print(tree_row.head(10))


"""trial to test if I could merge some columns:
tree_row['root_problems'] = tree_row['root_stone'] + tree_row['root_grate'] + tree_row['root_other']
but didn't work"""

"""to check if I have null values"""
tree_row.isnull().sum()
print(tree_row.isnull().sum())

"""to change the blank values in 'health', 'spc_common', 'guards', 'sidewalk', 'problems'
"""
print()
print("\n")
tree_row.health = tree_row['health'].fillna('Unknown')
tree_row.spc_common = tree_row['spc_common'].fillna('Unknown')
tree_row.guards = tree_row['guards'].fillna('Unknown')
tree_row.sidewalk = tree_row['sidewalk'].fillna('Unknown')
tree_row.problems = tree_row['problems'].fillna('Unknown')
print(tree_row.isnull().sum())

print(tree_row.dtypes)

"""to replace values 'Yes' and 'No' by Boolean values True or False
replace()
df_trees[column_name] = df_trees[column_name].replace(to_replace='Yes', value=True)
    df_trees[column_name] = df_trees[column_name].replace(to_replace='No', value=False)
    df_trees[column_name] = df_trees[column_name].astype('bool')
so first replace yes to true and no to false, the the column astype('bool')
'root_stone', 'root_grate', 'root_other', 'trnk_wire', 'trnk_light', 'trnk_other', 'brnch_ligh', 
'brnch_shoe', 'brnch_othe',
"""
print(tree_row.columns.tolist())

tree_row['root_stone'] = tree_row['root_stone'].replace(to_replace='Yes', value=True)
tree_row['root_stone'] = tree_row['root_stone'].replace(to_replace='No', value=False)
tree_row['root_stone'] = tree_row['root_stone'].astype('bool')

print(tree_row.root_stone)

tree_row['root_grate'] = tree_row['root_grate'].replace(to_replace='Yes', value=True)
tree_row['root_grate'] = tree_row['root_grate'].replace(to_replace='No', value=False)
tree_row['root_grate'] = tree_row['root_grate'].astype('bool')

tree_row['root_other'] = tree_row['root_other'].replace(to_replace='Yes', value=True)
tree_row['root_other'] = tree_row['root_other'].replace(to_replace='No', value=False)
tree_row['root_other'] = tree_row['root_other'].astype('bool')

tree_row['trnk_wire'] = tree_row['trnk_wire'].replace(to_replace='Yes', value=True)
tree_row['trnk_wire'] = tree_row['trnk_wire'].replace(to_replace='No', value=False)
tree_row['trnk_wire'] = tree_row['trnk_wire'].astype('bool')

tree_row['trnk_light'] = tree_row['trnk_light'].replace(to_replace='Yes', value=True)
tree_row['trnk_light'] = tree_row['trnk_light'].replace(to_replace='No', value=False)
tree_row['trnk_light'] = tree_row['trnk_light'].astype('bool')

tree_row['trnk_other'] = tree_row['trnk_other'].replace(to_replace='Yes', value=True)
tree_row['trnk_other'] = tree_row['trnk_other'].replace(to_replace='No', value=False)
tree_row['trnk_other'] = tree_row['trnk_other'].astype('bool')

tree_row['brnch_ligh'] = tree_row['brnch_ligh'].replace(to_replace='Yes', value=True)
tree_row['brnch_ligh'] = tree_row['brnch_ligh'].replace(to_replace='No', value=False)
tree_row['brnch_ligh'] = tree_row['brnch_ligh'].astype('bool')

tree_row['brnch_shoe'] = tree_row['brnch_shoe'].replace(to_replace='Yes', value=True)
tree_row['brnch_shoe'] = tree_row['brnch_shoe'].replace(to_replace='No', value=False)
tree_row['brnch_shoe'] = tree_row['brnch_shoe'].astype('bool')

tree_row['brnch_othe'] = tree_row['brnch_othe'].replace(to_replace='Yes', value=True)
tree_row['brnch_othe'] = tree_row['brnch_othe'].replace(to_replace='No', value=False)
tree_row['brnch_othe'] = tree_row['brnch_othe'].astype('bool')



"""to remove the duplicate rows drop_duplicate()"""

tree_dedupped = tree_row.drop_duplicates()

print(tree_dedupped)

tree_dedupped.to_csv('cleaned_tree.csv')
