class Constraint:
    def __init__(self):
        self._id = None
        self._style_id = None
        self._constraint_type = None
        self._attribute = None
        self._constrain = None
        self._val = None

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_style_id(self):
        return self._style_id

    def set_style_id(self, style_id):
        self._style_id = style_id

    def get_constraint_type(self):
        return self._constraint_type

    def set_constraint_type(self, constraint_type):
        self._constraint_type = constraint_type

    def get_attribute(self):
        return self._attribute

    def set_attribute(self, attribute):
        self._attribute = attribute

    def get_constrain(self):
        return self._constrain

    def set_constrain(self, constrain):
        self._constrain = constrain

    def get_val(self):
        return self._val

    def set_val(self, val):
        self._val = val

class BinaryConstraint(Constraint):
    def __init__(self):
        super().__init__()
        self._reference_object1_id = None
        self._reference_object2_id = None

    def get_reference_object1_id(self):
        return self._reference_object1_id

    def set_reference_object1_id(self, reference_object1_id):
        self._reference_object1_id = reference_object1_id

    def get_reference_object2_id(self):
        return self._reference_object2_id

    def set_reference_object2_id(self, reference_object2_id):
        self._reference_object2_id = reference_object2_id

class UnaryConstraint(Constraint):
    def __init__(self):
        super().__init__()
        self._reference_object_id = None

    def get_reference_object_id(self):
        return self._reference_object_id

    def set_reference_object_id(self, reference_object_id):
        self._reference_object_id = reference_object_id

class CardinalityConstraint(Constraint):
    def __init__(self):
        super().__init__()
        self._item_type = None
        self._min_count = None
        self._max_count = None

    def get_item_type(self):
        return self._item_type

    def set_item_type(self, item_type):
        self._item_type = item_type

    def get_min_count(self):
        return self._min_count

    def set_min_count(self, min_count):
        self._min_count = min_count

    def get_max_count(self):
        return self._max_count

    def set_max_count(self, max_count):
        self._max_count = max_count

class MutexConstraint(Constraint):
    def __init__(self):
        super().__init__()
        self._item_type_1 = None
        self._item_type_2 = None

    def get_item_type_1(self):
        return self._item_type_1

    def set_item_type_1(self, item_type_1):
        self._item_type_1 = item_type_1

    def get_item_type_2(self):
        return self._item_type_2

    def set_item_type_2(self, item_type_2):
        self._item_type_2 = item_type_2

class ImplicationConstraint(Constraint):
    def __init__(self):
        super().__init__()
        self._if_type = None
        self._then_type = None

    def get_if_type(self):
        return self._if_type

    def set_if_type(self, if_type):
        self._if_type = if_type

    def get_then_type(self):
        return self._then_type

    def set_then_type(self, then_type):
        self._then_type = then_type