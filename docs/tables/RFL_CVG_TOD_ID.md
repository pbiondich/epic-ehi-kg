# RFL_CVG_TOD_ID

> This table holds the bed day types (TOD) IDs for the related multi Auth-Cert Bed Days Type (I RFL 8501) item.

**Primary key:** `REFERRAL_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique ID of the referral. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated coverage for this referral record. Together with REFERRAL_ID, this forms the foreign key to the REFERRAL_CVG_BED table. |
| 3 | `VALUE_LINE` | INTEGER | PK | Line count of related multi |
| 4 | `AUTH_CERT_TOD_ID` | NUMERIC |  | Coverage Level Bed Day Type |
| 5 | `AUTH_CERT_TOD_ID_BED_DAY_TYPE_NAME` | VARCHAR |  | The name of the bed day type record (i.e. ICU or non-authorized.) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

