from mapper.clothing_type_mapper import ClothingTypeMapper
from bo.clothing_type import ClothingType

class ClothingTypeService:
    @staticmethod
    def get_all_types():
        return ClothingTypeMapper.find_all()

    @staticmethod
    def create_type(type_data):
        clothing_type = ClothingType()
        clothing_type.set_name(type_data['name'])
        clothing_type.set_usage(type_data['usage'])
        return ClothingTypeMapper.insert(clothing_type)

    @staticmethod
    def get_type_by_id(type_id):
        return ClothingTypeMapper.find_by_id(type_id)

    @staticmethod
    def delete_type(type_id):
        return ClothingTypeMapper.delete(type_id)