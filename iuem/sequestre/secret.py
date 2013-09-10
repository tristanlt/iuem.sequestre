# -*- coding: utf-8 -*-
from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.namedfile.field import NamedImage
from plone.namedfile.field import NamedBlobFile
#from iuem.sequestre import _

from collective.z3cform.datetimewidget import DatetimeWidget

from AccessControl import getSecurityManager
from Products.CMFCore.utils import getToolByName

#from collective import dexteritytextindexer
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

#from zope.schema.interfaces import IVocabularyFactory

#from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

#from plone.formwidget.autocomplete import AutocompleteFieldWidget
#from z3c.formwidget.query.interfaces import IQuerySource
#from zope.schema.interfaces import IContextSourceBinder
#from zope.component import queryUtility

#from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

#import z3c.form.field


class ISecret(form.Schema):
    """Un secret a garder
    """
    
    secrettxt = schema.TextLine(
            title=(u"Secret texte"),
            description=(u"Si le secret est sous forme de texte merci de le placer ici."),
            required=False
        )
    secretfile = NamedBlobFile(
            title=(u"Secret fichier"),
            description=(u"Si le secret est sous forme de fichier merci de le placer ici."),
            required=False,
        )
    typemachine = schema.TextLine(
            title=(u"Type de machine"),
            description=(u""),
            required=False,
        )
    typesecret = schema.TextLine(
            title=(u"Type de secret"),
            description=(u""),
            required=False,
        )
    datestart = schema.Date(
            title=(u"Date de mise en service du secret"),
            required=False
        )
    datestop = schema.Int(
            title=(u"Validité"),
            description=(u"Durée de validité du secret (en mois)"),
            required=False
        )
    mailcontact = schema.TextLine(
            title=(u"Contact"),
            description=(u"Mail de la personne référente"),
            required=False
        )
    url = schema.TextLine(
            title=(u"URL liée"),
            description=(u"Vous pouvez faire pointer cette fiche vers une page web (inventaire, documentation...)"),
            required=False
        )

alsoProvides(ISecret, IFormFieldProvider)

@form.default_value(field=ISecret['mailcontact'])
def default_mail(data):
    membership = getToolByName(data.context, 'portal_membership')
    user = getSecurityManager().getUser()
    leuser=membership.getMemberById(user.getUserName())
    return leuser.getProperty('email')

class View(grok.View):
    grok.context(ISecret)
    grok.require('zope2.View')