# src/server/main.py
from flask import Flask
from flask_cors import CORS
from flask_restx import Api, Resource, fields
from admin.Administration import HalilsTaverneAdministration
from server.bo.BinaryConstraint import BinaryConstraint
from server.bo.CardinalityConstraint import CardinalityConstraint
from server.bo.ClothingItems import ClothingItem
from server.bo.ConstraintRule import Constraint
from server.bo.ImplicationConstraint import ImplicationConstraint
from server.bo.MutexConstraint import MutexConstraint
from server.bo.Outfit import Outfit
from server.bo.Style import Style
from server.bo.UnaryConstraint import UnaryConstraint
from server.bo.User import User
from server.bo.Wardrobe import Wardrobe
import traceback
from server.db.conversion import convert_quantity
from SecurityDecorator import secured

app = Flask(__name__)

#CORS aktivieren
#CORS steht für Cross-Origin Resource Sharing und ist ein Mechanismus, der es Webseiten ermöglicht, Ressourcen von anderen Domains zu laden.
"""CORS(app, resources={r"/api/":{"origins":"*"}})"""
CORS(app, supports_credentials=True, resources=r'/wardrobe/*')

#API-Objekt erstellen
api = Api(app, version='1.0', title='DigitalWardrobeDemo API',
          description='An API for managing a digital wardrobe.')


# Namespace
#Der Namespace ist Container für die API-Endpunkte, die zu einem bestimmten Thema gehören.
Wardrobe_ns = api.namespace('wardrobe', description='Wardrobe-related functionalities')

# Modelle für Flask-Restx: Flast-Restx verwendet die Modelle, um die JSON-Objekte zu serialisieren und zu deserialisieren,
#Restx ist eine Erweiterung von Flask, die es ermöglicht, RESTful APIs zu erstellen.
#RESTful APIs sind APIs, die auf dem REST-Prinzip basieren, das besagt, dass jede Ressource über eine eindeutige URL angesprochen wird.


#Im folgenden Abschnitt werden die Modelle für die verschiedenen Business-Objekte definiert.
bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Unique identifier of a business object')
})


user = api.inherit('User', bo, {
    'firstname': fields.String(attribute='_firstname', required=True, description='First name of the user'),
    'lastname': fields.String(attribute='_lastname', required=True, description='Last name of the user'),
    'nickname': fields.String(attribute='_nickname', description='Nickname of the user'),
    'google_id': fields.String(attribute='_google_id', required=True, description='Google ID of the user'),
    'email': fields.String(attribute='_email', required=True, description='Email address of the user')
})


clothing = api.inherit('Clothing', bo, {
    'name': fields.String(attribute='_name', required=True, description='Name of the clothing item'),
    'type_id': fields.Integer(attribute='_type_id', required=True, description='Type of the clothing item'),
    'color': fields.String(attribute='_color', description='Color of the clothing item'),
    'wardrobe_id': fields.Integer(attribute='_wardrobe_id', required=True, description='Identifier of the associated wardrobe'),
    'seasons': fields.List(fields.String, attribute='_seasons', description='Seasons associated with the clothing item'),
    'occasions': fields.List(fields.String, attribute='_occasions', description='Occasions suitable for the clothing item')
})

constraint = api.inherit('Constraint', bo, {
    'style_id': fields.Integer(attribute='_style_id', required=True, description='Identifier of the associated style'),
    'type': fields.String(attribute='_type', required=True, description='Type of the constraint (e.g., binary, unary)'),
    'value': fields.String(attribute='_value', required=True, description='Constraint-specific rules in JSON format')
})

outfit = api.inherit('Outfit', bo, {
    'name': fields.String(attribute='_name', required=True, description='Name of the outfit'),
    'style_id': fields.Integer(attribute='_style_id', required=True, description='Identifier of the associated style'),
    'wardrobe_id': fields.Integer(attribute='_wardrobe_id', required=True, description='Identifier of the wardrobe associated with the outfit'),
    'items': fields.List(fields.Integer, attribute='_items', description='List of clothing item IDs in the outfit'),
    'occasions': fields.List(fields.String, attribute='_occasions', description='Occasions for which the outfit is suitable'),
    'rating': fields.Integer(attribute='_rating', description='User rating for the outfit'),
    'times_worn': fields.Integer(attribute='_times_worn', description='Number of times the outfit has been worn')
})

