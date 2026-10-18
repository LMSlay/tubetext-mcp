# TubeText MCP servers

Remote MCP servers that give Claude, Cursor, VS Code, ChatGPT and any other MCP client access to [TubeText](https://apify.com/tubetext) tools: video transcripts, comment sentiment, AI video breakdowns, esports match timelines, ad library data, e-commerce prices, reviews, China data and travel prices.

There is nothing to install or host. Each server is a URL on Apify's hosted MCP server (`mcp.apify.com`) that exposes a small, focused set of TubeText Actors as tools. You sign in with your own Apify account (OAuth) or pass your Apify API token. You pay per result at each Actor's Store price, with a free monthly credit on every Apify account.

## Servers

| Server | What it does | Tools (Apify Actors) |
|---|---|---|
| **TikTok Transcripts, Comments, Video Breakdown & Shot Analysis**<br>`io.github.LMSlay/tubetext-tiktok-transcripts` | TikTok transcripts, comment sentiment by moment, AI breakdowns and director-level shot analysis. | [tiktok-transcript](https://apify.com/tubetext/tiktok-transcript)<br>[youtube-tiktok-comments-api](https://apify.com/tubetext/youtube-tiktok-comments-api)<br>[video-breakdown-ai](https://apify.com/tubetext/video-breakdown-ai)<br>[shot-by-shot-video-analysis](https://apify.com/tubetext/shot-by-shot-video-analysis) |
| **YouTube Transcripts, Comments & Channel Analytics**<br>`io.github.LMSlay/tubetext-youtube-transcripts` | YouTube transcripts, comment sentiment and the moments viewers react to, plus channel stats. | [youtube-transcript-fast](https://apify.com/tubetext/youtube-transcript-fast)<br>[youtube-tiktok-comments-api](https://apify.com/tubetext/youtube-tiktok-comments-api)<br>[youtube-channel-analytics](https://apify.com/tubetext/youtube-channel-analytics)<br>[socialblade-scraper](https://apify.com/tubetext/socialblade-scraper)<br>[shot-by-shot-video-analysis](https://apify.com/tubetext/shot-by-shot-video-analysis) |
| **Instagram, Facebook, X, Reddit & Podcast Transcripts**<br>`io.github.LMSlay/tubetext-social-video-transcripts` | Transcribe Instagram Reels, Facebook, X and Reddit videos, podcasts (RSS, Apple) and any video URL. | [instagram-reels-transcript](https://apify.com/tubetext/instagram-reels-transcript)<br>[facebook-video-transcript](https://apify.com/tubetext/facebook-video-transcript)<br>[twitter-x-video-transcript](https://apify.com/tubetext/twitter-x-video-transcript)<br>[podcast-transcript](https://apify.com/tubetext/podcast-transcript)<br>[any-video-podcast-transcript](https://apify.com/tubetext/any-video-podcast-transcript)<br>[reddit-video-transcript](https://apify.com/tubetext/reddit-video-transcript) |
| **Meta Ad Library & Video Ad Analyzer**<br>`io.github.LMSlay/tubetext-ad-intelligence` | Meta Ad Library ads plus AI teardowns and shot-by-shot analysis of Meta and YouTube video ads. | [meta-ad-library-videos](https://apify.com/tubetext/meta-ad-library-videos)<br>[video-ad-analyzer](https://apify.com/tubetext/video-ad-analyzer)<br>[shot-by-shot-video-analysis](https://apify.com/tubetext/shot-by-shot-video-analysis) |
| **E-commerce Prices: Amazon, Taobao, AliExpress, Idealo**<br>`io.github.LMSlay/tubetext-ecommerce-prices` | Products, prices and sellers from Amazon, Taobao/Tmall, AliExpress, TikTok Shop and Idealo (EU). | [amazon-product-search-scraper](https://apify.com/tubetext/amazon-product-search-scraper)<br>[taobao-tmall-scraper](https://apify.com/tubetext/taobao-tmall-scraper)<br>[aliexpress-search-scraper](https://apify.com/tubetext/aliexpress-search-scraper)<br>[tiktok-shop-product-scraper](https://apify.com/tubetext/tiktok-shop-product-scraper)<br>[idealo-price-scraper](https://apify.com/tubetext/idealo-price-scraper) |
| **Reviews + AI Insights: Steam, Agoda, Google Play**<br>`io.github.LMSlay/tubetext-reviews-insights` | Steam game, Agoda/Booking.com hotel and Google Play app reviews with optional AI insight reports. | [steam-reviews-scraper](https://apify.com/tubetext/steam-reviews-scraper)<br>[agoda-reviews-scraper](https://apify.com/tubetext/agoda-reviews-scraper)<br>[google-play-reviews-ai](https://apify.com/tubetext/google-play-reviews-ai) |
| **China Data: Taobao, Bilibili, WeChat, Trending**<br>`io.github.LMSlay/tubetext-china-data` | Taobao/Tmall, Bilibili videos + transcripts, WeChat articles, China hot search, suppliers by photo. | [taobao-tmall-scraper](https://apify.com/tubetext/taobao-tmall-scraper)<br>[bilibili-scraper](https://apify.com/tubetext/bilibili-scraper)<br>[bilibili-video-transcript](https://apify.com/tubetext/bilibili-video-transcript)<br>[china-trending-topics](https://apify.com/tubetext/china-trending-topics)<br>[wechat-articles-scraper](https://apify.com/tubetext/wechat-articles-scraper)<br>[alibaba-yiwu-image-search](https://apify.com/tubetext/alibaba-yiwu-image-search) |
| **Travel & Local Prices: Flights, Hotels, Gas**<br>`io.github.LMSlay/tubetext-travel-local-prices` | Google Flights fares and price calendar, Google Hotels rates by date, US/Canada gas station prices. | [google-flights-scraper](https://apify.com/tubetext/google-flights-scraper)<br>[google-hotels-scraper](https://apify.com/tubetext/google-hotels-scraper)<br>[gas-prices-scraper](https://apify.com/tubetext/gas-prices-scraper) |
| **Esports Match Timelines: Valorant & CS2**<br>`io.github.LMSlay/tubetext-esports-match-data` | Round-by-round Valorant and CS2 scores read from public broadcast VODs on YouTube and Twitch. | [esports-match-timeline](https://apify.com/tubetext/esports-match-timeline)<br>[youtube-transcript-fast](https://apify.com/tubetext/youtube-transcript-fast)<br>[youtube-tiktok-comments-api](https://apify.com/tubetext/youtube-tiktok-comments-api) |

## Connect

**Claude Code**
```bash
claude mcp add --transport http tubetext-tiktok "https://mcp.apify.com/?tools=fetch-actor-details,tubetext/tiktok-transcript,tubetext/youtube-tiktok-comments-api,tubetext/video-breakdown-ai,tubetext/shot-by-shot-video-analysis"
```

**Claude Desktop / claude.ai**: Settings → Connectors → Add custom connector → paste a server URL from the list below, then sign in to Apify.

**Cursor / VS Code / other clients** (`mcp.json`):
```json
{
  "mcpServers": {
    "tubetext-tiktok": {
      "url": "https://mcp.apify.com/?tools=fetch-actor-details,tubetext/tiktok-transcript,tubetext/youtube-tiktok-comments-api,tubetext/video-breakdown-ai,tubetext/shot-by-shot-video-analysis"
    }
  }
}
```
Clients without OAuth: add the header `Authorization: Bearer <your Apify API token>` ([get one here](https://console.apify.com/account/integrations)).

### Server URLs

- **TikTok Transcripts, Comments, Video Breakdown & Shot Analysis**: `https://mcp.apify.com/?tools=fetch-actor-details,tubetext/tiktok-transcript,tubetext/youtube-tiktok-comments-api,tubetext/video-breakdown-ai,tubetext/shot-by-shot-video-analysis`
- **YouTube Transcripts, Comments & Channel Analytics**: `https://mcp.apify.com/?tools=fetch-actor-details,tubetext/youtube-transcript-fast,tubetext/youtube-tiktok-comments-api,tubetext/youtube-channel-analytics,tubetext/socialblade-scraper,tubetext/shot-by-shot-video-analysis`
- **Instagram, Facebook, X, Reddit & Podcast Transcripts**: `https://mcp.apify.com/?tools=fetch-actor-details,tubetext/instagram-reels-transcript,tubetext/facebook-video-transcript,tubetext/twitter-x-video-transcript,tubetext/podcast-transcript,tubetext/any-video-podcast-transcript,tubetext/reddit-video-transcript`
- **Meta Ad Library & Video Ad Analyzer**: `https://mcp.apify.com/?tools=fetch-actor-details,tubetext/meta-ad-library-videos,tubetext/video-ad-analyzer,tubetext/shot-by-shot-video-analysis`
- **E-commerce Prices: Amazon, Taobao, AliExpress, Idealo**: `https://mcp.apify.com/?tools=fetch-actor-details,tubetext/amazon-product-search-scraper,tubetext/taobao-tmall-scraper,tubetext/aliexpress-search-scraper,tubetext/tiktok-shop-product-scraper,tubetext/idealo-price-scraper`
- **Reviews + AI Insights: Steam, Agoda, Google Play**: `https://mcp.apify.com/?tools=fetch-actor-details,tubetext/steam-reviews-scraper,tubetext/agoda-reviews-scraper,tubetext/google-play-reviews-ai`
- **China Data: Taobao, Bilibili, WeChat, Trending**: `https://mcp.apify.com/?tools=fetch-actor-details,tubetext/taobao-tmall-scraper,tubetext/bilibili-scraper,tubetext/bilibili-video-transcript,tubetext/china-trending-topics,tubetext/wechat-articles-scraper,tubetext/alibaba-yiwu-image-search`
- **Travel & Local Prices: Flights, Hotels, Gas**: `https://mcp.apify.com/?tools=fetch-actor-details,tubetext/google-flights-scraper,tubetext/google-hotels-scraper,tubetext/gas-prices-scraper`
- **Esports Match Timelines: Valorant & CS2**: `https://mcp.apify.com/?tools=fetch-actor-details,tubetext/esports-match-timeline,tubetext/youtube-transcript-fast,tubetext/youtube-tiktok-comments-api`

## Example prompts

- "Get the transcript of this TikTok and break down its hook and shot list: <url>"
- "Break down this ad shot by shot and show where viewers replayed or commented: <url>"
- "Transcribe the last 10 videos on this YouTube channel and summarize the main topics."
- "Which moments of this YouTube video did viewers react to, and how did the top comments feel about them? <url>"
- "Give me the round-by-round score timeline of this Valorant match VOD: <url>"
- "Pull Nike's active video ads from Meta Ad Library and tell me which angles they test."
- "Compare prices for this product on Idealo in Germany, France and Italy."
- "What do Steam players complain about most in the recent reviews of <game>?"

## Costs and safety

- Every tool is a pay-per-event Apify Actor. Each Actor's Store page lists its price. Failed or empty results are not billed.
- The Actors accept a maximum cost per run and stop cleanly when they reach it. The MCP server sets no cap of its own, so ask your agent to pass `maxTotalChargeUsd` for large jobs.
- No login or cookies are used. The tools read public pages only.

## Feedback

Problem or missing feature? Open an issue on the Actor's Store page (Issues tab) or [here](https://github.com/LMSlay/tubetext-mcp/issues). Business or custom work: [email us](mailto:tubettext@gmail.com).

Published to the [official MCP Registry](https://registry.modelcontextprotocol.io) under `io.github.LMSlay/*` via GitHub Actions OIDC (`.github/workflows/publish-mcp-registry.yml`).
