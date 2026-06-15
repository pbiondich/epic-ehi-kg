# MSP_COB_STATUS

> The MSP_COB_STATUS table contains information related to the MSPQ Coordination of Benefits status. This status determines whether Medicare is primary or secondary to other insurances for a patient on a given contact, based on answers filled out for the MSPQ.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `MSP_COB_STATUS_C_NAME` | VARCHAR | org | The Coordination of Benefits status category number for the Medicare Secondary Payor Questionnaire (MSPQ). Indicates whether Medicare is primary or secondary to other insurance for a given contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

