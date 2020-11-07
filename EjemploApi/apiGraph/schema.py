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

class CreateCliente(graphene.Mutation):
    cliente=graphene.Field(ClienteType)

    class Arguments:
        num_doc = graphene.String()
        tipo_num_doc = graphene.String()
        grupo_riesgo = graphene.String()
        capacidad_pago = graphene.Float()

    def mutate(self,info,**kwargs):
        cliente = Cliente(
            num_doc = kwargs.get('num_doc'),
            tipo_num_doc = kwargs.get('tipo_num_doc'),
            grupo_riesgo = kwargs.get('grupo_riesgo'),
            capacidad_pago = kwargs.get('capacidad_pago')
        )
        # Save in the database
        cliente.save()
        return CreateCliente(cliente=cliente)

class Mutation(graphene.ObjectType):
    create_cliente = CreateCliente.Field()
    # I could include more operations here, I would need to create other classes similar to CreateCliente
    