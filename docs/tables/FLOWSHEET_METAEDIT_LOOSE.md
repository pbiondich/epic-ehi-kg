# FLOWSHEET_METAEDIT_LOOSE

> Historical third-party metadata (e.g. from Apple's HealthKit) is split across three tables. This table holds key names from each key-value pair. The key category values, for keys that have been assigned category values, are held on table FLOWSHEET_METAEDIT_STRICT, and the values are held on FLOWSHEET_METAEDIT_VAL. Reporting on this metadata can be more easily accomplished by joining these tables on primary key (FSD_ID, GROUP_LINE, VALUE_LINE).

**Primary key:** `FSD_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FSD_ID` | VARCHAR | PK FK→ | The unique identifier for the Flowsheets data record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `EDITD_3P_META_KEY` | VARCHAR |  | Within a line, each position represents a key in a dictionary of third-party metadata attached to the historical Flowsheets value with the corresponding line number. This item stores the key's full name as a string, and is not intended to be programmed against nor indexed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FSD_ID` | [IP_FLWSHT_REC](IP_FLWSHT_REC.md) | sole_pk | high |

