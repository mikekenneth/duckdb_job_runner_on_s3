import streamlit as st
from datetime import datetime
from models import Job


with st.form("DuckDb as an Engine"):
    st.write("# Enter the Query to be executed")
    sql_query = st.text_area(label="SQL Query")

    sql_source_type = st.selectbox(label="Query Source Type", options=["minio_s3", "aws_s3"])

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        job = Job.create(sql_query=sql_query, status="NEW", source_type=sql_source_type, created_on=datetime.now())
        job.save()
        st.success(f"Successfully created Job - {job.job_id}")
