from utils import pandas_util, encode_data_util
from pipeline import PipelineCreator
from custom_transformers import  OrderedCategoricalDataEncoder, OneHotEncoder, NumericAttributeStandardizer
# import numpy as np
import pandas as pd


# os_util.get_zip_file_by_url("https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.tgz", "/Users/mngup/ml/housing.tgz")

# os_util.untar_file("/Users/mngup/ml/housing.tgz", "/Users/mngup/ml")

# df = pandas_util.load_data_frame_from_csv_file("/Users/mngup/ml/housing.csv")
df = pandas_util.load_data_frame_from_csv_file("/Users/mngup/ml/house_prices_kaggle_train.csv")

# print(df.info())

# Missing data implies that house does not have lott frontage
df['LotFrontage'].fillna(0, inplace=True)
# Missing date can be assumed tthat house does not have an alley
df['Alley'].fillna('NA', inplace=True)
# Missing data can be assumed that MasVnrType does not exists
df['MasVnrType'].fillna('None', inplace=True)
# Missing data can be assumed that MasVnrArea is zero
df['MasVnrArea'].fillna(0, inplace=True)
# Missing data can be assumed that BsmtQual not exists
df['BsmtQual'].fillna('NA', inplace=True)
# Missing data can be assumed that BsmtCond not exists
df['BsmtCond'].fillna('NA', inplace=True)
# Fill one row with No if other basement features are available
df.loc[df.BsmtQual.notna() & df.BsmtExposure.isna(), 'BsmtExposure'] = 'No'
# Missing data can be assumed that BsmtExposure not exists
df['BsmtExposure'].fillna('NA', inplace=True)
df['BsmtFinType1'].fillna('NA', inplace=True)
df.loc[332, 'BsmtFinType2'] = 'LwQ'
df['BsmtFinType2'].fillna('NA', inplace=True)

df['Electrical'].fillna('SBrkr', inplace=True)

df['FireplaceQu'].fillna('NA', inplace=True)

df['GarageType'].fillna('NA', inplace=True)
df['GarageYrBlt'].fillna(df['GarageYrBlt'].min(), inplace=True)
df['GarageFinish'].fillna('NA', inplace=True)
df['GarageQual'].fillna('NA', inplace=True)
df['GarageCond'].fillna('NA', inplace=True)
df['PoolQC'].fillna('NA', inplace=True)
df['Fence'].fillna('NA', inplace=True)
df['MiscFeature'].fillna('NA', inplace=True)


# Defining six columns for basement finished type: GLQ, ALQ, BLQ, Rec, LwQ, Unf. Along with area for each
default_list = [0 for x in range(df.shape[0])]
df['GLQ'] = pd.Series(default_list.copy(),  index=df.index)
df['ALQ'] = pd.Series(default_list.copy(),  index=df.index)
df['BLQ'] = pd.Series(default_list.copy(),  index=df.index)
df['Rec'] = pd.Series(default_list.copy(),  index=df.index)
df['LwQ'] = pd.Series(default_list.copy(),  index=df.index)

for index, row in df.iterrows():
    if row['BsmtFinType1'] != 'NA' and row['BsmtFinType1'] != 'Unf':
        df.loc[index, row['BsmtFinType1']] = int(row['BsmtFinSF1'])
    if row['BsmtFinType2'] != 'NA' and row['BsmtFinType2'] != 'Unf':
        df.loc[index, row['BsmtFinType2']] += int(row['BsmtFinSF2'])


# for index, row in df.iterrows():
#     if df.loc[index, 'GLQ'] + df.loc[index, 'ALQ'] + df.loc[index, 'BLQ'] + df.loc[index, 'Rec'] + df.loc[index, 'LwQ'] + df.loc[index, 'BsmtUnfSF'] != df.loc[index, 'TotalBsmtSF']:
#         print(index)

# print(df['GLQ'].value_counts())
# print(df['ALQ'].value_counts())
# print(df['BLQ'].value_counts())
# print(df['Rec'].value_counts())
# print(df['LwQ'].value_counts())




# Merge (condition1, condition2), (Exterior1st,Exterior2nd)  and create a new feature

# Convert date columns into numerical attribute by setting oldest date to 0 and increase by 1 for each year/month/week/day
# YearBuilt, YearRemodAdd, GarageYrBlt, MoSold, YrSold
df['YearBuilt'] = df['YearBuilt'] - df['YearBuilt'].min()
df['YearRemodAdd'] = df['YearRemodAdd'] - df['YearRemodAdd'].min()
df['GarageYrBlt'] = (df['GarageYrBlt'] - df['GarageYrBlt'].min()).astype(int)
di = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9:"September", 10:"October", 11:"November", 12:"December" }
df['MoSold'] = df['MoSold'].map(di)
df['YrSold'] = df['YrSold'] - df['YrSold'].min()






one_hot_encoding_columns = ["MSSubClass", "MSZoning", "Street", "Alley", "LotShape", "LandContour", "Utilities", "LotConfig",
                            "LandSlope", "Neighborhood", "BldgType", "HouseStyle", "RoofStyle", "RoofMatl", "ExterQual", "ExterCond",
                            "Foundation", "Heating", "CentralAir", "Electrical", "Functional", "PavedDrive", "SaleType", "SaleCondition", "MoSold"]
