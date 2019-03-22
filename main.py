
import pandas as pd
import matplotlib.pyplot as plt

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