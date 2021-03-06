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


class PolicySettings(Model):
    """Defines contents of a web application firewall global configuration.

    :param enabled_state: describes if the policy is in enabled state or
     disabled state. Possible values include: 'Disabled', 'Enabled'
    :type enabled_state: str or ~azure.mgmt.frontdoor.models.EnabledState
    :param mode: Describes if it is in detection mode  or prevention mode at
     policy level. Possible values include: 'Prevention', 'Detection'
    :type mode: str or ~azure.mgmt.frontdoor.models.Mode
    """

    _attribute_map = {
        'enabled_state': {'key': 'enabledState', 'type': 'str'},
        'mode': {'key': 'mode', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PolicySettings, self).__init__(**kwargs)
        self.enabled_state = kwargs.get('enabled_state', None)
        self.mode = kwargs.get('mode', None)
