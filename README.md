# Superagent Python Library

[![pypi](https://img.shields.io/pypi/v/fern-superagent.svg)](https://pypi.python.org/pypi/superagent-py)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

## Installation

Add this dependency to your project's build file:

```bash
pip install superagent-py
# or
poetry add superagent-py
```

## Usage

```python
from superagent.client import Superagent

client = Superagent(token="API_TOKEN")

agent = client.agents.get_agent("<AGENT_ID>")

print("Received response from superagent", agent)
```

## Async Client

```python
from superagent.client import AsyncSuperagent

import asyncio

client = AsyncSuperagent(token="API_TOKEN")

async def get_agent() -> None:
    agent = client.agents.get_agent("<AGENT_ID>")
    print(token_response)

asyncio.run(get_agent())
```

## Handling Exceptions

All exceptions thrown by the SDK will sublcass [moneykit.ApiError](./src/moneykit/core/api_error.py).

```python
from superagent.core import ApiError

try:
  client.agents.get_agent("<AGENT_ID>")
except APIError as e:
  # handle any api related error
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 422         | `UnprocessableEntityError` |

## Beta status

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning the package version to a specific version in your pyproject.toml file. This way, you can install the same version each time without breaking changes unless you are intentionally looking for the latest version.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
