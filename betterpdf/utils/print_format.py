import frappe
from frappe import _
from frappe.utils import scrub_urls

import os
import io
import subprocess
import time
import six

from frappe.utils.pdf import PdfFileReader, PdfFileWriter, cleanup, prepare_options, get_file_data_from_writer, PDF_CONTENT_ERRORS
from frappe.core.doctype.access_log.access_log import make_access_log

app_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../")


def get_pdf(html, options=None, output=None):
  html = scrub_urls(html)
  html, options = prepare_options(html, options)

  filedata = ''

  try:
    # Set filename property to false, so no file is actually created
    runproc = subprocess.Popen(
        [f'{app_path}/html2pdf/html2pdf.js', '-', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    # Send HTML
    runproc.stdin.write(bytes(html, 'utf-8'))
    runproc.stdin.close()
    # Wait for finish with a 5 second timeout
    timeout_start = time.time()
    while runproc.returncode is None:
      if time.time() - timeout_start > 5:
        frappe.throw("PDF generation timed out")
        raise
      runproc.poll()

    if runproc.returncode > 0:
      frappe.throw("PDF generation failed")
      raise

    filedata = runproc.stdout.read()

    # https://pythonhosted.org/PyPDF2/PdfFileReader.html
    # create in-memory binary streams from filedata and create a PdfFileReader object
    reader = PdfFileReader(io.BytesIO(filedata))
  except OSError as e:
    if any([error in str(e) for error in PDF_CONTENT_ERRORS]):
      if not filedata:
        frappe.throw(_("PDF generation failed because of broken image links"))

      # allow pdfs with missing images if file got created
      if output:  # output is a PdfFileWriter object
        output.appendPagesFromReader(reader)
    else:
      raise
  finally:
    cleanup(options)

  if "password" in options:
    password = options["password"]
    if six.PY2:
      password = frappe.safe_encode(password)

  if output:
    output.appendPagesFromReader(reader)
    return output

  writer = PdfFileWriter()
  writer.appendPagesFromReader(reader)

  if "password" in options:
    writer.encrypt(password)

  filedata = get_file_data_from_writer(writer)

  return filedata


@frappe.whitelist()
def download_pdf(doctype, name, format=None, doc=None, no_letterhead=0):
  html = frappe.get_print(doctype, name, format, doc=doc,
                          no_letterhead=no_letterhead)
  frappe.local.response.filename = "{name}.pdf".format(
      name=name.replace(" ", "-").replace("/", "-"))
  frappe.local.response.filecontent = get_pdf(html)
  frappe.local.response.type = "pdf"


@frappe.whitelist()
def report_to_pdf(html, orientation="Landscape"):
  make_access_log(file_type='PDF', method='PDF', page=html)
  frappe.local.response.filename = "report.pdf"
  frappe.local.response.filecontent = get_pdf(
      html, {"orientation": orientation})
  frappe.local.response.type = "pdf"
