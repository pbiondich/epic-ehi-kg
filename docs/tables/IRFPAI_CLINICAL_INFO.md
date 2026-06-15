# IRFPAI_CLINICAL_INFO

> This table contains clinical information collected on the IRF-PAI.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 68

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier of the abstraction for this row. |
| 2 | `IMPAIRMENT_GROUP_ADMSN_C` | VARCHAR |  | The code that best describes the primary reason for admission to the rehab facility. |
| 3 | `IMPAIRMENT_GROUP_DISCHRG_C` | VARCHAR |  | The code that best describes the primary impairment throughout the stay. If the patient develops a more resource-intensive impairment during the stay, this element could be different from the admission element. |
| 4 | `EATING_ADMSN_C` | INTEGER |  | Eating assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 5 | `EATING_DISCHRG_C` | INTEGER |  | Eating assessment at Discharge, scored using Functional Independence Measure (FIM) levels 1-7. |
| 6 | `EATING_GOAL_C` | INTEGER |  | Goal for Eating assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 7 | `GROOMING_ADMSN_C` | INTEGER |  | Grooming assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 8 | `GROOMING_DISCHRG_C` | INTEGER |  | Grooming assessment at Discharge, scored using Functional Independence Measure (FIM) levels 1-7. |
| 9 | `GROOMING_GOAL_C` | INTEGER |  | Goal for Grooming assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 10 | `BATHING_ADMSN_C` | INTEGER |  | Bathing assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 11 | `BATHING_DISCHRG_C` | INTEGER |  | Bathing assessment at Discharge, scored using Functional Independence Measure (FIM) levels 1-7. |
| 12 | `BATHING_GOAL_C` | INTEGER |  | Goal for Bathing assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 13 | `DRESSING_UPPER_ADMSN_C` | INTEGER |  | Dressing Upper assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 14 | `DRESSING_UPPER_DISCHRG_C` | INTEGER |  | Dressing Upper assessment at Discharge, scored using Functional Independence Measure (FIM) levels 1-7. |
| 15 | `DRESSING_UPPER_GOAL_C` | INTEGER |  | Goal for Dressing Upper assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 16 | `DRESSING_LOWER_ADMSN_C` | INTEGER |  | Dressing Lower assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 17 | `DRESSING_LOWER_DISCHRG_C` | INTEGER |  | Dressing Lower assessment at Discharge, scored using Functional Independence Measure (FIM) levels 1-7. |
| 18 | `DRESSING_LOWER_GOAL_C` | INTEGER |  | Goal for Dressing Lower assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 19 | `TOILETING_ADMSN_C` | INTEGER |  | Toileting assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 20 | `TOILETING_DISCHRG_C` | INTEGER |  | Toileting assessment at Discharge, scored using Functional Independence Measure (FIM) levels 1-7. |
| 21 | `TOILETING_GOAL_C` | INTEGER |  | Goal for Toileting assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 22 | `BLADDER_ADMSN_C` | INTEGER |  | Bladder assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 23 | `BLADDER_DISCHRG_C` | INTEGER |  | Bladder assessment at Discharge, scored using Functional Independence Measure (FIM) levels 1-7. |
| 24 | `BLADDER_GOAL_C` | INTEGER |  | Goal for Bladder assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 25 | `BOWEL_ADMSN_C` | INTEGER |  | Bowel assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 26 | `BOWEL_DISCHRG_C` | INTEGER |  | Bowel assessment at Discharge, scored using Functional Independence Measure (FIM) levels 1-7. |
| 27 | `BOWEL_GOAL_C` | INTEGER |  | Goal for Bowel assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 28 | `BED_CHAIR_WHEELCHAIR_ADMSN_C` | INTEGER |  | Transfers: Bed, Chair, Wheelchair assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 29 | `BED_CHAIR_WHEELCHAIR_DISCHRG_C` | INTEGER |  | Transfers: Bed, Chair, Wheelchair assessment at Discharge, scored using Functional Independence Measures (FIM) levels 1-7. |
| 30 | `BED_CHAIR_WHEELCHAIR_GOAL_C` | INTEGER |  | Goal for Transfers: Bed, Chair, Wheelchair assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 31 | `TOILET_TRANS_ADMSN_C` | INTEGER |  | Transfers: Toilet assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 32 | `TOILET_TRANS_DISCHRG_C` | INTEGER |  | Transfers: Toilet assessment at Discharge, scored using Functional Independence Measure (FIM) levels 1-7. |
| 33 | `TOILET_TRANS_GOAL_C` | INTEGER |  | Goal for Transfers: Toilet assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 34 | `TUB_SHOWER_TRANS_ADMSN_C` | INTEGER |  | Transfers: Tub, Shower assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 35 | `TUB_SHOWER_TRANS_DISCHRG_C` | INTEGER |  | Transfers: Tub, Shower assessment at Discharge, scored using Functional Independence Measure (FIM) levels 1-7. |
| 36 | `TUB_SHOWER_TRANS_GOAL_C` | INTEGER |  | Goal for Transfers: Tub, Shower assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 37 | `WALK_WHEELCHAIR_MODE_C` | INTEGER |  | Walk/Wheelchair assessment Mode at Admission. |
| 38 | `WALK_WHEELCHAIR_ADMSN_C` | INTEGER |  | Walk/Wheelchair assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 39 | `WALK_WHEELCHAIR_DISCHRG_C` | INTEGER |  | Walk/Wheelchair assessment at Discharge, scored using Functional Independence Measure (FIM) levels 1-7. |
| 40 | `WALK_WHEELCHAIR_GOAL_C` | INTEGER |  | Goal for Walk/Wheelchair assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 41 | `STAIRS_ADMSN_C` | INTEGER |  | Stairs assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 42 | `STAIRS_DISCHRG_C` | INTEGER |  | Stairs assessment at Discharge, scored using Functional Independence Measure (FIM) levels 1-7. |
| 43 | `STAIRS_GOAL_C` | INTEGER |  | Goal for Stairs assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 44 | `COMPREHENSION_MODE_ADMSN_C` | INTEGER |  | Comprehension assessment Mode at Admission. |
| 45 | `COMPREHENSION_ADMSN_C` | INTEGER |  | Comprehension assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 46 | `COMPREHENSION_MODE_DISCHRG_C` | INTEGER |  | Comprehension assessment Mode at Discharge. |
| 47 | `COMPREHENSION_DISCHRG_C` | INTEGER |  | Comprehension assessment at Discharge, scored using Functional Independence Measure (FIM) levels 1-7. |
| 48 | `COMPREHENSION_GOAL_C` | INTEGER |  | Goal for Comprehension assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 49 | `EXPRESSION_MODE_ADMSN_C` | INTEGER |  | Expression assessment Mode at Admission. |
| 50 | `EXPRESSION_ADMSN_C` | INTEGER |  | Expression assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 51 | `EXPRESSION_MODE_DISCHRG_C` | INTEGER |  | Expression assessment Mode at Discharge. |
| 52 | `EXPRESSION_DISCHRG_C` | INTEGER |  | Expression assessment at Discharge, scored using Functional Independence Measure (FIM) levels 1-7. |
| 53 | `EXPRESSION_GOAL_C` | INTEGER |  | Goal for Expression assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 54 | `SOCIAL_INTERACTION_ADMSN_C` | INTEGER |  | Social Interaction assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 55 | `SOCIAL_INTERACTION_DISCHRG_C` | INTEGER |  | Social Interaction assessment at Discharge, scored using Functional Independence Measure (FIM) levels 1-7. |
| 56 | `SOCIAL_INTERACTION_GOAL_C` | INTEGER |  | Goal for Social Interaction assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 57 | `PROBLEM_SOLVING_ADMSN_C` | INTEGER |  | Problem Solving assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 58 | `PROBLEM_SOLVING_DISCHRG_C` | INTEGER |  | Problem Solving assessment at Discharge, scored using Functional Independence Measure (FIM) levels 1-7. |
| 59 | `PROBLEM_SOLVING_GOAL_C` | INTEGER |  | Goal for Problem Solving assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 60 | `MEMORY_ADMSN_C` | INTEGER |  | Memory assessment at Admission, scored using Functional Independence Measure (FIM) levels 1-7. |
| 61 | `MEMORY_DISCHRG_C` | INTEGER |  | Memory assessment at Discharge, scored using Functional Independence Measure (FIM) levels 1-7. |
| 62 | `MEMORY_GOAL_C` | INTEGER |  | Goal for Memory assessment, scored using Functional Independence Measure (FIM) levels 1-7. |
| 63 | `FIRST_INTERRUPTION_START_DATE` | DATETIME |  | The date of the first interruption to the inpatient rehabilitation facility (IRF) stay. |
| 64 | `FIRST_INTERRUPTION_END_DATE` | DATETIME |  | The date of the patient's return from the first interruption to the inpatient rehabilitation facility (IRF) stay. |
| 65 | `SECOND_INTERRUPTION_START_DATE` | DATETIME |  | The date of the second interruption to the inpatient rehabilitation facility (IRF) stay. |
| 66 | `SECOND_INTERRUPTION_END_DATE` | DATETIME |  | The date of the patient's return from the second interruption to the inpatient rehabilitation facility (IRF) stay. |
| 67 | `THIRD_INTERRUPTION_START_DATE` | DATETIME |  | The date of the third interruption to the inpatient rehabilitation facility (IRF) stay. |
| 68 | `THIRD_INTERRUPTION_END_DATE` | DATETIME |  | The date of the patient's return from the third interruption to the inpatient rehabilitation facility (IRF) stay. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

