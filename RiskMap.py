import seaborn as sns
import pandas as pd
import numpy as np

# Create a dataframe (data table)
df = pd.DataFrame(columns=['risk', 'likelihood', 'impact', 'score'])

df['risk']=['users', 'team', 'budget', 'security']

df['likelihood']=[0.2,0.3,0.1,0.5]


df['score']=df['impact']*df['likelihood']
df['impact']=[1,2,7,10]

df['score']=df['impact']*df['likelihood']

scoresPivot=df.pivot('impact', 'likelihood', 'score')
print(scoresPivot)

labelsPivot=df.pivot('impact', 'likelihood', 'risk')
print(labelsPivot)

#replaces no labels with empty strings
labelsPivot.fillna('',inplace=True)

#simple heatmap
p1=sns.heatmap(scoresPivot, cmap="OrRd",annot=labelsPivot, fmt='')
