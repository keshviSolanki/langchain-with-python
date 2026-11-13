# Weather Search Agent 🌦️

A tool-using AI agent built with Python, LangChain, and OpenAI. It follows the
ReAct (Reasoning and Acting) pattern to search the web and retrieve current
weather information.

## Features

- OpenAI chat model through LangChain
- ReAct agent with tool selection
- Web search using DuckDuckGo
- Current weather lookup using Weatherstack
- Environment-variable based API key configuration

## Project structure

```text
weather-search-agent/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── agent.py
│   └── tools/
│       ├── __init__.py
│       ├── search_tool.py
│       └── weather_tool.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- An OpenAI API key
- A Weatherstack API key

## Setup (Windows PowerShell)

1. Open a terminal in this project folder.

2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Create your local `.env` file from the example:

   ```powershell
   Copy-Item .env.example .env
   ```

5. Open `.env` and add your own API keys:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   WEATHERSTACK_API_KEY=your_weatherstack_api_key
   ```

   Never commit `.env` or share your API keys.

## Run

Run the default example:

```powershell
python -m src.main
```

Or pass your own question:

```powershell
python -m src.main --question "Find the capital of Gujarat and check its current weather"
```

## How it works

1. The user submits a question.
2. The ReAct agent reasons about which tool is needed.
3. DuckDuckGo Search can find factual web information such as a state capital.
4. The weather tool calls Weatherstack for the selected city.
5. The agent combines the tool results into a natural-language answer.

## Architecture

```text
User Question
     |
     v
OpenAI Chat Model
     |
     v
LangChain ReAct Agent
     |
     v
Tool Selection
   /       \
  v         v
Web Search  Weather Tool
(DuckDuckGo)   |
               v
          Weatherstack
   \         /
    v       v
    Agent Executor
          |
          v
     Final Answer
```

## Notes

- Weatherstack availability and returned fields depend on your Weatherstack plan.
- DuckDuckGo search results and live weather data require an internet connection.
- The agent prompt is pulled from LangChain Hub when the agent is created.
- This project uses the classic LangChain `create_react_agent` and
  `AgentExecutor` API. If you upgrade LangChain to a newer major API, the
  agent implementation may need migration.

## License

Add a license if you intend to publish or distribute this project.
