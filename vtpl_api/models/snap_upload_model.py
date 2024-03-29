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


class SnapUploadModel(object):
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
        'portfolio_id': 'str',
        'full_name': 'str',
        'age': 'int',
        'sex': 'Gender',
        'type': 'FaceCategory',
        'snaps': 'list[UploadSnap]'
    }

    attribute_map = {
        'portfolio_id': 'portfolioId',
        'full_name': 'fullName',
        'age': 'age',
        'sex': 'sex',
        'type': 'type',
        'snaps': 'snaps'
    }

    def __init__(self, portfolio_id=None, full_name=None, age=None, sex=None, type=None, snaps=None):  # noqa: E501
        """SnapUploadModel - a model defined in OpenAPI"""  # noqa: E501

        self._portfolio_id = None
        self._full_name = None
        self._age = None
        self._sex = None
        self._type = None
        self._snaps = None
        self.discriminator = None

        if portfolio_id is not None:
            self.portfolio_id = portfolio_id
        if full_name is not None:
            self.full_name = full_name
        if age is not None:
            self.age = age
        if sex is not None:
            self.sex = sex
        if type is not None:
            self.type = type
        if snaps is not None:
            self.snaps = snaps

    @property
    def portfolio_id(self):
        """Gets the portfolio_id of this SnapUploadModel.  # noqa: E501


        :return: The portfolio_id of this SnapUploadModel.  # noqa: E501
        :rtype: str
        """
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id):
        """Sets the portfolio_id of this SnapUploadModel.


        :param portfolio_id: The portfolio_id of this SnapUploadModel.  # noqa: E501
        :type: str
        """

        self._portfolio_id = portfolio_id

    @property
    def full_name(self):
        """Gets the full_name of this SnapUploadModel.  # noqa: E501


        :return: The full_name of this SnapUploadModel.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this SnapUploadModel.


        :param full_name: The full_name of this SnapUploadModel.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def age(self):
        """Gets the age of this SnapUploadModel.  # noqa: E501


        :return: The age of this SnapUploadModel.  # noqa: E501
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this SnapUploadModel.


        :param age: The age of this SnapUploadModel.  # noqa: E501
        :type: int
        """

        self._age = age

    @property
    def sex(self):
        """Gets the sex of this SnapUploadModel.  # noqa: E501


        :return: The sex of this SnapUploadModel.  # noqa: E501
        :rtype: Gender
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this SnapUploadModel.


        :param sex: The sex of this SnapUploadModel.  # noqa: E501
        :type: Gender
        """

        self._sex = sex

    @property
    def type(self):
        """Gets the type of this SnapUploadModel.  # noqa: E501


        :return: The type of this SnapUploadModel.  # noqa: E501
        :rtype: FaceCategory
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SnapUploadModel.


        :param type: The type of this SnapUploadModel.  # noqa: E501
        :type: FaceCategory
        """

        self._type = type

    @property
    def snaps(self):
        """Gets the snaps of this SnapUploadModel.  # noqa: E501

        _id of faceSnap #$ref: '#/components/schemas/faceSnap'  # noqa: E501

        :return: The snaps of this SnapUploadModel.  # noqa: E501
        :rtype: list[UploadSnap]
        """
        return self._snaps

    @snaps.setter
    def snaps(self, snaps):
        """Sets the snaps of this SnapUploadModel.

        _id of faceSnap #$ref: '#/components/schemas/faceSnap'  # noqa: E501

        :param snaps: The snaps of this SnapUploadModel.  # noqa: E501
        :type: list[UploadSnap]
        """

        self._snaps = snaps

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
        if not isinstance(other, SnapUploadModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
