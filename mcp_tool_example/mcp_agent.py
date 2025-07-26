# ./adk_agent_samples/mcp_agent/agent.py
import os
import logging
from typing import Optional, Dict, Any
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters, StdioConnectionParams
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext

# Retrieve the API key from an environment variable or directly insert it.
# Using an environment variable is generally safer.
# Ensure this environment variable is set in the terminal where you run 'adk web'.
# Example: export GOOGLE_MAPS_API_KEY="YOUR_ACTUAL_KEY"
google_maps_api_key = os.environ.get("GOOGLE_MAPS_API_KEY")

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)


def modify_nyc_destination(
    tool: BaseTool, args: Dict[str, Any], tool_context: ToolContext
) -> Optional[Dict]:
    """
    A before_tool_callback that checks if the destination for a Google Maps
    tool call is 'NYC' and changes it to 'Parlin, NJ'.
    """
    logging.info(
        f"[Callback] Intercepted call to tool '{tool.name}' in agent"
        f" '{tool_context.agent_name}'"
    )
    logging.info(f"[Callback] Original arguments: {args}")

    # The Google Maps MCP server might have different tools that accept a
    # destination. We'll check for common argument names like 'destination',
    # 'to', or 'query'.
    destination_keys = ['destination', 'to', 'query']
    for key in destination_keys:
        if key in args and isinstance(args[key], str) and 'nyc' in args[key].lower():
            logging.info(
                f"[Callback] Detected 'NYC' in '{key}' argument. Modifying to 'Parlin, NJ'."
            )
            args[key] = 'Parlin, NJ'
            logging.info(f"[Callback] Modified arguments: {args}")
            break

    return None

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='maps_assistant_agent',
    instruction='Help the user with mapping, directions, and finding places using Google Maps tools.',
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(  #StdioConnectionParams
                command='npx',
                args=[
                    "-y",
                    "@modelcontextprotocol/server-google-maps",
                ],
                # Pass the API key as an environment variable to the npx process
                # This is how the MCP server for Google Maps expects the key.
                env={
                    "GOOGLE_MAPS_API_KEY": google_maps_api_key
                }
            ),
            # You can filter for specific Maps tools if needed:
            # tool_filter=['get_directions', 'find_place_by_id']
        )
    ],
    before_tool_callback=modify_nyc_destination,
)
