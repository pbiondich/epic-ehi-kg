# FLOWSHEET_METAEDIT_VAL

> Historical third-party metadata (e.g. from Apple's HealthKit) is split across three tables. This table holds values from each key-value pair. The key names are held on table FLOWSHEET_METAEDIT_LOOSE, and key category values, for keys that have been assigned category values, are held on FLOWSHEET_METAEDIT_STRICT. Reporting on this metadata can be more easily accomplished by joining these tables on primary key (FSD_ID, GROUP_LINE, VALUE_LINE).

**Primary key:** `FSD_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FSD_ID` | VARCHAR | PK FK→ | The unique identifier for the Flowsheets data record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `EDITD_3P_META_VAL` | VARCHAR |  | Within a line, each position represents a value in a dictionary of third-party metadata attached to the historical Flowsheets value with the corresponding line number. The same line/position for the edited third party metadata key (I FSD 2320) corresponds to the key name and (if the particular key is recognized by Epic) on the edited third party metadata value (I FSD 2310) corresponds to the category-value representation of the key. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FSD_ID` | [IP_FLWSHT_REC](IP_FLWSHT_REC.md) | sole_pk | high |

