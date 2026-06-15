# CAL_REFERENCE_PAT

> The patients and encounters referenced by the communication.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | VARCHAR | PK shared | The unique ID for the Communication Tracking record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REF_PAT_CONTEXT_C_NAME` | VARCHAR | org | The category number for the context of the patient encounter which is referenced by the communication. |
| 4 | `REF_REFERRAL_ID` | NUMERIC |  | The unique ID of the referral that is referenced by the communication. |
| 5 | `REF_WAITING_LIST_ID` | NUMERIC |  | The unique ID of the Waiting List that is referenced by the communication. |
| 6 | `REF_ADT_EVENT_ID` | NUMERIC |  | ADT event in regards to which this communication was sent. |
| 7 | `REF_PEND_EVENT_ID` | VARCHAR |  | The ID number of the pending event for which this communication was sent. |
| 8 | `REF_CLEANING_ID` | NUMERIC |  | The bed management event for which this communication was sent. |
| 9 | `REF_TXPORT_ID` | NUMERIC |  | The ID number of the transport request for which this communication was sent. |
| 10 | `REF_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 11 | `REF_MSG_ID` | VARCHAR |  | The ID number of the specific In Basket message that caused this email messages to be sent. |
| 12 | `REF_HLR_ID` | NUMERIC |  | The unique ID associated with the logistics job record associated for this row of this patient encounter communication interaction. |
| 13 | `REF_TECH_ID` | NUMERIC |  | The unique ID associated with the logistics technician record for this row of this patient encounter communication interaction. |
| 14 | `REF_APPEAL_GRV_ID` | NUMERIC |  | The health plan appeal or grievance record associated with this call. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

