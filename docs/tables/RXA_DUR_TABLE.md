# RXA_DUR_TABLE

> Contains information relating to Drug Utilization Review (DUR) conflicts in adjudication records. Adjudication records are used by Ambulatory Pharmacy during prescription copay adjudication.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `REASON_FOR_SERV_C_NAME` | VARCHAR |  | NCPDP code identifying the type of utilization conflict detected or the reason for the pharmacist's professional service. |
| 7 | `CLINICAL_SIGN_C_NAME` | VARCHAR |  | NCPDP code identifying the significance or severity level of a clinical event. |
| 8 | `OTHER_PHR_IND_C_NAME` | VARCHAR |  | NCPDP code indicating the pharmacy responsible for the previous event involved in the DUR conflict. |
| 9 | `PREV_FILL_DATE` | DATETIME |  | The date that the prescription was previously filled |
| 10 | `QUANT_OF_PREV_FILL` | NUMERIC |  | Amount of the conflicting agent that was previously filled (in metric decimal units). |
| 11 | `DATABASE_INDICAT_C_NAME` | VARCHAR |  | NCPDP code identifying the source of drug information used for DUR processing. |
| 12 | `OTH_PRSCRBR_IND_C_NAME` | VARCHAR |  | NCPDP code comparing the prescriber of the current prescription to the prescriber of the previously filled conflicting prescription. |
| 13 | `DUR_FREE_TXT_MSG` | VARCHAR |  | Text that provides additional detail regarding a DUR conflict. |
| 14 | `PROF_SERVICE_C_NAME` | VARCHAR |  | NCPDP code identifying the type of utilization conflict detected or the reason for the pharmacist's professional service. |
| 15 | `SERVICE_RESULT_C_NAME` | VARCHAR |  | Action taken by a pharmacist in response to a conflict or the result of a pharmacist’s professional service. |
| 16 | `EFFORT_LEVEL_C_NAME` | VARCHAR |  | The level of service for the DUR. Indicates how much effort and time was spent by the pharmacist dealing with the DUR or PPS. |
| 17 | `COAGENT_QUALIFIER_C_NAME` | VARCHAR |  | NCPDP code qualifying the value in ‘DUR Co-Agent ID’ when a pharmacist when resolving an DUR when doing an Rx Adjudication. |
| 18 | `COAGENT_ID` | VARCHAR |  | The field used to respond to DURs for prescription adjudication |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

