from django.conf import settings

from gsheets.client import GsheetsClient

def get_client_from_settings():

    return GsheetsClient(settings.SERVICE_ACCOUNT)