# AUT_PROC_MODS_HX

> This table contains information about the audit history of procedure modifiers. It extracts the related multiple response Authorization History - Procedure Modifiers (I AUT 1462) item. The current procedure modifier data is in AUT_PROC_MODS.

**Primary key:** `AUTH_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the authorization record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `PROC_MOD_ID` | VARCHAR |  | Audits changes made to the modifiers of an authorization's procedure. Modifiers are extracted to the CLARITY_MOD table. |
| 5 | `PROC_MOD_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_ID` | [AUTHORIZATIONS](AUTHORIZATIONS.md) | overflow_master | medium |

