# Text Summarization
Repo showcasing Vietnamese news summary tools.
## Summary
This repo introduces a simple but effective tool for summarizing paragraphs. This tool can work with PDF documents and plain text in Vietnamese language, finetuned based on "t5-vie-summarize" model.
## Setup

### Installing Dependencies
- Python 3 installation.
-  Python packages: Transformers, flask.

## Running

### Web UI

In order to run Web UI, you need to turn on the server by run `python3 app.py` in the repo folder. Then access the Web UI by running the `index.html` file if using locally, or can integrate and deploy to a domain if you want. This should open Web UI interface in the browser.


## Details

### Workflow


Depending on the document size, this tool works in following modes:
1. In the simple case, if the whole document can fit into model's context window then summarizartion is based on adding relevant summarization prompt.
2. In case of large documents, document processed using "map-reduce" pattern:
  1. The document is first split into smaller chunks which tries to respect paragraph and sentence boundarions.
  2. Each chunk is summarized separately (map step).
  3. Chunk summarization are summarized again to give final summary (reduce step).

### Local processing
- All processing is done locally on the user's machine. 
