# OCCURRENCE_CODES

> The EPISODE table contains high-level information on the episodes recorded in clinical system for your patients. When a provider sees a patient several times for an ongoing condition, such as prenatal care, these encounters can be linked to a single Episode of Care.

**Primary key:** `SUMMARY_BLOCK_ID`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the summary block record. |
| 2 | `REHAB_ONSET_DATE` | DATETIME |  | The date of onset of the symptoms being treated in the rehabilitation episode. This corresponds with occurrence code 11 on the claim. |
| 3 | `PT_CAREPLAN_DATE` | DATETIME |  | The date the physical therapy (PT) care plan was established or last updated. This corresponds with occurrence code 29 on the claim. |
| 4 | `OT_CAREPLAN_DATE` | DATETIME |  | The date the occupational therapy (OT) care plan was established or last updated. This corresponds with occurrence code 17 on the claim. |
| 5 | `SLP_CAREPLAN_DATE` | DATETIME |  | The date the speech-language pathology (SLP) care plan was established or last updated. This corresponds with occurrence code 30 on the claim. |
| 6 | `PT_TREATMENT_DATE` | DATETIME |  | The date physical therapy (PT) treatment started. This corresponds with occurrence code 35 on the claim. |
| 7 | `OT_TREATMENT_DATE` | DATETIME |  | The date occupational therapy (OT) treatment started. This corresponds with occurrence code 44 on the claim. |
| 8 | `SLP_TREATMENT_DATE` | DATETIME |  | The date speech-language pathology (SLP) treatment started. This corresponds with occurrence code 45 on the claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

