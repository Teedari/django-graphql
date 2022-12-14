from graphene import ObjectType, relay, Schema
from graphene_django import DjangoObjectType
from ingredients.models import Category, Ingredient
from ingredients.schema import Query as ingredient_query

# class CategoryType(DjangoObjectType):
#   class Meta:
#     model = Category
#     fields = ('id', 'name', 'ingredients')
    
# class IngredientType(DjangoObjectType):
#   class Meta:
#     model = Ingredient
#     fields = ('id', 'name', 'notes', 'category')
    
# class Query(graphene.ObjectType):
#   my_ingredients = graphene.List(IngredientType)
#   category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
  
#   def resolve_all_ingredients(root, info):
#     return Ingredient.objects.select_related('category').all()
  
#   def resolve_category_by_name(root, info, name):
#     try:
#       return Category.objects.get(name=name)
#     except Category.DoesNotExist:
#       return None
    
# schema = graphene.Schema(query=Query)


class Query(ingredient_query, ObjectType):
  pass


schema = Schema(query=Query)