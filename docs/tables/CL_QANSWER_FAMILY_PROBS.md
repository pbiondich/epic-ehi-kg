# CL_QANSWER_FAMILY_PROBS

> This table stores information about the medical problems the patient's family members have that the patient entered when filling out their family history.

**Primary key:** `ANSWER_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ANSWER_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the answer record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FAM_MEDICAL_HX_C_NAME` | VARCHAR | org | The family medical history category ID for the associated family member. |
| 4 | `FAM_MEM_PROBLEM_ASSOC_MEM` | VARCHAR |  | If the patient lists a family history problem, this is the unique identifier for the associated family member. |
| 5 | `FAM_MEM_PROBLEM_PAT_HX_RESP_C_NAME` | VARCHAR |  | The patient response category ID for the family member problem. |
| 6 | `FAM_MEM_PROBLEM_COMMENT` | VARCHAR |  | Additional information the patient provided about the problem associated with their family member when they were filling out their family history. |
| 7 | `FAM_MEM_PROBLEM_AGE_OF_ONSET` | INTEGER |  | Approximate age that the problem was identified in the associated family member that was provided by the patient when they were filling out their family history. |
| 8 | `FAM_MEM_PROBLEM_ONSET_AGE_END` | INTEGER |  | The end of age of onset range, if age of onset was answered as a range. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |

