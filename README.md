# Metricool MCP Server

This is a Model Context Protocol (MCP) server for interacting with the Metricool API. It allows AI agents to access and analyze social media metrics, campaign data and schedule posts to your Metricool account.

## Setup

### Prerequisites
MCP is still very new and evolving, we recommend following the [MCP documentation](https://modelcontextprotocol.io/quickstart#prerequisites) to get the MCP basics up and running.

- Python 3.8 or higher
- [A Metricool account with API access (Advanced Tier)](https://metricool.com)
- [Claude Desktop](https://claude.ai/) (or Cursor, or any MCP Client)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [git](https://git-scm.com/downloads/)

### Configuration
1. Configure Claude Desktop
Create the following file depending on your OS:

On MacOS: ~/Library/Application Support/Claude/claude_desktop_config.json

On Windows: %APPDATA%/Claude/claude_desktop_config.json

Paste this template in the file and replace <METRICOOL_USER_TOKEN> and <METRICOOL_USER_ID> with your Metricool API and ID information:

```json
{
    "mcpServers": {
        "mcp-metricool": {
            "command": "uvx",
            "args": [
                "--upgrade",
                "mcp-metricool"
            ],
            "env": {
                "METRICOOL_USER_TOKEN": "<METRICOOL_USER_TOKEN>",
                "METRICOOL_USER_ID": "<METRICOOL_USER_ID>"
            }
        }
    }
}
```

## Tools
The server implements 28 tools to interact with the Metricool API:

### Brand Management
1. `get_brands()`
   - Get simplified list of brands from your Metricool account. Used as auxiliary data for other tools.

2. `get_brands_complete()`
   - Get complete brand information including all available details for each brand.

### Content Analytics

3. `get_instagram_reels(init_date: str, end_date: str, blog_id: int)`
   - Get Instagram Reels analytics from your Metricool account.

4. `get_instagram_posts(init_date: str, end_date: str, blog_id: int)`
   - Get Instagram Posts analytics from your Metricool account.

5. `get_instagram_stories(init_date: str, end_date: str, blog_id: int)`
   - Get Instagram Stories analytics from your Metricool account.

6. `get_tiktok_videos(init_date: str, end_date: str, blog_id: int)`
   - Get TikTok Videos analytics from your Metricool account.

7. `get_facebook_reels(init_date: str, end_date: str, blog_id: int)`
   - Get Facebook Reels analytics from your Metricool account.

8. `get_facebook_posts(init_date: str, end_date: str, blog_id: int)`
   - Get Facebook Posts analytics from your Metricool brand account.

9. `get_facebook_stories(init_date: str, end_date: str, blog_id: int)`
   - Get Facebook Stories analytics from your Metricool brand account.

10. `get_thread_posts(init_date: str, end_date: str, blog_id: int)`
    - Get Threads Posts analytics from your Metricool brand account.

11. `get_x_posts(init_date: str, end_date: str, blog_id: int)`
    - Get X (Twitter) Posts analytics from your Metricool account.

12. `get_bluesky_posts(init_date: str, end_date: str, blog_id: int)`
    - Get Bluesky Posts analytics from your Metricool brand account.

13. `get_linkedin_posts(init_date: str, end_date: str, blog_id: int)`
    - Get LinkedIn Posts analytics from your Metricool brand account.

14. `get_pinterest_pins(init_date: str, end_date: str, blog_id: int)`
    - Get Pinterest Pins analytics from your Metricool brand account.

15. `get_youtube_videos(init_date: str, end_date: str, blog_id: int)`
    - Get YouTube Videos analytics from your Metricool brand account.

16. `get_twitch_videos(init_date: str, end_date: str, blog_id: int)`
    - Get Twitch Videos analytics from your Metricool account.

### Ads Campaigns

17. `get_facebookads_campaigns(init_date: str, end_date: str, blog_id: int)`
    - Get Facebook Ads Campaigns from your Metricool account.

18. `get_googleads_campaigns(init_date: str, end_date: str, blog_id: int)`
    - Get Google Ads Campaigns from your Metricool account.

19. `get_tiktokads_campaigns(init_date: str, end_date: str, blog_id: int)`
    - Get TikTok Ads Campaigns from your Metricool brand account.

### Competitor Analysis

20. `get_network_competitors(network: str, init_date: str, end_date: str, blog_id: int, limit: int, timezone: str)`
    - Get competitor analytics from your Metricool brand account.
    - Supported networks: Instagram, Facebook, X, Bluesky, YouTube, Twitch.

21. `get_network_competitors_posts(network: str, init_date: str, end_date: str, blog_id: int, limit: int, timezone: str)`
    - Get and analyze competitor posts from your Metricool brand account.
    - Supported networks: Instagram, Facebook, X, Bluesky, YouTube, Twitch.

### Scheduling

22. `post_schedule_post(date: str, blog_id: int, info: json)`
    - Schedule a post (or multipost) to your brands in Metricool.

23. `get_scheduled_posts(blog_id: int, start: str, end: str, timezone: str, extendedRange: bool)`
    - Get scheduled posts from your Metricool brand account.

24. `get_best_time_to_post(start: str, end: str, blog_id: int, provider: str, timezone: str)`
    - Get the best time to post for a specific social network. Returns days and hours with engagement values.

25. `update_schedule_post(id: str, date: str, blog_id: int, info: dict)`
    - Update a scheduled post from a previous conversation or existing schedule.

### Analytics & Metrics

26. `get_metrics(network: str)`
    - Get available metrics for analysis from a specific social network.

27. `get_analytics(blog_id: int, start: str, end: str, timezone: str, network: str, metric: list[str])`
    - Get analytics data from a specific social network for your Metricool brand account.

### Pinterest

28. `get_pinterest_boards(blog_id: int)`
    - Get Pinterest Boards from a specific Metricool brand account.
