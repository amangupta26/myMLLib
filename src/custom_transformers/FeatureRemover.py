from pipeline import PipelineCreator
from .CustomPipelineTransformer import CustomPipelineTransformer
import pandas as pd

class FeatureRemover(CustomPipelineTransformer):

    def __init__(self, columns_to_be_removed):
        pipeline_creator = PipelineCreator.PipelineCreator([]).add_standard_scaler_transformer()
        self.pipeline = pipeline_creator.get_pipeline()
        self.columns_to_be_removed = columns_to_be_removed

    def transform(self, data_frame):
        if isinstance(data_frame, pd.DataFrame):
            return data_frame.drop(columns=self.columns_to_be_removed, axis=1)
        raise ValueError("first parameter should be of type pandas DataFrame")
