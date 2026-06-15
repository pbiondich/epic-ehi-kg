# OR_LNLG_ANES_STAFF

> This table contains the Anesthesia Staff information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `ANESTH_STAFF_C_NAME` | VARCHAR | org | The anesthesia staff type. |
| 3 | `ANESTH_STAFF_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `ANESTH_RTLS_OFF_YN` | VARCHAR |  | Whether RTLS tracking has been manually turned off for the anesthesia staff on this case log. |
| 5 | `ANESTH_STAFF_MOD_UTC_DTTM` | DATETIME (UTC) |  | The time of the last modification to the anesthesia staff on this case log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

