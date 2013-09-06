Introduction
============

Procedure de backup
-------------------
Deux clefs dans le portal_registry :
collective.secretskeeper.cryptkey
collective.secretskeeper.backupdir

Il faut un utilisateur avec les droits zope2.ViewManagementScreens

curl -u admin:admin http://localhost:8080/Plone/fullexport
