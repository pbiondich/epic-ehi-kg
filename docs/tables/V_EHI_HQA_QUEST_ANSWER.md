# V_EHI_HQA_QUEST_ANSWER

> This view converts the QUEST_ANSWER column in CL_QANSWER_QA into an external-facing format for EHI Export. This table should be used in tandem with CL_QANSWER_QA, using the ANSWER_ID and LINE columns to join the two together.

**Primary key:** `ANSWER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ANSWER_ID` | VARCHAR | PK FK→ | The unique ID of the questionnaire answer record. |
| 2 | `LINE` | INTEGER | PK | Line count of the answers in the questionnaire record. |
| 3 | `QUEST_ANSWER_EXTERNAL` | VARCHAR |  | The actual answer to the question as it was seen by the answering user. This value is converted to an external format depending on the question response type (I LQL 110). For category values, this column will contain the category title. For all other value types, the value matches what is stored in CL_QANSWER_QA__QUEST_ANSWER. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |

