# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeletedVault(Model):
    """Deleted vault information with extended details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource ID for the deleted key vault.
    :vartype id: str
    :ivar name: The name of the key vault.
    :vartype name: str
    :ivar type: The resource type of the key vault.
    :vartype type: str
    :param properties: Properties of the vault
    :type properties:
     ~azure.mgmt.keyvault.v2016_10_01.models.DeletedVaultProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'DeletedVaultProperties'},
    }

    def __init__(self, **kwargs):
        super(DeletedVault, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.properties = kwargs.get('properties', None)
