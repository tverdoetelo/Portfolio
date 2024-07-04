import pandas as pd 
import numpy as np
import seaborn as sb
import scipy.stats as ss
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

name_of_file = 'HappyRabbit.xlsx'
df = pd.read_excel(name_of_file)
# print(df.info())
# print(df.describe())

#Valid format assignment
df['Rating, out of 5'] = df['Rating, out of 5'].astype('int')
df['Price, pounds'] = df['Price, pounds'].astype('int')
df['Reviews'] = df['Reviews'].astype('int')
# print(df.info())

#The summary of unique values
columns = df[['Name','Type','Color','Rating, out of 5','Reviews','Price, pounds','Sale','Price on sale']]
# for column in df:
#     print(len(df[column].unique()), df[column].unique())

#The variety of price
df['Price, pounds'].hist(bins = 29)
plt.title('The variety of price')
plt.xlabel('price')
plt.ylabel('counts')
# plt.savefig('The variety of price for Happy Rabbit Collection.png')
# plt.show()

#the best-selling product
# print(f'the best-selling product: {df[df['Reviews'] == df['Reviews'].max()]}')

#the product with the best rating
# print(f'the product with the best rating: {df[df['Rating, out of 5'] == df['Rating, out of 5'].max()]}')

#the product with the highest price
# print(f'the product with the highest price: {df[df['Price, pounds'] == df['Price, pounds'].max()]}')

#Sorting
df = df.sort_values(by=['Type'], inplace=False, ascending=False)

#vibrator’s percentage of all sales
sum_reviews = df['Reviews'].sum(axis=0)
df_vibrator = df.loc[df['Type'] == 'Vibrator']
sum_reviews_vibrator = df_vibrator['Reviews'].sum(axis=0)
percentage_vibrator = (sum_reviews_vibrator / sum_reviews)*100
# print(round(proportion_vibrator, 2))

#the product with the best rating among vibrators
# print(f'the product with the best rating among vibrators: {df_vibrator[df_vibrator['Rating, out of 5'] == df_vibrator['Rating, out of 5'].max()]}')

#Correlation for numeric columns
df_numerised = df.drop(['Name','Type','Color','Sale','Price on sale'], axis = 1)
columns_numerised = df_numerised[['Rating, out of 5','Reviews','Price, pounds',]]
correlation_matrix = df_numerised.corr(method = 'pearson')
# print(correlation_matrix)

def heatmap(columns, name): #Creating heatmap
    corr = columns.corr('pearson')
    sb.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation between numeric features for Happy Rabbit Collection')
    plt.savefig(name)
    plt.show()

# heatmap(columns_numerised, 'Correlation between numeric features for Happy Rabbit Collection.png')

df_category = df.drop(['Name','Sale','Price on sale'], axis = 1)
columns_category = df_category[['Type','Color','Rating, out of 5','Reviews','Price, pounds']]

def cramers_V(var1, var2):
    crosstab = np.array(pd.crosstab(var1, var2))
    stats = chi2_contingency(crosstab)[0]
    cram_V = stats / (np.sum(crosstab) * (min(crosstab.shape) - 1))
    return cram_V

def cramers_col(column_name):
    col = pd.Series(np.empty(df_category.columns.shape), index=df_category.columns, name=column_name)
    for row in df_category:
        cram = cramers_V(df_category[column_name], df_category[row])
        col[row] = round(cram, 2)
    return col

print(df_category.apply(lambda column: cramers_col(column.name)))

df_category['Type']=df_category['Type'].astype('category').cat.codes
df_category['Color']=df_category['Color'].astype('category').cat.codes

print(df_category.corr())

