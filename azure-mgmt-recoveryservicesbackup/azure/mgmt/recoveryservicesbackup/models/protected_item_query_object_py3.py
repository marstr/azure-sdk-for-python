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


class ProtectedItemQueryObject(Model):
    """Filters to list backup items.

    :param health_state: Health State for the backed up item. Possible values
     include: 'Passed', 'ActionRequired', 'ActionSuggested', 'Invalid'
    :type health_state: str or
     ~azure.mgmt.recoveryservicesbackup.models.HealthState
    :param backup_management_type: Backup management type for the backed up
     item. Possible values include: 'Invalid', 'AzureIaasVM', 'MAB', 'DPM',
     'AzureBackupServer', 'AzureSql', 'AzureStorage', 'AzureWorkload',
     'DefaultBackup'
    :type backup_management_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.BackupManagementType
    :param item_type: Type of workload this item represents. Possible values
     include: 'Invalid', 'VM', 'FileFolder', 'AzureSqlDb', 'SQLDB', 'Exchange',
     'Sharepoint', 'VMwareVM', 'SystemState', 'Client', 'GenericDataSource',
     'SQLDataBase', 'AzureFileShare', 'SAPHanaDatabase'
    :type item_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.DataSourceType
    :param policy_name: Backup policy name associated with the backup item.
    :type policy_name: str
    :param container_name: Name of the container.
    :type container_name: str
    :param backup_engine_name: Backup Engine name
    :type backup_engine_name: str
    :param friendly_name: Friendly name of protected item
    :type friendly_name: str
    :param fabric_name: Name of the fabric.
    :type fabric_name: str
    :param backup_set_name: Name of the backup set.
    :type backup_set_name: str
    """

    _attribute_map = {
        'health_state': {'key': 'healthState', 'type': 'str'},
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'item_type': {'key': 'itemType', 'type': 'str'},
        'policy_name': {'key': 'policyName', 'type': 'str'},
        'container_name': {'key': 'containerName', 'type': 'str'},
        'backup_engine_name': {'key': 'backupEngineName', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'fabric_name': {'key': 'fabricName', 'type': 'str'},
        'backup_set_name': {'key': 'backupSetName', 'type': 'str'},
    }

    def __init__(self, *, health_state=None, backup_management_type=None, item_type=None, policy_name: str=None, container_name: str=None, backup_engine_name: str=None, friendly_name: str=None, fabric_name: str=None, backup_set_name: str=None, **kwargs) -> None:
        super(ProtectedItemQueryObject, self).__init__(**kwargs)
        self.health_state = health_state
        self.backup_management_type = backup_management_type
        self.item_type = item_type
        self.policy_name = policy_name
        self.container_name = container_name
        self.backup_engine_name = backup_engine_name
        self.friendly_name = friendly_name
        self.fabric_name = fabric_name
        self.backup_set_name = backup_set_name
