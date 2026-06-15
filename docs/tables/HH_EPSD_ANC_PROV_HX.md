# HH_EPSD_ANC_PROV_HX

> Contains audit information on the history of the Ancillary Providers.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `ANC_PROV_COMMENT_HX` | VARCHAR |  | History of the comments left about or for Ancillary Providers. |
| 5 | `EDIT_USER_ID` | VARCHAR |  | History of the user ID who entered the data about the Ancillary Providers. |
| 6 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `EDIT_USER_DTTM` | DATETIME (UTC) |  | History of the instant the Ancillary Providers' data was edited. |
| 8 | `EDIT_LINE` | INTEGER |  | History of the line number of the Ancillary Provider whose data was edited. This is the line number found in column LINE of HH_EPSD_ANC_PROV. |
| 9 | `ANC_PROV_REL_C_NAME` | VARCHAR | org | History of the relationship to the patient for Ancillary Providers. |
| 10 | `START_DATE` | DATETIME |  | History of the start dates for Ancillary Providers. |
| 11 | `END_DATE` | DATETIME |  | History of the end dates for Ancillary Providers. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

