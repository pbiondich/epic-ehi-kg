# ORD_NLP_STATUS

> This table contains the NLP status of the order for the corresponding model.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NLP_MODEL_TYPE_C_NAME` | VARCHAR |  | Stores the NLP model type used as an index for items in this table. |
| 4 | `RIS_NLP_STATUS_C_NAME` | VARCHAR |  | Stores the NLP evaluation status of the order for the corresponding model. |
| 5 | `NLP_VERIFYING_USER_ID` | VARCHAR |  | The user (EMP) that most recently verified this order's NLP-extracted results for this row's NLP model. |
| 6 | `NLP_VERIFYING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `NLP_VERIFIED_DTTM` | DATETIME (UTC) |  | The instant that the user (EMP) in I ORD 52387 for this row performed the verifying action. |
| 8 | `SLOWEST_NLP_MODIFY_TYPE_C_NAME` | VARCHAR |  | Stores the way that an NLP model was modified. If it was modified multiple ways the slowest method is stored. |
| 9 | `NLP_OUTCOME_C_NAME` | VARCHAR |  | The outcome of a model generated result. Used to measure overall accuracy of NLP models. |
| 10 | `NLP_MODEL_VERSION` | INTEGER |  | The version of the NLP model that processed the order. |
| 11 | `NLP_MODEL_REVISION` | INTEGER |  | The Nebula code revision of the NLP model that processed the order. |
| 12 | `NLP_SERVER_REVISION` | INTEGER |  | The server code revision of the NLP model that processed the order. |
| 13 | `NLP_VERIFIED_LOC_DTTM` | DATETIME (Local) |  | The local instant that the user (EMP) in I ORD 52387 for this row performed the verifying action. |
| 14 | `SENT_TO_CHARACTERISTICS_YN` | VARCHAR |  | This item stores information on whether or not a study that was sent to the AIEF findings module was also sent to the characteristics extraction module. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

