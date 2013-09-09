""" Viewlets related to application logic.
"""

# Zope imports
from Products.CMFCore.interfaces import ISiteRoot
from zope.interface import Interface
from five import grok
import os, errno
import pickle
from iuem.sequestre.toolcryptdecrypt import encrypt_file
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

# Search for templates in the 'templates' directory
grok.templatedir('templates')

class FullExport(grok.View):
    """ Each Secrets Pickle stored and crypted 
    """
    grok.context(ISiteRoot)
    grok.require('zope2.ViewManagementScreens')
    def update(self, term=None):
        registry = getUtility(IRegistry)
        key = registry['iuem.sequestre.cryptkey']
        backup_path = registry['iuem.sequestre.backupdir']
        mkdir_p(backup_path)
        
        results = self.context.portal_catalog.searchResults(Type = "Vault")
        for vaultBrain in results:
            mkdir_p(backup_path+vaultBrain.getPath())

            resultsSecret = self.context.portal_catalog.searchResults(path={'query':vaultBrain.getPath(),'depth':1}, Type = "Secret")
            for secretBrain in resultsSecret:
                secret=secretBrain.getObject()
                secretDict={}
                secretDict['id']=secret.id
                secretDict['description']=secret.description
                secretDict['secrettxt']=secret.secrettxt
                secretDict['typemachine']=secret.typemachine
                secretDict['typesecret']=secret.typesecret
                secretDict['datestart']=secret.datestart
                secretDict['datestop']=secret.datestop
                secretDict['mailcontact']=secret.mailcontact
                secretDict['url']=secret.url
                #print(backup_path+vaultBrain.getPath()+secret.id)
                #import pdb; pdb.set_trace()
                
                output = open(backup_path+'/'+vaultBrain.getPath()+'/'+secret.id, 'wb')
                pickle.dump(secretDict, output)
                output.close()
                encrypt_file("AAAABCCCCDDDD",backup_path+'/'+vaultBrain.getPath()+'/'+secret.id,backup_path+'/'+vaultBrain.getPath()+'/'+secret.id+'.enc')
                os.remove(backup_path+'/'+vaultBrain.getPath()+'/'+secret.id)
                #print(secretBrain.getId,secretBrain.getPath())
                #import pdb; pdb.set_trace()

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise



#     def update(self, term=None):
#         vtool = getToolByName(context, 'portal_vocabularies')
#         voctypemachine=vtool.getVocabularyByName('typemachine')
#         voctypesecret=vtool.getVocabularyByName('typesecret')