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


class AzureFileShareReference(Model):
    """Details of the Azure File Share to mount on the cluster.

    All required parameters must be populated in order to send to Azure.

    :param account_name: Required. Name of the storage account.
    :type account_name: str
    :param azure_file_url: Required. URL to access the Azure File.
    :type azure_file_url: str
    :param credentials: Required. Information of the Azure File credentials.
    :type credentials: ~azure.mgmt.batchai.models.AzureStorageCredentialsInfo
    :param relative_mount_path: Required. Specifies the relative path on the
     compute node where the Azure file share will be mounted. Note that all
     cluster level file shares will be mounted under $AZ_BATCHAI_MOUNT_ROOT
     location and all job level file shares will be mounted under
     $AZ_BATCHAI_JOB_MOUNT_ROOT.
    :type relative_mount_path: str
    :param file_mode: Specifies the file mode. Default value is 0777. Valid
     only if OS is linux. Default value: "0777" .
    :type file_mode: str
    :param directory_mode: Specifies the directory Mode. Default value is
     0777. Valid only if OS is linux. Default value: "0777" .
    :type directory_mode: str
    """

    _validation = {
        'account_name': {'required': True},
        'azure_file_url': {'required': True},
        'credentials': {'required': True},
        'relative_mount_path': {'required': True},
    }

    _attribute_map = {
        'account_name': {'key': 'accountName', 'type': 'str'},
        'azure_file_url': {'key': 'azureFileUrl', 'type': 'str'},
        'credentials': {'key': 'credentials', 'type': 'AzureStorageCredentialsInfo'},
        'relative_mount_path': {'key': 'relativeMountPath', 'type': 'str'},
        'file_mode': {'key': 'fileMode', 'type': 'str'},
        'directory_mode': {'key': 'directoryMode', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AzureFileShareReference, self).__init__(**kwargs)
        self.account_name = kwargs.get('account_name', None)
        self.azure_file_url = kwargs.get('azure_file_url', None)
        self.credentials = kwargs.get('credentials', None)
        self.relative_mount_path = kwargs.get('relative_mount_path', None)
        self.file_mode = kwargs.get('file_mode', "0777")
        self.directory_mode = kwargs.get('directory_mode', "0777")
