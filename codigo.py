import pandas as pd
import seaborn as sns

df = pd.read_csv('gasolina.csv', sep=',')
grafico = sns.lineplot(data=df, x='dia',y='venda')
grafico.get_figure().savefig('teste.png')