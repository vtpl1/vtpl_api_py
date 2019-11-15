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


class MetaVehicleCongestionEvent(object):
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
        'no_of_vehicle': 'int'
    }

    attribute_map = {
        'no_of_vehicle': 'noOfVehicle'
    }

    def __init__(self, no_of_vehicle=0):  # noqa: E501
        """MetaVehicleCongestionEvent - a model defined in OpenAPI"""  # noqa: E501

        self._no_of_vehicle = None
        self.discriminator = None

        if no_of_vehicle is not None:
            self.no_of_vehicle = no_of_vehicle

    @property
    def no_of_vehicle(self):
        """Gets the no_of_vehicle of this MetaVehicleCongestionEvent.  # noqa: E501

        # of vehicle detected by engine during congestion  # noqa: E501

        :return: The no_of_vehicle of this MetaVehicleCongestionEvent.  # noqa: E501
        :rtype: int
        """
        return self._no_of_vehicle

    @no_of_vehicle.setter
    def no_of_vehicle(self, no_of_vehicle):
        """Sets the no_of_vehicle of this MetaVehicleCongestionEvent.

        # of vehicle detected by engine during congestion  # noqa: E501

        :param no_of_vehicle: The no_of_vehicle of this MetaVehicleCongestionEvent.  # noqa: E501
        :type: int
        """

        self._no_of_vehicle = no_of_vehicle

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
        if not isinstance(other, MetaVehicleCongestionEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other