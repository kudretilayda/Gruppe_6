from mapper.style_mapper import StyleMapper
from bo.style import Style

class StyleService:
    @staticmethod
    def get_all_styles():
        return StyleMapper.find_all()

    @staticmethod
    def get_style_by_id(style_id):
        return StyleMapper.find_by_id(style_id)

    @staticmethod
    def create_style(style_data):
        style = Style()
        style.set_features(style_data['features'])
        for constraint_data in style_data.get('constraints', []):
            constraint = StyleService._create_constraint(constraint_data)
            style.add_constraint(constraint)
        return StyleMapper.insert(style)

    @staticmethod
    def _create_constraint(constraint_data):
        # Helper method to create appropriate constraint objects
        constraint_type = constraint_data['type']
        if constraint_type == 'cardinality':
            from bo.constraint import Cardinality
            constraint = Cardinality()
            constraint.set_min_count(constraint_data.get('min_count', 0))
            constraint.set_max_count(constraint_data.get('max_count', float('inf')))
        elif constraint_type == 'mutex':
            from bo.constraint import Mutex
            constraint = Mutex()
        elif constraint_type == 'implication':
            from bo.constraint import Implication
            constraint = Implication()
        return constraint