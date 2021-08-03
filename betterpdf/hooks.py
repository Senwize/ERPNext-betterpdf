from . import __version__ as app_version

app_name = "betterpdf"
app_title = "Better PDF"
app_publisher = "Senwize B.V."
app_description = "Better PDF generator"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "timvanosch@senwize.com"
app_license = "MIT"

before_install = "betterpdf.setup.install.before_install"
after_install = "betterpdf.setup.install.after_install"

override_whitelisted_methods = {
    "frappe.utils.print_format.download_pdf": "betterpdf.utils.print_format.download_pdf",
    "frappe.utils.print_format.report_to_pdf": "betterpdf.utils.print_format.report_to_pdf",
}

# User Data Protection
# --------------------

user_data_fields = [
    {
        "doctype": "{doctype_1}",
        "filter_by": "{filter_by}",
        "redact_fields": ["{field_1}", "{field_2}"],
        "partial": 1,
    },
    {
        "doctype": "{doctype_2}",
        "filter_by": "{filter_by}",
        "partial": 1,
    },
    {
        "doctype": "{doctype_3}",
        "strict": False,
    },
    {
        "doctype": "{doctype_4}"
    }
]
