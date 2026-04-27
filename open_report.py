import os
import webbrowser

report_path = "/home/zhu/projects/Teedy/docs-core/target/site/jacoco/index.html"
if os.path.exists(report_path):
    print(f"Coverage report is successfully generated at: {report_path}")
