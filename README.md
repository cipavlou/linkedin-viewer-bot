# linkedin-viewer-bot

REQUIREMENTS

Python 3.5+
Firefox
Selenium
BeautifulSoup4

DESCRIPTION

This is a simple bot that enables you to "growth hack" your LinkedIn profile. 
It works by looking at other people's profiles such that people will then look 
at yours, inflating your profile views and bumping up your profile list
ranking.

It performs the following steps:

1. Launch Firefox
2. Go to LinkedIn.com and log in
3. Bring up list of profiles from search bar
4. Visit profiles (based on how many you specialise at the beginning)

Please note that this software is proof-of-concept only - using bots on LinkedIn
is against their terms and conditions

IMPROVEMENTS TO BE MADE

1. Click on profiles on search page rather than visit them directly to appear more lifelike
2. Click on search pages 2, 3, etc, rather than enter the url to not count against LinkedIn's commercial search limit
3. Packaging as a Windows appear
4. Compatibility with Google Chrome
5. Development of a GUI
6. Better error handling

BUGS
1. Bot doesn't visit exact number of profiles equal to specified (e.g., if you want to visit 100, it'll probably visit 90-odd)


