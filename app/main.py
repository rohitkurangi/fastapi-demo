from fastapi import FastAPI
from blog import  models
from blog.database import engine
from blog.routers import blog, user, authentication
import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

from typing import Optional

from fastapi import FastAPI

import graphene
from starlette.graphql import GraphQLApp


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    # cat = graphene.String(name=graphene.String(default_value="stranger"))
    cat = graphene.List(graphene.String, type_=graphene.String()) 


    def resolve_hello(self, info, name):
        return "Hello " + name

    def resolve_cat(self, info, **input):
        if input["type_"] == "white":
            return ["white cat"]
        else:
            return ["black cat"]



class Person(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    real_name = graphene.String()
    fake_name = graphene.String()

    def mutate(root, info, **input):
        the_name = input["name"]
        return {"real_name":f"MR. {the_name}", "fake_name":f"fake. {the_name}"}

class Mutation(graphene.ObjectType):
  createperson = Person.Field()

@app.get("/")
def read_root():
    return {"Hello": "graphql + fast api", "name": "rohit"}

app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query,mutation=Mutation)))