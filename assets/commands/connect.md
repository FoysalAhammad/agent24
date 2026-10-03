---
description: Add a provider to Agent24
agent: build
---

# /connect Command

Add a provider to Agent24. Allows you to select from available providers and add their API keys.

## Kaj (Bangla)

Ei command diye LLM provider add kora jay. Provider select kore API key dile connect hoy.

## Flow

1. Available providers list dekhao
2. Provider select koro
3. API key input koro
4. Connect confirm koro
5. Available models dekha jay

## Available Providers

- **OpenAI** - GPT-4, GPT-5, GPT-4o
- **Anthropic** - Claude Sonnet, Claude Haiku
- **Google** - Gemini Pro, Gemini Flash
- **OpenCode Zen** - Optimized models
- **Local** - Ollama, LM Studio

## Android Implementation

1. Provider selection dialog show koro
2. API key input field dekhao
3. API key validate koro (background e)
4. Connect success hole config e save koro
5. Available models fetch koro

## Desktop Reference

Real OpenCode te `/connect` command:
- OpenCode auth page open kore
- Browser e redirect kore
- API key auto-fetch kore

## Permissions

- Network access lage
- Storage write permission lage (config save)

## Example

```
/connect
```

Then select provider and enter API key.

## Config Save Location

Android:
```
/data/data/com.agnt24/files/home/.config/agent24/provider.json
```

## Provider Config Format

```json
{
  "provider": "anthropic",
  "apiKey": "sk-ant-xxxxx",
  "models": [
    "claude-sonnet-4-5",
    "claude-haiku-4-5"
  ]
}
```
