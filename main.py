import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data.head())
print()

one_hot = pd.DataFrame()
one_hot['robot'] = (data['whoAmI'] == 'robot').astype(bool)
one_hot['human'] = (data['whoAmI'] == 'human').astype(bool)

print(one_hot.head())
