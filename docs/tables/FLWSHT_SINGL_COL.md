# FLWSHT_SINGL_COL

> This table contains data on the last instant of data being filed to a single column template in Doc Flowsheets.

**Primary key:** `FSD_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FSD_ID` | VARCHAR | PK FK→ | The unique identifier for the record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SINGLE_FLO_ID` | VARCHAR |  | This item stores the Flowsheet ID of a row that has been documented on a single column template, with Single Column Recorded Instant - Single Rcrd (FSD 5005) holding the most recent time recorded for this row. |
| 4 | `SINGLE_RCRD_IN_DTTM` | DATETIME (UTC) |  | This item stores the most recent time recorded for a Flowsheet ID in the Single Column FLO ID (related item FSD 5000) that was documented on a single column template. The time is saved in the UTC (Coordinated Universal Time) time zone. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FSD_ID` | [IP_FLWSHT_REC](IP_FLWSHT_REC.md) | sole_pk | high |

