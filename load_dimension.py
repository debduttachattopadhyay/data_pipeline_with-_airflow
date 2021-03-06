from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'
    sql_insert="""
            insert into {dim_table}
            {source_tbl_query}
            """
    
    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 dim_table="",
                 source_tbl_query="",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshif_conn_id = redshift_conn_id
        self.dim_table=dim_table
        self.source_tbl_query=source_tbl_query

    def execute(self, context):
        self.log.info('LoadDimensionOperator not implemented yet')
        redshift_hook=PostgresHook(postgres_conn_id=self.redshift_conn_id)

        
        self.log.info("Data insert from Staging tables to Dim Table")
        sql_stmt_dim=LoadFactOperator.sql_insert.format (self.dim_table,
                                                        self.source_tbl_query)
        
        redshift.run(sql_stmt_dim)