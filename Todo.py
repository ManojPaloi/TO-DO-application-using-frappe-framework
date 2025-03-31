import frappe

def create_doctype():
    if not frappe.db.exists("DocType", "Task"):
        doc = frappe.get_doc({
            "doctype": "DocType",
            "name": "Task",
            "module": "ToDo App",
            "custom": 1,
            "fields": [
                {"fieldname": "title", "fieldtype": "Data", "label": "Title", "reqd": 1},
                {"fieldname": "description", "fieldtype": "Text", "label": "Description"},
                {"fieldname": "status", "fieldtype": "Select", "label": "Status", "options": "To-Do\nIn Progress\nDone"},
                {"fieldname": "due_date", "fieldtype": "Date", "label": "Due Date"},
                {"fieldname": "priority", "fieldtype": "Select", "label": "Priority", "options": "Low\nMedium\nHigh"}
            ],
            "permissions": [
                {"role": "System Manager", "read": 1, "write": 1, "create": 1, "delete": 1}
            ]
        })
        doc.insert()
        frappe.db.commit()


@frappe.whitelist()
def get_task_summary():
    return {
        "To-Do": frappe.db.count("Task", {"status": "To-Do"}),
        "In Progress": frappe.db.count("Task", {"status": "In Progress"}),
        "Done": frappe.db.count("Task", {"status": "Done"})
    }
