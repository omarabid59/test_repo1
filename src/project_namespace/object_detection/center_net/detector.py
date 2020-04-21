import numpy as np
from project_namespace.object_detection.detector_interface import DetectorInterface, DetectorData


class CenterNet(DetectorInterface):
	def __init__(self):
		super().__init__()

	def load_model(self, model_path: str) -> bool:
		"""
		Loads a model file
		"""
		raise NotImplementedError

	def detect(self, image_np: np.ndarray) -> DetectorData:
		raise NotImplementedError

