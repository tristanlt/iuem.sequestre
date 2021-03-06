# -*- coding: utf-8 -*-
from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage
from plone.namedfile.field import NamedBlobFile
#from iuem.sequestre import _

from AccessControl import getSecurityManager
from Products.CMFCore.utils import getToolByName

#from collective import dexteritytextindexer
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

class IVault(form.Schema):
    """Un coffre
    """
    mailcontact = schema.TextLine(
            title=(u"Contact"),
            description=(u"Mail de la personne référente"),
            required=False
        )
    affichesouscoffre = schema.Bool(
            title=(u"Afficher la liste des sous-coffres"),
            description=(u"Afficher la liste des sous-coffre dans la page de présentation du coffre."),
            required=True,
            default= False 
        )

alsoProvides(IVault, IFormFieldProvider)

@form.default_value(field=IVault['mailcontact'])
def default_mail(data):
    membership = getToolByName(data.context, 'portal_membership')
    user = getSecurityManager().getUser()
    leuser=membership.getMemberById(user.getUserName())
    return leuser.getProperty('email')

class View(grok.View):
    grok.context(IVault)
    grok.require('zope2.View')