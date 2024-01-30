# Analytical task: to build a model to predict the cost of an apartment.

import pandas as pd
import numpy as np
import seaborn as sb
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('home_price.csv')
columns = df[['last_price','total_area','rooms','ceiling_height','floors_total','living_area','floor','is_apartment','studio','open_plan',
           'kitchen_area','balcony','airports_nearest','cityCenters_nearest','parks_around3000','parks_nearest','ponds_around3000','ponds_nearest']]
print(df.info()) #information about raw data
# print(df.describe()) #information about raw data

df = df.replace({True : 1, False : 0}) #format replacement from bool to int

def heatmap(columns, name): #Creation of thermal map where correlation and annotation were calculated (correlation value)
    corr = columns.corr('pearson') #Create a variable for correlated features
    sb.heatmap(corr, annot=True, cmap='coolwarm')
    plt.savefig(name)
    plt.show()

heatmap(columns, 'Корреляция исходных данных.png')

# Data cleaning

df_mean = df.mean() 
df_std = df.std() 
 
def Hampel_test(df_orig):
    vals = df_orig.copy()
    difference = np.abs(vals.median()-vals)
    median_abs_deviation = difference.median()
    threshold = 3 * median_abs_deviation
    outlier_idx = difference > threshold
    vals[outlier_idx] = np.nan
    return(vals)

df = Hampel_test(df).fillna(df.mean().to_dict()) #replacement from NaN to average means
columns = df[['last_price','total_area','rooms','ceiling_height','floors_total','living_area','floor','is_apartment','studio','open_plan',
           'kitchen_area','balcony','airports_nearest','cityCenters_nearest','parks_around3000','parks_nearest','ponds_around3000','ponds_nearest']]

print (df.info()) #data information after cleaning
# print(df.describe()) #data information after cleaning

heatmap(columns, 'Correlation of data after cleaning.png')

# Identification of relevant and marginal parameters

df_unique = df.nunique ()
print(df_unique)

# in the column 'parks_around3000' there are only two unique values, 0 and the average we have substituted, which does not carry any significant information, so this parameter for further study is excluded.

data = df.drop(['is_apartment','studio','open_plan','balcony','airports_nearest','parks_nearest','parks_around3000','ponds_nearest'], axis = 1)
columns = data[['last_price','total_area','rooms','ceiling_height','floors_total','living_area','floor','kitchen_area','cityCenters_nearest','ponds_around3000']]

print (data.info()) #information about data after the selection of significant features
# print(data.describe()) #information about data after the selection of significant features

heatmap(columns, 'Correlation of data by significant parameters.png')

#addition of a new variable - the cost of m2, based on the detection of a good correlation between "total area" and "cost of apartments"
last_price = data['last_price'].tolist()
total_area = data['total_area'].tolist()
price_m2 = []
for i in range(len(last_price)):
  price_m2.append(last_price[i] / total_area[i])

data['price_m2'] = price_m2 
columns = data[['last_price','total_area','rooms','ceiling_height','floors_total','living_area','floor','kitchen_area','cityCenters_nearest','ponds_around3000', 'price_m2']]

# Hypothesis testing

def value_data(data1, data0, hypothesis):
    t_statistic, p_value = stats.ttest_ind(data1['last_price'], data0['last_price'])
    print('T-statictic', t_statistic)
    print('P-value', p_value)
    if p_value>0.05:
        print(f'There are no statistically significant differences, hypothesis H0{hypothesis} is rejected, hypothesis Н1{hypothesis} is accepted.\n')
    else:
        print(f'There are statistically significant differences, hypothesis H0{hypothesis} is accepted.\n') 

#Hypothesis1: 
# H01: prices for apartments in the center and far from the center are significantly different
# H11: prices for apartments in the center and far from the center are not significantly different

data_downtown = data[data['cityCenters_nearest']<=3000]
data_suburb = data[data['cityCenters_nearest']>3000]

value_data(data_downtown,data_suburb, 1)

#Hypothesis2: 
# H02: prices for apartments near the pond and far from the pond differ significantly
# H12: prices for apartments near the pond and far from the pond not differ significantly

data_pond1 = data[data['ponds_around3000']>0]
data_pond0 = data[data['ponds_around3000']==0]

