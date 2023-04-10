import pandas as pd
import numpy as np
import re
import warnings
warnings.filterwarnings("ignore")

def read_data_from_csv():
    hotels=pd.read_csv('zomato.csv')
    return hotels


def remove_unwanted_columns():
    #DO NOT REMOVE FOLLOWING LINE
    #call read_data_from_csv() function to get dataframe
    hotels=read_data_from_csv()
    
    return hotels.drop(["address","phone"],axis = 1)


def rename_columns():
    #DO NOT REMOVE FOLLOWING LINE
    #call remove_unwanted_columns() function to get dataframe
    
    
    #task2: rename columns,  only these columns are allowed in the dataset
    # 1.	Id
    # 2.	Name
    # 3.	online_order
    # 4.	book_table
    # 5.	rating
    # 6.	votes
    # 7.	location
    # 8.	rest_type
    # 9.	dish_liked
    # 10.	cuisines
    # 11.	approx_cost
    # 12.	type
    hotels=read_data_from_csv()
    hotels.drop(['address','phone'] , axis=1,inplace=True)
    hotels = hotels.rename(columns={
        'name': 'name',
        'rate': 'rating',
        'votes': 'votes',
        'approx_cost(for two people)': 'approx_cost',
        'listed_in(type)':'type'})
    return hotels



#task3: handle  null values of each column
def null_value_check():
    #DO NOT REMOVE FOLLOWING LINE
    #call rename_columns() function to get dataframe
    hotels=rename_columns()
    
    #deleting null values of name column
    hotels.dropna(subset=['name'], inplace=True)
    #handling null values of online_order
    hotels['online_order'].fillna(value='NA', inplace=True)
    #handling null values of book_table
    hotels['book_table'].fillna(value='NA', inplace=True)
    #handling null values of rating
    hotels['rating'].fillna(value=0, inplace=True)
    #handling null values of votes
    hotels['votes'].fillna(value=0, inplace=True)
    #handling null values of location
    hotels['location'].fillna(value='NA', inplace=True)
    #handling null values of rest_type
    hotels['rest_type'].fillna(value='NA', inplace=True)
    #handling null values of dishliked
    hotels['dish_liked'].fillna(value='NA', inplace=True)
    #handling null values of cuisines
    hotels['cuisines'].fillna(value='NA', inplace=True)
     #handling null values of approxcost
    hotels['approx_cost'].fillna(value=0, inplace=True)
    #handling null values of type
    hotels['type'].fillna(value='NA',inplace=True)

    return hotels


#task4 #find duplicates in the dataset
def find_duplicates():
    #DO NOT REMOVE FOLLOWING LINE
    #call null_value_check() function to get dataframe
    hotels=null_value_check()
    hotels = hotels.drop_duplicates(keep='first')
    hotels = hotels.dropna()
    
    
    #droping the duplicates value keeping the first
    return hotels


#task5 removing irrelevant text from all the columns
def removing_irrelevant_text():
    #DO NOT REMOVE FOLLOWING LINE
    #call find_duplicates() function to get dataframe
    hotels= find_duplicates()
  
    
    hotels=hotels[hotels['name'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['online_order'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['book_table'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['rating'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['votes'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['location'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['rest_type'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['dish_liked'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['cuisines'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['approx_cost'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['type'].str.contains('RATED|Rated')==False]


    return hotels


#task6: check for unique values in each column and handle the irrelevant values
def check_for_unique_values():
    #DO NOT REMOVE FOLLOWING LINE
    #call removing_irrelevant_text() function to get dataframe
    hotels=removing_irrelevant_text()
    #hotels = hotels[hotels['book_table'].isin(['YES', 'NO'])] 
    
   # Remove any unwanted characters from the ratings string
  
    hotels['online_order'] = hotels['online_order'].apply(lambda x: re.sub('[^a-zA-Z]', '', x))
    

# only keep values that are 'Yes' or 'No'
    hotels = hotels[hotels['online_order'].isin(['Yes', 'No'])]
    
    #hotels['rating'] = hotels['rating'].apply(lambda x: re.sub('[^0-9.]', '', x))
    
    
    hotels['rating'] = [s[:-2] for s in hotels['rating']]
    #hotels['rating'] = [s[:-1] for s in hotels['rating']] 
    
    # convert the column to a float type
    #hotels['rating'] = hotels['rating'].replace('N', 0)
   # hotels['rating'] = [x for x in  hotels['rating'] if x != '']
   
    hotels['rating'] = hotels['rating'].dropna('')
    hotels['rating'] = hotels['rating'].astype(str)
    hotels['rating'] = hotels['rating'].replace('N',0 ) 
    hotels.replace('', float(), inplace=True)
   
    return hotels


#task7: remove the unknown character from the dataset and export it to "zomatocleaned.csv"
def remove_the_unknown_character():
    #DO NOT REMOVE FOLLOWING LINE
    #call check_for_unique_values() function to get dataframe
    dataframe=check_for_unique_values()


    #remove unknown character from dataset
    
  
    
    
  
    
    #dataframe['name'] = dataframe['name'].str.replace(r'[^!@#\$%\^\&*\)]+$ [^\w\s]|_|\d|[^\x00-\x7F]', ' ')
    #dataframe['type'] = dataframe['type'].str.replace(r'[^!@#\$%\^\&*\)]+$ [^\w\s]|_|\d|[^\x00-\x7F]',  ' ')
   
  
    dataframe['name'] = dataframe['name'].str.replace(r'[Ãx][^A-Za-z]+', '')
    dataframe['type'] = dataframe['type'].str.replace(r'[Ãx][^A-Za-z]+', '')
    
    #dataframe['name'] = dataframe['name'].apply(lambda x: re.sub(r'[^!@#\$%\^\&*\)]+$ [^\w\s]|_|\d|[^\x00-\x7F]', '', x))
    #dataframe['type'] = dataframe['type'].apply(lambda x: re.sub(r'[^!@#\$%\^\&*\)]+$ [^\w\s]|_|\d|[^\x00-\x7F]', '', x))
    
    #dataframe['location'] = dataframe['location'].apply(lambda x: re.sub(r'[^!@#\$%\^\&*\)]+$ [^\w\s]|_|\d|[^\x00-\x7F]', '', x))

    
   # dataframe['name'] = dataframe['name'].str.replace('\s+', ' ')
    #dataframe['type'] = dataframe['type'].str.replace('\s+', ' ')
    #dataframe['name'] = dataframe['name'].str.replace(",", '')
    #dataframe['type'] = dataframe['type'].str.replace(",", '')
  
 
    #export cleaned Dataset to newcsv file named "zomatocleaned.csv"
    dataframe.to_csv('zomatocleaned.csv')
    
    
   
    return dataframe


#check if mysql table is created using "zomatocleaned.csv"
#Use this final dataset and upload it on the provided database for performing analysis in  MySQL
#To Run this task first Run the appliation for Terminal to create table named 'Zomato' and then run test.
def start():
    remove_the_unknown_character()

def task_runner():
    start()
