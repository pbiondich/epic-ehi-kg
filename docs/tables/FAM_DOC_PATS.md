# FAM_DOC_PATS

> This table stores data for patients linked to a family document.

**Primary key:** `FAM_DOC_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FAM_DOC_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the family document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LINKED_PAT_ID` | VARCHAR | FK→ | Patient for whom the family document is for. |
| 4 | `LINKED_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The contact serial number of the encounter for the patient on which to store family document data. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FAM_DOC_ID` | [FAM_DOC](FAM_DOC.md) | sole_pk | high |
| `LINKED_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `LINKED_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

