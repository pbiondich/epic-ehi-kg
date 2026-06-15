# CUST_SERVICE_FORMS

> This table contains information about the forms associated to this customer service communication.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the communication record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CRM_FORMS_LIST_FORM_ID` | VARCHAR |  | Holds both filed and unfiled forms attached to the communication. |
| 4 | `CRM_FORMS_LIST_FORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 5 | `CRM_FORMS_FILED_YN` | VARCHAR |  | Indicates whether the form is filed or not. |
| 6 | `FORM_CSN_ID` | NUMERIC |  | This item stores the contact serial number (I LQF 8) of the SmartForms used in this encounter. Additionally, like I NCS 630, this information is passed from the relevant host. If the host does not pass the information, then the SmartForm CSN may not appear in this item. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

