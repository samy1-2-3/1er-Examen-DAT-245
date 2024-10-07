import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler, KBinsDiscretizer

archivo = 'Student_performance_data _.csv'
leer1 = pd.read_csv(archivo)
leer2 = pd.read_csv(archivo)
leer3 = pd.read_csv(archivo)
leer4 = pd.read_csv(archivo)

print("Dataset Normal:")
print(leer1.head())

le = LabelEncoder()

for col in leer1.select_dtypes(include=['object']).columns:
    leer1[col + '_encoded'] = le.fit_transform(leer1[col])

print("\nDataset cambiado con labelencoder:")
print(leer1.head())

ohe = OneHotEncoder(sparse_output=False)

for col in leer2.select_dtypes(include=['object']).columns:
    encoded_features = ohe.fit_transform(leer2[[col]])
    encoded_df = pd.DataFrame(encoded_features, columns=ohe.get_feature_names_out([col]))
    leer2 = leer2.join(encoded_df)
    leer2.drop(col, axis=1, inplace=True)

print("\nDataset cambiado con onehotencoder:")
print(leer2.head())

scaler = MinMaxScaler()

num_cols = leer3.select_dtypes(include=['float64', 'int64']).columns
leer3[num_cols] = scaler.fit_transform(leer3[num_cols])

print("\nDataset cambiado normalizado:")
print(leer3.head())

discretizer = KBinsDiscretizer(n_bins=4, encode='ordinal', strategy='uniform')

df_discretized = pd.DataFrame(discretizer.fit_transform(leer4[num_cols]), columns=[f'{col}_discretizado' for col in num_cols])

leer4 = pd.concat([leer4, df_discretized], axis=1)

print("\nDataset discretizado:")
print(leer4.head())























