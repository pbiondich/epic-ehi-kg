# ARPB_TX_AGCY_HX

> Stores the history of the changes in the current collection agency assigned to a charge. (Not populated for agency account workqueue based assignment).

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | This line number identifies the sequence of changes in the assigned agency for a transaction. |
| 3 | `AGENCY_ID` | NUMERIC | FK→ | Stores the collection agency to which a charge is assigned. |
| 4 | `AGENCY_ID_COLL_AGENCY_NAME` | VARCHAR |  | The name of the collection agency. |
| 5 | `SENT_DTTM` | DATETIME (UTC) |  | Stores the instant a charge was sent to a collection agency. This value is stored as a UTC instant. |
| 6 | `RETURN_DTTM` | DATETIME (UTC) |  | Stores the instant a charge returned from its assigned collection agency. This value is stored as a UTC instant. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AGENCY_ID` | [CLARITY_AGENCY](CLARITY_AGENCY.md) | sole_pk | high |

