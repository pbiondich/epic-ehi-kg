# CL_LEARN_ASSESS_NS

> This table contains No add single response items for the patient learning assessment record. These items don't change overtime and there can be only one response per item.

**Primary key:** `LEARNING_ASSMT_ID`  
**Columns:** 3  
**Joined by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LEARNING_ASSMT_ID` | NUMERIC | PK | The unique ID for the patient learning assessment record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The patient (EPT) record with whom this learning assessment record is associated. |
| 3 | `INSTANT_NOADD_EDIT` | DATETIME (Local) |  | Date/Time stamp for the instance when the patient learning assessment record was last edited. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (4)

| From | Column | Confidence |
|------|--------|------------|
| [CL_LEARN_ASSESS_QA](CL_LEARN_ASSESS_QA.md) | `LEARNING_ASSMT_ID` | high |
| [CL_LEARN_ASSES_CMT](CL_LEARN_ASSES_CMT.md) | `LEARNING_ASSMT_ID` | high |
| [CL_LEARN_ASSES_OTS](CL_LEARN_ASSES_OTS.md) | `LEARNING_ASSMT_ID` | high |
| [CL_PLA_EDIT_HX](CL_PLA_EDIT_HX.md) | `LEARNING_ASSMT_ID` | high |

