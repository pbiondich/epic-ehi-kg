# AI_INTRCT_CONTACT_INFO

> Tracks overtime single response LLM items.

**Primary key:** `AI_INTRCT_ID`, `CONTACT_DATE_REAL`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AI_INTRCT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the interaction record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `AI_INTRCT_CSN_ID` | NUMERIC |  | The contact serial number (CSN) of the contact. |
| 4 | `AI_INTRCT_SESS_TYPE_C_NAME` | VARCHAR | org | Indicates the type of workflow that the agent(s) are assisting with. |
| 5 | `DISPLAY_NAME` | VARCHAR |  | Stores a name to show for the record |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AI_INTRCT_ID` | [AI_INTRCT_INFO](AI_INTRCT_INFO.md) | sole_pk | high |

