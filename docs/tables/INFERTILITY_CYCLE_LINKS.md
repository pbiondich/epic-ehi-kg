# INFERTILITY_CYCLE_LINKS

> The INFERTILITY_CYCLE_LINKS table contains information about patients participating in a fertility treatment cycle. The INFERTILITY_CYCLE_LINKS table is not able to safely export all of its columns without potentially compromising the other patients that are attached to the infertility treatment cycle. We created the view V_EHI_ICF_CYCLE_PATIENTS_DATA to filter the INFERTILITY_CYCLE_LINKS data based on the extracted patient's roles (e.g., sperm donor, intended parent) on the infertility treatment cycle. See view on more information on how data is filtered.

**Primary key:** `CYCLE_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CYCLE_ID` | NUMERIC | PK FK→ | The unique identifier for the fertility treatment cycle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ROLE_C_NAME` | VARCHAR |  | The role of the patient in the fertility treatment cycle. |
| 4 | `PAT_ANON_YN` | VARCHAR |  | The patient should be anonymous from other patients in this fertility treatment cycle (ex. egg donor). |
| 5 | `LINKED_PAT_ID` | VARCHAR | FK→ | The patient ID of a patient involved in a fertility treatment cycle. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CYCLE_ID` | [INFERTILITY_CYCLE](INFERTILITY_CYCLE.md) | sole_pk | high |
| `LINKED_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

