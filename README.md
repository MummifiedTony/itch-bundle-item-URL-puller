# itch-bundle-item-URL-puller
Pulls the URLs from all the items in any of the bundles bought on Itch.io

I made this because I’ve bought 8 bundles and want to start building a new way of sorting what I own on Itch.io. Since their library management system doesn’t do enough for my needs. I'm super new to coding so I used a lot of help from Chat GPT and this is the end result. Any questions feel free to ask.

The URLs that are already in the code are what I already own. Delete or add anything for your needs. Make sure to use the public page URLs. You can find these on your account https://itch.io/my-purchases/bundles > open each bundle in a new tab > Click the link to the right of “thank you for purchasing ...” and paste it into the code.

To help GPT get over the issue of not properly opening a headless Chrome page and auto-scrolling. I fed it working code from https://medium.com/analytics-vidhya/using-python-and-selenium-to-scrape-infinite-scroll-web-pages-825d12c24ec7 so that it knew how and what to integrate it into “my” code. Want to give proper credit to the people whose shoulders I'm standing on.

This code also eliminates duplicate URLs in the set. Since some items might be in two different bundles.

And then after everything is added to the set, the code prints a .txt doc with whatever name you want. Currently its “unique_item_links.txt” goes without saying you could change this to anything.

The end result being a super long list of all the items in any number of bundles that you want. For what I'm looking to do, it would be so slow that every time I wanted to test my next project’s code it would need to open a page and scroll to the bottom. Since the items in the bundle are static and don't change. I can use a txt file full of URLs to go straight to the items store pages and then continue from there.

Again i'm super new to coding. I love learning more about this stuff and if anything is wrong or needs to be fixed feel free to let me know @mummifiedtony on twitter
