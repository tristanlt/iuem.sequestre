# -*- coding: utf-8 -*-
from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage
from plone.namedfile.field import NamedBlobFile
#from collective.secretskeeper import _

from AccessControl import getSecurityManager
from Products.CMFCore.utils import getToolByName

#from collective import dexteritytextindexer
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

class ISecret(form.Schema):
    """Un secret a garder
    """
    #dexteritytextindexer.searchable('description')
    description = schema.Text(
            title=(u"Description"),
            description=(u"Type de secret a garder..."),
            required=False
        )
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
    datestart = schema.Datetime(
            title=(u"Date de mise en service"),
            required=False
        )
    datestop = schema.Int(
            title=(u"Validité"),
            description=(u"Durée de validité du secret (en mois)"),
            required=False
        )
    mailcontact = schema.TextLine(
            title=(u"Contact"),
            description=(u"Mail de la personne à prévenir"),
            required=False
        )
    url = schema.TextLine(
            title=(u"URL liée"),
            description=(u"Un lien vers la fiche d'une machine, d'un service..."),
            required=False
        )
    

alsoProvides(ISecret, IFormFieldProvider)

