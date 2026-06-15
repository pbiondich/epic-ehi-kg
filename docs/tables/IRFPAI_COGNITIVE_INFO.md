# IRFPAI_COGNITIVE_INFO

> This table stores the values documented in the IRF-PAI for Section C (Care Tool) cognition items.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier of the abstraction for this row. |
| 2 | `EXPRESSION_OF_IDEAS_WANTS_C` | INTEGER |  | This element measures expression of ideas and wants while considering both verbal and non-verbal expression and excluding language barriers. |
| 3 | `UNDERSTAND_VERBAL_AND_NONVRB_C` | INTEGER |  | This element measures understanding of verbal and nonverbal content, with a hearing aid or device if used, and excluding language barriers. |
| 4 | `COMMUNICATION_SCORE` | NUMERIC |  | The total score for a patient's ability to express ideas and verbal and nonverbal communication. |
| 5 | `BIMS_STATUS_C` | VARCHAR |  | Indicates if the staff believes the patient is capable of participating in a brief interview to evaluate the patient's mental status. |
| 6 | `REPETITION_OF_THREE_WORDS_NUM` | NUMERIC |  | Indicates the number of words the resident could recall properly after the first attempt. |
| 7 | `TEMPORAL_ORIENTATION_YEAR_C` | VARCHAR |  | Indicates that the patient is able to report the correct year or how inaccurate the patient's guess was. |
| 8 | `TEMPORAL_ORIENTATION_MONTH_C` | VARCHAR |  | Indicates that the patient is able to report the correct month or how inaccurate the patient's guess was. |
| 9 | `TEMPORAL_ORIENTATION_DAY_C` | INTEGER |  | Indicates that the patient is able to report the correct day of the week or how inaccurate the patient's guess was. |
| 10 | `RECALL_SOCK_C` | VARCHAR |  | Indicates the patient's ability to recall "sock" with or without cueing |
| 11 | `RECALL_BLUE_C` | VARCHAR |  | Indicates the patient's ability to recall "blue" with or without cueing |
| 12 | `RECALL_BED_C` | VARCHAR |  | Indicates the patient's ability to recall "bed" with or without cueing |
| 13 | `BIMS_SUMMARY_SCORE` | NUMERIC |  | The total Brief Interview for Mental Status (BIMS) assessment score for a patient at a particular assessment (99 indicates a question could not be completed during the interview). |
| 14 | `UNABLE_TO_COMPLETE_BIMS_YN` | VARCHAR |  | This element indicates if the Brief Interview for Mental Status (BIMS) interview was not able to be completed. |
| 15 | `STAFF_ASMT_FOR_MENTAL_STAT_C` | VARCHAR |  | Indicates whether the staff should attempt an assessment of the patient's mental status due to an incomplete interview. |
| 16 | `MEMORYRECALL_CURRENT_SEASON_YN` | VARCHAR |  | Indicates the patient's ability to recall current season. |
| 17 | `MEMORYRECALL_ROOM_LOCATION_YN` | VARCHAR |  | Indicates the patient's ability to recall room location. |
| 18 | `MEMORYRECALL_STAFF_NAMES_YN` | VARCHAR |  | Indicates the patient's ability to recall staff names. |
| 19 | `MEMORYRECALL_IN_HOSPUNIT_YN` | VARCHAR |  | Indicates the patient's ability to recall hospital or unit name. |
| 20 | `MEMORY_SCORE` | NUMERIC |  | The total memory score for the patient based on the patient's Brief Interview for Mental Status (BIMS) assessment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

