# TREATMENT_PLAN_AUDIT

> This table contains audit information for the fertility treatment plan. It tracks who changed the plan, when, and what value was changed.

**Primary key:** `MED_PRBLM_LIST_ID`, `LINE`  
**Columns:** 15  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MED_PRBLM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier for the medical problem list record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MOD_INST_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant in which the change was made to the Treatment Plan. |
| 4 | `MODIFY_USER_ID` | VARCHAR |  | Stores the user who updated the Treatment Plan. |
| 5 | `MODIFY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `START_DATE` | DATETIME |  | Stores the start date of the block for the patient instruction. This is part of the audit trail of changes made to the Treatment Plan. |
| 7 | `END_DATE` | DATETIME |  | Stores the end date of the block for the patient instruction. This is part of the audit trail of changes made to the Treatment Plan. |
| 8 | `DOSE` | NUMERIC |  | Stores the instructed dose for the treatment plan. This is part of the audit trail of changes made to the Treatment Plan. |
| 9 | `UNITS_C_NAME` | VARCHAR | org | Stores the units for the instructed dose. This is part of the audit trail of changes made to the Treatment Plan. |
| 10 | `FREQ_ID` | VARCHAR | FK→ | Stores the frequency for the administration instructions. This is part of the audit trail of changes made to the Treatment Plan. |
| 11 | `FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 12 | `ROUTE_C_NAME` | VARCHAR | org | Stores the route of administration for the instructions. This is part of the audit trail of changes made to the Treatment Plan. |
| 13 | `MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 14 | `ACTION_C_NAME` | VARCHAR |  | This tracks the action being audited. For example, if the user made a change, it will be audited as a pending change action. When signed, it will be audited as a signed action. This is part of the audit trail of changes made to the Treatment Plan. |
| 15 | `AUD_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores the encounter in which the change was made to the Treatment Plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUD_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `FREQ_ID` | [IP_FREQUENCY](IP_FREQUENCY.md) | sole_pk | high |
| `MED_PRBLM_LIST_ID` | [MDL_MD_PRBLM_LIST](MDL_MD_PRBLM_LIST.md) | sole_pk | high |

