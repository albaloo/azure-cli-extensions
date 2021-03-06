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


class CheckNameAvailabilityInput(Model):
    """Input of CheckNameAvailability API.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The resource name to validate.
    :type name: str
    :param type: Required. The type of the resource whose name is to be
     validated. Possible values include: 'Microsoft.Network/frontDoors',
     'Microsoft.Network/frontDoors/frontendEndpoints'
    :type type: str or ~azure.mgmt.frontdoor.models.ResourceType
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'ResourceType'},
    }

    def __init__(self, *, name: str, type, **kwargs) -> None:
        super(CheckNameAvailabilityInput, self).__init__(**kwargs)
        self.name = name
        self.type = type
