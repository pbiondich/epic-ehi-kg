# FLOWSHEET_META_STRICT

> Third-party metadata (e.g. from Apple's HealthKit) is split across three tables. This table holds category values used to represent keys from each key-value pair. The corresponding key names are held on table FLOWSHEET_META_LOOSE, and the values are held on FLOWSHEET_META_VAL. Reporting on this metadata can be more easily accomplished by joining these tables on primary key (FSD_ID, GROUP_LINE, VALUE_LINE).

**Primary key:** `FSD_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FSD_ID` | VARCHAR | PK FK→ | The unique identifier for the Flowsheets data record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `THRDPRTY_META_KEY_C_NAME` | VARCHAR | org | Within a line, each non-null position represents a key in a dictionary of third-party metadata attached to the Flowsheets value with the corresponding line number. Keys are represented with category values, allowing them to be more easily programmed against and indexed. If a key does not have a representative category value, it is left null in this item. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FSD_ID` | [IP_FLWSHT_REC](IP_FLWSHT_REC.md) | sole_pk | high |

