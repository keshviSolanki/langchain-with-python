
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from src.tools.search_tool import search_tool
from src.tools.weather_tool import get_weather_data


def create_weather_agent():

    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.2
    )

    tools = [
        search_tool,
        get_weather_data
    ]

    # Local ReAct prompt
    prompt_template = """
You are a helpful AI assistant with access to tools.

You have access to the following tools:

{tools}

Use the following format:

Question: the user's question
Thought: think about what to do
Action: the action to take, must be one of [{tool_names}]
Action Input: the input for the action
Observation: the result of the action
... (repeat Thought/Action/Action Input/Observation as needed)
Thought: I now know the final answer
Final Answer: the final answer to the user

Important:
- Use tools when external information is required.
- Do not invent weather information.
- Give a clear and accurate final answer.

Question: {input}
Thought:{agent_scratchpad}
"""

    prompt = PromptTemplate.from_template(prompt_template)

    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=6
    )

    return agent_executor
