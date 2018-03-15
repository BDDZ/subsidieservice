import pymongo

from subsidy_service import bunq

client = pymongo.MongoClient(host=['mongo'], port=27017,
                             document_class=dict, connect=True)

def add(citizen:dict):
    """
    Add a citizen to the subsidy.citizens collection.

    :param citizen: The citizen to be added
    :type citizen: dict
    :return: True if the operation was successful, else False
    """

    db = client.subsidy
    result = db.citizens.insert_one(citizen)

    new_record = db.citizens.find_one(citizen)
    new_record['_id'] = str(new_record['_id'])

    return new_record