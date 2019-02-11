from pipeline import PipelineCreator
from custom_transformers.CustomPipelineTransformer import CustomPipelineTransformer
import pandas as pd


class NumericAttributeStandardizer(CustomPipelineTransformer):
    def __init__(self):
        pipeline_creator = PipelineCreator.PipelineCreator([]).add_standard_scaler_transformer()
        self.pipeline = pipeline_creator.get_pipeline()

    def transform(self, data_frame):
        if isinstance(data_frame, pd.DataFrame):
            return pd.DataFrame(self.pipeline.fit_transform(data_frame))
        raise ValueError("first parameter should be of type pandas DataFrame")
