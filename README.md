# learning
Some sql, py, dax examples for learning, kaggle stuff

# Regex cheet sheet
For use in pandas use df['variable'] = df['variable'].replace('regex to replace', 'what to replace with', regex=True)

### Examples

Replace every simbol AFTER / .
df['variable'] = df['variable'].replace('/[^/]*$', '', regex=True)
