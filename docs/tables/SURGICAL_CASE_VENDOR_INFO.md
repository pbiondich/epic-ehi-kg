# SURGICAL_CASE_VENDOR_INFO

> This table contains information about implant vendors documented on the surgical case.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VENDOR_NAME_C_NAME` | VARCHAR |  | Implantable device manufacturer associated with the procedure. |
| 4 | `VENDOR_NOTES` | VARCHAR |  | Individualized notes that will be sent to this specific device manufacturer. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

