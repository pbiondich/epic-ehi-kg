# EOW_LINKED_PATS

> Linked EPT patients for EHI Export.

**Primary key:** `MSG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MSG_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the in basket message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LINKED_PAT_ID` | VARCHAR | FK→ | The list of patients (EPT) that this EOW is associated with for Electronic Health Information (EHI) Export |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `LINKED_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `MSG_ID` | [IB_MESSAGES](IB_MESSAGES.md) | sole_pk | high |

