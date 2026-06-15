# RFL_APPT_REQUEST

> This table stores appointment request information for home health/hospice initial and resumption visit scheduling.

**Primary key:** `CAREPLAN_ID`, `LINE`  
**Columns:** 15  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CAREPLAN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the care plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `REG_PAT_ENC_CSN_ID` | NUMERIC | FK→ | This item stores the CSN of the Home Health/Hospice Admission or ROC Planning encounter that generated the appointment requests. |
| 5 | `APPT_REQ_DISCIPLINE_C_NAME` | VARCHAR | org | Stores the home care discipline associated with the appointment request order for the CSN. |
| 6 | `APPT_REQUEST_ID` | NUMERIC |  | Stores the appointment request ORD associated with the CSN |
| 7 | `REFERRAL_ID` | NUMERIC | FK→ | Stores the referral (RFL) ID that associated with the appointment request ORD for the line. |
| 8 | `LCP_APPT_REQ_SUG_STAT_C_NAME` | VARCHAR |  | Stores the status associated with this appointment request suggestion. Categories can be found in I ECT 15520. |
| 9 | `SUG_EDITED_YN` | VARCHAR |  | Denotes whether an appointment request suggestion was edited by an end user. Backing category list is ECT 101. |
| 10 | `SUG_RULE_ID` | VARCHAR |  | Denotes which CER rule was used to create this appointment request suggestion. |
| 11 | `SUG_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 12 | `SUG_PRC_ID_PRC_NAME` | VARCHAR |  | The name of the visit type. |
| 13 | `SUG_START_DATE` | DATETIME |  | The start date of the target range of this visit within the appointment request suggestion. |
| 14 | `SUG_END_DATE` | DATETIME |  | The end date of the target range of this visit within the appointment request suggestion. |
| 15 | `SUG_NOTE_ID` | VARCHAR |  | Appointment notes for this visit within the appointment request suggestion. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |
| `REG_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

