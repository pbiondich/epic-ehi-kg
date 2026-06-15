# IB_MESSAGES_4

> The IB_MESSAGES_4 table contains basic information about In Basket messages.

**Overflow of:** [IB_MESSAGES](IB_MESSAGES.md)  
**Primary key:** `MSG_ID`  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MSG_ID` | VARCHAR | PK | The unique identifier for the task record. |
| 2 | `PROC_ALG_LPL_ID` | NUMERIC |  | A Patient Allergy Interaction message gets triggered whenever the entered allergy interacts with an existing order. This item stores the newly entered patient's allergy ID that interacts with the existing procedure orders. |
| 3 | `RFL_UPD_CVG_NEWLINE_NUM` | INTEGER |  | This item stores the line number of new coverage information that was updated by the most recent Care Everywhere referral update message. |
| 4 | `RFL_UPD_CVG_OLDLINE_NUM` | INTEGER |  | This item stores the line number of old coverage information that was updated by the most recent Care Everywhere referral update message. |
| 5 | `MYC_CONVO_THREAD_ID` | NUMERIC |  | Contains the MyChart Conversation for this message. |
| 6 | `NOTIF_SUBJ_SMARTTEXT_ID` | VARCHAR |  | The subject SmartText for the notification. Used if the Letter Review is sent as a MyChart Message. |
| 7 | `NOTIF_SUBJ_SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 8 | `NOTIF_USE_PDF_YN` | VARCHAR |  | Determines whether the notification will be sent as a PDF. |
| 9 | `QUERY_TICKET_ID` | NUMERIC |  | The unique ID of the Care Everywhere data exchange ticket for the patient associated with this message. This column along with the QUERY_TICKET_LINE column can be used to link to the CEID_QUERY_AUDIT table. |
| 10 | `QUERY_TICKET_LINE` | INTEGER |  | Line number of the query audit information in the Care Everywhere data exchange ticket for the patient associated with this message. This column along with the QUERY_TICKET_ID column can be used to link to the CEID_QUERY_AUDIT table. |
| 11 | `OUTSIDE_EVENT_IDENT` | VARCHAR |  | The event identifier for an outside document related to this message. |
| 12 | `OUTSIDE_DOC_IDENT` | VARCHAR |  | The document identifier for the outside document related to this message. |
| 13 | `POC_VERSION_CSN` | NUMERIC |  | Specifies the contact serial number (CSN) of the updated specialty plan of care version from which the In Basket message was generated. |
| 14 | `HH_EPISODE_ID` | NUMERIC |  | The Episode ID for the visit set associated with this message. |
| 15 | `HH_CONTACT_TYPE_ID_CONTACT_TYPE_NAME` | VARCHAR |  | Home Health Contact Type name |
| 16 | `HH_CONTACT_TIME_UNKNOWN` | VARCHAR |  | Whether the time for the visit set associated with this message has been determined. |
| 17 | `HH_RECURRENCE_PATTERN` | VARCHAR |  | The recurrence pattern for the visit set associated with this message. |
| 18 | `HH_VERBAL_ORDER_ID` | VARCHAR |  | The home care order ID for the visit set associated with this message. |
| 19 | `HH_LVO_VISIT_NUM` | VARCHAR |  | This column stores the line number on the home care order for the visit set associated with this message. |
| 20 | `IS_AUTO_RAR_RESUBMISSION_YN` | VARCHAR |  | Indicates whether this is a refill request that is automatically re-submitted by the system. 'Y' indicates that this is a refill request that is automatically re-submitted by the system. 'N' or NULL indicates this is not automatically re-submitted by the system or is not a refill request. |
| 21 | `FUT_TREATMENT_PLAN_ID` | NUMERIC |  | This stores the future treatment plan (TPL) ID tied to a route plan In Basket message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [IB_MESSAGES](IB_MESSAGES.md).

