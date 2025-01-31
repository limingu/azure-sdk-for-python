# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs."""

    INTERNAL = "Internal"


class ApiVersionParameter(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ApiVersionParameter."""

    TWO_THOUSAND_TWENTY09_01_PREVIEW = "2020-09-01-preview"
    TWO_THOUSAND_TWENTY_ONE04_04_PREVIEW = "2021-04-04-preview"
    TWO_THOUSAND_TWENTY_TWO03_01 = "2022-03-01"


class AutoTrackingConfiguration(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Auto-tracking configuration."""

    DISABLED = "disabled"
    X_BAND = "xBand"
    S_BAND = "sBand"


class Capability(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Capability of the Ground Station."""

    EARTH_OBSERVATION = "EarthObservation"
    COMMUNICATION = "Communication"


class CapabilityParameter(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """CapabilityParameter."""

    EARTH_OBSERVATION = "EarthObservation"
    COMMUNICATION = "Communication"


class ContactProfilesPropertiesProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current state of the resource's creation, deletion, or modification."""

    CREATING = "Creating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    UPDATING = "Updating"
    DELETING = "Deleting"


class ContactsPropertiesProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current state of the resource's creation, deletion, or modification."""

    CREATING = "Creating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    UPDATING = "Updating"
    DELETING = "Deleting"


class ContactsStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of a contact."""

    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    PROVIDER_CANCELLED = "providerCancelled"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class Direction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Direction (uplink or downlink)."""

    UPLINK = "uplink"
    DOWNLINK = "downlink"


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"


class Polarization(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Polarization. e.g. (RHCP, LHCP)."""

    RHCP = "RHCP"
    LHCP = "LHCP"
    LINEAR_VERTICAL = "linearVertical"
    LINEAR_HORIZONTAL = "linearHorizontal"


class Protocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Protocol either UDP or TCP."""

    TCP = "TCP"
    UDP = "UDP"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current state of the resource's creation, deletion, or modification."""

    CREATING = "Creating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    UPDATING = "Updating"
    DELETING = "Deleting"


class ReleaseMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Release Status of a ground station."""

    PREVIEW = "Preview"
    GA = "GA"


class SpacecraftsPropertiesProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current state of the resource's creation, deletion, or modification."""

    CREATING = "Creating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    UPDATING = "Updating"
    DELETING = "Deleting"


class Status(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of operation."""

    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"
    RUNNING = "Running"
