# coding: utf-8

"""
    Engine api

    Engine APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SubSystem(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'sub_system_id': 'str',
        'capabilities': 'list[Capability]',
        'is_syncing': 'bool',
        'last_synced': 'int',
        'updated': 'datetime',
        'created': 'datetime',
        'etag': 'str',
        'links': 'Links'
    }

    attribute_map = {
        'id': '_id',
        'sub_system_id': 'subSystemId',
        'capabilities': 'capabilities',
        'is_syncing': 'isSyncing',
        'last_synced': 'lastSynced',
        'updated': 'updated',
        'created': 'created',
        'etag': 'etag',
        'links': 'links'
    }

    def __init__(self, id=None, sub_system_id=None, capabilities=None, is_syncing=False, last_synced=None, updated=None, created=None, etag=None, links=None):  # noqa: E501
        """SubSystem - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._sub_system_id = None
        self._capabilities = None
        self._is_syncing = None
        self._last_synced = None
        self._updated = None
        self._created = None
        self._etag = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if sub_system_id is not None:
            self.sub_system_id = sub_system_id
        if capabilities is not None:
            self.capabilities = capabilities
        if is_syncing is not None:
            self.is_syncing = is_syncing
        self.last_synced = last_synced
        if updated is not None:
            self.updated = updated
        if created is not None:
            self.created = created
        if etag is not None:
            self.etag = etag
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this SubSystem.  # noqa: E501


        :return: The id of this SubSystem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubSystem.


        :param id: The id of this SubSystem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def sub_system_id(self):
        """Gets the sub_system_id of this SubSystem.  # noqa: E501

        unique id of the system in the central system database  # noqa: E501

        :return: The sub_system_id of this SubSystem.  # noqa: E501
        :rtype: str
        """
        return self._sub_system_id

    @sub_system_id.setter
    def sub_system_id(self, sub_system_id):
        """Sets the sub_system_id of this SubSystem.

        unique id of the system in the central system database  # noqa: E501

        :param sub_system_id: The sub_system_id of this SubSystem.  # noqa: E501
        :type: str
        """

        self._sub_system_id = sub_system_id

    @property
    def capabilities(self):
        """Gets the capabilities of this SubSystem.  # noqa: E501


        :return: The capabilities of this SubSystem.  # noqa: E501
        :rtype: list[Capability]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this SubSystem.


        :param capabilities: The capabilities of this SubSystem.  # noqa: E501
        :type: list[Capability]
        """

        self._capabilities = capabilities

    @property
    def is_syncing(self):
        """Gets the is_syncing of this SubSystem.  # noqa: E501

        If data sync process is ongoing from central to sub system  # noqa: E501

        :return: The is_syncing of this SubSystem.  # noqa: E501
        :rtype: bool
        """
        return self._is_syncing

    @is_syncing.setter
    def is_syncing(self, is_syncing):
        """Sets the is_syncing of this SubSystem.

        If data sync process is ongoing from central to sub system  # noqa: E501

        :param is_syncing: The is_syncing of this SubSystem.  # noqa: E501
        :type: bool
        """

        self._is_syncing = is_syncing

    @property
    def last_synced(self):
        """Gets the last_synced of this SubSystem.  # noqa: E501

        Epoch timestamp when the sub system was last synced with central system  # noqa: E501

        :return: The last_synced of this SubSystem.  # noqa: E501
        :rtype: int
        """
        return self._last_synced

    @last_synced.setter
    def last_synced(self, last_synced):
        """Sets the last_synced of this SubSystem.

        Epoch timestamp when the sub system was last synced with central system  # noqa: E501

        :param last_synced: The last_synced of this SubSystem.  # noqa: E501
        :type: int
        """

        self._last_synced = last_synced

    @property
    def updated(self):
        """Gets the updated of this SubSystem.  # noqa: E501


        :return: The updated of this SubSystem.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this SubSystem.


        :param updated: The updated of this SubSystem.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this SubSystem.  # noqa: E501


        :return: The created of this SubSystem.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SubSystem.


        :param created: The created of this SubSystem.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def etag(self):
        """Gets the etag of this SubSystem.  # noqa: E501


        :return: The etag of this SubSystem.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this SubSystem.


        :param etag: The etag of this SubSystem.  # noqa: E501
        :type: str
        """

        self._etag = etag

    @property
    def links(self):
        """Gets the links of this SubSystem.  # noqa: E501


        :return: The links of this SubSystem.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SubSystem.


        :param links: The links of this SubSystem.  # noqa: E501
        :type: Links
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubSystem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
