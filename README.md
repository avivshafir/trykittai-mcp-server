# TryKitt.ai FastMCP Server

A FastMCP (Model Context Protocol) server that provides email verification and finding capabilities using the [TryKitt.ai](https://trykitt.ai/) API. This server enables AI assistants to find and verify B2B email addresses with high accuracy and low bounce rates.

## Features

- **Email Verification**: Verify email addresses with advanced SMTP and catchall verification
- **Email Finding**: Find email addresses for individuals using their name and company domain
- **Job Management**: Track and monitor email verification/finding jobs
- **Real-time Processing**: Get immediate results for email operations
- **High Accuracy**: Leverages TryKitt.ai's advanced verification algorithms with <0.1% bounce rate

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd trykittai-mcp-server
```

2. Install dependencies using uv (recommended) or pip:
```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -r requirements.txt
```

## Setup

1. Get your TryKitt.ai API key:
   - Visit [TryKitt.ai](https://trykitt.ai/)
   - Sign up for an account
   - Navigate to your API settings to get your API key

2. Set your API key as an environment variable:
```bash
export TRYKITT_API_KEY="your_api_key_here"
```

Or create a `.env` file in the project root:
```
TRYKITT_API_KEY=your_api_key_here
```

## Usage

### Running the Server

Start the FastMCP server:
```bash
python server.py
```

The server will start and be available for MCP connections.

### Available Tools

#### 1. Email Verification (`verify_email_send`)

Verify if an email address is valid and deliverable.

**Parameters:**
- `email` (required): The email address to verify
- `custom_data` (optional): Custom data to associate with the request

**Example:**
```python
result = await verify_email_send("john.doe@example.com")
```

#### 2. Email Finding (`find_email`)

Find an email address for a person based on their name and company domain.

**Parameters:**
- `full_name` (required): The full name of the person
- `domain` (required): The company domain or website
- `linkedin_url` (optional): LinkedIn profile URL for better accuracy
- `custom_data` (optional): Custom data to associate with the request

**Example:**
```python
result = await find_email(
    full_name="John Doe",
    domain="example.com",
    linkedin_url="https://linkedin.com/in/johndoe"
)
```

#### 3. Job Status (`get_job_status`)

Check the status of a previously submitted job.

**Parameters:**
- `job_id` (required): The ID of the job to check

**Example:**
```python
result = await get_job_status("job_123456")
```

#### 4. List Jobs (`list_jobs`)

List all jobs (Note: This endpoint may have limited availability).

**Example:**
```python
result = await list_jobs()
```

## API Response Format

### Successful Email Verification
```json
{
  "id": "job_123456",
  "status": "completed",
  "result": {
    "email": "john.doe@example.com",
    "valid": true,
    "deliverable": true,
    "confidence": 0.95,
    "verification_type": "smtp_catchall"
  }
}
```

### Successful Email Finding
```json
{
  "id": "job_789012",
  "status": "completed",
  "result": {
    "email": "john.doe@example.com",
    "confidence": 0.88,
    "sources": ["pattern_matching", "web_scraping"]
  }
}
```

## Error Handling

The server handles various error scenarios:
- Invalid API keys
- Rate limiting
- Network timeouts
- Invalid email formats
- Domain verification failures

Common error responses:
```json
{
  "error": "Invalid API key",
  "code": 401
}
```

## Configuration

### Environment Variables

- `TRYKITT_API_KEY`: Your TryKitt.ai API key (required)

### SSL Configuration

The server is configured to work with TryKitt.ai's API endpoints. SSL verification is currently disabled for compatibility.

## Development

### Project Structure
```
trykittai-mcp-server/
├── server.py          # Main FastMCP server implementation
├── pyproject.toml     # Project dependencies and configuration
├── uv.lock           # Dependency lock file
├── README.md         # This file
├── LICENSE           # MIT License
└── .venv/            # Virtual environment
```

### Dependencies

- `fastmcp`: FastMCP framework for building MCP servers
- `httpx`: Async HTTP client for API requests
- `pydantic`: Data validation and settings management

## About TryKitt.ai

TryKitt.ai is an advanced email verification and finding service that:
- Provides unlimited free email verification for individual users
- Achieves <0.1% bounce rates through advanced verification
- Works 2-5X faster than alternative solutions
- Uses enterprise identity servers for catchall verification
- Detects job changes and validates against real systems

Learn more at [https://trykitt.ai/](https://trykitt.ai/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues related to:
- This MCP server: Open an issue in this repository
- TryKitt.ai API: Contact TryKitt.ai support
- FastMCP framework: Check the FastMCP documentation

## Changelog

### v1.0.0
- Initial release with email verification and finding capabilities
- Job status tracking
- Real-time processing support
- FastMCP integration
