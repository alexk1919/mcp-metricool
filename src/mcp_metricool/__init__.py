import os

from .server import mcp
from .tools import tools

def main() -> None:
    "Run the Metricool MCP server"
    # SSE transport is for the Docker/HTTP deployment path (see Dockerfile, port 8000).
    # Stdio clients (Claude Desktop/Code via `uvx mcp-metricool`) use the published
    # PyPI build, which sets transport='stdio'. Do not change this without also
    # updating the deployment target.
    mcp.run(
        transport="sse",
    )
