import graphene
from graphene_django import DjangoObjectType
from apiRest.models import Cliente

# Relate a django object with a graphine one.
class ClienteType(DjangoObjectType):
    class Meta:
        model = Cliente

# Unlike REST which requires a standard and static signature, graphQL define queries and mutations
class Query(graphene.ObjectType):
    all_clientes=graphene.List(ClienteType)

    def resolve_all_clientes(self, info, **kwargs):
        return Cliente.objects.all()
