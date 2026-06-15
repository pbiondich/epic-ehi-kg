# CUST_SERVICE_TRANS_PROC

> The CUST_SERVICE_TRANS_PROC table contains procedure-related information collected for a transfer patient in both free text and coded form.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique identifier for the customer service communication. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TRANS_PROC_TEXT` | VARCHAR |  | Recent or anticipated procedures for the transfer patient entered using free text. |
| 4 | `TRANS_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

