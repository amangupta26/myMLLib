from .CustomPipelineTransformer import CustomPipelineTransformer
from pipeline import PipelineCreator
from sklearn.preprocessing import LabelBinarizer

import pandas as pd

class PipelineFriendlyLabelBinarizer(LabelBinarizer):

    def fit_transform(self, X, y=None):
        return super().fit_transform(X)

class OneHotEncoder(CustomPipelineTransformer):
    def __init__(self):
        one_hot_encoder = ("one_hot_encoder", PipelineFriendlyLabelBinarizer())
        pipeline_creator = PipelineCreator.PipelineCreator([one_hot_encoder ])
        self.pipeline = pipeline_creator.get_pipeline()

    def transform(self, data_frame):
        if isinstance(data_frame, pd.DataFrame):
            res_data_frame = pd.DataFrame()
            for column in data_frame:
                temp = self.pipeline.fit_transform(data_frame[column])
                temp_data_frame = pd.DataFrame(temp[:,:temp.shape[1] - 1])
                temp_data_frame.columns = [column + "_" + str(i) for i in range(temp_data_frame.shape[1])]
                res_data_frame = pd.concat([res_data_frame, temp_data_frame], axis=1)
            return res_data_frame
        raise ValueError("first parameter should be of type pandas DataFrame")
