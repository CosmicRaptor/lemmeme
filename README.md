# lemmeme
A Discord Bot which fetches memes from lemmy! Made with [discord.py](https://github.com/Rapptz/discord.py).
Add to your server from [here](https://discord.com/api/oauth2/authorize?client_id=1131868715986722837&permissions=274878220288&scope=applications.commands%20bot). 

Please try to self host the bot if you can!

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
Open an issue with the upstream you would like to add. Alternatively, edit [utils/memes_aiohttp_parser.py](utils/memes_aiohttp_parser.py) and add your own meme sources to the list with appropriate formatting.
Only lemmy communities which do not require a login to view them are supported.

## Roadmap:
- [ ] Add a simple way for server administrators to add custom meme upstreams.
- [ ] Fix posts without images appearing in the meme command.
- [ ] Improve readability of the code.
