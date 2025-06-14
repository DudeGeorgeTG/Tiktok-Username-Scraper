# TikTok Username Scraper

This Python script automatically scrapes TikTok usernames by generating random search keywords in various alphabets and sending requests to TikTok’s public search API. It filters results based on a minimum follower count and saves valid usernames to a text file.

## 📌 Features

- Generates random keywords in multiple alphabets to mimic diverse searches.
- Uses dynamic headers and cookies to emulate legitimate requests.
- Filters usernames by a configurable minimum follower count.
- Prints results to the console and saves them to `scraped.txt`.
- Includes a loop limit (`max_iterations`) for safe testing.

## ⚙️ Configuration

- **Minimum Followers:**  
  Set the `min_followers` variable in the script to filter users by follower count. Default: `1000`.

- **Max Iterations:**  
  Use `max_iterations` to limit how many times the scraper loops while testing. Default: `10`.

## 🚀 How to Use

1. **Install dependencies:**
   ```bash
   pip install requests
