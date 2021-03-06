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

from .resource import Resource


class ManagedCluster(Resource):
    """Managed cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar provisioning_state: The current deployment or provisioning state,
     which only appears in the response.
    :vartype provisioning_state: str
    :param kubernetes_version: Version of Kubernetes specified when creating
     the managed cluster.
    :type kubernetes_version: str
    :param dns_prefix: DNS prefix specified when creating the managed cluster.
    :type dns_prefix: str
    :ivar fqdn: FDQN for the master pool.
    :vartype fqdn: str
    :param agent_pool_profiles: Properties of the agent pool.
    :type agent_pool_profiles:
     list[~azure.mgmt.containerservice.v2018_08_01_preview.models.ManagedClusterAgentPoolProfile]
    :param linux_profile: Profile for Linux VMs in the container service
     cluster.
    :type linux_profile:
     ~azure.mgmt.containerservice.v2018_08_01_preview.models.ContainerServiceLinuxProfile
    :param service_principal_profile: Information about a service principal
     identity for the cluster to use for manipulating Azure APIs.
    :type service_principal_profile:
     ~azure.mgmt.containerservice.v2018_08_01_preview.models.ManagedClusterServicePrincipalProfile
    :param addon_profiles: Profile of managed cluster add-on.
    :type addon_profiles: dict[str,
     ~azure.mgmt.containerservice.v2018_08_01_preview.models.ManagedClusterAddonProfile]
    :ivar node_resource_group: Name of the resource group containing agent
     pool nodes.
    :vartype node_resource_group: str
    :param enable_rbac: Whether to enable Kubernetes Role-Based Access
     Control.
    :type enable_rbac: bool
    :param network_profile: Profile of network configuration.
    :type network_profile:
     ~azure.mgmt.containerservice.v2018_08_01_preview.models.ContainerServiceNetworkProfile
    :param aad_profile: Profile of Azure Active Directory configuration.
    :type aad_profile:
     ~azure.mgmt.containerservice.v2018_08_01_preview.models.ManagedClusterAADProfile
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'fqdn': {'readonly': True},
        'node_resource_group': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'kubernetes_version': {'key': 'properties.kubernetesVersion', 'type': 'str'},
        'dns_prefix': {'key': 'properties.dnsPrefix', 'type': 'str'},
        'fqdn': {'key': 'properties.fqdn', 'type': 'str'},
        'agent_pool_profiles': {'key': 'properties.agentPoolProfiles', 'type': '[ManagedClusterAgentPoolProfile]'},
        'linux_profile': {'key': 'properties.linuxProfile', 'type': 'ContainerServiceLinuxProfile'},
        'service_principal_profile': {'key': 'properties.servicePrincipalProfile', 'type': 'ManagedClusterServicePrincipalProfile'},
        'addon_profiles': {'key': 'properties.addonProfiles', 'type': '{ManagedClusterAddonProfile}'},
        'node_resource_group': {'key': 'properties.nodeResourceGroup', 'type': 'str'},
        'enable_rbac': {'key': 'properties.enableRBAC', 'type': 'bool'},
        'network_profile': {'key': 'properties.networkProfile', 'type': 'ContainerServiceNetworkProfile'},
        'aad_profile': {'key': 'properties.aadProfile', 'type': 'ManagedClusterAADProfile'},
    }

    def __init__(self, **kwargs):
        super(ManagedCluster, self).__init__(**kwargs)
        self.provisioning_state = None
        self.kubernetes_version = kwargs.get('kubernetes_version', None)
        self.dns_prefix = kwargs.get('dns_prefix', None)
        self.fqdn = None
        self.agent_pool_profiles = kwargs.get('agent_pool_profiles', None)
        self.linux_profile = kwargs.get('linux_profile', None)
        self.service_principal_profile = kwargs.get('service_principal_profile', None)
        self.addon_profiles = kwargs.get('addon_profiles', None)
        self.node_resource_group = None
        self.enable_rbac = kwargs.get('enable_rbac', None)
        self.network_profile = kwargs.get('network_profile', None)
        self.aad_profile = kwargs.get('aad_profile', None)
