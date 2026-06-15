# RQG_NAME_HISTORY

> This table contains Name History Information for the Requisition Grouper (RQG) source.

**Primary key:** `RQG_GROUPER_ID`, `RQG_NAME_HX_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RQG_GROUPER_ID` | NUMERIC | PK FK→ | This is the primary key for RQG tables and refers to the ID number of the Requisition Grouper source. |
| 2 | `RQG_NAME_HX_LINE` | INTEGER | PK | The Line Count of Name entries. |
| 3 | `RQG_NAME_HX` | VARCHAR |  | Stores the history of the Requsition Grouper (RQG) source name. |
| 4 | `RQG_NAME_HX_DATE` | DATETIME |  | Stores the date of change associated with the Requsition Grouper (RQG) source name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `RQG_GROUPER_ID` | [RQG_DB_MAIN](RQG_DB_MAIN.md) | sole_pk | high |