style = api.inherit('Style', bo, {
    'name': fields.String(attribute='_name', required=True, description='Name of the style'),
    'description': fields.String(attribute='_description', description='Description of the style'),
    'creator_id': fields.Integer(attribute='_creator_id', required=True, description='ID of the user who created the style'),
    'is_public': fields.Boolean(attribute='_is_public', description='Whether the style is publicly available'),
    'seasons': fields.List(fields.String, attribute='_seasons', description='Seasons associated with the style'),
    'occasions': fields.List(fields.String, attribute='_occasions', description='Occasions suitable for the style'),
    'constraints': fields.List(fields.Nested(constraint), attribute='_constraints', description='List of constraints for the style'),
    'tags': fields.List(fields.String, attribute='_tags', description='Tags associated with the style')
})


#Alle Operationen für die verschiedenen Business-Objekte werden im folgenden Abschnitt definiert.
#User Operations
@fridge_ns.route('/users')
@fridge_ns.response(500, 'Server-Error')
class UserListOperations(Resource):

    @secured
    @fridge_ns.marshal_list_with(user)
    def get(self):
        """Auslesen aller User"""

        adm = HalilsTaverneAdministration()
        users = adm.get_all_users()
        return users


    @secured
    @fridge_ns.marshal_with(user, code=200)
    @fridge_ns.expect(user)
    def post(self):
        """Neuen User anlegen"""

        adm = HalilsTaverneAdministration()
        proposal = User.from_dict(api.payload)

        if proposal is not None:
            u = adm.create_user(
                proposal.get_nick_name(),
                proposal.get_first_name(),
                proposal.get_last_name(),
                proposal.get_household_id(),
                proposal.get_google_user_id()
            )
            return u, 200
        else:
            return '', 500
        # 500: server-fehler



@fridge_ns.route('/users/<int:id>')
@fridge_ns.response(500, 'Server-Error')
@fridge_ns.param('id', 'User ID')
class UserOperations(Resource):

    @secured
    @fridge_ns.marshal_with(user)
    def get(self, id):
        """User nach ID auslesen"""

        adm = HalilsTaverneAdministration()
        User = adm.get_user_by_id(id)
        return User


    @secured
    def delete(self, id):
        """user löschen"""
        adm = HalilsTaverneAdministration()
        User = adm.get_user_by_id(id)
        adm.delete_user(User)
        return '', 200

    @secured
    @fridge_ns.marshal_with(user)
    @fridge_ns.expect(user, validate=True)
    def put(self, id):
        """User Objekt updaten"""
        adm = HalilsTaverneAdministration()
        u = User.from_dict(api.payload)

        if u is not None:
            u.set_id(id)
            adm.save_user(u)
            return '', 200
        else:
            return '', 500



@fridge_ns.route('/user-by-google-id/<string:google_user_id>')
@fridge_ns.response(500, 'Server-Error')
@fridge_ns.param('google_user_id', 'Google_user_id of a user')
class UserByGoogleIdOperations(Resource):

    @secured
    @fridge_ns.marshal_list_with(user)
    def get(self, google_user_id):
        """user nach google_user_id auslesen"""
        adm = HalilsTaverneAdministration()
        User = adm.get_user_by_google_user_id(google_user_id)
        return User


@fridge_ns.route('/users-by-nick_name/<string:nick_name>')
@fridge_ns.response(500, 'Server-Error')
@fridge_ns.param('nick_name', 'Nickname of a user')
class UsersByNameOperations(Resource):

    @secured
    @fridge_ns.marshal_with(user)
    def get(self, nick_name):
        """User nach Nickname auslesen"""
        adm = HalilsTaverneAdministration()
        User = adm.get_user_by_nickname(nick_name)
        return User




