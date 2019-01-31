from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer, StandardScaler


class PipelineCreator:
    imputer_transformer = 'imputer'
    standard_scaler_transformer = 'standard_scaler'

    def __init__(self, list_transformers):
        self.list_transformers = list_transformers
        self.pipeline = None

    def add_custom_transformer(self, transformer_tuple):
        self.list_transformers.append(transformer_tuple)
        return self

    def add_imputer_transformer_by_strategy(self, strategy="median"):
        self.list_transformers.append((self.imputer_transformer, Imputer(strategy=strategy)))
        return self

    def add_standard_scaler_transformer(self):
        self.list_transformers.append((self.standard_scaler_transformer, StandardScaler()))
        return self

    def get_pipeline(self):
        self.pipeline = Pipeline(self.list_transformers)
        return self.pipeline

