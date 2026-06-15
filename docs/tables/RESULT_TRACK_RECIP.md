# RESULT_TRACK_RECIP

> Details of communication actions taken to deliver critical results to recipients and confirm receipt.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record for this row. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RSLT_TRK_RECIP_ST_C_NAME` | VARCHAR |  | per-recipient status for result tracking |
| 4 | `RSLT_TRK_RECIP_NAME` | VARCHAR |  | name of recipient (needed for ad hoc) |
| 5 | `RSLT_TRK_RCP_SER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `RSLT_TRK_RCP_EMP_ID` | VARCHAR |  | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| 7 | `RSLT_TRK_RCP_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `RSLT_TRK_RCP_POL_ID` | NUMERIC |  | The unique ID associated with the reading pool record for this row. |
| 9 | `RSLT_TRK_RCP_POL_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 10 | `RSLT_TRK_RECIP_ADHO` | VARCHAR |  | ad hoc string for result tracking (see item 52016) |
| 11 | `RSLT_TRK_RECIP_INST` | DATETIME (Local) |  | instant when a followup action was performed |
| 12 | `RSLT_TRK_RECIP_ME_C_NAME` | VARCHAR |  | method used to contact this recipient |
| 13 | `RSLT_TRK_RECIP_COMT` | VARCHAR |  | user-entered free text comment about followup with recipient |
| 14 | `RSLT_TRK_RCP_USR_ID` | VARCHAR |  | the user that performed the followup action from within epic |
| 15 | `RSLT_TRK_RCP_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 16 | `RSLTTRK_CMT_NOTE_ID` | VARCHAR |  | Result Tracking Recipient comment networked to HNO record |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