#Household Operations, die Operationen für die Haushalte
@fridge_ns.route('/Household')
@fridge_ns.response(500, 'Server-Error')
class HouseholdListOperation(Resource):

    @secured
    @fridge_ns.marshal_list_with(household)
    def get(self):
        adm = HalilsTaverneAdministration()
        households = adm.get_all_households()
        return households

    @secured
    @fridge_ns.expect(household)
    @fridge_ns.marshal_list_with(household)
    def post(self):
        adm = HalilsTaverneAdministration()
        proposal = Household.form_dict(api.payload)

        if proposal is not None:

            h = adm.create_household(proposal.get_name(), proposal.get_password())



            return h, 200
        else:
            return '', 500



@fridge_ns.route('/Household/<int:id>')
@fridge_ns.response(500, 'Server-Error')
@fridge_ns.param('id', 'Houshold ID')
class HouseholdOperations(Resource):

    @secured
    @fridge_ns.marshal_with(user)
    def get(self, id):
        adm = HalilsTaverneAdministration()
        hou = adm.get_users_by_household_id(id)
        return hou


    @secured
    def delete(self, id):
        adm = HalilsTaverneAdministration()
        hou = adm.find_household_by_id(id)
        adm.delete_household(hou)
        return '', 200

    @secured
    @fridge_ns.marshal_with(household)
    @fridge_ns.expect(household, validate=True)
    def put(self, id):
        """update eines household-objekts nach id"""

        adm = HalilsTaverneAdministration()
        h1 = Household.form_dict(api.payload)

        if h1 is not None:
            h1.set_id(id)
            adm.save_household(h1)
            return '', 200
        else:
            return '', 500


@fridge_ns.route('/HouseholdbyID/<int:id>')
@fridge_ns.response(500, 'Server-Error')
class HouseholdbyIDOperations(Resource):

    @secured
    @fridge_ns.marshal_list_with(household)
    def get(self, id):
        adm = HalilsTaverneAdministration()
        h = adm.find_household_by_id(id)
        return h




#Fridge Operations
@fridge_ns.route('/Fridge')
@fridge_ns.response(500, 'Server-Error')
class FridgeListOperations(Resource):

    @secured
    @fridge_ns.marshal_list_with(fridge)
    def get(self):
        adm = HalilsTaverneAdministration()
        fridge = adm.get_all_fridges()
        return fridge

    @secured
    @fridge_ns.expect(fridge)
    @fridge_ns.marshal_list_with(fridge)
    def post(self):
        adm = HalilsTaverneAdministration()
        proposal = Fridge.form_dict(api.payload)

        if proposal is not None:
            f = adm.create_fridge()
            return f, 200
        else:
            return '', 500





#FridgeEnty Operations
@fridge_ns.route('/FridgeEntries')
@fridge_ns.response(500, 'Server-Error')
class FridgeEntryListOperations(Resource):

    @secured
    @fridge_ns.marshal_list_with(fridge_entry)
    def get(self):
        adm = HalilsTaverneAdministration()
        fridge_entries = adm.get_all_fridge_entries()
        return fridge_entries

    @secured
    @fridge_ns.expect(fridge_entry)
    @fridge_ns.marshal_list_with(fridge_entry)
    # @secured
    def post(self):
        adm = HalilsTaverneAdministration()
        try:
            proposal = FridgeEntry.form_dict(api.payload)

            if proposal is not None:
                fe = adm.create_fridge_entry(
                    proposal.get_fridge_id(),
                    proposal.get_groceries_designation(),
                    proposal.get_quantity(),
                    proposal.get_unit()
                )
                return fe, 200
            else:
                return {'message': 'Invalid input'}, 400
        except KeyError as e:
            print('Missing field in input:', e)
            return {'message': f'Missing field in input: {e}'}, 400
        except ValueError as e:
            print('Invalid value:', e)
            return {'message': f'Invalid value: {e}'}, 400
        except Exception as e:
            print('Unexpected error:', e)
            print(traceback.format_exc())  # Stack trace für detailliertere Fehlerbehebung drucken
            return {'message': str(e)}, 500



@fridge_ns.route('/FridgeEntries/<int:fridge_id>')
@fridge_ns.response(500, 'Server-Error')
class FridgeEntrybyFridgeIdOperations(Resource):

    @secured
    @fridge_ns.marshal_list_with(fridge_entry)
    def get(self, fridge_id):

        adm = HalilsTaverneAdministration()
        ent = adm.get_fridge_entries_by_fridge_id(fridge_id)
        return ent




