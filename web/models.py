import toml
import peewee as PW


# Load Configuration
config = toml.load("../.config.toml")
db_config = config["db"]

db = PW.PostgresqlDatabase(
    db_config["db_name"],
    user=db_config["username"],
    password=db_config["password"],
    host=db_config["host"],
    port=db_config["port"],
)


class Job(PW.Model):
    class Meta:
        database = db
        table_name = "duckdb_jobs"

    job_id = PW.BigAutoField()
    sql_query = PW.TextField(null=False)
    status = PW.CharField(null=False, max_length=20)
    source_type = PW.CharField(null=False, max_length=20)
    output_file_path = PW.TextField(null=True)
    created_on = PW.DateTimeField(null=False)
    updated_on = PW.DateTimeField(null=True)


db.create_tables([Job])
