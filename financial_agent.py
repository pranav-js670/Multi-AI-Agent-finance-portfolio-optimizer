from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

web_search_agent = Agent(
    name="web_search_agent",
    role="Search the web for information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    api_key="GROQ_API_KEY",
    tools=[DuckDuckGo()],
    instructions=["Always include sources in your response"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    api_key="GROQ_API_KEY",
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    api_key="GROQ_API_KEY",
    instructions=["Always include sources in your response","Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

task_description = "Get the latest news and recommendations for Nvidia (NVDA)"
multi_ai_agent.print_response(task_description, stream=True)

