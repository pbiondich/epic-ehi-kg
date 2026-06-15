# AUTH_REQ_HX_TIMELINESS

> This table contains timeliness information for authorization request milestones.

**Primary key:** `AUTH_REQUEST_ID`, `CONTACT_DATE_REAL`  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_REQUEST_ID` | NUMERIC | PK FK→ | The unique identifier for the authorization request record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `PROV_WRITTEN_DECISION_DTTM` | DATETIME (Local) |  | The date and time (local) that the provider first received written notification of a decision. |
| 4 | `PROV_ORAL_DECISION_DTTM` | DATETIME (Local) |  | The date and time (local) that the provider first received oral notification of a decision. |
| 5 | `MEM_WRITTEN_DECISION_DTTM` | DATETIME (Local) |  | The date and time (local) that the member first received written notification of a decision. |
| 6 | `MEM_ORAL_DECISION_DTTM` | DATETIME (Local) |  | The date and time (local) that the member first received oral notification of a decision. |
| 7 | `REP_WRITTEN_DECISION_DTTM` | DATETIME (Local) |  | The date and time (local) that the authorized representative first received written notification of a decision. |
| 8 | `REP_ORAL_DECISION_DTTM` | DATETIME (Local) |  | The date and time (local) that the authorized representative first received oral notification of a decision. |
| 9 | `PROV_WRITTEN_NOTIF_EXT_DTTM` | DATETIME (Local) |  | The date and time (local) that the provider first received written notification of an extension. |
| 10 | `PROV_ORAL_NOTIF_EXT_DTTM` | DATETIME (Local) |  | The date and time (local) that the provider first received oral notification of an extension. |
| 11 | `MEM_WRITTEN_NOTIF_EXT_DTTM` | DATETIME (Local) |  | The date and time (local) that the member first received written notification of an extension. |
| 12 | `MEM_ORAL_NOTIF_EXT_DTTM` | DATETIME (Local) |  | The date and time (local) that the member first received oral notification of an extension. |
| 13 | `REP_WRITTEN_NOTIF_EXT_DTTM` | DATETIME (Local) |  | The date and time (local) that the authorized representative first received written notification of an extension. |
| 14 | `REP_ORAL_NOTIF_EXT_DTTM` | DATETIME (Local) |  | The date and time (local) that the authorized representative first received oral notification of an extension. |
| 15 | `PROV_WRITTEN_DNL_EXP_DTTM` | DATETIME (Local) |  | The date and time (local) that the provider first received written notification of a denial to expedite. |
| 16 | `PROV_ORAL_DNL_EXP_DTTM` | DATETIME (Local) |  | The date and time (local) that the provider first received oral notification of a denial to expedite. |
| 17 | `MEM_WRITTEN_DNL_EXP_DTTM` | DATETIME (Local) |  | The date and time (local) that the member first received written notification of a denial to expedite. |
| 18 | `MEM_ORAL_DNL_EXP_DTTM` | DATETIME (Local) |  | The date and time (local) that the member first received oral notification of a denial to expedite. |
| 19 | `REP_WRITTEN_DNL_EXP_DTTM` | DATETIME (Local) |  | The date and time (local) that the authorized representative first received written notification of a denial to expedite. |
| 20 | `REP_ORAL_DNL_EXP_DTTM` | DATETIME (Local) |  | The date and time (local) that the authorized representative first received oral notification of a denial to expedite. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_REQUEST_ID` | [AUTH_REQUEST](AUTH_REQUEST.md) | sole_pk | high |

