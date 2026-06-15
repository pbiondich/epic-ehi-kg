# OR_LNLG_ANEST_INFO

> This table contains the Anesthesia information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `ANES_INFO_CPT2_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 3 | `ANES_INFO_DIAG2_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `ANES_INFO_MOD2_C_NAME` | VARCHAR | org | The second CPT code modifier documented by anesthesia. |
| 5 | `ANES_INFO_MOD3_C_NAME` | VARCHAR |  | The third CPT code modifier documented by anesthesia. |
| 6 | `ANES_INFO_QTY` | INTEGER |  | The anesthesia information quantity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

