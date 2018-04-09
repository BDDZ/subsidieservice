# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.account_base import AccountBase  # noqa: F401,E501
from swagger_server import util


class Transaction(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, _from: AccountBase=None, to_iban: str=None, to_name: str=None, amount: float=None, datetime: datetime=None):  # noqa: E501
        """Transaction - a model defined in Swagger

        :param _from: The _from of this Transaction.  # noqa: E501
        :type _from: AccountBase
        :param to_iban: The to_iban of this Transaction.  # noqa: E501
        :type to_iban: str
        :param to_name: The to_name of this Transaction.  # noqa: E501
        :type to_name: str
        :param amount: The amount of this Transaction.  # noqa: E501
        :type amount: float
        :param datetime: The datetime of this Transaction.  # noqa: E501
        :type datetime: datetime
        """
        self.swagger_types = {
            '_from': AccountBase,
            'to_iban': str,
            'to_name': str,
            'amount': float,
            'datetime': datetime
        }

        self.attribute_map = {
            '_from': 'from',
            'to_iban': 'to_iban',
            'to_name': 'to_name',
            'amount': 'amount',
            'datetime': 'datetime'
        }

        self.__from = _from
        self._to_iban = to_iban
        self._to_name = to_name
        self._amount = amount
        self._datetime = datetime

    @classmethod
    def from_dict(cls, dikt) -> 'Transaction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The transaction of this Transaction.  # noqa: E501
        :rtype: Transaction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _from(self) -> AccountBase:
        """Gets the _from of this Transaction.


        :return: The _from of this Transaction.
        :rtype: AccountBase
        """
        return self.__from

    @_from.setter
    def _from(self, _from: AccountBase):
        """Sets the _from of this Transaction.


        :param _from: The _from of this Transaction.
        :type _from: AccountBase
        """

        self.__from = _from

    @property
    def to_iban(self) -> str:
        """Gets the to_iban of this Transaction.


        :return: The to_iban of this Transaction.
        :rtype: str
        """
        return self._to_iban

    @to_iban.setter
    def to_iban(self, to_iban: str):
        """Sets the to_iban of this Transaction.


        :param to_iban: The to_iban of this Transaction.
        :type to_iban: str
        """

        self._to_iban = to_iban

    @property
    def to_name(self) -> str:
        """Gets the to_name of this Transaction.


        :return: The to_name of this Transaction.
        :rtype: str
        """
        return self._to_name

    @to_name.setter
    def to_name(self, to_name: str):
        """Sets the to_name of this Transaction.


        :param to_name: The to_name of this Transaction.
        :type to_name: str
        """

        self._to_name = to_name

    @property
    def amount(self) -> float:
        """Gets the amount of this Transaction.


        :return: The amount of this Transaction.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        """Sets the amount of this Transaction.


        :param amount: The amount of this Transaction.
        :type amount: float
        """
        if amount is not None and amount < 0:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `0`")  # noqa: E501

        self._amount = amount

    @property
    def datetime(self) -> datetime:
        """Gets the datetime of this Transaction.


        :return: The datetime of this Transaction.
        :rtype: datetime
        """
        return self._datetime

    @datetime.setter
    def datetime(self, datetime: datetime):
        """Sets the datetime of this Transaction.


        :param datetime: The datetime of this Transaction.
        :type datetime: datetime
        """

        self._datetime = datetime
