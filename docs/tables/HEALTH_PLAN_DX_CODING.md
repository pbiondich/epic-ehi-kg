# HEALTH_PLAN_DX_CODING

> This table contains diagnosis coding from health plan risk adjustment review. Each line represents a diagnosis on the evidence associated with the coding record.

**Primary key:** `CODING_RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CODING_RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the coding record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 6 | `DX_ACTION_C_NAME` | VARCHAR |  | The action the user took on the diagnosis. |
| 7 | `DX_ACTION_COMMENT` | VARCHAR |  | The comment recorded by the user explaining the action they took on the diagnosis. |
| 8 | `DX_REMOVE_RSN_C_NAME` | VARCHAR | org | The reason the user selected for removing the diagnosis. |
| 9 | `RA_SOURCE_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The contact on the encounter-linked coding record that is the source for the changes to this diagnosis. |
| 10 | `RA_SOURCE_DOCUMENT_CSN_ID` | NUMERIC |  | The external encounter contact that was used to code this diagnosis. |
| 11 | `RA_SOURCE_DOCUMENT_ID` | VARCHAR |  | The attachment that was used to code this diagnosis. |
| 12 | `HIGH_RISK_DX_YN` | VARCHAR |  | Whether this diagnosis was considered to be high risk when the initial coding decision was made. |
| 13 | `HAS_AI_YN` | VARCHAR |  | Whether this diagnosis has supporting evidence found by AI when the initial coding decision was made. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `RA_SOURCE_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

