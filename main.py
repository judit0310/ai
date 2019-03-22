
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk

education = pd.read_excel('data/Data_Extract_From_Education_Statistics_-_All_Indicators.xlsx',index_col=0, sheet_name="Data",parse_cols="A,C:G")

income = pd.read_excel('data/Data_Extract_From_Poverty_and_Equity(1).xlsx',sheet_name="Data",index_col=0,parse_cols="A,C:G")
population = pd.read_excel('data/Data_Extract_From_Poverty_and_Equity(1).xlsx',sheet_name="Data",index_col=0,parse_cols="A,H:L")

print(education.columns)


def shortenColumnName(dataframe):
    for c in dataframe.columns:
        dataframe.rename(columns= {c : str(c)[-4:-1]},inplace=True)
    return dataframe

education = shortenColumnName(education).dropna()
income = shortenColumnName(income).dropna()
population = shortenColumnName(population).dropna()

plt.plot(population)
plt.legend(population.columns)
plt.show()
plt.plot(education.replace("..",0))
plt.legend(education.columns)
plt.show()
plt.plot(income.replace("..",0))
plt.legend(income.columns)
plt.show()
data = []
print(population.index)
for c in population.columns:
    for y in population.index:
       # print(population.loc[y,c])
        newdata ={"Year":y,"population":population.loc[y,c],"income":income.loc[y,c],"education":education.loc[y,c],"country":c}
        newSeries = pd.Series(newdata,index=["Year","population","income","education","country"])
        print(newSeries)
        data.append(newSeries)
newDataFrame = pd.DataFrame(data)

from sklearn.cluster import KMeans

without = newDataFrame.drop(["country","Year"],axis=1)

from sklearn.preprocessing import StandardScaler
scaled = StandardScaler().fit_transform(without.replace("..",0))
pred = KMeans(n_clusters=4).fit_predict(scaled)

result = newDataFrame["cluster"] = pd.Series(pred, index=newDataFrame.index)
print(result)