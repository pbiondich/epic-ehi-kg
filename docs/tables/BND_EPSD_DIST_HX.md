# BND_EPSD_DIST_HX

> This table stores the history of bundled payment distributions for the bundled episode.

**Primary key:** `EPISODE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the bundled episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BILL_DIST_HX_SOURCE_C_NAME` | VARCHAR |  | Stores the source of the bundled payment distribution |
| 4 | `BILL_DIST_HX_USER_ID` | VARCHAR |  | Stores the associated user who performed the bundled payment distribution |
| 5 | `BILL_DIST_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `BILL_DIST_HX_INST_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant a user performed the bundled payment distribution |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

