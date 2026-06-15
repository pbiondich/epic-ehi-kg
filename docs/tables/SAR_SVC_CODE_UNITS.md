# SAR_SVC_CODE_UNITS

> The number of units for the service authorization request (SAR) service code. This table extracts the related multiple response SAR Service Code Units (I RFL 234) item. Tables SAR_SVC_CODES and SAR_SVC_CODE_MODS contain additional information related to each row in this table. Join to them using the primary key columns in each table. Additionally, each row in these table relates to a parent row in the SAR_SVC_LN_INFO table. Join to it using the REFERRAL_ID columns and SAR_SVC_LN_INFO.LINE = GROUP_LINE from these tables.

**Primary key:** `REFERRAL_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `SAR_SVC_CODE_UNITS` | INTEGER |  | The number of units for the service in related column SAR_SVC_CODE__SAR_CODE. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

