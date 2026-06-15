# MYC_MESG_QUESR

> This table stores information on questionnaires that have been attached to web based chart system (WMG) messages.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The unique ID used to identify a web based chart system message record. |
| 2 | `LINE` | INTEGER | PK | The line number used to identify each row of read data associated with an individual web based chart system message record. |
| 3 | `ALLOW_QUESR_ID` | VARCHAR |  | This stores the IDs of the questionnaires linked to this message. |
| 4 | `ALLOW_QUESR_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

