# pip3 install neo4j-driver
# python3 example.py

from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "bolt://3.82.205.144:7687",
  auth=basic_auth("neo4j", "civilian-sacks-logs"))

cypher_query = '''
MATCH (n)
RETURN COUNT(n) AS count
LIMIT $limit
'''

with driver.session(database="neo4j") as session:
  results = session.read_transaction(
    lambda tx: tx.run(cypher_query,
                      limit="10").data())
  for record in results:
    print(record['count'])

driver.close()

