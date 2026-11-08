# Facebook Ad Library Scraper | Competitor Ad Intelligence & Creatives

[![Apify Store](https://img.shields.io/badge/Apify%20Store-View%20Actor-brightgreen?logo=apify)](https://apify.com/misterkhan/facebook-ads-library-scraper)
[![GitHub stars](https://img.shields.io/github/stars/crawlomatic/facebook-ads-library-scraper?style=social)](https://github.com/crawlomatic/facebook-ads-library-scraper)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python SDK](https://img.shields.io/badge/SDK-Python-3776AB?logo=python&logoColor=white)](https://github.com/apify/apify-client-python)
[![Node.js SDK](https://img.shields.io/badge/SDK-Node.js-339933?logo=node.js&logoColor=white)](https://github.com/apify/apify-client-js)

> Scrape Meta/Facebook active ad campaigns, creative copy, video/image URLs, targeting reach, and spend history.

---

## ⚡ Quick Start

You can run this scraper directly via the **[Apify Store Web Console](https://apify.com/misterkhan/facebook-ads-library-scraper)** with zero setup, or integrate it into your Python / Node.js backend using the code below.

### 🐍 Python Quickstart

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
# Get your token from https://console.apify.com/account/integrations
client = ApifyClient("YOUR_APIFY_TOKEN")

# Configure input parameters
run_input = {
  "startUrls": [
    {
      "url": "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=nike"
    }
  ]
}

print("🚀 Launching Facebook Ad Library Scraper | Competitor Ad Intelligence & Creatives on Crawlomatic Engine...")
run = client.actor("misterkhan/facebook-ads-library-scraper").call(run_input=run_input)

# Fetch results from the Actor's default dataset
dataset_items = client.dataset(run["defaultDatasetId"]).list_items().items
print(f"✅ Successfully fetched {len(dataset_items)} records!")

for item in dataset_items[:3]:
    print(item)
```

---

### 🟢 Node.js / JavaScript Quickstart

```bash
npm install apify-client
```

```javascript
import { ApifyClient } from 'apify-client';

// Initialize the ApifyClient with your API token
const client = new ApifyClient({
    token: 'YOUR_APIFY_TOKEN',
});

// Configure input parameters
const input = {
  "startUrls": [
    {
      "url": "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=nike"
    }
  ]
};

console.log('🚀 Launching Facebook Ad Library Scraper | Competitor Ad Intelligence & Creatives...');
const run = await client.actor('misterkhan/facebook-ads-library-scraper').call(input);

// Fetch results
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`✅ Extracted ${items.length} records!`);
console.dir(items.slice(0, 3));
```

---

## What does Facebook Ads Library Scraper do?

It's a fast and powerful ad spy and competitive intelligence tool that allows you to **get all active and inactive ads data from the Meta / Facebook Ad Library**: ad archive ID, advertiser page name and Page ID, ad copy, headlines, CTA button text, direct HD and SD video MP4 links, high-resolution images, carousel cards, clean unwrapped destination URLs, UTM parameters, days running, scaling winner badges, and EU/UK DSA reach data. To get that data, just **enter a keyword, advertiser Page ID, or Facebook Ad Library URL and click the "Save & Start" button**.

See [more Ad Spy & Lead Enrichment Scrapers](#want-to-enrich-advertiser-domains-with-emails-tech-stacks-or-instagram-data) if you need to **extract advertiser contact emails, detect landing page tech stacks, or scrape Instagram profiles**.

> 🛡️ **Zero Proxy Configuration Required:** Anti-blocking and regional routing are **handled automatically out of the box** — just paste your target URLs and click **Start**.

## What data can you extract with Facebook Ads Library Scraper?

**📢 Ad Copy, CTAs & Advertiser Info** — Ad archive ID (`adArchiveId`), direct Ad Library URL, advertiser `pageId`, `pageName`, page profile URL, page likes, headline `title`, primary `bodyText`, link description, and CTA button type (`SIGN_UP`, `SHOP_NOW`, `LEARN_MORE`) <br>
**🎬 Direct Video MP4s, Images & Carousels** — Direct `videoHdUrl` and `videoSdUrl` MP4 links, video preview thumbnails, high-resolution `imageUrls`, and every individual card inside `CAROUSEL` and DCO (Dynamic Creative) ads <br>
**🔗 Unwrapped Landing Pages & Funnel Type** — Clean `landingPageUrl` (unwrapped from l.facebook.com redirects), `landingPageDomain`, parsed `utmParameters`, and classified `funnelType` (`shopify_ecommerce`, `click_to_whatsapp`, `lead_gen_form`, `calendly_booking`, `custom_lander`) <br>
**🏆 Ad Longevity & Transparency Metrics** — Launch date (`startDateIso`), `daysRunning`, `collationCount` (active duplicate variations), `isScalingWinner` flag, plus optional landing-page enrichment (`emails`, `phones`, `socials`, `websiteContacts`, `websiteContactsEnriched`, `technologies`, `techStack`, `techStackScanned`), publisher platforms (facebook, instagram, threads), and EU/DSA reach and spend disclosures <br>

## Why scrape the Facebook Ads Library?

💪 Spying on competitor Meta Ads and isolating profitable evergreen creatives running 14+, 30+, or 60+ consecutive days <br>
🕵️ D2C e-commerce and SaaS market research across product niches, ad copy hooks, landing page funnels, and UTM structures <br>
✨ Feeding multimodal AI agents with direct competitor video MP4s, ad copy, and landing page URLs for automated creative analysis <br>
👍 Building a custom ad spy database or creative swipe file across Facebook, Instagram, Messenger, and Threads <br>
📩 Generating B2B agency lead lists of active advertisers and enriching their landing domains with verified emails and tech stacks <br>

## How do I use Facebook Ads Library Scraper?

Facebook Ads Library Scraper was designed to be easy to start with even if you've never extracted data from the web before. Here's how you can scrape Meta and Facebook Ads data with this tool:

1. [Create](https://console.apify.com/sign-up) a free Apify account using your email.
2. Open [Facebook Ads Library Scraper](https://apify.com/misterkhan/facebook-ads-library-scraper).
3. Enter search keywords (`searchQueries`), advertiser Page IDs (`pageIds`), or Facebook Ad Library URLs (`startUrls`).
4. Click "Start" and wait for the ads data to be extracted.
5. Download your data in JSON, XML, CSV, Excel, or HTML.

## Input

The input for Facebook Ads Library Scraper can be **search keywords**, **advertiser Facebook Page IDs**, or **direct Facebook Ad Library URLs**. You can also **filter by country, active status, media format (video or `image`), and minimum days active (`minDaysRunning`)**.

Click on the [input tab](https://apify.com/misterkhan/facebook-ads-library-scraper/input-schema) for an input example in JSON.

```json
{
    "searchQueries": [
        "shopify",
        "creatine gummies"
    ],
    "country": "US",
    "activeStatus": "active",
    "mediaType": "all",
    "minDaysRunning": 14,
    "maxItems": 40
}
```

**🔍 `query`** — brand or advertiser name (e.g. `Nike`). Optional when `startUrls` is provided <br>
**🔍 `searchQueries`, `pageIds` & `startUrls`** — Search by keywords/brands (["shopify", "medspa"]), numeric advertiser Page IDs (["359717073888008"]), or direct Ad Library URLs <br>
**🌍 `country`, `activeStatus`, `mediaType` & `platforms`** — Filter by ISO country code ("US", "GB", "DE", "ALL"), delivery state ("active", "inactive", "all"), and creative format ("all", "video", "image") <br>
**🏆 `minDaysRunning`, `startDateMin` & `startDateMax`** — Only return ads that have been actively running for at least this many days (e.g., 14 or 30 to filter strictly for winning ads) <br>
**⚡ `scrapeContacts` & `scrapeTechStack`** — Optional flags (off by default) to crawl each unique advertiser landing-page domain for emails/socials or website tech stacks <br>
**🔢 `maxItems`** — Maximum number of ads to extract across your search targets (40 by default) <br>

## Output sample

This scraper will deliver results in a dataset. You can choose in which format to download it: JSON, Excel, HTML, CSV, or XML. Here's an excerpt from the JSON dataset you'd get if you apply the input parameters above:

```json
[
    {
        "id": "1576835113754964",
        "adArchiveId": "1576835113754964",
        "adLibraryUrl": "https://www.facebook.com/ads/library/?id=1576835113754964",
        "collationId": "1626456112064707",
        "collationCount": 2,
        "isActive": true,
        "daysRunning": 338,
        "isScalingWinner": true,
        "startDateIso": "2025-11-12T08:00:00Z",
        "endDateIso": "2026-10-16T07:00:00Z",
        "pageId": "359717073888008",
        "pageName": "WhatChimp",
        "pageProfileUrl": "https://www.facebook.com/whatchimp/",
        "pageProfilePictureUrl": "https://scontent.xx.fbcdn.net/v/t39.35426-6/sample_profile.jpg",
        "pageCategories": [
            "Business"
        ],
        "pageLikeCount": 13991,
        "displayFormat": "DCO",
        "publisherPlatforms": [
            "facebook",
            "instagram",
            "threads"
        ],
        "title": "0% Markup Fees on API",
        "bodyText": "Send personalized bulk broadcasts on WhatsApp using the official WhatsApp Business API.",
        "caption": "whatchimp.com",
        "linkDescription": "Get 50% OFF Early-Bird Offer",
        "ctaText": "Sign up",
        "ctaType": "SIGN_UP",
        "landingPageUrl": "https://whatchimp.com/special-offer/",
        "landingPageDomain": "whatchimp.com",
        "funnelType": "custom_lander",
        "utmParameters": {},
        "imageUrls": [
            "https://scontent.xx.fbcdn.net/v/t39.35426-6/580616304_n.jpg?oe=6AD85831"
        ],
        "videos": [
            {
                "videoHdUrl": "https://video.xx.fbcdn.net/v/t42/sample_hd.mp4?oe=6AD85831",
                "videoSdUrl": "https://video.xx.fbcdn.net/v/t42/sample_sd.mp4?oe=6AD85831",
                "videoPreviewImageUrl": "https://scontent.xx.fbcdn.net/v/t39.35426-6/thumb.jpg?oe=6AD85831"
            }
        ],
        "carouselCards": [],
        "mediaExpiresAtIso": "2026-10-21T06:14:09Z",
        "euTotalReach": null,
        "impressionsText": null,
        "spend": null,
        "currency": null,
        "byline": null,
        "totalSearchResultsCount": 11897,
        "searchCountry": "US",
        "searchQuery": "shopify",
        "scrapedAt": "2026-10-19T08:35:00Z"
    }
]
```

## How much does it cost to scrape the Facebook Ads Library?

Facebook Ads Library Scraper uses **Pay-Per-Event (PPE)** pricing with **no Actor start fee**. You only pay for the ads delivered to your dataset and any optional landing-page domain enrichments that succeed, with automatic Apify Store volume discounts up to **91% off** on higher subscription plans:

**🆓 Free Plan ($5/mo free credit)** — Base Ad: `$5.00 / 1,000 ads` ($0.0050 per ad) · Optional Domain Contacts: +$5.00 / 1K domains · Optional Domain Tech Stack: +$10.00 / 1K domains <br>
**🥉 Starter / Bronze Plan** — Base Ad: `$1.10 / 1,000 ads` ($0.0011 per ad · 78% discount) · Optional Contacts: +$1.40 / 1K · Optional Tech Stack: +$2.00 / 1K <br>
**🥈 Scale / Silver Plan** — Base Ad: `$0.75 / 1,000 ads` ($0.00075 per ad · 85% discount) · Optional Contacts: +$0.95 / 1K · Optional Tech Stack: +$1.50 / 1K <br>
**🥇 Business / Gold+ Plan** — Base Ad: `$0.45 / 1,000 ads` ($0.00045 per ad · 91% discount) · Optional Contacts: +$0.60 / 1K · Optional Tech Stack: +$1.20 / 1K <br>

Optional landing-page enrichments (`scrapeContacts` and `scrapeTechStack`) are **disabled by default** and are deduplicated per unique landing domain—so if an advertiser runs 50 ads pointing to the same domain, that domain is only enriched and charged once.

> 💡 **Predictable, All-Inclusive Pay-Per-Event Pricing:** There is a **`$0.00` run start fee** and **no separate proxy configuration required**. You only pay the flat per-result rate above for data successfully delivered to your dataset — works out of the box on both **Free** and **Paid** Apify plans.

## How many results can you scrape with Facebook Ads Library Scraper?

Facebook Ads Library Scraper can return hundreds or thousands of active and inactive ads across keywords, advertiser pages, and countries. However, you have to keep in mind that scraping facebook.com/ads/library has several variables that may cause results to vary case by case:

- the number of returned ads depends on how many active creatives match your country, media format, and `minDaysRunning` longevity filter
- searching by specific advertiser `pageIds` returns the exact portfolio of ads currently published by that Facebook Page
- Free plan runs are capped at 40 ads per run to prevent accidental credit exhaustion (paid plans have no per-run cap)

Therefore, while we continuously test Facebook Ads Library Scraper to keep extraction speed and accuracy in check, the best way to gauge ad volume for your specific niche or competitor list is to run a test yourself.

## Want to enrich advertiser domains with emails, tech stacks, or Instagram data?

You can combine Facebook Ads Library Scraper with our other marketing, social media, and B2B lead generation scrapers:

📸 **[Instagram All-in-One Scraper](https://apify.com/misterkhan/instagram-all-in-one-scraper)** — Extract Instagram profiles, posts, reels, comments, hashtags, and bio contact details without login <br>
📧 **[Website Contact & Email Scraper](https://apify.com/misterkhan/contact-enricher-scraper)** — Extract verified business emails, phone numbers, and social profiles from any advertiser domain <br>
🔍 **[Website Tech Stack Scanner](https://apify.com/misterkhan/website-tech-stack-scanner)** — Detect 7,000+ technologies (Shopify, Klaviyo, Meta Pixel, GA4, GTM) on any landing page <br>
📍 **[Google Maps Places Scraper](https://apify.com/misterkhan/google-maps-scraper)** — Scrape local business leads, phone numbers, websites, and ratings by city or category <br>

## Integrations and Facebook Ads Library Scraper

Last but not least, **Facebook Ads Library Scraper can be connected with almost any cloud service, creative analytics dashboard, or B2B workflow** thanks to [integrations on the Apify platform](https://apify.com/integrations). You can integrate with **Clay, Make, Zapier, n8n, Slack, Airbyte, Notion, Airtable, Google Sheets, Google Drive**, [and more](https://docs.apify.com/integrations).
Or you can use [webhooks](https://docs.apify.com/integrations/webhooks) to carry out an action whenever an event occurs, e.g., automatically push new competitor video ads into Slack, Notion, or Airtable whenever a scheduled spy run finishes.

## Using Facebook Ads Library Scraper with the Apify API

The Apify API gives you programmatic access to the Apify platform. The API is organized around RESTful HTTP endpoints that enable you to manage, schedule, and run Apify Actors. The API also lets you access any datasets, monitor Actor performance, fetch results, create and update versions, and connect via the **Apify MCP Server** (`https://mcp.apify.com`).

To access the API using Node.js, use the `apify-client` npm package. To access the API using Python, use the `apify-client` PyPI package.

Check out the [Apify API reference](https://docs.apify.com/api/v2) docs for full details or click on the [API tab](https://apify.com/misterkhan/facebook-ads-library-scraper/api) for ready-to-run code examples.

## Frequently asked questions about Facebook Ads Library Scraper

**🛡️ Do I need a Facebook account, cookies, or custom proxies? <br>**
**No — everything works out of the box with zero setup.** Regional routing, session management, and anti-blocking are handled automatically so you do not need to configure custom proxy settings.

**🏆 How can I filter strictly for profitable "winning" ads? <br>**
Set `minDaysRunning` to 14 or 30 (with activeStatus: "active"). Ads that advertisers keep paying to run continuously for 2–4+ weeks or scale across multiple duplicate variations (isScalingWinner: true) are strong signals of profitable creatives.

**🎬 Why does each record include `mediaExpiresAtIso` for video and image URLs? <br>**
Meta signs fbcdn.net video and image URLs with a hex expiration parameter (oe=). The scraper automatically decodes that timestamp into `mediaExpiresAtIso` so your pipeline knows the exact UTC time before which MP4 videos and images should be archived if permanent storage is needed.

## Is it legal to scrape the Facebook Ads Library?

The Meta Ad Library is a public advertising transparency database published for public inspection. Our [ad intelligence scrapers](https://apify.com/misterkhan) are ethical, **do not extract any private user data**, and only collect publicly disclosed ad records.

If you're unsure about your specific use case, you can read the Apify blog post on the [legality of web scraping](https://blog.apify.com/is-web-scraping-legal/) and [ethical scraping](https://blog.apify.com/what-is-ethical-web-scraping-and-how-do-you-do-it/).

## Your feedback

We keep this Actor under active maintenance. If a run finishes successfully but returns fewer results than you expected, hangs, or errors — please **open an Issue before posting a public review** so we can diagnose and fix it for you.

**🛠️ How to report** — Use the Actor’s [Issues tab](https://apify.com/misterkhan/facebook-ads-library-scraper/issues/open) in Apify Console. Include the run ID, your input JSON, and what you expected vs. what you got. <br>
**⏱️ Response time** — We aim to reply within 24 hours on business days. <br>
**⭐ Reviews** — Happy with the results? A short positive review helps other users find a reliable scraper. Ran into a problem? Open an Issue first — we’ll work with you to resolve it before you leave a rating. <br>


---

## 🛡️ Architecture & Engine Reliability

This scraper runs on the **[Crawlomatic Engine](https://crawlomatic.com)**:
- **Zero Proxy Configuration:** Intelligent residential and datacenter proxy rotation with automated regional ccTLD binding.
- **WAF Bypass Engine:** Autonomous challenge solving for Cloudflare Turnstile, DataDome, PerimeterX, Kasada, and Akamai.
- **Pay-Per-Event (PPE) Pricing:** Transparent pay-as-you-go pricing with \$0 starting fee.

## 📄 License

Apache License 2.0. See [LICENSE](LICENSE) for details.

Developed & Maintained by **[Crawlomatic](https://crawlomatic.com)**.
