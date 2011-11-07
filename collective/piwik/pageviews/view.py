from Products.Five.browser  import BrowserView
import urllib2, simplejson
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from collective.piwik.core.interfaces import IPiwikSettings

class PageViews(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        self.request.response.setHeader('Content-Type', 'application/json')
        result = self.getPageViews()
        return simplejson.dumps(result)

    def getPageViews(self):
        """ Return the number of views and unique visits from Piwik 
        """
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IPiwikSettings)

        self.hits = 0
        self.unique = 0
        
        self.page_url = self.context.absolute_url()

        url = settings.piwik_server +'?module=API&method=Actions.getPageUrl&idSite=' + settings.piwik_siteid + '&period=year&date=last100&format=json&token_auth=' + settings.piwik_key + '&pageUrl=' + self.page_url

        try: 
            piwik_data = simplejson.load(urllib2.urlopen(url))
        except Exception, e: # might be a URLError, timeout etc
            piwik_data = {}

        if piwik_data.get('result') == 'error':
            piwik_data = {} # error on the communication.maybe wrong token?

        for year in piwik_data:
            if piwik_data[year]:
                self.hits += int(piwik_data[year][0]['nb_hits'])
                self.unique += int(piwik_data[year][0]['nb_visits'])

        return(self.hits, self.unique)
