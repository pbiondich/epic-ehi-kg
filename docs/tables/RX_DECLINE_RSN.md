# RX_DECLINE_RSN

> This table contains a list of decline reasons documented on a pharmacy enrollment.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RXDECLINE_RSN_C_NAME` | VARCHAR | org | The category number for the current reasons why the patient was declined from the program (or declined to participate in the program). This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

