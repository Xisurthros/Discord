# Discord Python App

### About
> This has general server control that can be easily added/modified for customization and intergration.\
> This bot is meant to run on a single server.\
> Set custom wake command.\
> Custom bot status.

### Important
> You will need to add your profiles ID to secrets.py before running the bot.
> Geting your profiles ID.
> * Open and discord server that you are in. It does not matter which server.
> * Open the users section and find your profile.
> * Rightclick your profile and at the bottom of the options you will see "Copy ID".
>
> This is to ensure **only** the owner has access to some custom bot actions and getting a DM from the bot if there are any issues with the bot.

### Requirements
> Python installed on your system.
> I will be using Python 3.10.4.\
> You will also need to create a Discord Application.
> Guide to do so will be below.

### Functions
> Current bot wake command.
> * "." without the quotes.
> * Can be changed in main at client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
>
> Main
> * [on_ready] - Custom bot status. 
> * [on_member_join] - Custom welcome message to new memebers. 
> * [on_member_remove] - Lets the sever know when and who left. 
> * [load] - Load cog extensions. 
> * [unload] - Unload cog extensions. 
>
> Admin
> * [ping] - Get bot latency.
> * [kick] - Kick specified user.
> * [un/ban] - Un/ban specified user.
> * [un/mute] - Un/mute specified user.
> * [banned_list] - Get list of all currenly banned users.
>
> Info
> * [user_info] - Get information about a specified users discord profile. (ID, Bot?, Top Role, Status, Activity, Created On, Joined On, Boosted)
> * [server_info] - Get information about your server. (ID, Owner, Region, Created at, Members, Humans, Bots, Banned Members, Statuses, Text Channels, Voice Channels, Categories, Roles, Invites)
>
> Poll
> * [poll] - Create an automated poll with up to 10 options.

### Creating a Discord Application | Getting your Discord Bot Token
> You will first need to be logged into <a href="https://discord.com/" target="_blank">Discord</a>.\
> Once logged in navigate the the <a href="https://discord.com/developers/applications" target="_blank">Application Page</a>.
>
> ![image](https://im2.ezgif.com/tmp/ezgif-2-f06fc62aa0.gif) \
> Here you will click the "New Application" button at the top right of the page.
>
> ![image](https://user-images.githubusercontent.com/76274780/183726302-42c622f2-1569-4bdd-841b-c4b476ca1ca5.png) \
> Give your bot a name and create.
>
> ![image](https://im2.ezgif.com/tmp/ezgif-2-0dc3a8de0e.gif) \
> ![image](https://user-images.githubusercontent.com/76274780/183726386-cecb1bc6-c5c3-4818-bd52-d11a06623224.png) \
> Go to the "Bot" section. Once here you will click "Add Bot" button.\
> Then an additional box will come up where you will need to click "Yes" to confirm the creation of your bot.
>
> ![image](https://user-images.githubusercontent.com/76274780/183727068-cf24d5cd-7595-464e-a436-cecc58c6c383.png) \
> Now you will need to get your bots token. \
> ![image](https://user-images.githubusercontent.com/76274780/183727113-0c594b6d-d8d1-48d0-a69a-5b7107442c58.png) \
> If you have "Reset Token" then go ahead and reset your token. And then select the "Copy" button.
>
> ![image](https://user-images.githubusercontent.com/76274780/183727924-cc596bb2-5c3c-4378-b795-04876055e1c1.png) \
> If you see "Copy" then go and click to copy.
> 
> The Token that you just copied is your bots password. It is very important that you keep this token private and do not let anyone else have access to it.
> If someone else gets access to this token they can login as your bot and cause problems to any servers that your bot is in.
>
> ![image](https://user-images.githubusercontent.com/76274780/183743145-e28e8ce2-2b92-41c3-93ca-58f612b45120.png) \
> Now that you have your bots token. Go into "secrets.py" and replace 'TOKEN' with your token. Keep the quotations.
>
> ![image](https://im4.ezgif.com/tmp/ezgif-4-b2c1cae8f1.gif)\
> While you are still on the same page where you got your token. You will find an option "REQUIRES OAUTH2 CODE GRANT" and turn this on. (This will help with Admin Permissions later on.) \
> Make sure you save any changes you make during this process.
>
> ![image](https://im.ezgif.com/tmp/ezgif-1-14ab67415f.gif) \
> ![image](https://user-images.githubusercontent.com/76274780/183733859-df865bf2-4560-45ae-8f20-7b328c581f4a.png) \
> ![image](https://user-images.githubusercontent.com/76274780/183733917-006178c4-eb9b-45ef-8641-49083cedebf1.png) \
> ![image](https://user-images.githubusercontent.com/76274780/183733939-6f7b6459-d623-46ba-b474-74930666b48f.png) 
>
> Finally you will now need to invite the bot to your server. \
> Head to OAuth2 under settings. And "URL Generator". \
> Under the "scopes" portion select "Bot". \
> Another section called "Bot Permissions" will be created below the "scopes" section.\
> Here you will add the permission you wish your bot to have. \
> Since all of my bots are create and hosted by my in my own servers I always select "Administrator". \
> **!!! Be careful giving permission to bots in your server as they can cause damanage if the wrong bot/person joins your sever !!!** \
> Finally under the "Bot Permissions" section you will find a URL. Copy this, paste it in your browser and it will invite the bot to your servers.

### Documentation
> https://discord.com/developers/docs/intro

### Future Plans
> Custom help messages for each cog extension.

### Contact
> If you have any issues/concerns/ideas feel free to shoot me a message over on Discord.\
> Username - jacohobb#2174 (Subject to change from time to time so if this doesn't work use the link below) \
> Profile URL  https://discord.com/users/198667876138221568