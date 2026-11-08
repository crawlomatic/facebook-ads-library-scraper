"""
Facebook Ad Library Scraper | Competitor Ad Intelligence & Creatives
Official Python client example powered by Crawlomatic Engine on Apify
"""
import os
import sys
from apify_client import ApifyClient

APIFY_TOKEN = os.environ.get("APIFY_TOKEN", "YOUR_APIFY_TOKEN")

def main():
    if APIFY_TOKEN == "YOUR_APIFY_TOKEN":
        print("⚠️ Please set your APIFY_TOKEN environment variable or pass your token to ApifyClient.")
        print("Get your token at: https://console.apify.com/account/integrations")
        sys.exit(1)

    client = ApifyClient(APIFY_TOKEN)

    run_input = {
  "startUrls": [
    {
      "url": "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=nike"
    }
  ]
}

    print("🚀 Calling misterkhan/facebook-ads-library-scraper...")
    run = client.actor("misterkhan/facebook-ads-library-scraper").call(run_input=run_input)

    dataset_items = client.dataset(run["defaultDatasetId"]).list_items().items
    print(f"✅ Extraction completed! Total items: {len(dataset_items)}")

    for idx, item in enumerate(dataset_items[:5], 1):
        print(f"\n--- Record {idx} ---")
        print(item)

if __name__ == "__main__":
    main()