int_encoding_columns = ["BsmtQual", "BsmtCond", "BsmtExposure", "HeatingQC", "KitchenQual", "FireplaceQu", "PoolQC"]
standardize_columns = ["LotFrontage", "LotArea", "1stFlrSF", "2ndFlrSF", "LowQualFinSF", "GrLivArea", "BsmtFullBath", "BsmtHalfBath", "FullBath", "HalfBath", "BedroomAbvGr", "KitchenAbvGr", "TotRmsAbvGrd", "Fireplaces", "GarageCars", "GarageArea", "WoodDeckSF", "OpenPorchSF", "EnclosedPorch", "3SsnPorch", "ScreenPorch", "PoolArea", "MiscVal"]
no_op_columns = ["OverallQual", "OverallCond"]
delete_columns = ["TotalBsmtSF"]

# df_integer_encoded = OrderedCategoricalDataEncoder.OrderedCategoricalDataEncoder().transform(df[int_encoding_columns])
# df_one_hot_encoded = OneHotEncoder.OneHotEncoder().transform(df[one_hot_encoding_columns])
df_standardized = NumericAttributeStandardizer.NumericAttributeStandardizer().transform(df[standardize_columns])
print(df_standardized.columns)



# print(df_test)


#
# rows_count = df.shape[0]
# print(pandas_util.get_nan_columns_map(df))
# columns_to_remove = ['Alley', 'GarageYrBlt']
# df = FeatureRemover.FeatureRemover(columns_to_be_removed=columns_to_remove).transform(df)
# df['LotFrontage'].fillna(0, inplace=True)
# df['MasVnrType'].fillna('None', inplace=True)
# df['MasVnrArea'].fillna(0, inplace=True)
# df['BsmtQual'].fillna('NA', inplace=True)
# df['BsmtCond'].fillna('NA', inplace=True)
# df['BsmtExposure'].fillna('NA', inplace=True)
# df['BsmtFinType1'].fillna('NA', inplace=True)
# df['BsmtFinType2'].fillna('NA', inplace=True)
# df['FireplaceQu'].fillna('NA', inplace=True)
# df['GarageType'].fillna('NA', inplace=True)
# df['GarageFinish'].fillna('NA', inplace=True)
# df['GarageQual'].fillna('NA', inplace=True)
# df['GarageCond'].fillna('NA', inplace=True)
#
# df['PoolQC'].fillna('NA', inplace=True)
#
# df['Fence'].fillna('NA', inplace=True)
#
# df['MiscFeature'].fillna('NA', inplace=True)
#
# df['Alley'].fillna('NA', inplace=True)
#
# df['Electrical'].fillna('SBrkr', inplace=True)
#
#
# print(df['PoolArea'].value_counts())



# df = FeatureRemover.FeatureRemover(['Alley', 'MiscFeature', 'Fence', 'PoolQC', 'FireplaceQu']).transform(df)
# df = pd.DataFrame(np.random.randint(1,6,size=(10, 2)))
# temp_dict = {1: "A", 2: "B", 3: "C", 4: "D", 5:   "E"}
# df = pd.concat([df[0].replace(temp_dict), df[1].replace(temp_dict)], axis=1)
# print(df.info())
# print(df.head)



# print(encode_data_util.one_hot_encode_single_column(df, "ocean_proximity"))

# plot_util.plot_all_features_of_pandas_data_frame(df)

# X, y = pandas_util.get_training_data_label_by_label_columns(df, ['median_house_value'])
# X_train, X_test, y_train, y_test = pandas_util.split_data_frame_train_test(X, y)

# pipeline = PipelineCreator.PipelineCreator([]).add_custom_transformer().get_pipeline()
# df_tr = pipeline.fit_transform(df)
# df_test = NumericAttributeStandardizer.NumericAttributeStandardizer().transform(df[['longitude']])
# df['ocean_proximity_1'] = df['ocean_proximity']
# df_test = OrderedCategoricalDataEncoder.OrderedCategoricalDataEncoder().transform(df[['ocean_proximity', 'ocean_proximity_1']])
# categorical_attributes_label_encoding = ['PoolQC', 'Fence', 'KitchenQual', 'FireplaceQu', 'GarageQual', 'GarageCond']
# df_test = OrderedCategoricalDataEncoder.OrderedCategoricalDataEncoder().transform(df[['KitchenQual']])
#
# print(df_test)
# print(df_test.shape)
# print(type(df_test))







# df["income_cat"] = np.ceil(df["median_income"] / 1.5)
# df["income_cat"].where(df["income_cat"] < 5, 5.0, inplace=True)
#
# df_train, df_test = pandas_util.stratified_shuffle_split_data_frame_train_test(df, df["income_cat"])
# X_train, y_train = pandas_util.get_training_data_label_by_label_columns(df_train, ['median_house_value'])
# df.drop("income_cat", axis=1, inplace=True)
# print(df.shape, X_train.shape, y_train.shape)










