from neo4j import GraphDatabase
from langchain import GraphAgent

class GraphAgent:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def run_query(self, query):
        with self.driver.session() as session:
            result = session.run(query)
            return [record for record in result]

    def ask_question(self, question):
        # Process the question and convert it to a Cypher query
        query = self.convert_question_to_query(question)
        return self.run_query(query)

    def convert_question_to_query(self, question):
        # Basic question conversion (this can be extended with LLMs or NLP techniques)
        if "tools in MERN stack" in question.lower():
            return "MATCH (t:Tool)-[:PART_OF]->(s:Stack {name: 'MERN Stack'}) RETURN t.name"
        # Add more question types here
        return ""

# Example usage
if __name__ == "__main__":
    agent = GraphAgent(uri="bolt://localhost:7687", user="neo4j", password="your_password")
    result = agent.ask_question("What are the tools in MERN stack?")
    print(result)
    agent.close()

from langchain.llms import OpenAI

class ExtendedGraphAgent(GraphAgent):
    def __init__(self, uri, user, password, openai_api_key):
        super().__init__(uri, user, password)
        self.llm = OpenAI(api_key=openai_api_key)

    def convert_question_to_query(self, question):
        # Use LLM to convert natural language question to Cypher query
        prompt = f"Convert the following question to a Cypher query: {question}"
        cypher_query = self.llm(prompt)
        return cypher_query

# Example usage
if __name__ == "__main__":
    agent = ExtendedGraphAgent(uri="bolt://localhost:7687", user="neo4j", password="your_password", openai_api_key="your_openai_api_key")
    result = agent.ask_question("List all tools in the MERN stack.")
    print(result)
    agent.close()
