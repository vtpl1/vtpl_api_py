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


class RegisteredFace(object):
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
        'registered_face_id': 'str',
        'full_name': 'str',
        'face_snaps': 'list[str]',
        'age': 'int',
        'sex': 'str',
        'type': 'FaceCategory',
        'updated': 'datetime',
        'created': 'datetime',
        'etag': 'str',
        'links': 'Links'
    }

    attribute_map = {
        'id': '_id',
        'registered_face_id': 'registeredFaceId',
        'full_name': 'fullName',
        'face_snaps': 'faceSnaps',
        'age': 'age',
        'sex': 'sex',
        'type': 'type',
        'updated': 'updated',
        'created': 'created',
        'etag': 'etag',
        'links': 'links'
    }

    def __init__(self, id=None, registered_face_id=None, full_name=None, face_snaps=None, age=None, sex=None, type=None, updated=None, created=None, etag=None, links=None):  # noqa: E501
        """RegisteredFace - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._registered_face_id = None
        self._full_name = None
        self._face_snaps = None
        self._age = None
        self._sex = None
        self._type = None
        self._updated = None
        self._created = None
        self._etag = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if registered_face_id is not None:
            self.registered_face_id = registered_face_id
        if full_name is not None:
            self.full_name = full_name
        if face_snaps is not None:
            self.face_snaps = face_snaps
        if age is not None:
            self.age = age
        if sex is not None:
            self.sex = sex
        if type is not None:
            self.type = type
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
        """Gets the id of this RegisteredFace.  # noqa: E501


        :return: The id of this RegisteredFace.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RegisteredFace.


        :param id: The id of this RegisteredFace.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def registered_face_id(self):
        """Gets the registered_face_id of this RegisteredFace.  # noqa: E501


        :return: The registered_face_id of this RegisteredFace.  # noqa: E501
        :rtype: str
        """
        return self._registered_face_id

    @registered_face_id.setter
    def registered_face_id(self, registered_face_id):
        """Sets the registered_face_id of this RegisteredFace.


        :param registered_face_id: The registered_face_id of this RegisteredFace.  # noqa: E501
        :type: str
        """

        self._registered_face_id = registered_face_id

    @property
    def full_name(self):
        """Gets the full_name of this RegisteredFace.  # noqa: E501


        :return: The full_name of this RegisteredFace.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this RegisteredFace.


        :param full_name: The full_name of this RegisteredFace.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def face_snaps(self):
        """Gets the face_snaps of this RegisteredFace.  # noqa: E501

        _id of faceSnap #$ref: '#/components/schemas/faceSnap'  # noqa: E501

        :return: The face_snaps of this RegisteredFace.  # noqa: E501
        :rtype: list[str]
        """
        return self._face_snaps

    @face_snaps.setter
    def face_snaps(self, face_snaps):
        """Sets the face_snaps of this RegisteredFace.

        _id of faceSnap #$ref: '#/components/schemas/faceSnap'  # noqa: E501

        :param face_snaps: The face_snaps of this RegisteredFace.  # noqa: E501
        :type: list[str]
        """

        self._face_snaps = face_snaps

    @property
    def age(self):
        """Gets the age of this RegisteredFace.  # noqa: E501


        :return: The age of this RegisteredFace.  # noqa: E501
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this RegisteredFace.


        :param age: The age of this RegisteredFace.  # noqa: E501
        :type: int
        """

        self._age = age

    @property
    def sex(self):
        """Gets the sex of this RegisteredFace.  # noqa: E501


        :return: The sex of this RegisteredFace.  # noqa: E501
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this RegisteredFace.


        :param sex: The sex of this RegisteredFace.  # noqa: E501
        :type: str
        """
        allowed_values = ["Male", "Female", "Other", "NA"]  # noqa: E501
        if sex not in allowed_values:
            raise ValueError(
                "Invalid value for `sex` ({0}), must be one of {1}"  # noqa: E501
                .format(sex, allowed_values)
            )

        self._sex = sex

    @property
    def type(self):
        """Gets the type of this RegisteredFace.  # noqa: E501


        :return: The type of this RegisteredFace.  # noqa: E501
        :rtype: FaceCategory
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RegisteredFace.


        :param type: The type of this RegisteredFace.  # noqa: E501
        :type: FaceCategory
        """

        self._type = type

    @property
    def updated(self):
        """Gets the updated of this RegisteredFace.  # noqa: E501


        :return: The updated of this RegisteredFace.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this RegisteredFace.


        :param updated: The updated of this RegisteredFace.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this RegisteredFace.  # noqa: E501


        :return: The created of this RegisteredFace.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this RegisteredFace.


        :param created: The created of this RegisteredFace.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def etag(self):
        """Gets the etag of this RegisteredFace.  # noqa: E501


        :return: The etag of this RegisteredFace.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this RegisteredFace.


        :param etag: The etag of this RegisteredFace.  # noqa: E501
        :type: str
        """

        self._etag = etag

    @property
    def links(self):
        """Gets the links of this RegisteredFace.  # noqa: E501


        :return: The links of this RegisteredFace.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this RegisteredFace.


        :param links: The links of this RegisteredFace.  # noqa: E501
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
        if not isinstance(other, RegisteredFace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