value_data(data_pond1,data_pond0, 2)

#Hypothesis3: 
# H03: prices for apartments with large and small kitchen differ significantly
# H13: Prices for apartments with large and small kitchen not differ significantly

data_kitchen_big = data[data['kitchen_area']>5]
data_kitchen_small = data[data['kitchen_area']<=5]

value_data(data_kitchen_big,data_kitchen_small, 3)

#Hypothesis4:
# H04: prices of apartments with high and low ceilings differ significantly
# H14: prices of apartments with high and low ceilings not differ significantly

data_ceiling_high = data[data['ceiling_height']>3]
data_ceiling_low = data[data['ceiling_height']<=3]

value_data(data_ceiling_high,data_ceiling_low, 4)

#Hypothesis5:
# H05: prices for apartments in houses with floors and floors are significantly different
# H15: prices for apartments in houses with floors and floors are not significantly different

data_floors_total1 = data[data['floors_total']>5]
data_floors_total0 = data[data['floors_total']<=5]

value_data(data_floors_total1,data_floors_total0, 5)

#Hypothesis6:
# H06: prices for apartments on the ground floor from apartments on other floors differ significantly
# H16: prices for apartments on the ground floor from apartments on other floors not differ significantly

data_floor1 = data[data['floor']==1]
data_floor = data[data['floor']>1]

value_data(data_floor1,data_floor, 6)

#Hypothesis7:
# H07: prices for apartments with different number of rooms differ significantly
# H17: prices for apartments with different number of rooms not differ significantly

# sb.boxplot(data=data, x=data['rooms'], y=data['last_price'])
# plt.savefig('Mean values and confidence intervals.png')
# plt.show()

data_rooms_sorted = data.groupby('rooms') 

def value_rooms(): #counting values only from the original dataframe
    counter = 0
    for i in range (0, 6): #ounting values only from data for apartments for which data on the number of rooms were originally
        for j in range (i+1, 6):
            data_room_i = data_rooms_sorted.get_group(i)
            data_room_j = data_rooms_sorted.get_group(j)
            stats.ttest_ind(data_room_i['last_price'], data_room_j['last_price'])
            t_statistics,p_value = stats.ttest_ind(data_room_i['last_price'], data_room_j['last_price'])
            print(t_statistics, p_value)
            if p_value>0.05:
                print(f'Statistically significant differences between apartments with the number of individual rooms {i} and {j} are not present')
            else:
                counter = counter +1
                print(f'Statistically significant differences between apartments with the number of individual rooms {i} and {j} are') 
    if counter != 15:
        print(f'No statistically significant differences, H07 is rejected, H17 is accepted.\n')
    else:
        print(f'Statistically significant differences exist, the hypothesis H07 is accepted.\n') 

value_rooms()

#All hypotheses advanced are accepted

#Apartment cost prediction

def prognose():
    square = int(input('\nWhat is the total area of the apartment (in m2)?\n'))
    room = int(input('\nHow many rooms in the apartment?\n'
                   'Enter values from 0 to 5\n'
                   'Enter 0 if this is a studio apartment\n'))
    kitchen = 0
    if room != 0: 
        kitchen = int(input('\nWhat is the area of the kitchen (in m2)?\n'))
    center = int(input('\nHow far is the apartment from the center (m)?\n'
                        'Enter 99999, if information does not exist\n'))
    data_prognose = data.loc[((data['rooms'] == room) & (data['kitchen_area'] <= kitchen) & (data['cityCenters_nearest'] <= center))]
    price_m2_mean = np.mean(data_prognose['price_m2'])
    price_m2_std = np.std(data['price_m2'])
    price_apartment = square * price_m2_mean
    confidence = 0.95
    z = stats.norm.ppf((1 + confidence) / 2)
    margin_error = z * price_m2_std * square
    price_apartment_confidence_interval_low = (price_apartment - margin_error)/1000000
    price_apartment_confidence_interval_up = (price_apartment + margin_error)/1000000
    print(f'Prognosed cost of the apartment from {round(price_apartment_confidence_interval_low,3)} to {round(price_apartment_confidence_interval_up,3)} million rubles')

prognose()