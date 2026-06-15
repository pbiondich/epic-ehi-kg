# DISCH_INSTR_HISTORY

> This table contains information about instances where discharge instructions were reviewed, updated, or signed.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DISCH_INSTR_USER_ID` | VARCHAR |  | The user that updated or reviewed the discharge instructions. For discharge instructions created before web transition, this could also store the user that reviewed the discharge instructions using e-signature. |
| 4 | `DISCH_INSTR_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `DISCH_INSTR_UTC_DTTM` | DATETIME (UTC) |  | The instant the discharge instructions were updated or marked as reviewed. For discharge instructions created before web transition, this could also store the instant the discharge instructions were reviewed using e-signature. |
| 6 | `DISCH_INSTR_DTTM` | DATETIME (Local) |  | The instant the discharge instructions were updated or marked as reviewed. For discharge instructions created before web transition, this could also store the instant the discharge instructions were reviewed using e-signature. |
| 7 | `DISCH_INSTR_ACTION_C_NAME` | VARCHAR |  | The category number for the action taken on discharge instructions. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 8 | `DISCH_INSTR_NOTE_CSN_ID` | NUMERIC |  | The contact serial number for the discharge instructions note contact where the action took place. |
| 9 | `DISCH_INSTR_DOCUMENT_ID` | VARCHAR |  | Document for the e-signature of the discharge instructions. This item will no longer be populated in the web version of Discharge Writer. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

