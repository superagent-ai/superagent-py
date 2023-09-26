<div align="center">

# Superagent Python SDK 🥷

### The open framework for building AI Assistants

<p>
<img alt="PyPi" src="https://img.shields.io/pypi/v/fern-superagent.svg" />
<img alt="Fern" src="https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen" />
<img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/homanp/superagent-py" />
<img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/homanp/superagent-py" />
<img alt="" src="https://img.shields.io/github/repo-size/homanp/superagent-py" />
<img alt="GitHub Issues" src="https://img.shields.io/github/issues/homanp/superagent-py" />
<img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/homanp/superagent-py" />
<img alt="Github License" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
<img alt="Discord" src="https://img.shields.io/discord/1110910277110743103?label=Discord&logo=discord&logoColor=white&style=plastic&color=d7b023)](https://discord.gg/e8j7mgjDUK" />
</p>

</div>

-----

Superagent is an open source framework that enables any developer to integrate production ready AI Assistants into any application in a matter of minutes.

-----

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

client = Superagent(token="API_TOKEN", base_url="https://api.beta.superagent.sh")

agent = client.agents.create(request={
    "name": "My Agent",
    "description": "My awesome agent",
    "isActive": True,
    "llmModel": "GPT_4_0613"
})

output = client.agent.invoke(
    agent_id=agent.data.id,
    input="Hi there!",
    enable_streaming=False,
    session_id="123"
)

print("Received response from superagent", agent.data)
```

## Async Client

```python
from superagent.client import AsyncSuperagent

agent = await client.agents.create(request={
    "name": "My Agent",
    "description": "My awesome agent",
    "isActive": True,
    "llmModel": "GPT_4_0613"
})

output = await client.agent.invoke(
    agent_id=agent.data.id,
    input="Hi there!",
    enable_streaming=False,
    session_id="123"
)

print("Received response from superagent", agent.data)
```

## Handling Exceptions

All exceptions thrown by the SDK will sublcass [moneykit.ApiError](./src/moneykit/core/api_error.py).

```python
from superagent.core import ApiError

try:
  client.agents.get(agent_id="12312")
except APIError as e:
  # handle any api related error
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 422         | `UnprocessableEntityError` |

## Acknowledgements

A special thanks to the [Fern](https://buildwithfern.com/) team for all support with the Superagent libraries and SDKS ❤️.

## Beta status

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning the package version to a specific version in your pyproject.toml file. This way, you can install the same version each time without breaking changes unless you are intentionally looking for the latest version.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
