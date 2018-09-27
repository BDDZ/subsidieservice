# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.status_base import StatusBase  # noqa: F401,E501
from swagger_server import util


class ServiceStatus(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, url: str=None, active: bool=None):  # noqa: E501
        """ServiceStatus - a model defined in Swagger

        :param name: The name of this ServiceStatus.  # noqa: E501
        :type name: str
        :param url: The url of this ServiceStatus.  # noqa: E501
        :type url: str
        :param active: The active of this ServiceStatus.  # noqa: E501
        :type active: bool
        """
        self.swagger_types = {
            'name': str,
            'url': str,
            'active': bool
        }

        self.attribute_map = {
            'name': 'name',
            'url': 'url',
            'active': 'active'
        }

        self._name = name
        self._url = url
        self._active = active

    @classmethod
    def from_dict(cls, dikt) -> 'ServiceStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The service-status of this ServiceStatus.  # noqa: E501
        :rtype: ServiceStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this ServiceStatus.


        :return: The name of this ServiceStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ServiceStatus.


        :param name: The name of this ServiceStatus.
        :type name: str
        """

        self._name = name

    @property
    def url(self) -> str:
        """Gets the url of this ServiceStatus.


        :return: The url of this ServiceStatus.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this ServiceStatus.


        :param url: The url of this ServiceStatus.
        :type url: str
        """

        self._url = url

    @property
    def active(self) -> bool:
        """Gets the active of this ServiceStatus.


        :return: The active of this ServiceStatus.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active: bool):
        """Sets the active of this ServiceStatus.


        :param active: The active of this ServiceStatus.
        :type active: bool
        """

        self._active = active
