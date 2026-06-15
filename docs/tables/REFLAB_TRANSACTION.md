# REFLAB_TRANSACTION

> This table contains transaction information for reference labs. Only transactions for reference labs are in this table, and only transactions with type set as charge (column TRAN_TYPE in table CLARITY_TDL_TRAN). These are based on the service area of the transaction which will have the billing system set to reference lab billing (column BILLING_SYSTEM_C in table CLARITY_SA).

**Primary key:** `TX_ID`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the transaction. |
| 2 | `TEST_ID_TEST_NAME` | VARCHAR |  | The name of the test record. |
| 3 | `LAB_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |
| 4 | `RL_RQG_ID` | NUMERIC |  | The unique ID of the requisition grouper for this transaction. |
| 5 | `RL_SUBMITTER_ID` | NUMERIC |  | The unique ID of the submitter for this transaction. |
| 6 | `RL_SUBMITTER_ID_RECORD_NAME` | VARCHAR |  | The name of the submitter record. |
| 7 | `RL_REQUISITION_ID` | NUMERIC |  | The unique ID of the Requisition for this transaction. |
| 8 | `RL_SPECIMEN_ID` | VARCHAR |  | The unique ID of the specimen for this transaction. |
| 9 | `RL_SPECIMEN_LINE` | INTEGER |  | The specimen line of the specimen this transaction belongs to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

