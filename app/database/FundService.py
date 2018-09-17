
class FundService:
    def __init__(self, models):
        self.models = models
        self.INEXISTENT_MASTER_BOVESPA_CODE = 'INEXISTENT_MASTER_BOVESPA_CODE'
    
    def master_bovespa_code_exists(self):
        return True

    def validate_insert_data(self,
                             fund_bovespa_code_entry,
                             master_bovespa_code_entry,
                             fund_name_entry,
                             description_entry):
        return (isinstance(fund_bovespa_code_entry, int) and 
                isinstance(master_bovespa_code_entry, int))

    def insert_fund(self,
                    fund_bovespa_code_entry,
                    master_bovespa_code_entry,
                    fund_name_entry,
                    description_entry):

        sqlQuery =  \
            'INSERT INTO TB_FUNDS (BOVESPA_CODE, MASTER_BOVESPA_CODE, FUND_NAME, DESCRIPTION) VALUES ({}, {}, {}, {})'.format(
                fund_bovespa_code_entry,
                master_bovespa_code_entry,
                "'{}'".format(fund_name_entry),
                "'{}'".format(description_entry),
            )
        
        print(sqlQuery)
