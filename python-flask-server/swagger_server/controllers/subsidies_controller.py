import connexion
import six

from swagger_server.models.subsidy import Subsidy  # noqa: E501
from swagger_server.models.subsidy_base import SubsidyBase  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util

import subsidy_service as service


@service.exceptions.exceptionHTTPencode
@service.auth.authenticate
def subsidies_get(status=None):  # noqa: E501
    """List all subsidies

    Subsidies are listed without their transactions. To get the transaction for the account associated with a particular subsidy, please use &#x60;GET /subsidies/{id}&#x60;. # noqa: E501

    :param status: The subsidy status filter can have the following values:  * **PENDING_ACCOUNT**: The citizen does not yet have a profile at a supported bank, and so has not received the subsidy  * **PENDING_ACCEPT**: The citizen does have an available bank profile, but has not yet accepted the request to access the subsidy account  * **OPEN**: The citizen has access to the subsidy  * **SHARE_CLOSED**: The citizen has canceled their access to the subsidy account and can no longer access the funds  * **CLOSED**: The subsidy has been ended via the subsidy service and the associated bank account is closed  * **ALL**: Lists all subsidies regardless of status.  If &#x60;status&#x60; left blank or not provided, this endpoint will list all PENDING_* and OPEN subsidies.
    :type status: str

    :rtype: List[SubsidyBase]
    """
    response = service.subsidies.read_all(status)
    output = [SubsidyBase().from_dict(doc) for doc in response]
    return output


@service.exceptions.exceptionHTTPencode
@service.auth.authenticate
def subsidies_id_actions_approve_post(id, body):  # noqa: E501
    """Approve a subsidy

     # noqa: E501

    :param id: 
    :type id: str
    :param body: user approving subsidy
    :type body: dict | bytes

    :rtype: Subsidy
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    raise service.exceptions.NotImplementedException('Not yet implemented')


@service.exceptions.exceptionHTTPencode
@service.auth.authenticate
def subsidies_id_delete(id):  # noqa: E501
    """Close a subsidy

    When closing a subsidy, the following steps are carried out:  * The share with the recipient citizen is ended, such that they lose access to the associated bank account  * Any remaining funds are transferred from the bank account to the master account  * The bank account is closed at the bank  * The &#x60;status&#x60; is changed to CLOSED  Since the object is never actually deleted from the database, past subsidies can still be inspected using &#x60;GET /subsidies/{id}&#x60;, or &#x60;GET /subsidies?status&#x3D;CLOSED&#x60;. # noqa: E501

    :param id: 
    :type id: str

    :rtype: None
    """
    service.subsidies.delete(id)
    return None


@service.exceptions.exceptionHTTPencode
@service.auth.authenticate
def subsidies_id_get(id):  # noqa: E501
    """Returns a specific subsidy

    Subsidies gotten by &#x60;id&#x60; include all the information listed in &#x60;GET /subsidies&#x60;, plus all the transactions from the associated account. # noqa: E501

    :param id: 
    :type id: str

    :rtype: Subsidy
    """
    response = service.subsidies.read(id)
    return Subsidy.from_dict(response)


@service.exceptions.exceptionHTTPencode
@service.auth.authenticate
def subsidies_id_patch(id, body):  # noqa: E501
    """Edit a subsidy&#39;s information

     # noqa: E501

    :param id: 
    :type id: str
    :param body: subsidy properties to be updated
    :type body: dict | bytes

    :rtype: Subsidy
    """
    if connexion.request.is_json:
        body = SubsidyBase.from_dict(connexion.request.get_json())  # noqa: E501
    raise service.exceptions.NotImplementedException('Not yet implemented')
    # response = service.subsidies.update(id, body)
    # return Subsidy.from_dict(response)


@service.exceptions.exceptionHTTPencode
@service.auth.authenticate
def subsidies_id_put(id, body):  # noqa: E501
    """Re-upload a subsidy&#39;s information

     # noqa: E501

    :param id: 
    :type id: str
    :param body: subsidy details
    :type body: dict | bytes

    :rtype: Subsidy
    """
    if connexion.request.is_json:
        body = SubsidyBase.from_dict(connexion.request.get_json())  # noqa: E501
    raise service.exceptions.NotImplementedException('Not yet implemented')
    # response = service.subsidies.replace(id, body)
    # return Subsidy.from_dict(response)


@service.exceptions.exceptionHTTPencode
@service.auth.authenticate
def subsidies_post(body):  # noqa: E501
    """Create a new subsidy

    When creating a new subsidy, the following steps are carried out:  1. A new bank account is created under the configured bank profile  2. The subsidy amount is transferred from the indicated &#x60;master&#x60; to the new account  3. A share request is sent to the recipient   For these reasons, the following fields are required in the body:  * &#x60;master.id&#x60; or &#x60;master.iban&#x60; (the master must exist in the database)  * &#x60;recipient.id&#x60; or &#x60;recipient.phone_number&#x60; (the recipient must exist in the database)  * &#x60;amount&#x60;   The remaining fields will be created by the server. Note that &#x60;start_date&#x60; and &#x60;end_date&#x60; are not yet implemented and so will be ignored.   If the citizen has a bank profile at a supported bank and the share request was successfully sent, the &#x60;status&#x60; will come back as PENDING_ACCEPT. Otherwise, the &#x60;status&#x60; will come back as PENDING_ACCOUNT. The system will periodically attempt to resend the share request in case the citizen has created a bank profile. # noqa: E501

    :param body: The subsidy to create
    :type body: dict | bytes

    :rtype: Subsidy
    """
    if connexion.request.is_json:
        body = SubsidyBase.from_dict(connexion.request.get_json())  # noqa: E501

    response = service.subsidies.create(body.to_dict())
    return Subsidy.from_dict(response)