@fridge_ns.route('/FridgeEntry/<string:groceries_designation>')
@fridge_ns.response(500, 'Server-Error')
@fridge_ns.response(404, 'FridgeEntry not found')
@fridge_ns.response(200, 'FridgeEntry successfully updated')
@fridge_ns.param('groceries_designation', 'Name of a grocerie')
class FridgeEntryOperations(Resource):

    @secured
    def delete(self, groceries_designation):
        adm = HalilsTaverneAdministration()
        fridge_entry = adm.find_fridge_entry_by_designation(groceries_designation)
        adm.delete_fridge_entry(fridge_entry)
        return '', 200

    @secured
    @fridge_ns.expect(fridge_entry)
    @fridge_ns.marshal_with(fridge_entry)
    def put(self, groceries_designation):
        adm = HalilsTaverneAdministration()
        fe = FridgeEntry.form_dict(api.payload)
        print("Heres the fe:" , fe)
        if fe is not None:
            fe.set_groceries_designation(fe.get_groceries_designation())
            adm.save_fridge_entry(fe)
            return '', 200
        else:
            return '', 500

    @secured
    @fridge_ns.expect(fridge_entry)
    @fridge_ns.marshal_with(fridge_entry)
    def get(self, groceries_designation):
        adm = HalilsTaverneAdministration()
        fe = adm.find_fridge_entry_by_designation(groceries_designation)
        return fe




@fridge_ns.route('/COOK/<string:recipe_title>', methods=['PUT'])
@fridge_ns.response(500, 'Server-Error')
@fridge_ns.param('recipe_title', 'Recipe name')
class UseRecipeIngredients(Resource):

    @secured
    def put(self, recipe_title):
        """Zutaten eines rezepts von entry abziehen"""
        adm = HalilsTaverneAdministration()
        """Rezept ID auslesen"""
        recipe_id = adm.get_recipe_id_by_title(recipe_title)
        """ Rezept Einträge auslesen"""
        recipe_entries = adm.find_recipe_entries_by_recipe_id(recipe_id[0])
        for recipe_entry in recipe_entries:
            """Fridge Einträge auslesen"""
            fridge_entry = adm.find_fridge_entry_by_designation(recipe_entry.get_groceries_designation())
            if fridge_entry:
                # Umrechnung der Mengenangaben
                recipe_quantity_in_fridge_units = convert_quantity(recipe_entry.get_quantity(), recipe_entry.get_unit(), fridge_entry[3])
                if recipe_quantity_in_fridge_units is not None and fridge_entry[2] >= recipe_quantity_in_fridge_units:
                    new_quantity = fridge_entry[2] - recipe_quantity_in_fridge_units
                    adm.update_fridge_entry_quantity(fridge_entry[0], fridge_entry[1], new_quantity, fridge_entry[3])
                else:
                    return {"error": f"Not enough in fridge."}, 400
            else:
                return {"error": f"Not enough in fridge."}, 400

        return {"message": "Lets cook."}, 200






#RecipeEntry Operations
@fridge_ns.route('/RecipeEntries')
@fridge_ns.response(500, 'Server-Error')
class RecipeEntryListOperation(Resource):

    @secured
    @fridge_ns.marshal_list_with(recipe_entry)
    def get(self):
        adm = HalilsTaverneAdministration()
        recipe_entries = adm.get_all_recipes_entries()
        return recipe_entries

    @secured
    @fridge_ns.expect(recipe_entry)
    @fridge_ns.marshal_list_with(recipe_entry)
    def post(self):
        adm = HalilsTaverneAdministration()
        proposal = RecipeEntry.from_dict(api.payload)
        if proposal is not None:
            re = adm.create_recipe_entry(
                proposal.get_recipe_id(),
                proposal.get_groceries_designation(),
                proposal.get_quantity(),
                proposal.get_unit()
            )
            return re, 200
        else:
            return '', 500



