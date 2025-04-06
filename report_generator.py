from jinja2 import Environment, FileSystemLoader
import pdfkit

def generate_html_report(findings):
    env = Environment(loader=FileSystemLoader('templates/'))
    template = env.get_template('report_template.html')
    return template.render(findings=findings)

def generate_pdf(html_content):
    options = {'enable-local-file-access': None}
    pdfkit.from_string(html_content, 'security_report.pdf', options=options)