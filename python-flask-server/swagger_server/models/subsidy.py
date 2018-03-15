# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.citizen_base import CitizenBase  # noqa: F401,E501
from swagger_server.models.master_account_base import MasterAccountBase  # noqa: F401,E501
from swagger_server.models.subsidy_base import SubsidyBase  # noqa: F401,E501
from swagger_server.models.transaction import Transaction  # noqa: F401,E501
from swagger_server.models.user import User  # noqa: F401,E501
from swagger_server import util


class Subsidy(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None, master: MasterAccountBase=None, recipient: CitizenBase=None, creator: User=None, approver1: User=None, approver2: User=None, approve_date1: datetime=None, approve_date2: datetime=None, frequency: str=None, amount: float=None, expiry: datetime=None, transactions: List[Transaction]=None):  # noqa: E501
        """Subsidy - a model defined in Swagger

        :param id: The id of this Subsidy.  # noqa: E501
        :type id: int
        :param name: The name of this Subsidy.  # noqa: E501
        :type name: str
        :param master: The master of this Subsidy.  # noqa: E501
        :type master: MasterAccountBase
        :param recipient: The recipient of this Subsidy.  # noqa: E501
        :type recipient: CitizenBase
        :param creator: The creator of this Subsidy.  # noqa: E501
        :type creator: User
        :param approver1: The approver1 of this Subsidy.  # noqa: E501
        :type approver1: User
        :param approver2: The approver2 of this Subsidy.  # noqa: E501
        :type approver2: User
        :param approve_date1: The approve_date1 of this Subsidy.  # noqa: E501
        :type approve_date1: datetime
        :param approve_date2: The approve_date2 of this Subsidy.  # noqa: E501
        :type approve_date2: datetime
        :param frequency: The frequency of this Subsidy.  # noqa: E501
        :type frequency: str
        :param amount: The amount of this Subsidy.  # noqa: E501
        :type amount: float
        :param expiry: The expiry of this Subsidy.  # noqa: E501
        :type expiry: datetime
        :param transactions: The transactions of this Subsidy.  # noqa: E501
        :type transactions: List[Transaction]
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'master': MasterAccountBase,
            'recipient': CitizenBase,
            'creator': User,
            'approver1': User,
            'approver2': User,
            'approve_date1': datetime,
            'approve_date2': datetime,
            'frequency': str,
            'amount': float,
            'expiry': datetime,
            'transactions': List[Transaction]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'master': 'master',
            'recipient': 'recipient',
            'creator': 'creator',
            'approver1': 'approver1',
            'approver2': 'approver2',
            'approve_date1': 'approveDate1',
            'approve_date2': 'approveDate2',
            'frequency': 'frequency',
            'amount': 'amount',
            'expiry': 'expiry',
            'transactions': 'transactions'
        }

        self._id = id
        self._name = name
        self._master = master
        self._recipient = recipient
        self._creator = creator
        self._approver1 = approver1
        self._approver2 = approver2
        self._approve_date1 = approve_date1
        self._approve_date2 = approve_date2
        self._frequency = frequency
        self._amount = amount
        self._expiry = expiry
        self._transactions = transactions

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
    def id(self) -> int:
        """Gets the id of this Subsidy.


        :return: The id of this Subsidy.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Subsidy.


        :param id: The id of this Subsidy.
        :type id: int
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
    def creator(self) -> User:
        """Gets the creator of this Subsidy.


        :return: The creator of this Subsidy.
        :rtype: User
        """
        return self._creator

    @creator.setter
    def creator(self, creator: User):
        """Sets the creator of this Subsidy.


        :param creator: The creator of this Subsidy.
        :type creator: User
        """

        self._creator = creator

    @property
    def approver1(self) -> User:
        """Gets the approver1 of this Subsidy.


        :return: The approver1 of this Subsidy.
        :rtype: User
        """
        return self._approver1

    @approver1.setter
    def approver1(self, approver1: User):
        """Sets the approver1 of this Subsidy.


        :param approver1: The approver1 of this Subsidy.
        :type approver1: User
        """

        self._approver1 = approver1

    @property
    def approver2(self) -> User:
        """Gets the approver2 of this Subsidy.


        :return: The approver2 of this Subsidy.
        :rtype: User
        """
        return self._approver2

    @approver2.setter
    def approver2(self, approver2: User):
        """Sets the approver2 of this Subsidy.


        :param approver2: The approver2 of this Subsidy.
        :type approver2: User
        """

        self._approver2 = approver2

    @property
    def approve_date1(self) -> datetime:
        """Gets the approve_date1 of this Subsidy.


        :return: The approve_date1 of this Subsidy.
        :rtype: datetime
        """
        return self._approve_date1

    @approve_date1.setter
    def approve_date1(self, approve_date1: datetime):
        """Sets the approve_date1 of this Subsidy.


        :param approve_date1: The approve_date1 of this Subsidy.
        :type approve_date1: datetime
        """

        self._approve_date1 = approve_date1

    @property
    def approve_date2(self) -> datetime:
        """Gets the approve_date2 of this Subsidy.


        :return: The approve_date2 of this Subsidy.
        :rtype: datetime
        """
        return self._approve_date2

    @approve_date2.setter
    def approve_date2(self, approve_date2: datetime):
        """Sets the approve_date2 of this Subsidy.


        :param approve_date2: The approve_date2 of this Subsidy.
        :type approve_date2: datetime
        """

        self._approve_date2 = approve_date2

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
        allowed_values = ["daily", "weekly", "bi-weekly", "monthly", "yearly"]  # noqa: E501
        if frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `frequency` ({0}), must be one of {1}"
                .format(frequency, allowed_values)
            )

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

    @property
    def transactions(self) -> List[Transaction]:
        """Gets the transactions of this Subsidy.


        :return: The transactions of this Subsidy.
        :rtype: List[Transaction]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions: List[Transaction]):
        """Sets the transactions of this Subsidy.


        :param transactions: The transactions of this Subsidy.
        :type transactions: List[Transaction]
        """

        self._transactions = transactions
