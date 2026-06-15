# DENTAL_MOUTH_HX

> This table saves information about the history of a patient's mouth.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DENT_BASELINE_YN` | VARCHAR |  | This flag indicates whether the patient's tooth chart was saved as a baseline at a given time. |
| 4 | `PERIO_EXAM_HX_DATE` | DATETIME |  | This item stores the clinical date of a periodontal exam. By default this will be the encounter date, but users can specify a past date as well. |
| 5 | `HT_APRV_DTTM_HX_DTTM` | DATETIME (Attached) |  | The history of the date and time when the hard tissue chart was approved. |
| 6 | `HT_APRV_USER_HX_ID` | VARCHAR |  | The history of the unique ID of the user who approved the hard tissue chart. |
| 7 | `HT_APRV_USER_HX_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `HT_NEED_APRV_HX_YN` | VARCHAR |  | Indicates whether the hard tissue chart requires approval for this patient and contact. 'Y' indicates that the hard tissue chart needs approval for the patient in the encounter. 'N' and NULL indicate that the hard tissue chart does not need approval. |
| 9 | `PERIO_APRV_DTTM_HX_DTTM` | DATETIME (Attached) |  | The history of the date and time when the periodontal chart was approved. |
| 10 | `PERIO_APRV_USER_HX_ID` | VARCHAR |  | The history of the unique ID of the user who approved the periodontal chart. |
| 11 | `PERIO_APRV_USER_HX_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `PERI_NEED_APRV_HX_YN` | VARCHAR |  | Indicates whether the periodontal chart requires approval for this patient and contact. 'Y' indicates that the periodontal chart needs approval for the patient in the encounter. 'N' and NULL indicate that the periodontal chart does not need approval. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

