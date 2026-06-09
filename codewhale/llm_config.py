"""LLM Provider Configuration"""

LLM_PROVIDERS = {
    "openai": {
        "base_url": "https://api.openai.com/v1",
        "api_key_env": "OPENAI_API_KEY",
    },
    "astraflow": {
        "base_url": "https://api-us-ca.umodelverse.ai/v1",
        "api_key_env": "ASTRAFLOW_API_KEY",
    },
}