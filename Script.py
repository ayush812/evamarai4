class script(object):
    START_TXT = """π·π΄π»πΎ {},
πΌπ π½π°πΌπ΄ πΈπ <a href=https://t.me/{}>{}</a>, πΈ π²π°π½ πΏππΎππΈπ³π΄ πΌπΎππΈπ΄π, πΉπππ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ π°π½π³ π΄π½πΉπΎπ π©"""
    HELP_TXT = """π·π΄π {}
π·π΄ππ΄ πΈπ ππ·π΄ π·π΄π»πΏ π΅πΎπ πΌπ π²πΎπΌπΌπ°π½π³π."""
    ABOUT_TXT = """β― πΌπ π½π°πΌπ΄: {}
β― π²ππ΄π°ππΎπ: <a href=https://t.me/master793bot><b></b>α΄α΄α΄€α΄α΄Κπ½πΏπΉ</a>
β― π»πΈπ±ππ°ππ: πΏπππΎπΆππ°πΌ
β― π»π°π½πΆππ°πΆπ΄: πΏπππ·πΎπ½ πΉ
β― π³π°ππ° π±π°ππ΄: πΌπΎπ½πΆπΎ π³π±
β― π±ππΈπ»π³ πππ°πππ: v1.0.1 [ π±π΄ππ° ]"""
    SOURCE_TXT = """<b>NOTE:</b> 
- Source - <a href=https://github.com>Ι΄ΚΙͺ α΄α΄Ι΄Ι’α΄ Κsα΄α΄</a>
"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. TechMagazine-AutoFilterBot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- TechMagazine-AutoFilterBot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. TechMagazine-AutoFilterBot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/skmovieslinks)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specified user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """β ππΎππ°π» π΅πΈπ»π΄π: <code>{}</code>
β ππΎππ°π» πππ΄ππ: <code>{}</code>
β ππΎππ°π» π²π·π°ππ: <code>{}</code>
β πππ΄π³ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±
β π΅ππ΄π΄ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
