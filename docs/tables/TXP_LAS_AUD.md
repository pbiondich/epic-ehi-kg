# TXP_LAS_AUD

> The audit trail for the lung allocation score of a patient.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LAS_AUDIT` | NUMERIC |  | Stores the audit information for the lung allocation score for the transplant episode. |
| 4 | `LAS_DATE_AUDIT_DT` | DATETIME |  | Stores the audit trail information for the lung allocation score dates for the transplant episode. |
| 5 | `LAS_EXCEP_OTH_AUDIT` | VARCHAR |  | Stores the audit trail information for the lung allocation score free-text exceptions for the transplant episode. |
| 6 | `LAS_UPDATE_USER_ID` | VARCHAR |  | Stores the user who made the corresponding update to the lung allocation score for the transplant episode. |
| 7 | `LAS_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `LAS_UPDATE_INSTANT_DTTM` | DATETIME (UTC) |  | The instant the corresponding change to lung allocation score was made for the transplant episode. |
| 9 | `LAS_CHANGE_TYPE_C_NAME` | VARCHAR |  | The type of change that was made to the lung allocation score history. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

