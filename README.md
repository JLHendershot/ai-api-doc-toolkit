# ai-api-doc-toolkit

ai-api-doc-toolkit uses Python and the Claude AI API to fetch data from a REST API endpoint, generate a plain-English summary of the response, and compile that summary into formatted markdown documentation.

## How It Works

The toolkit runs as a three-script pipeline. Each script handles one stage of the process and passes its output to the next.

**fetch_api_data.py** reads from config/api_config.json and makes a GET request to each configured API endpoint. The response is trimmed to the configured limit and saved to data/{api_name}_raw.json.

**summarize_response_ai.py** reads the raw JSON and sends it to Claude via the Anthropic API. The prompt instructs Claude to produce a one-sentence description of what the endpoint does, a plain-English explanation of each field in the response, and one example use case for the endpoint. The response is saved to data/{api_name}_summary.json as structured JSON containing an endpoint summary, field descriptions, use cases, and an example.

**export_docs.py** loads the raw API data and the AI-generated summary, builds a structured markdown document, and writes it to docs/{api_name}_summary.md.

## Project Structure

```
ai-api-doc-toolkit/
├── scripts/
│   ├── fetch_api_data.py                 # Fetches and saves raw API response
│   ├── summarize_response_ai.py          # Sends data to Claude for AI analysis
│   └── export_docs.py                    # Builds final markdown documentation
├── data/
│   ├── {api_name}_raw.json               # Raw API output (generated)
│   └── {api_name}_summary.json           # Claude's plain-English summary (generated)
├── docs/
│   └── jsonplaceholder_posts_summary.md  # Final compiled documentation (generated)
|──  config/
│   └── api_config.json                   # API endpoint configuration

```

## Requirements

- Python 3.x
- An [Anthropic API key](https://console.anthropic.com/)

1. Install dependencies:

```bash
pip install anthropic requests
```

2. Set your API key as an environment variable:

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

## Usage

1. You should configure config/api_config.json with your API endpoints first.
2. Run the scripts in order from the project root:

```bash
python scripts/fetch_api_data.py
python scripts/summarize_response_ai.py
python scripts/export_docs.py
```

The final documentation is available in the docs/ folder, named {api_name}_summary.md for each configured API.

## Tools and Technologies

- **Python** — scripting and file I/O
- **Anthropic Claude API** — AI-powered response analysis and documentation writing
- **JSONPlaceholder** — used as the default example API
- **Markdown** — output format for generated documentation
