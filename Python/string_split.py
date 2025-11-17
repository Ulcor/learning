import pandas as pd

d = {'text': ['/rawwr', 'Users/dasdsa', 'afsfasf/sfaf']}
df = pd.DataFrame(data=d)

df['text'] = df['text'].str.split('/').str.join(' ')
print(df)