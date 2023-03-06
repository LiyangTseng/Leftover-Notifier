'''
Manually handle credentials verifications regarding gspread since Render uses Github project
'''
import os

def load_credentials():
    credentials = {}

    credentials['type'] = os.getenv('type', None)
    credentials['project_id'] = os.getenv('project_id', None)
    credentials['private_key_id'] = os.getenv('private_key_id', None)
    credentials['private_key'] = os.getenv('private_key', None).replace('\\n', '\n')
    credentials['client_email'] = os.getenv('client_email', None)
    credentials['client_id'] = os.getenv('client_id', None)
    credentials['auth_uri'] = os.getenv('auth_uri', None)
    credentials['token_uri'] = os.getenv('token_uri', None)
    credentials['auth_provider_x509_cert_url'] = os.getenv('auth_provider_x509_cert_url', None)
    credentials['client_x509_cert_url'] = os.getenv('client_x509_cert_url', None)

    return credentials