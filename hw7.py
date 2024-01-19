
import pandas as pd
import random
# Создание DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
# Просмотр первых пяти строк DataFrame
data.head()
# Преобразование DataFrame в формат "one hot"
data_one_hot = pd.get_dummies(data, columns=['whoAmI'])
# Показ первых пяти строк преобразованного DataFrame
data_one_hot.head()


# Без get_dummies
import pandas as pd
# Воссоздание исходного DataFrame
lst = ['robot'] * 10 + ['human'] * 10
data = pd.DataFrame({'whoAmI': lst})
# Создание столбцов "one hot" вручную
data_one_hot_manual = pd.DataFrame()
data_one_hot_manual['whoAmI_human'] = data['whoAmI'].apply(lambda x: 1 if x == 'human' else 0)
data_one_hot_manual['whoAmI_robot'] = data['whoAmI'].apply(lambda x: 1 if x == 'robot' else 0)
# Показ первых пяти строк преобразованного DataFrame
data_one_hot_manual.head()