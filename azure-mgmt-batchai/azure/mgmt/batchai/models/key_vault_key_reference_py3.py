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


class KeyVaultKeyReference(Model):
    """Describes a reference to Key Vault Key.

    All required parameters must be populated in order to send to Azure.

    :param source_vault: Required. Fully qualified resource Id for the Key
     Vault.
    :type source_vault: ~azure.mgmt.batchai.models.ResourceId
    :param key_url: Required. The URL referencing a key in a Key Vault.
    :type key_url: str
    """

    _validation = {
        'source_vault': {'required': True},
        'key_url': {'required': True},
    }

    _attribute_map = {
        'source_vault': {'key': 'sourceVault', 'type': 'ResourceId'},
        'key_url': {'key': 'keyUrl', 'type': 'str'},
    }

    def __init__(self, *, source_vault, key_url: str, **kwargs) -> None:
        super(KeyVaultKeyReference, self).__init__(**kwargs)
        self.source_vault = source_vault
        self.key_url = key_url
