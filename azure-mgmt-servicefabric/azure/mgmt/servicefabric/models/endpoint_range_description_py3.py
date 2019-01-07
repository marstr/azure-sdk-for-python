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


class EndpointRangeDescription(Model):
    """Port range details.

    All required parameters must be populated in order to send to Azure.

    :param start_port: Required. Starting port of a range of ports
    :type start_port: int
    :param end_port: Required. End port of a range of ports
    :type end_port: int
    """

    _validation = {
        'start_port': {'required': True},
        'end_port': {'required': True},
    }

    _attribute_map = {
        'start_port': {'key': 'startPort', 'type': 'int'},
        'end_port': {'key': 'endPort', 'type': 'int'},
    }

    def __init__(self, *, start_port: int, end_port: int, **kwargs) -> None:
        super(EndpointRangeDescription, self).__init__(**kwargs)
        self.start_port = start_port
        self.end_port = end_port
