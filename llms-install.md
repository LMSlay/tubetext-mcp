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
- **API token.** If the client has no OAuth, ask the user for their Apify API token (https://console.apify.com/account/integrations) and send it as the header `Authorization: Bearer <token>`. Never write the token into a file that is committed to git.

A free Apify account includes monthly platform credit. Each tool is a pay-per-event Apify Actor; prices are on each Actor's Store page, and failed or empty results are not billed.

## 3. Client configuration
**Cline / Cursor / VS Code (`mcp.json` / `cline_mcp_settings.json`):**
```json
{
  "mcpServers": {
    "tubetext-tiktok": {
      "type": "streamableHttp",
      "url": "https://mcp.apify.com/?tools=fetch-actor-details,tubetext/tiktok-transcript,tubetext/youtube-tiktok-comments-api,tubetext/video-breakdown-ai,tubetext/shot-by-shot-video-analysis"
    }
  }
}
```
If you use a token, add `"headers": { "Authorization": "Bearer <APIFY_TOKEN>" }` to the server entry.

**Claude Code:**
```bash
claude mcp add --transport http tubetext-tiktok "https://mcp.apify.com/?tools=fetch-actor-details,tubetext/tiktok-transcript,tubetext/youtube-tiktok-comments-api,tubetext/video-breakdown-ai,tubetext/shot-by-shot-video-analysis"
```

## 4. Verify
List the tools. You should see `tubetext--tiktok-transcript`, `tubetext--video-breakdown-ai` and `tubetext--shot-by-shot-video-analysis` (plus Apify helper tools such as `get-dataset-items`). Then do a test call with one public TikTok URL.

Runs can take longer than 45 s. If a call returns a run ID, poll it with `get-actor-run` and read results with `get-dataset-items`. For large jobs, ask the user for a cost cap and pass `maxTotalChargeUsd`.
