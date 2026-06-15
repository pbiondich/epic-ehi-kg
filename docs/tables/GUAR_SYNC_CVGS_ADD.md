# GUAR_SYNC_CVGS_ADD

> The GUAR_SYNC_CVGS_ADD table contains coverage records that were added to guarantor account records as a result of guarantor syncing.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the guarantor account record for this row. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `GUAR_SYNC_ADDCVG_ID` | NUMERIC |  | List of coverage records that have been added to this guarantor account at one time as a result of guarantor account syncing. Once a coverage record has been added to a guarantor account by guarantor account syncing and then a user manually removes that coverage from the guarantor account, this item keeps track of the coverage record so that the coverage record is not added to the guarantor account again by guarantor account syncing. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

