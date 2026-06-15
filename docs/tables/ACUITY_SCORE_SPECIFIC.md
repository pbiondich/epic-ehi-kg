# ACUITY_SCORE_SPECIFIC

> Extracted table for scoring system-related data from scoring system data filed to RDI.

**Primary key:** `REGISTRY_DATA_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `SCORE_FILE_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the scoring system information is filed in UTC. |
| 5 | `SCORE_FILE_LOC_DTTM` | DATETIME (Local) |  | The date and time when the scoring system information is filed in local time. It is calculated from the UTC rule filing instant. |
| 6 | `TOTAL_SCORE` | NUMERIC |  | This item stores the score for the scoring system record in the Scoring System ID item (RDI 40300). |
| 7 | `ACUITY_SYSTEM_CSN_ID` | NUMERIC |  | Stores the contact serial number of the predictive model that generated this score. |
| 8 | `MODEL_VERSION_C_NAME` | VARCHAR |  | Stores the category value from Predictive Model Version (I ECT 82010) that represents the contact of the predictive model that generated this score. |
| 9 | `CLOUD_VERSION_DATE` | DATETIME |  | For certain models, this item stores the date on which this version of the model that was used to calculate the score was released. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

