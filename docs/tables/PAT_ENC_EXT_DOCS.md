# PAT_ENC_EXT_DOCS

> This table gives information about whether external systems contain documents for a given encounter that Epic may or may not know about.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `CONTACT_DATE` | DATETIME |  | This column is the contact date that the external documents are associated with. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | This column is the ID of the contact owner in Care Everywhere. |
| 5 | `DOC_IN_EXT_SYS_YN` | VARCHAR |  | This item indicates whether there is data in an external system for this encounter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

