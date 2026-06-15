# MYC_MESG_SEX_PRTNR

> This table contains patient answers to the "sexual partners" question submitted in a history questionnaire.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The unique identifier for the message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SEX_QUESN_PTNRS_C_NAME` | VARCHAR | org | The patient's response to the sexual activity partners question. |
| 4 | `SEX_QUESN_PTNRS_IDX` | INTEGER |  | The sexual partners question index item. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

