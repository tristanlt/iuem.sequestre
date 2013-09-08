Introduction
============

Procedure de backup
-------------------
Deux clefs dans le portal_registry :
iuem.sequestre.cryptkey
iuem.sequestre.backupdir

Il faut un utilisateur avec les droits zope2.ViewManagementScreens

curl -u admin:admin http://localhost:8080/Plone/fullexport
