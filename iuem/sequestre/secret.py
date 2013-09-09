# -*- coding: utf-8 -*-
from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage
from plone.namedfile.field import NamedBlobFile
#from iuem.sequestre import _

from collective.z3cform.datetimewidget import DatetimeWidget

from AccessControl import getSecurityManager
from Products.CMFCore.utils import getToolByName

#from collective import dexteritytextindexer
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.schema.interfaces import IVocabularyFactory

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.component import queryUtility


class GetTypeMachineVoc(object):
    grok.implements(IVocabularyFactory)
    
    def __call__(self, context):
        vtool = getToolByName(context, 'portal_vocabularies')
        vocab=vtool.getVocabularyByName('typemachine')
        terms=[]
        for vocabkey in vocab.getVocabularyDict().iterkeys():
            terms.append(SimpleVocabulary.createTerm(vocabkey,vocab.getVocabularyDict()[vocabkey]))
        return SimpleVocabulary(terms)

grok.global_utility(GetTypeMachineVoc, name=u"iuem.sequestre.typemachinevoc")

class GetTypeSecretVoc(object):
    grok.implements(IVocabularyFactory)
    
    def __call__(self, context):
        vtool = getToolByName(context, 'portal_vocabularies')
        vocab=vtool.getVocabularyByName('typesecret')
        terms=[]
        for vocabkey in vocab.getVocabularyDict().iterkeys():
            terms.append(SimpleVocabulary.createTerm(vocabkey,vocab.getVocabularyDict()[vocabkey]))
        return SimpleVocabulary(terms)

grok.global_utility(GetTypeSecretVoc, name=u"iuem.sequestre.typesecretvoc")


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
    typemachine = schema.Choice(
            title=(u"Type de machine"),
            description=(u""),
            required=False,
            vocabulary='iuem.sequestre.typemachinevoc'
        )
    typesecret = schema.Choice(
            title=(u"Type de secret"),
            description=(u""),
            required=False,
            vocabulary='iuem.sequestre.typesecretvoc'
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