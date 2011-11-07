
Introduction
============

collective.piwik.pageviews is a view that displays unique visits and pageviews, using Piwik!

The Piwik open source analytics system (http://piwik.org/) is used to store and retrieve the page views.

Works with Plone 4 sites, not tested on Plone 3. Needs Piwik version 1.6 or higher. 

How to get it working
=====================

 - You need to have access to a working Piwik installation. The architecture allows API calls to be sent on the Piwik server, in case authentication is needed to view the site's stats (which is the default case on Piwik). 

To use it, you have to do the following steps:

 - In case it's not already there, add the Piwik Tracking Tag to Javascript web stats support field at <SITEURL>/@@site-controlpanel (we have to use Piwik obviously!)

 - On the eggs section of your buildout.cfg add collective.piwik.pageviews and run ./bin/buildout -vN buildout.cfg for the product to be installed

 - Log in as admin and go to the Add-ons configuration section (<SITEURL>/prefs_install_products_form) and activate collective.piwik.core. This is a package dependancy necessary for piwik.pageviews to function. 

 -  Next, go to <SITEURL>/@@piwik-settings and provide the following information:
   -  the Piwik server's url with the slash on the end (example http://piwik.unweb.me/piwik/)
   - the Site id of Piwik (example 12). A piwik installation can track multiple sites, and each one has a unique site id

   - Piwik's API key, which is a token auth key (example 5f298e9c697ec59b68d080cd9be47416), or anonymous if anonymous read access is granted. 

 - If you do the above steps, a view appears below the IBelowContentTitle displaying the number of views of a page (both unique views and pageviews). The view is loaded after the page has loaded, so your site won't slow down while quering the piwik server. 

Tweaks
======

If you want to change the behavior, edit collective/piwik/pageviews/viewlet.pt (apply styles, remove page hits or page views, etc)

If you don't see any view appearing below the Title, check that the Piwik's setting are correct (<SITEURL>/@@piwik-settings)

You might also like to try these two products: 

collective.piwik.flowplayer (http://pypi.python.org/pypi/collective.piwik.flowplayer) that displays a video play counter in Plone sites that use flowplayer,  and collective.piwik.now (http://pypi.python.org/pypi/collective.piwik.now) that displays a portlet with the number of users currently using your Plone site.

Credits
=======

Created by `unweb.me`_ and Giorgos Logiotatidis  during the Bristol 2010 Plone conference.

.. _unweb.me: https://unweb.me

Thanks to Engagemedia.org for sponsoring our tickets and registrations.


Contributors
~~~~~~~~~~~~

- Markos Gogoulos, mgogoulos at unweb.me
- Dimitris Moraitis, dimo at unweb.me
- Giorgos Logiotatidis, seadog at sealabs.net

