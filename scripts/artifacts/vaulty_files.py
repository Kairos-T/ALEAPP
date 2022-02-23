import sqlite3

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, is_platform_windows 
from scripts.parse3 import ParseProto

def get_vaulty_files(files_found, report_folder, seeker, wrap_text):

    title = "Vaulty - Files"

    # Media database
    db_filepath = str(files_found[0])
    conn = sqlite3.connect(db_filepath)
    c = conn.cursor()
    sql = """SELECT _id, datetime(Media.datetaken / 1000, 'unixepoch'), datetime(Media.date_modified / 1000, 'unixepoch'), path, _data FROM Media"""
    c.execute(sql)
    results = c.fetchall()
    conn.close()

    # Data results
    data_headers = ('ID', 'Created', 'Added to Vault', 'Original Filepath', 'Vault Filepath')
    data_list = results
    
    # Reporting
    report = ArtifactHtmlReport(title)
    report.start_artifact_report(report_folder, title)
    report.add_script()
    report.write_artifact_data_table(data_headers, data_list, db_filepath, html_escape=False)
    report.end_artifact_report()
    
    tsv(report_folder, data_headers, data_list, title)
