import pandas as pd
import numpy as np
import seaborn as sb
import scipy as sp
import matplotlib
from scipy import stats
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.pyplot import figure

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

matplotlib.rcParams['figure.figsize'] = (12,8)

df = pd.read_csv('movies.csv')
columns = df[['name','rating','genre','year','released','score','votes','director',
              'writer','star','country','budget','gross','company','runtime']]
# print(df.info())

#Deleting empty lines
df = df.dropna()
# print(df.info())

#Valid format assignment
df['budget'] = df['budget'].astype('int')
df['gross'] = df['gross'].astype('int')
df['runtime'] = df['runtime'].astype('int')
# print(df.info())

#Sorting
df = df.sort_values(by=['gross'], inplace=False, ascending=False)
# print(df)

#Deleting duplicates & ouliers
df = df.drop_duplicates()
df.boxplot(column=['gross'], grid= False , color='black')
plt.show()
df = df.loc[df['gross'] > 0] 
# print(df.info())

#Drawing scatter plot: budget & gross / scores & gross earning correlation

def scatter_plot(columns,col1,col2,title,xname,yname,name): #Creating scatter plot
    plt.scatter(x=col1, y=col2)
    plt.title(title)
    plt.xlabel(xname)
    plt.ylabel(yname)
    sb.regplot(x=xname, y=yname, data=df, scatter_kws={'color':'red'}, line_kws={'color':'blue'})
    plt.savefig(name)
    plt.show()

scatter_plot(columns,df['budget'],df['gross'],'Budget & gross earnings correlation','budget','gross','Budget & gross earnings correlation.png')
scatter_plot(columns,df['score'],df['gross'],'Score & gross earnings correlation','score','gross','Score & gross earnings correlation.png')

#Correlation for Movies
data_heatmap = df.drop(['name','rating','genre','released','director','writer','star','country','company',], axis = 1)
columns = data_heatmap[['year','score','votes','budget','gross','runtime']]

correlation_matrix = data_heatmap.corr(method = 'pearson')
# print(correlation_matrix)

def heatmap(columns, name): #Creating heatmap
    corr = columns.corr('pearson')
    sb.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation between movie features')
    plt.savefig(name)
    plt.show()

heatmap(columns, 'Correlation between numeric features.png')

df_numerised = df
for col_name in df_numerised.columns:
    if (df_numerised[col_name].dtype == 'object'):
        df_numerised[col_name] = df_numerised[col_name].astype('category')
        df_numerised[col_name] = df_numerised[col_name].cat.codes
# print(df_numerised.info())

data_heatmap = df_numerised
columns = df[['name','rating','genre','year','released','score','votes','director',
              'writer','star','country','budget','gross','company','runtime']]
heatmap(columns, 'Correlation between all movie features.png')

correlation_matrix = df_numerised.corr(method = 'pearson')
correlation_pairs = correlation_matrix.unstack()
sorted_corr_pairs = correlation_pairs.sort_values()
# print(sorted_corr_pairs)

high_corr_pairs = sorted_corr_pairs[((sorted_corr_pairs) < 1) & ((sorted_corr_pairs) > 0.5)]
print(high_corr_pairs)
