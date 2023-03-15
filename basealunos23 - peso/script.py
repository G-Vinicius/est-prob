import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("basealunos23-copy.xlsx")
count_40to50 = 0
count_50to60 = 0
count_60to70 = 0
count_70to80 = 0
count_80to90 = 0
count_90to100 = 0

for i in df['Peso']:
  if (i >= 40 and i < 50):
    count_40to50 += 1
  elif (i >= 50 and i < 60):
    count_50to60 += 1
  elif (i >= 60 and i < 70):
    count_60to70 += 1
  elif (i >= 70 and i < 80):
    count_70to80 += 1
  elif (i >= 80 and i < 90):
    count_80to90 += 1
  elif (i >= 90 and i < 100):
    count_90to100 += 1
  else:
    print("")

total = count_40to50 + count_50to60 + count_60to70 + count_70to80 + count_80to90 + count_90to100

row1 = ["[40-50)", "[50-60)", "[60-70)", "[70-80)", "[80-90)", "[90-100)", "Total"]
row2 = [count_40to50, count_50to60, count_60to70, count_70to80, count_80to90, count_90to100, total]
dfilt = {'peso': row1, 'contagem por pessoa': row2}
new_df = pd.DataFrame(dfilt)
print(new_df)


plt.bar(new_df["peso"], new_df["contagem por pessoa"])
plt.title('Pessoas por faixa de peso')
plt.xlabel('Faixa de peso')
plt.ylabel('Número de pessoas')
plt.show()