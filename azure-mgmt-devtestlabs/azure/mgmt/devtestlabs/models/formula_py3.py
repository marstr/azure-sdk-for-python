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


class Formula(Model):
    """A formula.

    :param description: The description of the formula.
    :type description: str
    :param author: The author of the formula.
    :type author: str
    :param os_type: The OS type of the formula.
    :type os_type: str
    :param creation_date: The creation date of the formula.
    :type creation_date: datetime
    :param formula_content: The content of the formula.
    :type formula_content: ~azure.mgmt.devtestlabs.models.LabVirtualMachine
    :param vm: Information about a VM from which a formula is to be created.
    :type vm: ~azure.mgmt.devtestlabs.models.FormulaPropertiesFromVm
    :param provisioning_state: The provisioning status of the resource.
    :type provisioning_state: str
    :param id: The identifier of the resource.
    :type id: str
    :param name: The name of the resource.
    :type name: str
    :param type: The type of the resource.
    :type type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'description': {'key': 'properties.description', 'type': 'str'},
        'author': {'key': 'properties.author', 'type': 'str'},
        'os_type': {'key': 'properties.osType', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
        'formula_content': {'key': 'properties.formulaContent', 'type': 'LabVirtualMachine'},
        'vm': {'key': 'properties.vm', 'type': 'FormulaPropertiesFromVm'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, description: str=None, author: str=None, os_type: str=None, creation_date=None, formula_content=None, vm=None, provisioning_state: str=None, id: str=None, name: str=None, type: str=None, location: str=None, tags=None, **kwargs) -> None:
        super(Formula, self).__init__(**kwargs)
        self.description = description
        self.author = author
        self.os_type = os_type
        self.creation_date = creation_date
        self.formula_content = formula_content
        self.vm = vm
        self.provisioning_state = provisioning_state
        self.id = id
        self.name = name
        self.type = type
        self.location = location
        self.tags = tags
