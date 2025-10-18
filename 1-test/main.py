from strands_agents import Agent

agent = Agent()

def invoke(agent: Agent, input: str) -> str:
    return agent(input)

if __name__ == "__main__":
    print(invoke(agent, "Hello, agent!"))