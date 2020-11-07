import graphene
import apiGraph.schema

# This define the location of the graphql query called 'Query', which is placed 
# inside the folder 'apiGraph', file 'schema.py' and class Query
class Query(apiGraph.schema.Query):
    pass

class Mutation(apiGraph.schema.Mutation):
    pass

# It define that a query of Graphql is define by the name 'Query'
#schema = graphene.Schema(query=Query)
schema = graphene.Schema(query=Query, mutation=Mutation)
