# INFERTILITY_CYCLE

> The INFERTILITY_CYCLE table contains information about fertility treatment cycles.

**Primary key:** `CYCLE_ID`  
**Columns:** 37  
**Org-specific columns:** 3  
**Joined by:** 17 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CYCLE_ID` | NUMERIC | PK | The unique identifier for the fertility treatment cycle record. |
| 2 | `CYCLE_NAME` | VARCHAR |  | The fertility treatment cycle name. |
| 3 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the status (hidden, soft-deleted, etc.) of the Fertility cycle record. |
| 4 | `TREATMENT_TYPE_C_NAME` | VARCHAR |  | The type of REI (Reproductive Endocrinology and Infertility) treatment the patient underwent. Options include ART (Assisted Reproductive Technology) and non-ART. |
| 5 | `TREATMENT_START_DATE` | DATETIME |  | The start date of the fertility treatment cycle is when the medication to stimulate follicular development is given, the first day of natural menses for unstimulated cycles, or when a patient receives steroids to prepare the endometrium for frozen cycles. |
| 6 | `CYCLE_OUTCOME_C_NAME` | VARCHAR |  | The outcome of the fertility treatment cycle. |
| 7 | `CYCLE_RESOLUTION_DATE` | DATETIME |  | The outcome date of the fertility treatment cycle. |
| 8 | `CYCLE_STATUS_C_NAME` | VARCHAR |  | The status of the fertility treatment cycle. |
| 9 | `RECORD_CREATION_DT` | DATETIME |  | The date the record was created. |
| 10 | `CREATED_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 11 | `CANCEL_REASON_C_NAME` | VARCHAR | org | The reason the fertility treatment was canceled. |
| 12 | `CANCEL_REASON_CMT` | VARCHAR |  | Comment for the cycle cancellation reason. |
| 13 | `COMPLICATIONS_CMT` | VARCHAR |  | Comment for the cycle complications field. |
| 14 | `EGGS_RETRIEVED_NUM` | INTEGER |  | The number of eggs retrieved on the fertility cycle. |
| 15 | `EGG_RETRIEVAL_DATE` | DATETIME |  | The date the eggs were retrieved. |
| 16 | `EMBRYO_NO_TRANSFER_RSN_C_NAME` | VARCHAR | org | Reason for why an embryo wasn't transferred for the fertility treatment cycle. |
| 17 | `EMBRYO_NO_TRANSFER_RSN_CMT` | VARCHAR |  | Comment for the no transfer reason field. |
| 18 | `ESET_YN` | VARCHAR |  | Whether the patient chose to do a single embryo transfer for this cycle. |
| 19 | `INSEMINATION_DATE` | DATETIME |  | The date of insemination by intrauterine insemination or therapeutic donor insemination. |
| 20 | `SPERM_COLLECT_METHOD_CMT` | VARCHAR |  | Comment for the sperm collection methods field. |
| 21 | `TREATMENT_REASONS_CMT` | VARCHAR |  | Comment for the reasons for treatment field. |
| 22 | `PREV_CYCLE_YN` | VARCHAR |  | Flags if a cycle was documented retroactively. This should not be used to filter cycles for Society for Assisted Reproductive Technology (SART) reporting. This flag does not necessarily imply the department the cycle was created in is not responsible for the cycle's SART reporting. |
| 23 | `CYCLE_LOC_C_NAME` | VARCHAR | org | Location that owns the outcome of the cycle. This location would also be responsible for reporting this cycle to registries. |
| 24 | `CYCLE_LOC_CMT` | VARCHAR |  | Comment for the cycle location field. |
| 25 | `TREATMENT_PLAN_PAST_DAYS_NUM` | INTEGER |  | Number of days to look prior to the cycle start date to find medications that are relevant to this cycle's treatment. |
| 26 | `TREATMENT_PLAN_FUTURE_DAYS_NUM` | INTEGER |  | Number of days to look into the future to find medications that are relevant to this cycle's treatment. |
| 27 | `EMBRYO_TRANSFER_NUMBER` | INTEGER |  | Stores the number of embryos transferred during a cycle. |
| 28 | `EMBRYO_TRANSFER_PROC_DATE` | DATETIME |  | Stores the date of an embryo transfer for during a cycle. |
| 29 | `REI_CYCLE_VERSION_C_NAME` | VARCHAR |  | This keeps track of what features were available when the cycle was created, which allows cycles created prior to the feature to exclude that feature. For example, cycles that were created before the embryo transfer documentation was introduced should not show that documentation. This item is only set when the cycle is created, is never updated, and is not directly displayed to end users as it has no clinical significance. |
| 30 | `EMBRYO_CRYO_NUM` | INTEGER |  | The number of embryos cryopreserved for a fertility cycle. |
| 31 | `EGG_CRYO_NUM` | INTEGER |  | The number of eggs cryopreserved for a fertility cycle. |
| 32 | `SPERM_CRYO_NUM` | INTEGER |  | The number of sperm samples cryopreserved for a fertility cycle. |
| 33 | `WAS_PLANNING_YN` | VARCHAR |  | This tracks whether the cycle had a status of planning at the time that the cycle was finished or deleted. This is relevant for identifying cycles that were never started and were completed while still in a planning status. |
| 34 | `TRIGGER_DATE` | DATETIME |  | This item stores the planned trigger date for this cycle. |
| 35 | `CYCLE_TRIGGER_TM` | DATETIME (UTC) |  | This item stores the planned ovulation trigger time for this cycle. |
| 36 | `OOCYTE_THAW_DATE` | DATETIME |  | The date of the oocyte thaw procedure. |
| 37 | `EMBRYO_THAW_DATE` | DATETIME |  | The date of the embryo thaw procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (17)

