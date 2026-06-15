# AUT_PROC_MODS

> This table contains information about the procedure modifiers associated with each procedure in AUT_PROC_DETAILS. It extracts the related multiple response Procedure Modifiers item. Each row in this table relates to a parent row in AUT_PROC_DETAILS. Join to it using the AUTH_ID columns and AUT_PROC_DETAILS.LINE = GROUP_LINE.

**Primary key:** `AUTH_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_ID` | NUMERIC | PK FK→ | The authorization ID for the authorization record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `PROC_MOD_ID` | VARCHAR |  | Modifier which applies to the procedure being authorized. Modifiers are extracted to the CLARITY_MOD table. |
| 5 | `PROC_MOD_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_ID` | [AUTHORIZATIONS](AUTHORIZATIONS.md) | overflow_master | medium |

