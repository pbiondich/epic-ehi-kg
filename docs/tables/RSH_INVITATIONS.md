# RSH_INVITATIONS

> This table contains details about every research study invitation that was sent for a patient-study association.

**Primary key:** `ENROLL_ID`, `LINE`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the enrollment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INVITATION_USER_ID` | VARCHAR |  | The unique ID of the user that sent the research study invitation. |
| 4 | `INVITATION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `INVITATION_LAST_MOD_SOURCE_C_NAME` | VARCHAR |  | The modification source category ID for the research study invitation. |
| 6 | `INVITATION_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant at which the research study invitation was sent. |
| 7 | `INVITATION_DTTM` | DATETIME (Attached) |  | The local instant at which the research study invitation was sent. |
| 8 | `INVITATION_SENT_YN` | VARCHAR |  | Indicates whether the research study invitation was successfully sent to one or more recipients. 'Y' indicates that the invitation was successfully sent. 'N' or NULL indicates that the invitation was not successfully sent. |
| 9 | `INVITATION_TICKLER_SENT_YN` | VARCHAR |  | Indicates whether any ticklers were sent for this research study invitation. 'Y' indicates that one or more ticklers were sent for the invitation. 'N' or NULL indicate that no ticklers were sent for the invitation. |
| 10 | `INVITATION_MYC_RESPONSE_TYPE_C_NAME` | VARCHAR |  | The response type to the research study invitation. |
| 11 | `INVITATION_RESPONSE_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant that the research study invitation was responded to. |
| 12 | `INVITATION_RESPONSE_MYPT_ID` | VARCHAR |  | The unique ID of the MyChart user that responded to the research study invitation. |
| 13 | `INVITE_RETRACT_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant at which the research study invitation was retracted. |
| 14 | `INVITATION_OUTREACH_CSN_ID` | NUMERIC |  | The unique contact serial number of the outreach contact that is associated with the invitation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

