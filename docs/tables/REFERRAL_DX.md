# REFERRAL_DX

> The REFERRAL_DX table contains diagnosis information stored with referrals.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number of the diagnosis associated with the referral. For example, if a referral has two associated diagnoses, the first diagnosis will have a line value of 1, while the second diagnosis will have a line value of 2. |
| 3 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `DX_TEXT` | VARCHAR |  | Free text associated with each additional diagnosis (I RFL 1000). |
| 5 | `DX_CODE_TYPE_C_NAME` | VARCHAR | org | Stores the code type of the additional diagnosis |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

