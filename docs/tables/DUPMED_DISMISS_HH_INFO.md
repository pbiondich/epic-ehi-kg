# DUPMED_DISMISS_HH_INFO

> This table stores data related to duplicate medications on the Home Health Remote Client.

**Primary key:** `ORDER_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `DUPMED_DISMISS_EMP_ID` | VARCHAR |  | This item stores the user who dismissed the duplicate medication warning that the Remote Client showed after the medication was added. |
| 3 | `DUPMED_DISMISS_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 4 | `DUPMED_DISMISS_CSN` | NUMERIC |  | This item stores the patient contact serial number (CSN) associated with the update which dismissed the duplicate warning for this order on the Remote Client. |
| 5 | `DUPMED_DISMISS_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant when the Remote Client was synchronized after the duplicate warning for this order was dismissed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

