# CLM_DOC_CTRL_INFO

> Document control information.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the Claim Info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ATTCHMT_MAIL_DT` | DATETIME |  | The date an attachment is sent. |
| 4 | `ATTCHMT_TRNSMT_CD_C_NAME` | VARCHAR |  | Code defining the method by which attachments are being sent. |
| 5 | `CLM_CVG_DCN_ID` | NUMERIC |  | The coverage associated with a particular Document Control Number (DCN). |
| 6 | `DOC_CTRL_NUM_CVGREL` | VARCHAR |  | Document Control Number that is specific to a coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