@fridge_ns.route('/RecipeEntries/<int:recipe_id>')
@fridge_ns.response(500, 'Server-Error')
@fridge_ns.response(404, 'RecipeEntry not found')
@fridge_ns.response(200, 'RecipeEntry successfully retrieved')
@fridge_ns.param('recipe_id', 'Recipe ID')
class RecipeEntryListOperationByID(Resource):

    @secured
    @fridge_ns.marshal_list_with(recipe_entry)
    def get(self, recipe_id):
        adm = HalilsTaverneAdministration()
        reci = adm.find_recipe_entries_by_recipe_id(recipe_id)
        if reci:
            return reci, 200
        else:
            return [], 200 #Sollte es noch keine Einträge geben, so wird kein Fehler erzeugt



@fridge_ns.route('/RecipeEntry/<string:groceries_designation>/<int:recipe_id>')
@fridge_ns.response(500, 'Server-Error')
@fridge_ns.response(404, 'RecipeEntry not found')
@fridge_ns.response(200, 'RecipeEntry successfully deleted')
@fridge_ns.param('groceries_designation', 'Designation of a grocerie')
@fridge_ns.param('recipe_id', 'Recipe ID')
class RecipeEntryOperationsByDesignationAndID(Resource):

    @secured
    @fridge_ns.marshal_list_with(recipe_entry)
    def delete(self, groceries_designation, recipe_id):
        """Anhand der groceries_designation und der recipe_id wird zunächst der Eintrag geladen,
            bei dem es zu einer Übereinstimmung kommt. Danach wird die Delete-Methode aufgerufen
            und der jeweilige Eintrag entfernt."""
        adm = HalilsTaverneAdministration()
        re = adm.find_recipe_entries_by_recipe_id_and_designation(groceries_designation, recipe_id)

        if re and re.get_groceries_designation() == groceries_designation:
            adm.delete_recipe_entry(re)
            return '', 200
        else:
            return '', 404

    @secured
    @fridge_ns.marshal_list_with(recipe_entry)
    def put(self, groceries_designation, recipe_id):
        adm = HalilsTaverneAdministration()
        re = RecipeEntry.from_dict(api.payload)
        if re is not None:
            adm.update_recipe_entry(re)
            return '', 200
        else:
            return '', 500


@fridge_ns.route('/RecipeEntry/<string:groceries_designation>')
@fridge_ns.response(500, 'Server-Fehler')
@fridge_ns.response(404, 'RecipeEntry not found')
@fridge_ns.response(200, 'RecipeEntry successfully updated')
@fridge_ns.param('groceries-designation', 'Designation of a grocerie')
class RecipeEntryListOperations2(Resource):

    @secured
    @fridge_ns.marshal_list_with(recipe_entry)
    def get(self, groceries_designation):
        adm = HalilsTaverneAdministration()
        reci = adm.get_recipe_entries_by_designation(groceries_designation)
        return reci




#Recipe Operations
@fridge_ns.route('/RecipeList')
@fridge_ns.response(500, 'Server-Error')
@fridge_ns.response(404, 'Recipe not found')
@fridge_ns.response(200, 'Recipe successfully updated')
class RecipeListOperations(Resource):

    @secured
    @fridge_ns.marshal_list_with(recipe)
    def get(self):
        adm = HalilsTaverneAdministration()
        recipes = adm.get_all_recipes()
        return recipes
    
    @secured
    @fridge_ns.expect(recipe)
    @fridge_ns.marshal_list_with(recipe)
    def post(self):
        adm = HalilsTaverneAdministration()

        proposal = Recipe.from_dict(api.payload)
        
        if proposal is not None:
            r = adm.create_recipe(
                proposal.get_title(),
                proposal.get_number_of_persons(),
                proposal.get_creator(),
                proposal.get_description(),
                proposal.get_household_id(),
            )
            return r, 200
        else:
            return '', 500



@fridge_ns.route('/RecipeList/<int:household_id>')
@fridge_ns.response(500, 'Server-Error')
class RecipebyHouseholdIdOperations(Resource):

    @secured
    @fridge_ns.marshal_list_with(recipe)
    def get(self, household_id):
        adm = HalilsTaverneAdministration()
        rec = adm.get_recipes_by_household_id(household_id)
        return rec




