import pandas as pd
X = pd.DataFrame(
  {'city': ['London', 'London', 'Paris', 'Sallisaw'],
    'title': ["His Last Bow", "How Watson Learned the Trick",
      "A Moveable Feast", "The Grapes of Wrath"],
    'expert_rating': [5, 3, 4, 5],
    'user_rating': [4, 5, 4, 3]})
    

from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import OneHotEncoder

column_trans = ColumnTransformer(
    [('categories', OneHotEncoder(dtype='int'), ['city'])],
    remainder='passthrough', verbose_feature_names_out=False)

column_trans.fit_transform(X)

column_trans.get_feature_names_out()

column_trans.transform(X).toarray()


from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_selector
ct = ColumnTransformer([
      ('scale', StandardScaler(),
      make_column_selector(dtype_include=np.number)),
      ('onehot',
      OneHotEncoder(),
      make_column_selector(pattern='city', dtype_include=object))])
ct.fit_transform(X)


