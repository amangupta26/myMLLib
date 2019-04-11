from pipeline import PipelineCreator
from .CustomPipelineTransformer import CustomPipelineTransformer
from utils import pandas_util
import pandas as pd


class NumericAttributeStandardizer(CustomPipelineTransformer):
    def __init__(self):
        pipeline_creator = PipelineCreator.PipelineCreator([]).add_standard_scaler_transformer()
        self.pipeline = pipeline_creator.get_pipeline()

    def transform(self, data_frame):
        if isinstance(data_frame, pd.DataFrame):
            res_data_frame =  pd.DataFrame(self.pipeline.fit_transform(data_frame))
            res_data_frame.columns = pandas_util.get_data_frame_column_names_by_list(data_frame)
            return res_data_frame
        raise ValueError("first parameter should be of type pandas DataFrame")
