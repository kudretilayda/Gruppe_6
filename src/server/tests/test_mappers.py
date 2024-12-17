from src.server.bo.ClothingItem import ClothingItem
from src.server.bo.ClothingType import ClothingType
from src.server.bo.Constraints import UnaryConstraint
from src.server.bo.Outfit import Outfit
from src.server.bo.Style import Style
from src.server.bo.User import User
from src.server.bo.Wardrobe import Wardrobe
from src.server.db.ClothingItemMapper import ClothingItemMapper
from src.server.db.ClothingTypeMapper import ClothingTypeMapper
from src.server.db.ConstraintMapper import ConstraintMapper
from src.server.db.OutfitMapper import OutfitMapper
from src.server.db.StyleMapper import StyleMapper
from src.server.db.UserMapper import UserMapper
from src.server.db.WardrobeMapper import WardrobeMapper


def test_clothing_item_mapper():
    print("\nTesting ClothingItemMapper...")
    with ClothingItemMapper() as mapper:
        try:
            # Create test
            item = ClothingItem()
            item.set_wardrobe_id(1)
            item.set_clothing_type(1)
            item.set_item_name("Test Item")

            created_item = mapper.insert(item)
            print(f"Created item with ID: {created_item.get_id()}")

            # Read test
            found_item = mapper.find_by_key(created_item.get_id())
            print(f"Found item: {found_item}")

            # Update test
            found_item.set_item_name("Updated Item")
            mapper.update(found_item)
            print("Updated item name")

            # Delete test
            mapper.delete(found_item)
            print("Deleted test item")

        except Exception as e:
            print(f"Error in ClothingItemMapper test: {str(e)}")


def test_clothing_type_mapper():
    print("\nTesting ClothingTypeMapper...")
    with ClothingTypeMapper() as mapper:
        try:
            # Create test
            type_obj = ClothingType()
            type_obj.set_name("Test Type")
            type_obj.set_usage("Test Usage")

            created_type = mapper.insert(type_obj)
            print(f"Created type with ID: {created_type.get_id()}")

            # Read test
            found_type = mapper.find_by_key(created_type.get_id())
            print(f"Found type: {found_type}")

            # Delete test
            mapper.delete(found_type)
            print("Deleted test type")

        except Exception as e:
            print(f"Error in ClothingTypeMapper test: {str(e)}")


def test_user_mapper():
    print("\nTesting UserMapper...")
    with UserMapper() as mapper:
        try:
            # Create test
            user = User()
            user.set_firstname("Test")
            user.set_lastname("User")
            user.set_google_id("test123")
            user.set_email("test@test.com")

            created_user = mapper.insert(user)
            print(f"Created user with ID: {created_user.get_id()}")

            # Read test
            found_user = mapper.find_by_key(created_user.get_id())
            print(f"Found user: {found_user}")

            # Delete test
            mapper.delete(found_user)
            print("Deleted test user")

        except Exception as e:
            print(f"Error in UserMapper test: {str(e)}")
def test_style_mapper():
    print("\nTesting StyleMapper...")
    with StyleMapper() as mapper:
        try:
            # Create test
            style = Style()
            style.set_style_features("Test Features")
            style.set_style_constraints([
                "Constraint1",
                "Constraint2",
                "Constraint3"
            ])

            created_style = mapper.insert(style)
            print(f"Created style with ID: {created_style.get_id()}")

            # Read test
            found_style = mapper.find_by_key(created_style.get_id())
            print(f"Found style: {found_style}")

            # Delete test
            mapper.delete(found_style)
            print("Deleted test style")

        except Exception as e:
            print(f"Error in StyleMapper test: {str(e)}")


def test_wardrobe_mapper():
    print("\nTesting WardrobeMapper...")
    with WardrobeMapper() as mapper:
        try:
            # Create test
            wardrobe = Wardrobe()
            wardrobe.set_id(1)  #
            created_wardrobe = mapper.insert(wardrobe)
            print(f"Created wardrobe with ID: {created_wardrobe.get_id()}")

            # Read test
            found_wardrobe = mapper.find_by_key(created_wardrobe.get_id())
            print(f"Found wardrobe: {found_wardrobe}")

            # Delete test
            mapper.delete(found_wardrobe)
            print("Deleted test wardrobe")

        except Exception as e:
            print(f"Error in WardrobeMapper test: {str(e)}")


def test_outfit_mapper():
    print("\nTesting OutfitMapper...")
    with OutfitMapper() as mapper:
        try:
            # Create test
            outfit = Outfit()
            outfit.set_outfit_name("Test Outfit")
            outfit.set_style(1)  # Assuming style with ID 1 exists

            created_outfit = mapper.insert(outfit)
            print(f"Created outfit with ID: {created_outfit.get_id()}")

            # Read test
            found_outfit = mapper.find_by_key(created_outfit.get_id())
            print(f"Found outfit: {found_outfit}")

            # Delete test
            mapper.delete(found_outfit)
            print("Deleted test outfit")

        except Exception as e:
            print(f"Error in OutfitMapper test: {str(e)}")


def test_constraint_mapper():
    print("\nTesting ConstraintMapper...")
    with ConstraintMapper() as mapper:
        try:
            # Create test
            constraint = UnaryConstraint(
                style_id=1,  # Assuming style with ID 1 exists
                reference_object_id=1,
                attribute="color",
                condition="equals",
                val="blue"
            )

            created_constraint = mapper.insert(constraint)
            print(f"Created constraint with ID: {created_constraint.get_id()}")

            # Read test
            found_constraint = mapper.find_by_key(created_constraint.get_id())
            print(f"Found constraint: {found_constraint}")

            # Delete test
            mapper.delete(found_constraint)
            print("Deleted test constraint")

        except Exception as e:
            print(f"Error in ConstraintMapper test: {str(e)}")


def main():
    print("Starting Mapper Tests...")

    # Führe alle Tests aus
    test_user_mapper()
    test_wardrobe_mapper()
    test_clothing_type_mapper()
    test_clothing_item_mapper()
    test_style_mapper()
    test_outfit_mapper()
    test_constraint_mapper()

    print("\nAll tests completed!")


if __name__ == "__main__":
    main()