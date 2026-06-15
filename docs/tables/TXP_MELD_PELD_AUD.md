# TXP_MELD_PELD_AUD

> The audit trail for the Model for End-Stage Liver Disease (MELD), Pediatric End-Stage Liver Disease (PELD), and liver status of the patient.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MELD_AUDIT` | INTEGER |  | Stores the audit information for Model for End-Stage Liver Disease (MELD) values for the transplant episode. |
| 4 | `PELD_AUDIT` | INTEGER |  | Stores the audit information for Pediatric Model for End-Stage Liver Disease (PELD) values for the transplant episode. |
| 5 | `MELD_DATE_AUDIT_DT` | DATETIME |  | Stores the audit information for the Model for End-Stage Liver Disease (MELD) dates for the transplant episode. |
| 6 | `PELD_DATE_AUDIT_DT` | DATETIME |  | Stores the audit information for Pediatric Model for End-Stage Liver Disease (PELD) dates for the transplant episode. |
| 7 | `MELDPELD_OTHR_AUDIT` | VARCHAR |  | Stores the audit information for the Model for End-Stage Liver Disease (MELD), Pediatric Model for End-Stage Liver Disease (PELD), and liver status free-text exceptions for the transplant episode. |
| 8 | `LIVER_ST_AUDIT_C_NAME` | VARCHAR |  | Stores the audit trail information for the liver status for the transplant episode. |
| 9 | `MELDPELD_UPD_USR_ID` | VARCHAR |  | Stores the user responsible for the corresponding audit event for the transplant episode. |
| 10 | `MELDPELD_UPD_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `MELD_PELD_UPD_INST_DTTM` | DATETIME (UTC) |  | The instant the corresponding audit event occurred for the transplant episode. |
| 12 | `MELDPELD_AUD_EVNT_C_NAME` | VARCHAR |  | Stores the type of audit event (add, edit, or remove) that took place for the transplant episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

