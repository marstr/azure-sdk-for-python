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


class PerfMonSample(Model):
    """Performance monitor sample in a set.

    :param time: Point in time for which counter was measured.
    :type time: datetime
    :param instance_name: Name of the server on which the measurement is made.
    :type instance_name: str
    :param value: Value of counter at a certain time.
    :type value: float
    """

    _attribute_map = {
        'time': {'key': 'time', 'type': 'iso-8601'},
        'instance_name': {'key': 'instanceName', 'type': 'str'},
        'value': {'key': 'value', 'type': 'float'},
    }

    def __init__(self, *, time=None, instance_name: str=None, value: float=None, **kwargs) -> None:
        super(PerfMonSample, self).__init__(**kwargs)
        self.time = time
        self.instance_name = instance_name
        self.value = value
