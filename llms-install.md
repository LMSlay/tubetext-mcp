# Installing TubeText MCP servers (instructions for AI coding agents)

TubeText servers are **remote** MCP servers hosted on Apify (`mcp.apify.com`, Streamable HTTP). There is nothing to install, build or run locally.

## 1. Pick a server URL
Choose the bundle that matches the user's request (full list in README.md → "Server URLs"):
- TikTok transcripts, comments + AI video breakdown: `https://mcp.apify.com/?tools=fetch-actor-details,tubetext/tiktok-transcript,tubetext/youtube-tiktok-comments-api,tubetext/video-breakdown-ai,tubetext/shot-by-shot-video-analysis`
- YouTube transcripts, comments + channel analytics: `https://mcp.apify.com/?tools=fetch-actor-details,tubetext/youtube-transcript-fast,tubetext/youtube-shorts-scraper,tubetext/youtube-tiktok-comments-api,tubetext/youtube-channel-analytics,tubetext/socialblade-scraper,tubetext/shot-by-shot-video-analysis`
- For the other 7 bundles (social video transcripts, ad intelligence, e-commerce prices, reviews, China data, travel prices, esports match data), copy the URL from README.md.

## 2. Authentication
Use one of these:
- **OAuth (preferred).** Clients that support MCP OAuth (Claude, Cursor, VS Code, Cline) open a browser window to sign in to Apify on first use. No token handling needed.
- **API token.** If the client has no OAuth, have the user configure an existing token privately using their client's supported secret handling (https://console.apify.com/account/integrations). The authorization header is `Authorization: Bearer <token>`. Do not ask them to paste a token into chat, a public issue or a committed file.

Review the selected Actor's live Pricing tab before any run. A failed or empty result may avoid a particular result event while still incurring Actor Start, data-fetch or other charges. Optional AI processing and downstream services may add costs.

## 3. Client configuration
**Generic remote-client example:**
```json
{
  "mcpServers": {
    "tubetext-tiktok": {
      "url": "https://mcp.apify.com/?tools=fetch-actor-details,tubetext/tiktok-transcript,tubetext/youtube-tiktok-comments-api,tubetext/video-breakdown-ai,tubetext/shot-by-shot-video-analysis"
    }
  }
}
```
Configuration filenames, top-level keys and transport fields vary by client. Generate the exact configuration in the [Apify MCP configurator](https://mcp.apify.com/) or follow your client's documentation; do not copy one client's schema into another. [VS Code reference](https://code.visualstudio.com/docs/agents/reference/mcp-configuration). Prefer OAuth over storing a raw token in JSON.

**Claude Code:**
```bash
claude mcp add --transport http tubetext-tiktok "https://mcp.apify.com/?tools=fetch-actor-details,tubetext/tiktok-transcript,tubetext/youtube-tiktok-comments-api,tubetext/video-breakdown-ai,tubetext/shot-by-shot-video-analysis"
```

## 4. Verify discovery before running anything
List the available tools and inspect their current schemas. For the TikTok bundle, check for `tubetext--tiktok-transcript`, `tubetext--video-breakdown-ai` and `tubetext--shot-by-shot-video-analysis`. Report missing tools rather than assuming directory-cached schemas are current. Tool discovery is not a live Actor test.

Do not launch an Actor merely to verify installation. If the user authorizes a paid functional test, agree on one public URL, the exact Actor, input options and a cost limit first. For YouTube captions-only work, explicitly use `aiFallback: false`; AI transcription is otherwise enabled by default. See the [bounded YouTube example](README.md#start-with-a-bounded-youtube-use-case).

Use the current tool schema for run-limit placement. With Apify's generic `call-actor`, put `maxTotalChargeUsd`, `maxItems`, `timeout` and `memory` in `callOptions`, not in Actor input ([official reference](https://docs.apify.com/mcp)). Do not assume the selected Actor wrapper accepts those same fields. A run limit is not a cap on downstream model or integration spending.

If a call returns a run ID before completion, inspect that run with `get-actor-run` and retrieve its dataset with `get-dataset-items` when those tools are available. Do not start a duplicate paid run just because the first call timed out. Preserve run IDs, dataset IDs and exports, and inspect unsuccessful rows before using the output.
