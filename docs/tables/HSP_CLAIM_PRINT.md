# HSP_CLAIM_PRINT

> This table contains claim print record information for claims associated with a given hospital account or liability bucket.

**Primary key:** `CLAIM_PRINT_ID`, `CONTACT_DATE_REAL`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | Stores the claim record ID associated with a single hospital account or liability bucket. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | The contact date for the creation of the record in internal format. (There is only one contact date per CLP record.) |
| 3 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | The ID of the hospital account with which this claim record is associated. |
| 4 | `CM_PHY_OWN_ID` | VARCHAR |  | ID of the physical deployment owner for this record. Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

