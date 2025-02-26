import discord
from discord.ext import commands
import requests
import logging

BOT_CREATOR = "bed0c"
BOT_PURPOSE = "https://github.com/bed0c"
DISCORD_TOKEN = "DISCORD_TOKEN"
ROBLOX_COOKIE = "ROBLOX_COOKIE"
CLIENT_ID = "BOT_CLIENT_ID"
GUILD_ID = "SERVER_ID"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)
tree = bot.tree 

def check_inventory(user_id, asset_id):
    """Checks if a user owns a specific item in their inventory."""
    headers = {
        "Cookie": f".ROBLOSECURITY={ROBLOX_COOKIE}",
        "User-Agent": "Mozilla/5.0",
        "Accept-Charset": "utf-8"
    }
    url = f"https://inventory.roblox.com/v1/users/{user_id}/items/Asset/{asset_id}"
    
    try:
        logger.info(f"Checking inventory for User ID: {user_id}, Asset ID: {asset_id}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return len(data.get("data", [])) > 0
    except requests.exceptions.RequestException as e:
        logger.error(f"API error: {e}")
        return None

@bot.event
async def on_ready():
    await tree.sync()
    logger.info(f"✅ Bot '{bot.user}' is now online! Developer: {BOT_CREATOR} | Server: {BOT_PURPOSE}")

@tree.command(name="check", description="Check if a Roblox user owns a specific item.")
async def check(interaction: discord.Interaction, user_id: int, asset_id: int):
    """Slash command: Checks if a user owns a specific item."""
    result = check_inventory(user_id, asset_id)
    
    embed = discord.Embed(title="📦 Roblox Inventory Check", color=0xffcc00)
    if result is None:
        embed.description = "⚠️ API error! Please try again later."
    elif result:
        embed.color = 0x00ff00
        embed.description = f"✅ **User {user_id} owns the item {asset_id}!**"
    else:
        embed.color = 0xff0000
        embed.description = f"❌ **User {user_id} does not own the item {asset_id}!**"
    
    embed.set_footer(text=f"Developer: {BOT_CREATOR} | Server: {BOT_PURPOSE}")
    await interaction.response.send_message(embed=embed)

if __name__ == "__main__":
    try:
        bot.run(DISCORD_TOKEN)
    except Exception as e:
        logger.error(f"Error while running bot: {e}")
