# Mastodon hourly animal bot (with alt text!)

This Github repo contains the very simple code used by the <a rel="me" href="https://oomfie.city/@hourlycapy">@hourlycapy​@oomfie.city</a> Mastodon bot, it is *somewhat* modular as it can be easily edited to send any images that can be accessed through TinyFox's APIs. This should also be pretty easy code as I am still a beginner with Python, so even if you're a beginner this should still be easy to understand (even if it's very messy!).

Check out a running example of this code at <a href="https://oomfie.city/@hourlycapy">@hourlycapy​@oomfie.city</a>.

# Dependencies

This script relies on the following Python packages :<br>
<a href="https://pypi.org/project/requests/">requests</a><br>
<a href="https://pypi.org/project/shutils/">shutils</a><br>
<a href="https://pypi.org/project/Mastodon.py/">Mastodon.py</a><br>
<br>You can install all of these at once by copy pasting `pip3 install requests mastodon.py` in your favourite commmand prompt. Although a requirements.txt file is also provided and can be used with `pip install -r requirements.txt`.

# Setup

Setup is pretty easy, this guide assumes you already have your Mastodon bot account and access token in place, **and a web-server that can be publicly accessed** *if you want to use the automated alt-text tool*.
<br> If you haven't, make an account on any bot-friendly server, and make an app in your account's setting (which can be found at https://instance.example/settings/applications). As for the web-server part, there are a lot of guides, but there is an alt-text-less version of the script if you do not want to bother.
> **Warning**<br>
> The access token will change whenever you log-in to your bot's account, make sure to change it back in your script's file if you do.

Once you are ready, download the `capybot.py` (or capybot_no_alt_text.py) script :
* For the no alt-text variant : simply replace the Mastodon access token that is located at lines 60, and set another image API (located at line 9) if you want something else than capybaras. And voilà!
* For the automated alt-text variant : replace your web server's URL at line 35 and 48, then, replace the Mastodon access token that is located at lines 60, and set another image API (located at line 9) if you want something else than capybaras. You should be ready to go!
   * | :point_up:    | Depending on the server, you might need to add an absolute path to the file at lines 21 and 66. |
     |---------------|:------------------------|
   * In case of file permission problems on Linux, the best way would be to have your file in a `/home/` folder (for example, `/home/luttyz`), and use the `ln -s` command as sudo
   * Example : `sudo ln -s /home/luttyz/capybara.jpg /var/www/my_webapp__7/capybara.jpg` <-- especially useful for YunoHost users

<br> If you want to run this bot hourly, the easiest way would be to use a `cron` task on a Linux machine, simple type `crontab -e` in your favourite command prompt and copy paste `4 * * * *  python3 /location/of/the/script/capybot.py`, from now on the script will run every hour.<br>
(Note : there is a slight delay in the example as to avoid hitting your bot's, TinyFox's, and the alt-text API's servers all at the same time, which can be a PITA for server maintainers when at scale)

# Acknowledgements

**In case of questions : contact <a href="https://oomfie.city/@luttyz">@luttyz​@oomfie.city</a> or <a href="https://matrix.to/#/@luttyz:birdchat.ml">@luttyz:birdchat.ml</a>** 

Thanks to that one school friend who is obsessed with capybaras, TinyFox for the awesome API, Vercel for the free and publicly accessible instance of CLIP-2, and Microsoft for making Bing AI free lol.
<br> This script is licensed under the WTFPL, just do whatever the fuck you want with it. :blobfoxhappy:
