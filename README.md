# Multi-Agent Finance Portfolio Optimizer

This project demonstrates the power of a multi-agent AI system designed to provide real-time insights, stock recommendations, and portfolio optimization using various data sources and tools. By combining different AI agents for web search and financial analysis, it offers a comprehensive solution to financial decision-making.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [AI Agents](#ai-agents)
- [Workflow](#workflow)
- [Usage](#usage)
- [License](#license)

## Overview

The **Multi-Agent Finance Portfolio Optimizer** integrates multiple AI agents for two distinct tasks:
1. **Web Search Agent** - Responsible for searching the web for relevant financial data.
2. **Finance Agent** - Specialized in analyzing financial data, including stock prices, analyst recommendations, and company news.

These agents collaborate in real-time to gather data, process it, and present actionable insights that help optimize a financial portfolio or make informed investment decisions.

## Technologies Used

### **Frameworks & Tools**

- **`PhiData`**: A framework used to build and manage AI agents, enabling tool use and collaborative decision-making.
- **`Llama-3`**: A state-of-the-art AI model used for processing natural language queries and generating responses.
- **`YFinanceTools`**: A collection of tools used to access financial data, including stock prices, company news, analyst recommendations, and financial fundamentals.
- **`DuckDuckGo`**: A search engine tool used by the web search agent to gather external, real-time data from the web.
- **`Python`**: The programming language used for implementing the agents and orchestrating the workflow.

### **Key Libraries & Dependencies**

- `phi-agent`
- `phi.model.groq`
- `phi.tools.yfinance`
- `phi.tools.duckduckgo`
- `pandas` (for data handling and table formatting)

## AI Agents

### 1. **Web Search Agent**
   - **Role**: This agent is designed to search the web for real-time information, including news and articles related to specific stocks or financial topics. It uses **DuckDuckGo** to perform searches and returns relevant, up-to-date information.
   - **Tools**:
     - **DuckDuckGo** for web search
   - **Instructions**: Always include sources in the response.

### 2. **Finance Agent**
   - **Role**: This agent is specialized in gathering and analyzing financial data. It provides real-time stock prices, analyst recommendations, financial fundamentals, and company news. The agent uses the **YFinanceTools** for accessing financial data.
   - **Tools**:
     - **YFinanceTools** for stock data (price, recommendations, fundamentals, and news)
   - **Instructions**: Use tables to display financial data for clarity.

### 3. **Multi-Agent System**
   - **Role**: The multi-agent system is a coordination of the **Web Search Agent** and **Finance Agent** to deliver a comprehensive response. It can handle complex requests that involve both real-time web data and financial analysis, providing a complete, actionable answer to user queries.

## Workflow

1. **User Request**: The system receives a user query (e.g., "Get the latest news and recommendations for Nvidia (NVDA)").
2. **Web Search Agent**: The **Web Search Agent** uses **DuckDuckGo** to search the web for the latest news and articles related to the stock or company.
3. **Finance Agent**: Simultaneously, the **Finance Agent** queries **YFinanceTools** to get the latest stock price, analyst recommendations, and relevant company news from Yahoo Finance.
4. **Data Combination**: The **Multi-Agent System** combines the results from both agents and formats them into a user-friendly response.
5. **Response**: The system returns the gathered insights to the user, including relevant stock data, analyst recommendations, and web search results.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/pranav-js670/Multi-AI-Agent-finance-portfolio-optimizer.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Run the script to get real-time stock recommendations and news:
   ```bash
   python financial_agent.py
   ```

## License

This project is licensed under the MIT License.