@fridge_ns.route('/Recipe/<int:recipe_id>')
@fridge_ns.response(500, 'Server-Error')
class RecipeOperations(Resource):

    @secured
    @fridge_ns.marshal_with(recipe)
    def get(self, recipe_id):
        adm = HalilsTaverneAdministration()
        reci = adm.get_recipe_by_id(recipe_id)
        return reci

    @secured
    @fridge_ns.marshal_list_with(recipe)
    def put(self, recipe_id):
        adm = HalilsTaverneAdministration()
        re = Recipe.form_dict(api.payload)
        if re is not None:
            re.set_id(recipe_id)
            adm.update_recipe(re)
            return '', 200
        else:
            return '', 500

    @secured
    def delete(self, recipe_id):
        adm = HalilsTaverneAdministration()
        recipe = adm.get_recipe_by_id(recipe_id)
        adm.delete_recipe(recipe)
        return '', 200





#Fridge Operations
@fridge_ns.route('/fridge-id-by-google-id/<string:google_user_id>')
@fridge_ns.response(500, 'Server-Error')
class FridgeIdByGoogleIdResource(Resource):

    @secured
    def get(self, google_user_id):
        adm = HalilsTaverneAdministration()
        fridge_id = adm.get_fridge_id_by_google_user_id(google_user_id)
        if fridge_id is not None:
            return {'fridge_id': fridge_id}, 200
        else:
            return {'message': 'Fridge ID not found'}, 404






#Household Operations
@fridge_ns.route('/household-id-by-google-id/<string:google_user_id>')
@fridge_ns.response(500, 'Server-Error')
class HouseholdIdByGoogleUserId(Resource):

    @secured
    def get(self, google_user_id):
        adm = HalilsTaverneAdministration()
        household_id = adm.get_household_id_by_google_user_id(google_user_id)
        if household_id is not None: 
            return {'household_id': household_id}, 200
        else:
            return {'message': 'Household ID not found'}, 404






#Unit Operations
@fridge_ns.route('/Unit')
@fridge_ns.response(500, 'Server-Fehler')
@fridge_ns.response(404, 'RecipeEntry not found')
@fridge_ns.response(200, 'RecipeEntry successfully deleted')
@fridge_ns.param('groceries_designation', 'Bezeichnung eines Lebensmittels')
@fridge_ns.param('recipe_id', 'ID eines Rezepts')
class UnitOperations(Resource):

    @secured
    @fridge_ns.expect(unit)
    @fridge_ns.marshal_list_with(unit)
    def post(self):
        adm = HalilsTaverneAdministration()

        proposal = Unit.from_dict(api.payload)

        if proposal is not None:
            u = adm.create_unit(
                proposal.get_designation(),
                proposal.get_household_id()
            )
            return u, 200
        else:
            return '', 500



@fridge_ns.route('/Unit/<string:designation>/<int:household_id>')
@fridge_ns.response(500, 'Server-Fehler')
@fridge_ns.response(404, 'RecipeEntry not found')
@fridge_ns.response(200, 'RecipeEntry successfully deleted')
@fridge_ns.param('groceries_designation', 'Bezeichnung eines Lebensmittels')
@fridge_ns.param('recipe_id', 'ID eines Rezepts')
class UnitOperationsByDesignationAndID(Resource):
    
    @secured
    @fridge_ns.marshal_list_with(unit)
    def get(self, designation, household_id):
        """Anhand der designation und der household_id werden zunächst die Einträge geladen,
            bei dem es zu einer Übereinstimmung kommt. Danach wird die Get-Methode aufgerufen
            und die jeweiligen Einträge geladen"""

        adm = HalilsTaverneAdministration()
        re = adm.get_unit_by_designation_and_household_id(designation, household_id)
        return re




@fridge_ns.route('/Unit/<int:id>')
@fridge_ns.response(500, 'Server-Fehler')
class UnitsbyHouseholdIdOperations(Resource):

    @secured
    @fridge_ns.marshal_list_with(unit)
    def get(self, id):
        adm = HalilsTaverneAdministration()
        units = adm.get_all_units_by_household_id(id)
        print(units)
        if units:
            return units, 200
        else:
            return {'message': 'Units not found'}, 404

    def delete(self, id):

        adm = HalilsTaverneAdministration()
        adm.delete_unit_by_id(id)
        return '', 200




if __name__ == '__main__':
    app.run(debug=True)
