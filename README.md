
# Reddit Joke Bot 🃏

Introducing the **Reddit Joke Bot** — a delightful Python-based bot designed to spread laughter on Reddit. Whenever a comment in the 'ChuckNorrisJokes' subreddit contains the word "Chuck," our bot promptly responds with a random Chuck Norris joke sourced from ICNDb.com.

## 🚀 Features

- **Keyword Detection**: Actively monitors comments for the presence of the keyword "Chuck."
- **Automated Replies**: Generates a spontaneous reply with a Chuck Norris joke.
- **Continuous Operation**: Runs in a loop, checking for new comments every 5 minutes.
- **Avoids Duplication**: Maintains a record of comments replied to, ensuring no comment receives the same joke twice.
- **Easy Configuration**: Separate configuration file (`config.py`) for managing credentials and settings.

## 📁 File Structure

- 📄 `reddit_bot.py`: The nerve center of the bot, encompassing the logic for interfacing with Reddit, detecting keywords, fetching jokes, and replying to comments.
- 📄 `config.py`: A configuration file containing necessary credentials for the Reddit API.
- 📜 `comments_replied_to.txt`: A text file storing the IDs of comments the bot has already responded to.

## 🔧 Setup & Execution

1. Set up your Reddit API credentials and update the `config.py` file accordingly.
2. Install the required Python libraries:
   ```bash
   pip install praw requests
   ```
3. Launch the bot:
   ```bash
   python reddit_bot.py
   ```

## 🧠 Technical Insights

- **Reddit Interface**: The bot utilizes the `praw` library to seamlessly interface with Reddit and manage actions such as login and comment replies.
- **Joke Source**: Jokes are dynamically fetched from [ICNDb.com](http://api.icndb.com) using the `requests` library.
- **Continuous Monitoring**: The bot operates in a loop, periodically scanning for new comments and delivering jokes.

## 🧪 Testing

1. Execute the bot using the steps mentioned above.
2. Post a comment containing the word "Chuck" in the 'ChuckNorrisJokes' subreddit.
3. Await the bot's joke-filled reply.
4. Verify that the bot's response aligns with the functionality described.
