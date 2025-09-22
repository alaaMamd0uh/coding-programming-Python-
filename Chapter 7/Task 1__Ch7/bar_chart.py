
import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Category': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Values': [25, 18, 32, 14, 27, 35, 21, 29, 19, 23]
}
df=pd.DataFrame(data)


plt.bar(df['Category'], df['Values'])
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()

minVal=df['Values'].min()#  minimum value = 14 (cat D) weakest performance
maxVal=df['Values'].max()# #  maximum value = 35 (cat F)  strongest performance
meanVal=df['Values'].mean()## #  mean is about = 24.3 shows the general trend of the data

print(f"min= {minVal}") ### lowest value
print(f"max= {maxVal}") # highest value
print(f"Mean= {meanVal}") # average of the data

