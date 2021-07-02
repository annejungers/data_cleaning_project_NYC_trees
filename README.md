# data_cleaning_project_NYC_trees

Objectives of the mission 

be able to use pandas + be able to clean a dataset


What & Why

the NYC population has to go to the nearest tree in their street and gather information about that tree. 

This is all in an effort to make the population aware that nature is important, even in big Metropolis like NYC. 

Need to clean the messy data registered by the NYC people about the tree

Description

Clean the data:

1). To ask yourself the right questions and select the right columns and remove the redundant columns
del
or
to remove more than one colunms in the original datafram : 
tree_raw.drop(columns=['stump_diam', 'block_id', 'curb_loc', 'spc_latin', 'steward', 'zip_city',
                       'borocode', 'cncldist', 'st_assem', 'st_senate', 'nta', 'state',
                       'latitude', 'longitude'], inplace=True)

2). To figure out if there are any missing value in the dataframe, 
and sum up the total for each column
df.isnull().sum()

3). Replace ‘ ‘ value by ‘Unknow’  (in “Health for example”)
tree_row.health = tree_row['health'].fillna('Unknown')
tree_row.spc_common = tree_row['spc_common'].fillna('Unknown')
tree_row.guards = tree_row['guards'].fillna('Unknown')
tree_row.sidewalk = tree_row['sidewalk'].fillna('Unknown')
tree_row.problems = tree_row['problems'].fillna('Unknown')

4). Put Boolean True or False to replace No or Yes 
df_trees[column_name] = df_trees[column_name].replace(to_replace='Yes', value=True)
    df_trees[column_name] = df_trees[column_name].replace(to_replace='No', value=False)
    df_trees[column_name] = df_trees[column_name].astype('bool')
so first replace yes to true and no to false, the the column astype('bool')
ex
tree_row['root_stone'] = tree_row['root_stone'].replace(to_replace='Yes', value=True)
tree_row['root_stone'] = tree_row['root_stone'].replace(to_replace='No', value=False)
tree_row['root_stone'] = tree_row['root_stone'].astype('bool')

5). To see if you find some duplicate rows
tree_dedupped = tree_row.drop_duplicates()

6). To convert the file into csv
tree_dedupped.to_csv('cleaned_tree.csv')

