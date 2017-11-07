# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.8.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1alpha1ExternalAdmissionHookConfiguration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'api_version': 'str',
        'external_admission_hooks': 'list[V1alpha1ExternalAdmissionHook]',
        'kind': 'str',
        'metadata': 'V1ObjectMeta'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'external_admission_hooks': 'externalAdmissionHooks',
        'kind': 'kind',
        'metadata': 'metadata'
    }

    def __init__(self, api_version=None, external_admission_hooks=None, kind=None, metadata=None):
        """
        V1alpha1ExternalAdmissionHookConfiguration - a model defined in Swagger
        """

        self._api_version = None
        self._external_admission_hooks = None
        self._kind = None
        self._metadata = None
        self.discriminator = None

        if api_version is not None:
          self.api_version = api_version
        if external_admission_hooks is not None:
          self.external_admission_hooks = external_admission_hooks
        if kind is not None:
          self.kind = kind
        if metadata is not None:
          self.metadata = metadata

    @property
    def api_version(self):
        """
        Gets the api_version of this V1alpha1ExternalAdmissionHookConfiguration.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :return: The api_version of this V1alpha1ExternalAdmissionHookConfiguration.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1alpha1ExternalAdmissionHookConfiguration.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1alpha1ExternalAdmissionHookConfiguration.
        :type: str
        """

        self._api_version = api_version

    @property
    def external_admission_hooks(self):
        """
        Gets the external_admission_hooks of this V1alpha1ExternalAdmissionHookConfiguration.
        ExternalAdmissionHooks is a list of external admission webhooks and the affected resources and operations.

        :return: The external_admission_hooks of this V1alpha1ExternalAdmissionHookConfiguration.
        :rtype: list[V1alpha1ExternalAdmissionHook]
        """
        return self._external_admission_hooks

    @external_admission_hooks.setter
    def external_admission_hooks(self, external_admission_hooks):
        """
        Sets the external_admission_hooks of this V1alpha1ExternalAdmissionHookConfiguration.
        ExternalAdmissionHooks is a list of external admission webhooks and the affected resources and operations.

        :param external_admission_hooks: The external_admission_hooks of this V1alpha1ExternalAdmissionHookConfiguration.
        :type: list[V1alpha1ExternalAdmissionHook]
        """

        self._external_admission_hooks = external_admission_hooks

    @property
    def kind(self):
        """
        Gets the kind of this V1alpha1ExternalAdmissionHookConfiguration.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :return: The kind of this V1alpha1ExternalAdmissionHookConfiguration.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1alpha1ExternalAdmissionHookConfiguration.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1alpha1ExternalAdmissionHookConfiguration.
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """
        Gets the metadata of this V1alpha1ExternalAdmissionHookConfiguration.
        Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata.

        :return: The metadata of this V1alpha1ExternalAdmissionHookConfiguration.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1alpha1ExternalAdmissionHookConfiguration.
        Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata.

        :param metadata: The metadata of this V1alpha1ExternalAdmissionHookConfiguration.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1alpha1ExternalAdmissionHookConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
