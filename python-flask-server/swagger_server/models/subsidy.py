# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.account_base import AccountBase  # noqa: F401,E501
from swagger_server.models.citizen_base import CitizenBase  # noqa: F401,E501
from swagger_server.models.master_account_base import MasterAccountBase  # noqa: F401,E501
from swagger_server.models.subsidy_base import SubsidyBase  # noqa: F401,E501
from swagger_server import util


class Subsidy(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, master: MasterAccountBase=None, recipient: CitizenBase=None, account: AccountBase=None, frequency: str=None, amount: float=None, expiry: datetime=None):  # noqa: E501
        """Subsidy - a model defined in Swagger

        :param id: The id of this Subsidy.  # noqa: E501
        :type id: str
        :param name: The name of this Subsidy.  # noqa: E501
        :type name: str
        :param master: The master of this Subsidy.  # noqa: E501
        :type master: MasterAccountBase
        :param recipient: The recipient of this Subsidy.  # noqa: E501
        :type recipient: CitizenBase
        :param account: The account of this Subsidy.  # noqa: E501
        :type account: AccountBase
        :param frequency: The frequency of this Subsidy.  # noqa: E501
        :type frequency: str
        :param amount: The amount of this Subsidy.  # noqa: E501
        :type amount: float
        :param expiry: The expiry of this Subsidy.  # noqa: E501
        :type expiry: datetime
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'master': MasterAccountBase,
            'recipient': CitizenBase,
            'account': AccountBase,
            'frequency': str,
            'amount': float,
            'expiry': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'master': 'master',
            'recipient': 'recipient',
            'account': 'account',
            'frequency': 'frequency',
            'amount': 'amount',
            'expiry': 'expiry'
        }

        self._id = id
        self._name = name
        self._master = master
        self._recipient = recipient
        self._account = account
        self._frequency = frequency
        self._amount = amount
        self._expiry = expiry

    @classmethod
    def from_dict(cls, dikt) -> 'Subsidy':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The subsidy of this Subsidy.  # noqa: E501
        :rtype: Subsidy
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Subsidy.


        :return: The id of this Subsidy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Subsidy.


        :param id: The id of this Subsidy.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Subsidy.


        :return: The name of this Subsidy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Subsidy.


        :param name: The name of this Subsidy.
        :type name: str
        """

        self._name = name

    @property
    def master(self) -> MasterAccountBase:
        """Gets the master of this Subsidy.


        :return: The master of this Subsidy.
        :rtype: MasterAccountBase
        """
        return self._master

    @master.setter
    def master(self, master: MasterAccountBase):
        """Sets the master of this Subsidy.


        :param master: The master of this Subsidy.
        :type master: MasterAccountBase
        """

        self._master = master

    @property
    def recipient(self) -> CitizenBase:
        """Gets the recipient of this Subsidy.


        :return: The recipient of this Subsidy.
        :rtype: CitizenBase
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient: CitizenBase):
        """Sets the recipient of this Subsidy.


        :param recipient: The recipient of this Subsidy.
        :type recipient: CitizenBase
        """

        self._recipient = recipient

    @property
    def account(self) -> AccountBase:
        """Gets the account of this Subsidy.


        :return: The account of this Subsidy.
        :rtype: AccountBase
        """
        return self._account

    @account.setter
    def account(self, account: AccountBase):
        """Sets the account of this Subsidy.


        :param account: The account of this Subsidy.
        :type account: AccountBase
        """

        self._account = account

    @property
    def frequency(self) -> str:
        """Gets the frequency of this Subsidy.


        :return: The frequency of this Subsidy.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency: str):
        """Sets the frequency of this Subsidy.


        :param frequency: The frequency of this Subsidy.
        :type frequency: str
        """

        self._frequency = frequency

    @property
    def amount(self) -> float:
        """Gets the amount of this Subsidy.


        :return: The amount of this Subsidy.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        """Sets the amount of this Subsidy.


        :param amount: The amount of this Subsidy.
        :type amount: float
        """
        if amount is not None and amount < 0:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `0`")  # noqa: E501

        self._amount = amount

    @property
    def expiry(self) -> datetime:
        """Gets the expiry of this Subsidy.


        :return: The expiry of this Subsidy.
        :rtype: datetime
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry: datetime):
        """Sets the expiry of this Subsidy.


        :param expiry: The expiry of this Subsidy.
        :type expiry: datetime
        """

        self._expiry = expiry
