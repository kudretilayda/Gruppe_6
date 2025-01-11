from src.server.bo.BusinessObject import BusinessObject


class Style(BusinessObject):

    def __init__(self):
        super().__init__()
        self._style_id = int
        self._style_features = ""
        self.style_constraints = []
        self.clothing_type = []

    def get_style_id(self):
        return self._style_id

    def set_style_id(self, style_id: int):
        self._style_id = style_id

    def get_style_features(self):
        return self._style_features

    def set_style_features(self, features: str):
        self._style_features = features

    def get_style_constraints(self):
        return self.style_constraints

    