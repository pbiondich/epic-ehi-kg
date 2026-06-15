# COLL_AGENCY_HX

> This table contains collection agency history information.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COLL_HX_AGENCY_ID` | NUMERIC |  | The ID of the collection agency which is associated with this history information. |
| 4 | `COLL_HX_AGENCY_ID_COLL_AGENCY_NAME` | VARCHAR |  | The name of the collection agency. |
| 5 | `COLL_HX_SUBMIT_DATE` | DATETIME |  | The date when account is submitted to the collection agency. |
| 6 | `COLL_HX_RESOLV_DATE` | DATETIME |  | The date when the agency resolved the submission. |
| 7 | `COLL_HX_RES_TYPE_C_NAME` | VARCHAR |  | The collection history resolution type category number for this history information. |
| 8 | `COLL_HX_SUBMIT_DTTM` | DATETIME (UTC) |  | The UTC instant this transaction was submitted to collections. |
| 9 | `COLL_HX_RESOLV_DTTM` | DATETIME (UTC) |  | The UTC instant this transaction was resolved with collections. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

