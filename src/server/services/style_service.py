from typing import List, Optional, Dict
import logging
from src.server.db.StyleMapper import StyleMapper
from src.server.db.ConstraintMapper import ConstraintMapper
from src.server.bo.Style import Style
from src.server.bo.Constraints import (
    ConstraintRule, UnaryConstraint, BinaryConstraint,
    MutexConstraint, ImplicationConstraint, CardinalityConstraint
)

class StyleService:
    """Service-Klasse für alle Style bezogenen Operationen"""

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.style_mapper = StyleMapper()
        self.constraint_mapper = ConstraintMapper()

    def create_style(self, name: str, features: Dict, constraints: List[Dict]) -> Style:
        """Erstellt einen neuen Style mit Constraints"""
        try:
            # Style erstellen
            style = Style()
            style.set_name(name)
            style.set_style_features(features)
            created_style = self.style_mapper.insert(style)

            # Constraints hinzufügen
            for constraint_data in constraints:
                constraint = self._create_constraint(created_style.get_id(), constraint_data)
                self.constraint_mapper.insert(constraint)

            self.logger.info(f"Created style: {created_style.get_id()} with {len(constraints)} constraints")
            return created_style

        except Exception as e:
            self.logger.error(f"Error creating style: {str(e)}")
            raise

    def get_style_by_id(self, style_id: int) -> Optional[Style]:
        """Holt einen Style mit allen zugehörigen Constraints"""
        try:
            style = self.style_mapper.find_by_key(style_id)
            if style:
                # Constraints laden
                constraints = self.constraint_mapper.find_by_style_id(style_id)
                style.set_style_constraints(constraints)
            return style
        except Exception as e:
            self.logger.error(f"Error getting style {style_id}: {str(e)}")
            raise

    def get_all_styles(self) -> List[Style]:
        """Holt alle Styles mit ihren Constraints"""
        try:
            styles = self.style_mapper.find_all()
            # Für jeden Style die Constraints laden
            for style in styles:
                constraints = self.constraint_mapper.find_by_style_id(style.get_id())
                style.set_style_constraints(constraints)
            return styles
        except Exception as e:
            self.logger.error(f"Error getting all styles: {str(e)}")
            raise

    def update_style(self, style: Style) -> Style:
        """Aktualisiert einen Style und seine Constraints"""
        try:
            # Style aktualisieren
            updated_style = self.style_mapper.update(style)
            
            # Alte Constraints löschen
            old_constraints = self.constraint_mapper.find_by_style_id(style.get_id())
            for constraint in old_constraints:
                self.constraint_mapper.delete(constraint)
                
            # Neue Constraints speichern
            for constraint in style.get_style_constraints():
                self.constraint_mapper.insert(constraint)

            self.logger.info(f"Updated style: {style.get_id()}")
            return updated_style

        except Exception as e:
            self.logger.error(f"Error updating style {style.get_id()}: {str(e)}")
            raise

    def delete_style(self, style_id: int) -> bool:
        """Löscht einen Style und alle zugehörigen Constraints"""
        try:
            style = self.get_style_by_id(style_id)
            if style:
                # Erst Constraints löschen
                constraints = self.constraint_mapper.find_by_style_id(style_id)
                for constraint in constraints:
                    self.constraint_mapper.delete(constraint)
                    
                # Dann Style löschen
                self.style_mapper.delete(style)
                self.logger.info(f"Deleted style: {style_id}")
                return True
            return False
        except Exception as e:
            self.logger.error(f"Error deleting style {style_id}: {str(e)}")
            raise

    def _create_constraint(self, style_id: int, constraint_data: Dict) -> ConstraintRule:
        """Erstellt ein Constraint-Objekt aus Dictionary-Daten"""
        constraint_type = constraint_data.get('type')
        
        if constraint_type == 'unary':
            return UnaryConstraint(
                style_id=style_id,
                reference_object_id=constraint_data['reference_object_id'],
                attribute=constraint_data['attribute'],
                condition=constraint_data['condition'],
                value=constraint_data['value']
            )
        elif constraint_type == 'binary':
            return BinaryConstraint(
                style_id=style_id,
                object_1_id=constraint_data['object_1_id'],
                object_2_id=constraint_data['object_2_id'],
                attribute=constraint_data['attribute'],
                condition=constraint_data['condition']
            )
        elif constraint_type == 'mutex':
            return MutexConstraint(
                style_id=style_id,
                item_type_1_id=constraint_data['item_type_1_id'],
                item_type_2_id=constraint_data['item_type_2_id']
            )
        elif constraint_type == 'implication':
            return ImplicationConstraint(
                style_id=style_id,
                if_type_id=constraint_data['if_type_id'],
                then_type_id=constraint_data['then_type_id']
            )
        elif constraint_type == 'cardinality':
            return CardinalityConstraint(
                style_id=style_id,
                item_type_id=constraint_data['item_type_id'],
                min_count=constraint_data.get('min_count', 0),
                max_count=constraint_data.get('max_count')
            )
        else:
            raise ValueError(f"Unknown constraint type: {constraint_type}")