# APPEAL_GRV_SUBJECT_RESULT

> This table contains information about the subject and result of an appeal.

**Primary key:** `APPEAL_GRV_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `APPEAL_GRV_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the appeal/grievance record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SUBJECT_CLAIM_ID` | NUMERIC |  | The unique ID of the claim that is under appeal. |
| 4 | `RESULT_CLAIM_ID` | NUMERIC |  | The unique ID of the claim created as a result of the appeal to effectuate the appeal decision. |
| 5 | `APPEAL_DECISION_C_NAME` | VARCHAR |  | The appeal decision category ID for the appeal/grievance subject. |
| 6 | `RESULT_FREE_TEXT` | VARCHAR |  | Stores a free text result ID for an appeal or grievance. |
| 7 | `SUBJECT_FREE_TEXT` | VARCHAR |  | The name or ID of an appeal or grievance subject that does not correspond to a record that is in the system. |
| 8 | `IND_EFFEC_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant that the appeal decision was effectuated. For claim appeals, this is the date/time the result claim was paid in UTC. This is only populated if the subject claim required effectuation based on the decision. If the subject claim is external, then this will be filled out manually during the appeal workflow. Otherwise the system will calculate it automatically. |
| 9 | `IND_EFFEC_INST_LOCAL_DTTM` | DATETIME (Attached) |  | The instant that the appeal decision was effectuated. For claim appeals, this is the date/time the result claim was paid, in local time based on time zone of the appeal/grievance. This is only populated if the subject claim required effectuation based on the decision. If the subject claim is external, then this will be filled out manually during the appeal workflow. Otherwise the system will calculate it automatically. |
| 10 | `PAYMENT_AUTH_UTC_DTTM` | DATETIME (UTC) |  | The date and time that the payment was authorized in UTC. This is only populated if the Subject Claim (SUBJECT_CLAIM_ID) is external, and then this will be filled out manually during the appeal workflow. |
| 11 | `PAYMENT_AUTH_LOC_DTTM` | DATETIME (Attached) |  | The date and time that the payment was authorized. This is only populated if the Subject Claim (SUBJECT_CLAIM_ID) is external, and then this will be filled out manually during the appeal workflow. This stores the local date/time based on the TAT Reportable Time Zone (APPEAL_GRV_TAT_RPT_TIME_ZONE_C). |
| 12 | `PAYMENT_RECIPIENT_C_NAME` | VARCHAR |  | Currently unused. |
| 13 | `NO_PAYMENT_REQ_YN` | VARCHAR |  | Indicates whether payment is required for the result claim ('Y') or not ('N' or NULL). If there is no result claim this will always be NULL. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `APPEAL_GRV_ID` | [APPEAL_GRV](APPEAL_GRV.md) | sole_pk | high |

