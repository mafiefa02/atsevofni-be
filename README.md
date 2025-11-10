# Backend for Atsevofni Challenge Overview

Atsevofni is not a real name, it is an alias for a fintech company operating in Indonesia, their real company name is confuscated for privacy purposes. They got me a challenge to build a dashboard presenting stock prices, using whatever stacks I am comfortable with.

This is the repository for said challenge's backend, built with FastAPI (Python).

## Quickstart

Prerequisites:

- The [uv](https://docs.astral.sh/uv) package manager
- Python 3.13+

If you don't have [uv](https://docs.astral.sh/uv) already installed, you can follow this [guide](https://docs.astral.sh/uv/getting-started/installation/).

### Starting the dev server

1. Clone this repository

```bash
git clone https://github.com/mafiefa02/atsevofni-be && cd atsevofni-be
```

2. Initialize new virtual environment and activate it

```bash
uv venv && source .venv/bin/activate
```

3. Install the dependencies

```bash
uv sync
```

4. Run the server!

```bash
uv run fastapi dev src/main.py
```

## What about deploying it?

There are many ways to deploy the service, the easiest way is to use the existing `Dockerfile`.
