import asyncio
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_google_genai import ChatGoogleGenerativeAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

model= ChatGoogleGenerativeAI(model="gemini-2.0-flash",api_key="")
server_params = StdioServerParameters(
    command="python",
    args=["mcp_server.py"]
)

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            
            agent=create_react_agent(model, tools)
            agent_response = await agent.ainvoke({"messages":"Analyse how revenue for MSFT is changing over time."})
            print(agent_response["messages"][-1].content))


if __name__ == "__main__":
    asyncio.run(main())
