# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python implementation of a "think" MCP (Model Context Protocol) server using FastMCP from the official MCP Python SDK. The server provides thinking/reasoning capabilities to MCP clients through a simple tool interface.

## Development Commands

### Setup and Installation
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Unix/macOS)  
source venv/bin/activate

# Install MCP SDK with CLI support
pip install "mcp[cli]"

# Install additional dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### Running and Testing
```bash
# Run the MCP server via uvx from local directory (recommended)
uvx --from . q-think-mcp

# Run the MCP server as a Python module
python -m q_think_mcp

# Run the MCP server directly  
python q_think_mcp/server.py

# Run via MCP CLI (if configured)
mcp run q_think_mcp.server

# After publishing to PyPI, you can run directly:
# uvx q-think-mcp

# Run tests
pytest

# Run tests with coverage
pytest --cov=q_think_mcp

# Run linting
ruff check .

# Run type checking
mypy q_think_mcp/
```

## Architecture

### FastMCP-based Implementation

This project uses FastMCP from the official MCP Python SDK for simplified server creation:

1. **Main Server** (`think_server.py`)
   - FastMCP server instance with think tool
   - Uses `@mcp.tool()` decorator for tool registration
   - Handles automatic serialization and validation

2. **Think Tool Implementation** (`q_think_mcp/server.py`)
   - Single function decorated with `@mcp.tool()`
   - Takes structured input parameters
   - Returns formatted thinking responses

### Key Dependencies
- `mcp[cli]`: Official MCP Python SDK with CLI support
- `pydantic`: Data validation (built into FastMCP)
- `typing`: Type hints for automatic schema generation

### FastMCP Key Features
- **Automatic Schema Generation**: Type hints become JSON schema
- **Built-in Validation**: Input/output validation via type annotations
- **Simplified Server Setup**: Minimal boilerplate code
- **CLI Integration**: Easy testing with MCP CLI tools

## Think Tool Implementation

FastMCP implementation using decorators:

### Implementation
```python
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel

mcp = FastMCP("Q-Think MCP Server")

class ThinkResponse(BaseModel):
    thought_process: str
    reasoning_steps: list[str]
    confidence: float
    metadata: dict

@mcp.tool()
def think(thought: str) -> ThinkResponse:
    """
    Use the tool to think about something. It will not obtain new information or change the database, 
    but just append the thought to the log. Use it when complex reasoning or some cache memory is needed.
    """
    # Process the thought and return structured response
    # Implementation details in think_server.py
```

### Tool Schema
The think tool follows this exact schema:
```json
{
  "name": "think",
  "description": "Use the tool to think about something. It will not obtain new information or change the database, but just append the thought to the log. Use it when complex reasoning or some cache memory is needed.",
  "input_schema": {
    "type": "object",
    "properties": {
      "thought": {
        "type": "string",
        "description": "A thought to think about."
      }
    },
    "required": ["thought"]
  }
}
```

## File Structure Guidelines

```
q-think-mcp/
├── q_think_mcp/          # Main package directory
│   ├── __init__.py       # Package initialization
│   ├── __main__.py       # Module entry point for python -m
│   └── server.py         # Main FastMCP server
├── requirements.txt       # Dependencies
├── pyproject.toml        # Project configuration
├── tests/
│   └── test_think_server.py # Tests for think functionality
├── README.md             # Project documentation
└── CLAUDE.md             # This file
```

## Testing Strategy

- Unit tests for think function logic
- FastMCP server functionality tests
- MCP client integration tests using official SDK tools
- Testing via MCP CLI: `mcp run think_server.py`

## Development Tips

### FastMCP Best Practices
- Use type hints for automatic schema generation
- Return Pydantic models for structured output
- Keep tool functions focused and single-purpose
- Use descriptive docstrings (become tool descriptions)

### Testing with MCP CLI
```bash
# Install MCP CLI tools
pip install "mcp[cli]"

# Test the server
mcp run think_server.py

# Interactive testing
mcp client think_server.py
```

### Error Handling
FastMCP automatically handles:
- Input validation via type hints
- JSON serialization/deserialization
- MCP protocol message formatting
- Client connection management