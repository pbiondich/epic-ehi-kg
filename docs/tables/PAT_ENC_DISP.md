# PAT_ENC_DISP

> The PAT_ENC_DISP table contains information from the Follow-up action on the Visit Navigator tab for the ambulatory clinical system. This information specifies how and when a patient and provider should follow up with each other after an encounter. This table also contains information about the level of service (LOS) associated with the encounter.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 15  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 2 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 3 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 4 | `DX_FOLLOWUP_C_NAME` | VARCHAR | org | This column typically stores special instructions that the lab should follow when processing this patient's lab orders. However, some organizations choose to store other information in this column. |
| 5 | `ORDER_INSTR_C_NAME` | VARCHAR | org | This column typically stores the method of follow-up used to communicate order results with the patient. However, some organizations choose to store other information in this column. |
| 6 | `LOS_DROPPED_C_NAME` | VARCHAR |  | The category number that indicates whether the Level of Service was dropped for this encounter. The category value will be equal to "pending" only while it is in the orders queue. |
| 7 | `LOS_AUTH_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `LOS_TRIG_ERR_YN` | VARCHAR |  | Whether or not there was an LOS trigger error when dropping the charge. |
| 9 | `LOS_NEW_OR_EST_C_NAME` | VARCHAR |  | The category number that indicates whether the patient is a new (first time being seen) or established patient. |
| 10 | `LOS_HX_LEVEL_C_NAME` | VARCHAR |  | The category number for how extensively the patient's history was discussed as entered in the Level of Service calculator. |
| 11 | `LOS_EXAM_LEVEL_C_NAME` | VARCHAR |  | The category number for the extent of the exam as entered in the Level of Service calculator. |
| 12 | `LOS_MDM_LEVEL_C_NAME` | VARCHAR |  | The category number for the complexity of the medical decision-making in this encounter as entered in the Level of Service calculator. |
| 13 | `LOS_NO_CHG_RSN_C_NAME` | VARCHAR |  | The reason that a charge was not triggered for a level of service. This item being populated does not imply any issues with system integrity or system build; it will be set both for legitimate reasons that a charge was not triggered as well as non-legitimate reasons. |
| 14 | `LOS_SERV_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 15 | `LOS_NEW_OR_EST_HISTORY_DATE` | DATETIME |  | When the New vs Established defaulting extension runs, this stores the service date of the historical charge that was found that establishes this visit. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

