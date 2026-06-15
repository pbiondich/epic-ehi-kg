# PAT_ENC_RSH

> This table extracts information for patient encounters linked to patient research study records.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `ENC_RESEARCH_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 5 | `ENROLL_ID` | NUMERIC | FK→ | This column stores the unique identifiers for associated enrollment information records for the study/patient combination for the research studies linked to this patient encounter. |
| 6 | `MANUAL_LINK_YN` | VARCHAR |  | Indicates whether the non-inferred columns of this table are based on manual user linkage. Y indicates that a user manually linked the encounter to the patient timeline. N indicates the data was inferred based on the encounter date and the patient timeline's dates. |
| 7 | `PROTOCOL_ID` | NUMERIC | shared | This column stores the unique identifier for the protocol linked from the encounter within the patient's study timeline. This column does not use inferred timeline linkages from research linked Clinical or Combined protocols for data integrity. |
| 8 | `PROTOCOL_ID_PROTOCOL_NAME` | VARCHAR |  | The SmartSet/Protocol record name. This is different from the display name, which is stored in CL_PRL_SS_OT.DISPLAY_NAME. |
| 9 | `PROTOCOL_VER` | INTEGER |  | If the encounter is linked to a protocol, this is the version number of that protocol. This column does not use inferred timeline linkages from research linked Clinical or Combined protocols for data integrity. |
| 10 | `PROTOCOL_CONT_DATE_REAL` | FLOAT |  | If the encounter is linked to a protocol, this is the unique contact date of the protocol, in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. This column does not use inferred timeline linkages from research linked Clinical or Combined protocols for data integrity. |
| 11 | `UNIQ_DAY_NUM` | INTEGER |  | The encounter is linked to this unique day number within the protocol of the patient's study timeline. This column does not use inferred timeline linkages from research linked Clinical or Combined protocols for data integrity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

