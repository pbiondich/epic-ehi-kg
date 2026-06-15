# PAT_REL_PHONE_NUM

> This table contains information about the patient contacts' phone numbers. The records included in this table are Patient Relationships (RLA) records.

**Primary key:** `PAT_RELATIONSHIP_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_RELATIONSHIP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient contact record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PHONE_NUM` | VARCHAR |  | Patient contact's phone number. |
| 4 | `PHONE_NUM_TYPE_C_NAME` | VARCHAR | org | The phone number type category ID for the patient contact's phone number. |
| 5 | `PRIMARY_PHONE_YN` | VARCHAR |  | Indicates whether the phone number for this patient contact is the primary phone number. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_RELATIONSHIP_ID` | [PAT_RELATIONSHIP_LIST](PAT_RELATIONSHIP_LIST.md) | sole_pk | high |

