class AneelDataProcessing:
    def __init__(self):
        pass

    def process_updated_data(self, filename):
        from pyspark.sql import SparkSession
        spark = SparkSession.builder.appName('SparkSession').getOrCreate()
        try:
            df = (spark
                  .read
                  .options(header='True',
                           inferSchema='True',
                           delimiter=';')
                  .csv()
                  )

            #TODO: Transformations to DF

            # Writing to datawarehouse using Parquet Files
            (df
             .write
             .mode("overwrite")
             .partitionBy("AnmPeriodoReferencia")
             .parquet("../datawarehouse_files/datawarehouse.parquet")
             )
            return True
        except Exception as e:
            raise Exception(e)


