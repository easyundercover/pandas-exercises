#print("Hello World") #02.01 create a script

import pandas as pd
#data_frame = pd.read_csv(".learn/assets/pokemon_data.csv") #03 datasets 
#print(data_frame)

#ages = [23,45,7,34,6,63,36,78,54,34] #04 series
#data = pd.Series(ages)
#print(data)

#datetime = pd.date_range(start='05/01/2021', end='05/12/2021') #04.1 date range
#print(datetime)

#my_series = pd.Series([2, 4, 6, 8, 10]) #04.2 series apply
#def dividebytwo(x):
#    return x/2
#print(my_series.apply(dividebytwo))

#data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porche", "Cayenne", "White"]] #05 dataframes
#df = pd.DataFrame(data,columns=['Brand','Model','Color'])
#print(df)

#data = [  #05.1 dataframe dict
#    { 
#        "brand": "Toyota", 
#        "make": "Corolla",
#        "color": "Blue"
#    },
#    {
#        "brand": "Ford", 
#        "make": "K",
#        "color": "Yellow"
#    },
#    {
#        "brand": "Porche", 
#        "make": "Cayenne",
#        "color": "White"
#    },
#        {
#        "brand": "Tesla", 
#        "make": "Model S",
#        "color": "Red"
#    }
#]
#df = pd.DataFrame.from_dict(data)
#print(df)

#data_frame = pd.read_csv('.learn/assets/pokemon_data.csv') #5.2 dataframe iloc
#print(data_frame.iloc[133,6])

#print(data_frame.head(3)) #05.3 file head

#print(data_frame.tail(3)) #05.4 dataframe tail

#print(data_frame[['Name','Type 1']][0:10]) #05.5 columns

#print(data_frame.loc[data_frame['Attack'] > 80]) #05.6 loc function

#print(len(data_frame.loc[data_frame['Legendary'] == True])) #05.7 filter and count

df = pd.read_csv('.learn/assets/us_baby_names_right.csv') #06.1 clean datasets
#print(df.head(5))

#del df["Unnamed: 0"] #06.1 remove column
#print(df.head(5))
#df = df.iloc[: , 1:] #Esto también lo hace

#print(df['Gender'].value_counts()) #06.2 value counts

#result = df.groupby(['Name']).sum() #06.3 group by
#print(len(result))