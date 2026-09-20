import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)


with driver.session() as session:
    result = session.run(""" MATCH (s:Student) RETURN s.name AS name""")

    for record in result:
        print(record["name"])

def get_students():
    with driver.session() as session:

        result = session.run("""
            MATCH (s:Student)
            RETURN s.name AS name, s.year AS year
        """)

        students = []

        for record in result:
            students.append({
                "name": record["name"],
                "year": record["year"]
            })

        return students
def get_departments():
    with driver.session () as session:
        result= session.run(""")

