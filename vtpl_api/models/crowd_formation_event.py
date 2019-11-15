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


class CrowdFormationEvent(object):
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
        'meta_crowd_formation_event': 'MetaCrowdFormationEvent'
    }

    attribute_map = {
        'meta_crowd_formation_event': 'metaCrowdFormationEvent'
    }

    def __init__(self, meta_crowd_formation_event=None):  # noqa: E501
        """CrowdFormationEvent - a model defined in OpenAPI"""  # noqa: E501

        self._meta_crowd_formation_event = None
        self.discriminator = None

        if meta_crowd_formation_event is not None:
            self.meta_crowd_formation_event = meta_crowd_formation_event

    @property
    def meta_crowd_formation_event(self):
        """Gets the meta_crowd_formation_event of this CrowdFormationEvent.  # noqa: E501


        :return: The meta_crowd_formation_event of this CrowdFormationEvent.  # noqa: E501
        :rtype: MetaCrowdFormationEvent
        """
        return self._meta_crowd_formation_event

    @meta_crowd_formation_event.setter
    def meta_crowd_formation_event(self, meta_crowd_formation_event):
        """Sets the meta_crowd_formation_event of this CrowdFormationEvent.


        :param meta_crowd_formation_event: The meta_crowd_formation_event of this CrowdFormationEvent.  # noqa: E501
        :type: MetaCrowdFormationEvent
        """

        self._meta_crowd_formation_event = meta_crowd_formation_event

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
        if not isinstance(other, CrowdFormationEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
