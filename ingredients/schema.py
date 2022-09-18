from graphene_django import DjangoObjectType, filter
from graphene import (relay, ObjectType, List)

from .models import Category, Ingredient

class IngredientType(DjangoObjectType):
  class Meta:
    model = Ingredient
    fields = ('id', 'name', 'category')

class CategoryNode(DjangoObjectType):
  class Meta: 
    model = Category
    filter_fields = ['name', 'ingredients']
    interfaces = (relay.Node, )
    

class IngredientNode(DjangoObjectType):
  class Meta:
    model = Ingredient
    filter_fields = {
      'name': ['exact', 'icontains', 'istartswith'],
      'notes': ['exact', 'icontains'],
      'category': ['exact'],
      'category__name': ['exact'],
    }
    
    interfaces = (relay.Node, )


class Query(ObjectType):
  category = relay.Node.Field(CategoryNode)
  all_categories = filter.DjangoFilterConnectionField(CategoryNode)
  ingredients = List(IngredientType)
  
  ingredient  = relay.Node.Field(IngredientNode)
  all_ingredients = filter.DjangoFilterConnectionField(IngredientNode)
  
  def resolve_ingredients(root, info):
    return Ingredient.objects.select_related('category').all()