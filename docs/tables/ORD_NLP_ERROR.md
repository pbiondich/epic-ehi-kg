# ORD_NLP_ERROR

> This table contains information about NLP error codes and error messages for imaging orders that failed processing by Nebula.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NLP_ERROR_CODE_C_NAME` | VARCHAR |  | The AIServices error code or other Radiant specific error code that was returned for this order if it failed being processed by the AIEF Nebula model. |
| 4 | `NLP_ERROR_MESSAGE` | VARCHAR |  | The specific error message that AIServices returned or Radiant specific error messages for when an order was sent to Nebula for processing but failed for one reason or another. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

