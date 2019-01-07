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


class ContainerServiceOrchestratorProfile(Model):
    """Profile for the container service orchestrator.

    All required parameters must be populated in order to send to Azure.

    :param orchestrator_type: Required. The orchestrator to use to manage
     container service cluster resources. Valid values are Kubernetes, Swarm,
     DCOS, DockerCE and Custom. Possible values include: 'Kubernetes', 'Swarm',
     'DCOS', 'DockerCE', 'Custom'
    :type orchestrator_type: str or
     ~azure.mgmt.containerservice.v2017_07_01.models.ContainerServiceOrchestratorTypes
    :param orchestrator_version: The version of the orchestrator to use. You
     can specify the major.minor.patch part of the actual version.For example,
     you can specify version as "1.6.11".
    :type orchestrator_version: str
    """

    _validation = {
        'orchestrator_type': {'required': True},
    }

    _attribute_map = {
        'orchestrator_type': {'key': 'orchestratorType', 'type': 'str'},
        'orchestrator_version': {'key': 'orchestratorVersion', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ContainerServiceOrchestratorProfile, self).__init__(**kwargs)
        self.orchestrator_type = kwargs.get('orchestrator_type', None)
        self.orchestrator_version = kwargs.get('orchestrator_version', None)
