# ai-api-doc-toolkit

ai-api-doc-toolkit uses Python and the Claude AI API to fetch data from a REST API endpoint, generate a plain-English summary of the response, and compile that summary into formatted markdown documentation.

## How It Works

The toolkit runs as a three-script pipeline. Each script handles one stage of the process and passes its output to the next.

**fetch_api_data.py** makes a GET request to the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/posts), a free public REST API used for prototyping. The response is converted to JSON, trimmed to the first five results, and saved to `data/raw_api_response.json`.

**summarize_response_ai.py** reads the raw JSON and sends it to Claude via the Anthropic API. The prompt instructs Claude to produce a one-sentence description of what the endpoint does, a plain-English explanation of each field in the response, and one example use case for the endpoint. The response is saved to `data/ai_summary.txt`.

**export_docs.py** loads the raw API data and the AI-generated summary, builds a structured markdown document, and writes it to `docs/generated_api_summary.md`.

## Project Structure

```
ai-api-doc-toolkit/
├── scripts/
│   ├── fetch_api_data.py          # Fetches and saves raw API response
│   ├── summarize_response_ai.py   # Sends data to Claude for AI analysis
│   └── export_docs.py             # Builds final markdown documentation
├── data/
│   ├── raw_api_response.json      # Raw API output (generated)
│   └── ai_summary.txt             # Claude's plain-English summary (generated)
├── docs/
│   └── generated_api_summary.md  # Final compiled documentation (generated)
└── examples/
```

## Requirements

- Python 3.x
- An [Anthropic API key](https://console.anthropic.com/)

Install dependencies:

```bash
pip install anthropic requests
```

Set your API key as an environment variable:

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

## Usage

Run the scripts in order from the project root:

```bash
python scripts/fetch_api_data.py
python scripts/summarize_response_ai.py
python scripts/export_docs.py
```

The final documentation is available at `docs/generated_api_summary.md`.

## Tools and Technologies

- **Python** — scripting and file I/O
- **Anthropic Claude API** — AI-powered response analysis and documentation writing
- **JSONPlaceholder** — public REST API used as the data source
- **Markdown** — output format for generated documentation
