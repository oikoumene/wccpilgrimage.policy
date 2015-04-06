from collective.grok import gs
from wccpilgrimage.policy import MessageFactory as _

@gs.importstep(
    name=u'wccpilgrimage.policy', 
    title=_('wccpilgrimage.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wccpilgrimage.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
