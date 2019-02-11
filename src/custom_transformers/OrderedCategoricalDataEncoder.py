from .CustomPipelineTransformer import CustomPipelineTransformer
from pipeline import PipelineCreator
from sklearn.preprocessing import LabelEncoder

import pandas as pd


class PipelineFriendlyLabelEncoder(LabelEncoder):

    def fit_transform(self, X, y=None):
        return super().fit_transform(X)


class OrderedCategoricalDataEncoder(CustomPipelineTransformer):
    def __init__(self):
        label_encoder = ("label_encoder", PipelineFriendlyLabelEncoder())
        pipeline_creator = PipelineCreator.PipelineCreator([label_encoder])
        self.pipeline = pipeline_creator.get_pipeline()

    def transform(self, data_frame):
        if isinstance(data_frame, pd.DataFrame):
            res_data_frame = pd.DataFrame()
            for column in data_frame:
                temp_data_frame = data_frame[column]
                print(temp_data_frame.values)
                temp_data_frame = pd.DataFrame(self.pipeline.fit_transform(temp_data_frame.values.ravel()))
                res_data_frame = pd.concat([res_data_frame, temp_data_frame], axis=1)
            return res_data_frame
        raise ValueError("first parameter should be of type pandas DataFrame")
