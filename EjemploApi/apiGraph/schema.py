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
    some_clientes=graphene.List(ClienteType, num_doc=graphene.String(), tipo_num_doc=graphene.String())

    def resolve_all_clientes(self, info, **kwargs):
        return Cliente.objects.all()

    def resolve_some_clientes(self, info, **kwargs):
        return Cliente.objects.filter(num_doc=kwargs.get('num_doc'), tipo_num_doc=kwargs.get('tipo_num_doc'))
