import urllib2, simplejson
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from collective.piwik.core.interfaces import IPiwikSettings

class PiwikPagesViewlet(ViewletBase):
    render = ViewPageTemplateFile('viewlet.pt')

    def update(self):
        #self.pageviews = self.get_pageviews()
        pass

