import pandas as pd
import numpy  as np


data = pd.read_csv('../../Mortality-dataset/2005_test.csv')

print('csv loaded.')

attributes = ['manner_of_death' ,
             'education_1989_revision' ,
             'detail_age' ,
             'place_of_death_and_decedents_status' ,
             'month_of_death' , 'race', 'sex', 'marital_status']

data = data[attributes]
# manner_of_death NaN not allowed.#
#education_1989_revision 99 or NaN not allowed.#
#detail_age 9 or NaN not allowed.#
#place_of_death_and_decenddant_status 9 or NaN not allowed.#
#month_of_death NaN not allowed.
#race NaN not allowed.
#sex NaN not allowed.
#marital_status NaN not allowed.
data = data[ ((data['manner_of_death'].notnull()) &
             ((data['education_1989_revision'] != 99 ) & (data['education_1989_revision'].notnull())) &
             ( (data['detail_age'] != 9) & (data['detail_age'].notnull())) &
             ((data['place_of_death_and_decedents_status'] != 9 ) & (data['place_of_death_and_decedents_status'].notnull())) &
             ((data['month_of_death'].notnull())) &
              ((data['race'].notnull())) &
              ((data['sex'].notnull())) &
              ((data['marital_status'].notnull()))) ]

print(len(data))

sex_codes = { 'M' : 1 , 'F' : 2}

for item in data.index.get_values():
    data.at[item,'sex'] = sex_codes[data.at[item,'sex']]

print('gender encoded.')

marital_codes =  { 'D' : 1 , 'M' :2 , 'S' : 3 , 'U' : 4 , 'W' : 5}

for item in data.index.get_values():
    data.at[item,'marital_status'] = marital_codes[data.at[item,'marital_status']]

print('marital_status encoded.')

#print(data)
data.to_pickle('../data_2005_test.pkl')
#print(len(data))
#print(data.ix[2]['sex'])
#for item in data:
#    print(item)

#print(data)
