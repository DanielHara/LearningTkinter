
class ClientService:
    def __init__(self, models):
        self.models = models
        self.INVALID_BOVESPA_CODE = 'INVALID BOVESPA CODE'
        self.INVALID_IS_MASTER_ACCOUNT = 'INVALID IS_MASTER_ACCOUNT'
    
    def validate_insert_data(self, bovespa_code, name, description, is_master_account):
        return (bovespa_code.isdigit() and isinstance(is_master_account, bool))

    def insert_client(self, bovespa_code, name, description, is_master_account):
        sqlQuery =  \
            'INSERT INTO TB_CLIENTS (BOVESPA_CODE, NAME, DESCRIPTION, IS_MASTER_ACCOUNT) VALUES ({}, {}, {}, {})'.format(
                bovespa_code,
                "'{}'".format(name),
                "'{}'".format(description),
                is_master_account
            )
        
        print(sqlQuery)
