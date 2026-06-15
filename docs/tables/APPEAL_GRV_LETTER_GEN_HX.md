# APPEAL_GRV_LETTER_GEN_HX

> All successes, failures, and intermediate actions that occurred while generating letters.

**Primary key:** `APPEAL_GRV_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `APPEAL_GRV_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the appeal/grievance record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `HISTORY_KEY` | INTEGER |  | GRP 5100 is sorted by occur instant, but if the TAG record is locked by a different process when we try to log an action, we will have to wait and try again later. This means that the occur instant may not exactly correlate the order in which certain lines were logged. This item keeps track of the technical order that actions were logged. |
| 5 | `LETTER_HX_GUID` | VARCHAR |  | The letter that caused this history action will have a matching GUID in I TAG 5020. |
| 6 | `APPEAL_GRV_LETTER_ACT_C_NAME` | VARCHAR |  | The action that occurred to cause this line to be logged. |
| 7 | `OCCUR_UTC_DTTM` | DATETIME (UTC) |  | The instant that the action logged in I TAG 5103 occurred. |
| 8 | `COMMITTING_USER_ID` | VARCHAR |  | The logged in user of the process that caused this action to occur. |
| 9 | `COMMITTING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `LETTER_HX_COMMENT` | VARCHAR |  | Any details that are too specific to be recorded with the history action (I TAG 5103), like specific error messages, can be recorded here. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `APPEAL_GRV_ID` | [APPEAL_GRV](APPEAL_GRV.md) | sole_pk | high |

