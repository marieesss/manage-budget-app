from app.db import db
from app.models.categorie import Categorie
from app.utils.request import generate_response
from sqlalchemy.exc import IntegrityError

class CategorieService:
      
    def create_categorie(name: str, type : str = "expense"):
        """ Create a categorie

        Parameters
        -----------------

        Returns
        ----------
        Confirmation message 
        """
        try:
            categorie = Categorie(
                type=type,
                name=name
            )
            try: 
                db.session.add(categorie)
                db.session.commit()
                return generate_response(message="Categorie created", status=400, error="Conflict")   
            except IntegrityError:
                db.session.rollback()
                return generate_response(message="Categorie already exists", status=200)   
        except Exception as error:
            db.session.rollback()
            return generate_response(message="An unexpected error occurred", status=500, error=str(error))
        
    def get_all_categories():
        """ Get all categories

        Parameters
        -----------------

        Returns
        ----------
        Array : 
            id
            name
            created_at
        """
        try:
            categories = Categorie.get_all_categories()
            if not categories: 
                return generate_response(message="categories not found", status=400, error="Conflict")                    
            categories_data=[]
            for categorie in categories:
                categories_data.append({"id": categorie.id, "name": categorie.name, "type": categorie.type.name})
            return categories_data
        except Exception as error:
            print(error)
            raise error
        
    def get_all_categories_by_type(categorie_type):
        """ Get all categories

        Parameters
        -----------------

        Returns
        ----------
        Array : 
            id
            name
            created_at
        """
        try:
            categories = Categorie.get_all_categories_by_type(categorie_type=categorie_type)
            if not categories: 
                return generate_response(message="categories not found", status=400, error="Conflict")                    
            categories_data=[]
            for categorie in categories:
                categories_data.append({"id": categorie.id, "name": categorie.name, "type": categorie.type.name})
            return categories_data
        except Exception as error:
            print(error)
            raise error
        
      
