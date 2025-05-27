from fastmcp import FastMCP
from typing import List, Dict, Optional
import httpx
import json
import os

# Initialize FastMCP server
mcp = FastMCP("TryKitt.ai MCP Server")

# Base URL for the API
BASE_URL = "https://api.trykitt.ai"

# Get API key from environment variable
API_KEY = os.getenv("TRYKITT_API_KEY")

# Initialize HTTP client with headers and SSL verification disabled
http_client = httpx.AsyncClient(
    base_url=BASE_URL,
    headers={"x-api-key": API_KEY} if API_KEY else {},
    verify=False,  # Disable SSL verification
)


@mcp.tool()
async def verify_email_send(email: str, custom_data: Optional[str] = None) -> Dict:
    """
    verify an email using trykitt.

    Args:
        email: The email address to verify
        custom_data: Optional custom data to associate with the request
    """
    payload = {"email": email, "realtime": True}
    if custom_data:
        payload["customData"] = custom_data

    response = await http_client.post("/job/verify_email", json=payload)
    return response.json()


@mcp.tool()
async def find_email(
    full_name: str,
    domain: str,
    linkedin_url: Optional[str] = None,
    custom_data: Optional[str] = None,
) -> Dict:
    """
    Find an email address for a person.

    Args:
        full_name: The full name of the person
        domain: The company domain or website
        linkedin_url: Optional LinkedIn profile URL
        custom_data: Optional custom data to associate with the request
    """
    payload = {"fullName": full_name, "domain": domain, "realtime": True}
    if linkedin_url:
        payload["linkedinStandardProfileURL"] = linkedin_url
    if custom_data:
        payload["customData"] = custom_data

    response = await http_client.post("/job/find_email", json=payload)
    return response.json()


@mcp.tool()
async def get_job_status(job_id: str) -> Dict:
    """
    Get the status of a job.

    Args:
        job_id: The ID of the job to check
    """
    response = await http_client.get(f"/job?id={job_id}")
    return response.json()


@mcp.tool()
async def list_jobs() -> Dict:
    """
    List jobs
    """
    response = await http_client.get(f"/job")
    return response.json()


if __name__ == "__main__":
    mcp.run()
