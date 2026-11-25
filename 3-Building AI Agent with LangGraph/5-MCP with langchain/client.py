from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio
async def main():
    client = MultiServerMCPClient(
        {
            ## tool 1
            "math" : {
                "command":"python",
            "args" : ["mathserver.py"], ## absolute path
            "transport" : "stdio"    
            },

            ## tool 2
            "weather": {
                "url" : "http://127.0.0.1:8000/mcp",
                "transport" : "streamable_http"
            }
        }

    )


    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tool = await client.get_tools()
    model = ChatGroq(model = "openai/gpt-oss-20b")
    agent = create_agent(
        model, tool
    )

    math_response = await agent.ainvoke({"messages" : [{"role" : "user", "content" : "what is (3 + 5) * 12 and what is the weather of california?"}]})

    print("Math response:", math_response['messages'][-1].content)
asyncio.run(main())
