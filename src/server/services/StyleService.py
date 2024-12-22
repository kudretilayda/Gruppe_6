# server/services/StyleService.py
from server.db.StyleMapper import StyleMapper
from server.bo.Style import Style

class StyleService:
    def __init__(self):
        self._mapper = StyleMapper()

    def create_style(self, name: str, description: str, created_by: str) -> Style:
        style = Style()
        style.set_style_name(name)
        style.set_style_description(description)
        style.set_created_by(created_by)
        return self._mapper.insert(style)

    def get_style(self, style_id: str) -> Style:
        return self._mapper.find_by_id(style_id)

    def delete_style(self, style_id: str) -> bool:
        style = self.get_style(style_id)
        if style:
            self._mapper.delete(style)
            return True
        return False