| From | Column | Confidence |
|------|--------|------------|
| [CYCLE_PLAN_STATUS](CYCLE_PLAN_STATUS.md) | `CYCLE_ID` | high |
| [INFERTILITY_CYCLE_LINKS](INFERTILITY_CYCLE_LINKS.md) | `CYCLE_ID` | high |
| [REI_ART_PROCS](REI_ART_PROCS.md) | `CYCLE_ID` | high |
| [REI_CYCLE_PAT_COMMENTS](REI_CYCLE_PAT_COMMENTS.md) | `CYCLE_ID` | high |
| [REI_DAILY_CYCLE_COMMENTS](REI_DAILY_CYCLE_COMMENTS.md) | `CYCLE_ID` | high |
| [REI_FERT_METHOD](REI_FERT_METHOD.md) | `CYCLE_ID` | high |
| [REI_HIDDEN_MEDS](REI_HIDDEN_MEDS.md) | `CYCLE_ID` | high |
| [REI_HIDDEN_MEDS_AUDIT](REI_HIDDEN_MEDS_AUDIT.md) | `CYCLE_ID` | high |
| [REI_LINKED_SPERM](REI_LINKED_SPERM.md) | `CYCLE_ID` | high |
| [REI_NEXT_VISIT_PLAN](REI_NEXT_VISIT_PLAN.md) | `CYCLE_ID` | high |
| [REI_NEXT_VISIT_PLAN_TESTS](REI_NEXT_VISIT_PLAN_TESTS.md) | `CYCLE_ID` | high |
| [REI_NON_ART_TRTS](REI_NON_ART_TRTS.md) | `CYCLE_ID` | high |
| [REI_PGT_TYPES](REI_PGT_TYPES.md) | `CYCLE_ID` | high |
| [SMRTDTA_ELEM_INFERT_CYCLE](SMRTDTA_ELEM_INFERT_CYCLE.md) | `CYCLE_ID` | high |
| [SPECIMEN_CYCLES](SPECIMEN_CYCLES.md) | `CYCLE_ID` | high |
| [TPL_CYCLES](TPL_CYCLES.md) | `CYCLE_ID` | high |
| [V_EHI_ICF_CYCLE_PATIENTS_DATA](V_EHI_ICF_CYCLE_PATIENTS_DATA.md) | `CYCLE_ID` | high |

