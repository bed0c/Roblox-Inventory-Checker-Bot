# 🔍 Roblox Inventory Checker Bot

<p align="center">
    <i>A powerful and efficient Discord bot that allows users to verify whether a Roblox user owns a specific item.</i>  
    <br>Built with <b>Python</b>, <b>Discord.py</b>, and <b>Roblox's Inventory API</b>.
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+">
    <img src="https://img.shields.io/badge/Discord.py-2.3.2-blue.svg" alt="Discord.py 2.3.2">
    <img src="https://img.shields.io/badge/Status-Online-brightgreen.svg" alt="Status">
    <img src="https://img.shields.io/github/license/bed0c/Roblox-Inventory-Checker-Bot.svg" alt="License">
</p>

---

## 📌 About This Project
Roblox Inventory Checker Bot is a **feature-rich Discord bot** that enables users to check whether a **Roblox user owns a specific item**.  
It is built using **Python** and **Discord.py** and seamlessly integrates with **Roblox's Inventory API**, providing a smooth and **modern embed-based** response system.

### ⚡ Key Features
✔️ **Check Roblox inventory** – Verify item ownership instantly.  
🎨 **Modern embed responses** – Aesthetic, structured, and easy to read.  
📡 **Advanced logging** – Tracks bot activity and API errors in real-time.  
🚀 **Discord Slash Commands** – Uses the latest `/check` command system.  

---

## 🛠️ Installation & Setup

### 📥 1. Clone the Repository
~~~sh
git clone https://github.com/bed0c/Roblox-Inventory-Checker-Bot.git
cd Roblox-Inventory-Checker-Bot
~~~

### 📦 2. Install Dependencies
~~~sh
pip install -r requirements.txt
~~~

### ⚙️ 3. Configure the Bot
Update the following environment variables in the script:

- `DISCORD_TOKEN` → Your Discord bot token
- `ROBLOX_COOKIE` → Your .ROBLOSECURITY cookie for API access
- `CLIENT_ID` → Your bot's client ID
- `GUILD_ID` → The Discord server ID where commands should sync

> **⚠️ Security Warning:** Never share your **.ROBLOSECURITY** cookie, as it grants full access to your Roblox account.

### 🚀 4. Run the Bot
~~~sh
python bot.py
~~~

---

## 🎮 Usage
Once the bot is running, use the following command in Discord:
~~~sh
/check user_id: <RobloxUserID> asset_id: <AssetID>
~~~

**Example:**
~~~sh
/check user_id: 12345678 asset_id: 987654321
~~~

## 📜 Example Output
If the user **owns** the item:  
✅ **User 12345678 owns the item 987654321!**

If the user **does not own** the item:  
❌ **User 12345678 does not own the item 987654321!**

If there's an **API error**:  
⚠️ **API error! Please try again later.**

---

## 🤝 Contributing
Contributions are highly appreciated!  
If you want to improve this project, feel free to fork the repository, open an issue, or submit a pull request.

---

## 📜 License
This project is licensed under the **MIT License**.  
See the full license [here](https://github.com/bed0c/Roblox-Inventory-Checker-Bot/blob/main/LICENSE).

## 👤 Developer
Created by: [bed0c](https://github.com/bed0c) 🚀

<p align="center">
    <i>Made with ❤️ by <b>bed0c</b></i>
</p>
