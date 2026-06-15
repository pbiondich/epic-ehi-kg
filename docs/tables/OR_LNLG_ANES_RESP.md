# OR_LNLG_ANES_RESP

> Stores the responsible anesthesia staff information.

**Primary key:** `RECORD_ID`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `ANES_STAFF_TYPE_C_NAME` | VARCHAR | org | The anesthesia staff type category number for the responsible staff member. |
| 3 | `ANES_STAFF_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

