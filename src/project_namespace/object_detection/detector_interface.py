import numpy as np


class DetectorData:
    def __init__(self):
        self.bbs: np.ndarray = np.zeros(shape=(1, 0, 4))
        self.classes: np.ndarray = np.zeros(shape=(1, 0, 4))
        self.scores: np.ndarray = np.zeros(shape=(1, 0, 4))


class DetectorInterface:
	def __init__(self):
		self.__data = DetectorData()

	def load_model(self, model_path: str) -> bool:
		"""
		Loads a model file
		"""
		raise NotImplementedError

	def detect(self, image_np: np.ndarray) -> DetectorData:
		raise NotImplementedError
