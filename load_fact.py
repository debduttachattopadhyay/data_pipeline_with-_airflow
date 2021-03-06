from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'
    sql_insert="""
            insert into {fact_table}
            {source_tbl_query}
            """

    @apply_defaults
    def __init__(self,
                redshift_conn_id="",
                 fact_table="",
                 source_tbl_query="",
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshif_conn_id = redshift_conn_id
        self.source_tbl_query=source_tbl_query
        self.fact_table=fact_table

    def execute(self, context):
        self.log.info('LoadFactOperator not implemented yet')
        aws_hook=AwsHook(self.aws_credentials_id)
        aws_credentials=aws_hook.get_credentials()
        redshift_hook=PostgresHook(postgres_conn_id=self.redshift_conn_id)

        
        self.log.info("Data insert from Staging tables to Fact Table")
        sql_stmt=LoadFactOperator.sql_insert.format (self.fact_table
                                                     ,self.source_tbl_query
                                                     )
        redshift.run(sql_stmt)