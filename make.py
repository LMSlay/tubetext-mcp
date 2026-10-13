"""Generate registry/<slug>/server.json for the TubeText MCP Registry bundles (remote = mcp.apify.com, no hosted server)."""
import json, os
NS = "io.github.LMSlay"
REPO = "https://github.com/LMSlay/tubetext-mcp"
BUNDLES = [
  ("tiktok-transcripts", "TikTok Transcripts & Video Breakdown",
   "TikTok video transcripts (captions or Whisper AI) plus AI hook, shot list and script breakdown.",
   ["tiktok-transcript", "video-breakdown-ai"]),
  ("youtube-transcripts", "YouTube Transcripts & Channel Analytics",
   "YouTube transcripts from videos, Shorts, playlists or channels, plus channel and Social Blade stats.",
   ["youtube-transcript-fast", "youtube-channel-analytics", "socialblade-scraper"]),
  ("social-video-transcripts", "Instagram, Facebook, X & Podcast Transcripts",
   "Transcribe Instagram Reels, Facebook and X videos, podcasts (RSS, Apple) and any video URL to text.",
   ["instagram-reels-transcript", "facebook-video-transcript", "twitter-x-video-transcript", "podcast-transcript", "any-video-podcast-transcript"]),
  ("ad-intelligence", "Meta Ad Library & Video Ad Analyzer",
   "Facebook/Instagram ads from Meta Ad Library plus AI teardowns of Meta and YouTube video ads.",
   ["meta-ad-library-videos", "video-ad-analyzer"]),
  ("ecommerce-prices", "E-commerce Prices: Amazon, Taobao, AliExpress, Idealo",
   "Products, prices and sellers from Amazon, Taobao/Tmall, AliExpress, TikTok Shop and Idealo (EU).",
   ["amazon-product-search-scraper", "taobao-tmall-scraper", "aliexpress-search-scraper", "tiktok-shop-product-scraper", "idealo-price-scraper"]),
  ("reviews-insights", "Reviews + AI Insights: Steam, Agoda, Google Play",
   "Steam game, Agoda/Booking.com hotel and Google Play app reviews with optional AI insight reports.",
   ["steam-reviews-scraper", "agoda-reviews-scraper", "google-play-reviews-ai"]),
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
