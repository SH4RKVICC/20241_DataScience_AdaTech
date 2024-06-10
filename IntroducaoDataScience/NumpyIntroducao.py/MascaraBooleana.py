import numpy as np

is_covid_positive = np.array(['Yes', 'No', 'No', 'Yes', 'No', 'Yes'])
mask = (is_covid_positive == 'Yes')
is_covid_positive[mask] = 'C19'
print(is_covid_positive)

