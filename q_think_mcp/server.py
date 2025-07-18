"""
Q-Think MCP Server

A thinking MCP server implementation using FastMCP that provides
reasoning and analysis capabilities to MCP clients.
"""

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Q-Think MCP Server")


@mcp.tool()
def think(thought: str):
    """Use the tool to think about something. It will not obtain new information or change the database, but just append the thought to the log. Use it when complex reasoning or some cache memory is needed.

    Args:
        thought: A thought to think about.
    """
    print(f"Received thought: {thought}")


def main():
    """Main entry point for the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
