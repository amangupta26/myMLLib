from abc import ABC, abstractmethod


class CustomPipelineTransformer(ABC):

    @abstractmethod
    def transform(self, data_frame):
        return