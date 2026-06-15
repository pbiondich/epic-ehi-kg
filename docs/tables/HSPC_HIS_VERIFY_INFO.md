# HSPC_HIS_VERIFY_INFO

> This table contains information about the verification user (Hospice Item Set Item Z0500A) and the verification date and time (Hospice Item Set Item Z0500B).

**Primary key:** `DATASET_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DATASET_ID` | NUMERIC | PK shared | The unique identifier for the data set record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HIS_SIGNED_USER_ID` | VARCHAR |  | This item stores the users who signed and verified completion of the Hospice Item Set. |
| 4 | `HIS_SIGNED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `HIS_SIGNED_INSTANT_DTTM` | DATETIME (UTC) |  | This item stores the instant that the Hospice Item Set was signed and verified as complete. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

