# PAT_REL_EMAIL_ADDR

> This table contains information about the patient contacts' email addresses. The records included in this table are Patient Relationships (RLA) records.

**Primary key:** `PAT_RELATIONSHIP_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_RELATIONSHIP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient contact record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PRIMARY_EMAIL_YN` | VARCHAR |  | Indicates whether the email address for this patient contact is the primary email address |
| 4 | `EMAIL_ADDRESS` | VARCHAR |  | Patient contact's email address. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_RELATIONSHIP_ID` | [PAT_RELATIONSHIP_LIST](PAT_RELATIONSHIP_LIST.md) | sole_pk | high |

