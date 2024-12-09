import json
from typing import List, Dict, Tuple

class ConstraintHelper:
    """Hilfsklasse für die Verwaltung und Überprüfung von Style-Constraints"""

    @staticmethod
    def create_binary_constraint(item1_type: int, item2_type: int, relation: str) -> str:
        """Erstellt einen binären Constraint zwischen zwei Kleidungstypen"""
        constraint = {
            "type1": item1_type,
            "type2": item2_type,
            "relation": relation  # z.B. "must_match", "must_not_match", "requires"
        }
        return json.dumps(constraint)

    @staticmethod
    def create_cardinality_constraint(item_type: int, min_count: int, max_count: int) -> str:
        """Erstellt einen Kardinalitäts-Constraint für einen Kleidungstyp"""
        constraint = {
            "type": item_type,
            "min": min_count,
            "max": max_count
        }
        return json.dumps(constraint)

    @staticmethod
    def create_color_constraint(colors: List[str]) -> str:
        """Erstellt einen Farb-Constraint"""
        constraint = {
            "allowed_colors": colors
        }
        return json.dumps(constraint)

    @staticmethod
    def check_binary_constraint(constraint: Dict, items: List[Dict]) -> Tuple[bool, str]:
        """Überprüft einen binären Constraint"""
        type1 = constraint["type1"]
        type2 = constraint["type2"]
        relation = constraint["relation"]

        items_of_type1 = [item for item in items if item["type_id"] == type1]
        items_of_type2 = [item for item in items if item["type_id"] == type2]

        if relation == "must_match":
            # Prüft ob die Farben übereinstimmen
            if items_of_type1 and items_of_type2:
                colors1 = set(item.get("color", "") for item in items_of_type1)
                colors2 = set(item.get("color", "") for item in items_of_type2)
                if not colors1.intersection(colors2):
                    return False, f"Farben von Typ {type1} und {type2} stimmen nicht überein"

        elif relation == "must_not_match":
            # Prüft ob die Farben sich unterscheiden
            if items_of_type1 and items_of_type2:
                colors1 = set(item.get("color", "") for item in items_of_type1)
                colors2 = set(item.get("color", "") for item in items_of_type2)
                if colors1.intersection(colors2):
                    return False, f"Farben von Typ {type1} und {type2} dürfen nicht übereinstimmen"

        elif relation == "requires":
            # Prüft ob der erforderliche Typ vorhanden ist
            if items_of_type1 and not items_of_type2:
                return False, f"Typ {type1} erfordert Typ {type2}"

        return True, "Constraint erfüllt"

    @staticmethod
    def check_cardinality_constraint(constraint: Dict, items: List[Dict]) -> Tuple[bool, str]:
        """Überprüft einen Kardinalitäts-Constraint"""
        item_type = constraint["type"]
        min_count = constraint["min"]
        max_count = constraint["max"]

        items_of_type = [item for item in items if item["type_id"] == item_type]
        count = len(items_of_type)

        if count < min_count:
            return False, f"Mindestens {min_count} Items vom Typ {item_type} erforderlich"
        if count > max_count:
            return False, f"Maximal {max_count} Items vom Typ {item_type} erlaubt"

        return True, "Constraint erfüllt"

    @staticmethod
    def check_style_compatibility(items: List[Dict], style_constraints: List[Dict]) -> Tuple[bool, List[str]]:
        """Überprüft ob ein Set von Kleidungsstücken allen Style-Constraints entspricht"""
        messages = []
        for constraint in style_constraints:
            if constraint["constraint_type"] == "BINARY":
                valid, msg = ConstraintHelper.check_binary_constraint(
                    json.loads(constraint["value"]), items)
                if not valid:
                    messages.append(msg)

            elif constraint["constraint_type"] == "CARDINALITY":
                valid, msg = ConstraintHelper.check_cardinality_constraint(
                    json.loads(constraint["value"]), items)
                if not valid:
                    messages.append(msg)

        return len(messages) == 0, messages

    @staticmethod
    def suggest_fixes(items: List[Dict], failed_constraints: List[str]) -> List[str]:
        """Schlägt Verbesserungen für nicht erfüllte Constraints vor"""
        suggestions = []
        for failure in failed_constraints:
            if "Mindestens" in failure:
                suggestions.append(f"Fügen Sie weitere Kleidungsstücke hinzu: {failure}")
            elif "Maximal" in failure:
                suggestions.append(f"Entfernen Sie einige Kleidungsstücke: {failure}")
            elif "Farben" in failure:
                suggestions.append(f"Wählen Sie Kleidungsstücke mit passenden Farben: {failure}")
            else:
                suggestions.append(f"Anpassung erforderlich: {failure}")

        return suggestions

    @staticmethod
    def validate_outfit(outfit_items: List[Dict], style_constraints: List[Dict]) -> Dict:
        """Validiert ein komplettes Outfit gegen alle Style-Constraints"""
        valid, messages = ConstraintHelper.check_style_compatibility(outfit_items, style_constraints)
        
        result = {
            "is_valid": valid,
            "messages": messages
        }

        if not valid:
            result["suggestions"] = ConstraintHelper.suggest_fixes(outfit_items, messages)

        return result