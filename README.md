# lemmeme
A Discord Bot which fetches memes from lemmy! Made with [discord.py](https://github.com/Rapptz/discord.py)

## Key features
- Caches memes every 15 minutes from lemmy into RAM, no disk writes involved.
- Low memory footprint, and low web queries to lemmy.
- Uses the lemmy RSS feed for fetching memes, no login required.

## Self hosting
- Get [Docker](https://www.docker.com/)
- Clone this repository.
- Set your bot's token in [token.env](/token.env)
- Run `docker-compose up -d` to build and run the bot's container.

### Adding custom meme upstreams
Open an issue with the upstream you would like to add. Alternatively, edit [cogs/memes.py](cogs/memes.py) and add your own meme sources to the list.
Only lemmy communities which do not require a login to view them are supported.
