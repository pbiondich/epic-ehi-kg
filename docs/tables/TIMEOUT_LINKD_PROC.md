# TIMEOUT_LINKD_PROC

> This table stores information about the procedures linked to the timeout.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the timeout record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `LINK_PROC_SURG_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 7 | `LINK_PROC_LAT_C_NAME` | VARCHAR | org | Stores the laterality of the linked procedure. |
| 8 | `LINK_PROC_ORP_ID` | VARCHAR |  | Stores a pointer to the procedure record that is linked to the timeout. |
| 9 | `LINK_PROC_ORP_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 10 | `LINK_PROC_PNL_NUM` | INTEGER |  | Stores the panel number of the linked procedure. |
| 11 | `LINK_PROC_FREE_TEXT` | VARCHAR |  | Stores the free-text name of the linked procedure when the timeout was documented. This prevents later changes in the procedure's free-text name from altering the meaning of the timeout. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

