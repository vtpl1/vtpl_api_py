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


class CrowdDispersionEventsResponse(object):
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
        'items': 'list[CrowdDispersionEvent]',
        'links': 'Links',
        'meta': 'Meta'
    }

    attribute_map = {
        'items': 'items',
        'links': 'links',
        'meta': 'meta'
    }

    def __init__(self, items=None, links=None, meta=None):  # noqa: E501
        """CrowdDispersionEventsResponse - a model defined in OpenAPI"""  # noqa: E501

        self._items = None
        self._links = None
        self._meta = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if links is not None:
            self.links = links
        if meta is not None:
            self.meta = meta

    @property
    def items(self):
        """Gets the items of this CrowdDispersionEventsResponse.  # noqa: E501


        :return: The items of this CrowdDispersionEventsResponse.  # noqa: E501
        :rtype: list[CrowdDispersionEvent]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CrowdDispersionEventsResponse.


        :param items: The items of this CrowdDispersionEventsResponse.  # noqa: E501
        :type: list[CrowdDispersionEvent]
        """

        self._items = items

    @property
    def links(self):
        """Gets the links of this CrowdDispersionEventsResponse.  # noqa: E501


        :return: The links of this CrowdDispersionEventsResponse.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CrowdDispersionEventsResponse.


        :param links: The links of this CrowdDispersionEventsResponse.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def meta(self):
        """Gets the meta of this CrowdDispersionEventsResponse.  # noqa: E501


        :return: The meta of this CrowdDispersionEventsResponse.  # noqa: E501
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this CrowdDispersionEventsResponse.


        :param meta: The meta of this CrowdDispersionEventsResponse.  # noqa: E501
        :type: Meta
        """

        self._meta = meta

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
        if not isinstance(other, CrowdDispersionEventsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
