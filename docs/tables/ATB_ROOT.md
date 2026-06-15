# ATB_ROOT

> ATB ROOT Data.

**Primary key:** `AUTH_BUNDLE_ID`  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the authorization bundle record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | Patient for ATB |
| 3 | `REFERRAL_ID` | NUMERIC | FK→ | Associated Authorization Referral |
| 4 | `COVERAGE_ID` | NUMERIC | FK→ | Coverage associated with the ATB. |
| 5 | `TYPE_SVC_LINE_C_NAME` | VARCHAR |  | The Type of Service Line category ID for the Auth Bundle that identifies the type of a service line, for example differentiating a procedure from a bed day. |
| 6 | `REF_TO_MAIN_AUTH_BUNDLE_ID` | NUMERIC |  | The reference to the Main ATB. Main ATBs won't have this data item set, most other ATB types will have it set. |
| 7 | `AUTH_EVENT_TYPE_C_NAME` | VARCHAR |  | The event type of this ATB if this ATB is an event record. |
| 8 | `EVENT_IS_EDITABLE_YN` | VARCHAR |  | Whether this event typed ATB is editable as opposed to if it is an immutable and historical record. |
| 9 | `EVENT_STATUS_C_NAME` | VARCHAR |  | The event status of the record, as in whether the event is in progress or finished. |
| 10 | `ABANDON_SVC_ROOT_ID` | NUMERIC |  | The pointer to the Authorization type Auth Bundle record to be set when this Service Line or Service Line Event type Auth Bundle is considered to be "Deleted". |
| 11 | `SERVICE_ID_REF` | VARCHAR |  | The reference ID to use when referring to a Service Line from an outside context. |
| 12 | `EVENT_RESOLUTION_INST_UTC_DTTM` | DATETIME (UTC) |  | Contains the instant that an event was completed or discarded. The instant is stored as the value in UTC. |
| 13 | `EVENT_RESOLUTION_USER_ID` | VARCHAR |  | Contains the user that completed or discarded the event. |
| 14 | `EVENT_RESOLUTION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `ATB_HAS_AUTH_EDITOR_EDITS_YN` | VARCHAR |  | This item tracks whether an end user has made a notable edit to the ATB through the authorization editor, like adding a diagnosis, resolving a task, or submitting authorization. Only end user edits that originate in a Hyperspace style workflow are relevant. |
| 16 | `LAST_REQ_EVENT_AUTH_BUNDLE_ID` | NUMERIC |  | This item stores a reference to the most recent historical event ATB record which represents a request submitted to the payer. |
| 17 | `LAST_DEC_EVENT_AUTH_BUNDLE_ID` | NUMERIC |  | This item stores a reference to the most recent historical event ATB record which represents a decision from the payer. |
| 18 | `PAYR_REQ_OUTREACH_YN` | VARCHAR |  | Tracks if the payer requested outreach by returning an action code of Contact Payer (CT). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

