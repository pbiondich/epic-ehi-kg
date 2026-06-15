# TREATMENT_PLAN

> This represents the fertility treatment plan for a given simple generic. It contains medication administration instructions documented for a fertility treatment cycle.

**Primary key:** `MED_PRBLM_LIST_ID`, `LINE`  
**Columns:** 15  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MED_PRBLM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier for the medical problem list record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `START_DATE` | DATETIME |  | Stores the start date of the block for the patient instruction. |
| 4 | `END_DATE` | DATETIME |  | Stores the end date of the block for the patient instruction. |
| 5 | `DOSE` | NUMERIC |  | Stores the instructed dose for the treatment plan. |
| 6 | `UNITS_C_NAME` | VARCHAR | org | Stores the units for the instructed dose. |
| 7 | `FREQ_ID` | VARCHAR | FK→ | Stores the frequency for the administration instructions |
| 8 | `FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 9 | `ROUTE_C_NAME` | VARCHAR | org | Stores the route of administration for the instructions. |
| 10 | `MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 11 | `STATUS_C_NAME` | VARCHAR |  | The signed or pending status of the block for this instruction. |
| 12 | `PEND_USER_ID` | VARCHAR |  | Stores the user that pended this change. This will be blank for signed changes. |
| 13 | `PEND_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 14 | `PENDING_UTC_DTTM` | DATETIME (UTC) |  | Stores the date/time instant when this change was pended. This will be blank for signed changes. |
| 15 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores the encounter of the block for the instructed dose. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FREQ_ID` | [IP_FREQUENCY](IP_FREQUENCY.md) | sole_pk | high |
| `MED_PRBLM_LIST_ID` | [MDL_MD_PRBLM_LIST](MDL_MD_PRBLM_LIST.md) | sole_pk | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

