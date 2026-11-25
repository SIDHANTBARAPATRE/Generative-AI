from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Math")


@mcp.tool()
def add(a:int, b:int)->int:
    """__Summary__
    Add to numbers
    """
    return a+b

@mcp.tool()
def multiple(a:int, b:int)->int:
    """Multiply two numbers"""
    return a*b

## Ttransport = "stdio" -> tells the server to use the staandard input/output to receive and respond to tool function call

if __name__=="__main__":
    mcp.run(transport="stdio")