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


class SourceEndPointSourceList(object):
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
        'source_id': 'str',
        'type': 'SourceType',
        'base_url': 'str',
        'user': 'str',
        '_pass': 'str'
    }

    attribute_map = {
        'source_id': 'sourceId',
        'type': 'type',
        'base_url': 'baseUrl',
        'user': 'user',
        '_pass': 'pass'
    }

    def __init__(self, source_id=None, type=None, base_url=None, user=None, _pass=None):  # noqa: E501
        """SourceEndPointSourceList - a model defined in OpenAPI"""  # noqa: E501

        self._source_id = None
        self._type = None
        self._base_url = None
        self._user = None
        self.__pass = None
        self.discriminator = None

        if source_id is not None:
            self.source_id = source_id
        if type is not None:
            self.type = type
        if base_url is not None:
            self.base_url = base_url
        if user is not None:
            self.user = user
        if _pass is not None:
            self._pass = _pass

    @property
    def source_id(self):
        """Gets the source_id of this SourceEndPointSourceList.  # noqa: E501


        :return: The source_id of this SourceEndPointSourceList.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this SourceEndPointSourceList.


        :param source_id: The source_id of this SourceEndPointSourceList.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

    @property
    def type(self):
        """Gets the type of this SourceEndPointSourceList.  # noqa: E501


        :return: The type of this SourceEndPointSourceList.  # noqa: E501
        :rtype: SourceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SourceEndPointSourceList.


        :param type: The type of this SourceEndPointSourceList.  # noqa: E501
        :type: SourceType
        """

        self._type = type

    @property
    def base_url(self):
        """Gets the base_url of this SourceEndPointSourceList.  # noqa: E501


        :return: The base_url of this SourceEndPointSourceList.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this SourceEndPointSourceList.


        :param base_url: The base_url of this SourceEndPointSourceList.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def user(self):
        """Gets the user of this SourceEndPointSourceList.  # noqa: E501


        :return: The user of this SourceEndPointSourceList.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SourceEndPointSourceList.


        :param user: The user of this SourceEndPointSourceList.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def _pass(self):
        """Gets the _pass of this SourceEndPointSourceList.  # noqa: E501


        :return: The _pass of this SourceEndPointSourceList.  # noqa: E501
        :rtype: str
        """
        return self.__pass

    @_pass.setter
    def _pass(self, _pass):
        """Sets the _pass of this SourceEndPointSourceList.


        :param _pass: The _pass of this SourceEndPointSourceList.  # noqa: E501
        :type: str
        """

        self.__pass = _pass

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
        if not isinstance(other, SourceEndPointSourceList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
