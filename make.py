"""Generate registry/<slug>/server.json for the TubeText MCP Registry bundles (remote = mcp.apify.com, no hosted server)."""
import json, os
NS = "io.github.LMSlay"
REPO = "https://github.com/LMSlay/tubetext-mcp"
BUNDLES = [
  ("tiktok-transcripts", "TikTok Transcripts, Comments, Video Breakdown & Shot Analysis",
   "TikTok transcripts, comment sentiment by moment, AI breakdowns and director-level shot analysis.",
   ["tiktok-transcript", "youtube-tiktok-comments-api", "video-breakdown-ai", "shot-by-shot-video-analysis"]),
  ("youtube-transcripts", "YouTube Transcripts, Comments & Channel Analytics",
   "YouTube transcripts, comment sentiment and the moments viewers react to, plus channel stats.",
   ["youtube-transcript-fast", "youtube-tiktok-comments-api", "youtube-channel-analytics", "socialblade-scraper", "shot-by-shot-video-analysis"]),
  ("social-video-transcripts", "Instagram, Facebook, X, Reddit & Podcast Transcripts",
   "Transcribe Instagram Reels, Facebook, X and Reddit videos, podcasts (RSS, Apple) and any video URL.",
   ["instagram-reels-transcript", "facebook-video-transcript", "twitter-x-video-transcript", "podcast-transcript", "any-video-podcast-transcript", "reddit-video-transcript"]),
  ("ad-intelligence", "Meta Ad Library & Video Ad Analyzer",
   "Meta Ad Library ads plus AI teardowns and shot-by-shot analysis of Meta and YouTube video ads.",
   ["meta-ad-library-videos", "video-ad-analyzer", "shot-by-shot-video-analysis"]),
  ("ecommerce-prices", "E-commerce Prices: Amazon, Taobao, AliExpress, Idealo",
   "Products, prices and sellers from Amazon, Taobao/Tmall, AliExpress, TikTok Shop and Idealo (EU).",
   ["amazon-product-search-scraper", "taobao-tmall-scraper", "aliexpress-search-scraper", "tiktok-shop-product-scraper", "idealo-price-scraper"]),
  ("reviews-insights", "Reviews + AI Insights: Steam, Agoda, Google Play",
   "Steam game, Agoda/Booking.com hotel and Google Play app reviews with optional AI insight reports.",
   ["steam-reviews-scraper", "agoda-reviews-scraper", "google-play-reviews-ai"]),
  ("china-data", "China Data: Taobao, Bilibili, WeChat, Trending",
   "Taobao/Tmall, Bilibili videos + transcripts, WeChat articles, China hot search, suppliers by photo.",
   ["taobao-tmall-scraper", "bilibili-scraper", "bilibili-video-transcript", "china-trending-topics", "wechat-articles-scraper", "alibaba-yiwu-image-search"]),
  ("travel-local-prices", "Travel & Local Prices: Flights, Hotels, Gas",
   "Google Flights fares and price calendar, Google Hotels rates by date, US/Canada gas station prices.",
   ["google-flights-scraper", "google-hotels-scraper", "gas-prices-scraper"]),
  ("esports-match-data", "Esports Match Timelines: Valorant & CS2",
   "Round-by-round Valorant and CS2 scores read from public broadcast VODs on YouTube and Twitch.",
   ["esports-match-timeline", "youtube-transcript-fast", "youtube-tiktok-comments-api"]),
]
for slug, title, desc, actors in BUNDLES:
    assert len(desc) <= 100, (slug, len(desc))
    tools = ",".join(["fetch-actor-details"] + [f"tubetext/{a}" for a in actors])
    d = {
      "$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json",
      "name": f"{NS}/tubetext-{slug}",
      "title": title,
      "description": desc,
      "repository": {"url": REPO, "source": "github"},
      "version": "1.0.0",
      "websiteUrl": f"https://apify.com/tubetext/{actors[0]}",
      "remotes": [{
        "type": "streamable-http",
        "url": f"https://mcp.apify.com/?tools={tools}",
        "headers": [{"name": "Authorization",
                     "description": "Optional. Clients with OAuth sign in to Apify instead. Otherwise your own Apify token as Bearer <token>.",
                     "isRequired": False, "isSecret": True}]}]}
    os.makedirs(f"registry/{slug}", exist_ok=True)
    json.dump(d, open(f"registry/{slug}/server.json", "w"), indent=2)
    print(f"{slug:26} {len(title):3} {len(desc):3} {d['remotes'][0]['url']}")
