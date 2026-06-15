# EXT_DATA_LAST_DONE

> This table stores the user and instant for the last time each external data type was marked as Done in Reconcile Outside Information.

**Primary key:** `PAT_ID`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `EXTALG_D_UTC_DTTM` | DATETIME (UTC) |  | Instant that external allergies were last marked as reviewed. |
| 3 | `EXTALG_D_USER_ID` | VARCHAR |  | User who last marked external allergies as reviewed. |
| 4 | `EXTALG_D_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `EXTMED_D_UTC_DTTM` | DATETIME (UTC) |  | Instant that external medications were last marked as reviewed. |
| 6 | `EXTMED_D_USER_ID` | VARCHAR |  | User who last marked external medications as reviewed. |
| 7 | `EXTMED_D_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `EXTPRB_D_UTC_DTTM` | DATETIME (UTC) |  | Instant that external problems were last marked as reviewed. |
| 9 | `EXTPRB_D_USER_ID` | VARCHAR |  | User who last marked external problems as reviewed. |
| 10 | `EXTPRB_D_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `EXTIMM_D_UTC_DTTM` | DATETIME (UTC) |  | Instant that external immunizations were last marked as reviewed. |
| 12 | `EXTIMM_D_USER_ID` | VARCHAR |  | User who last marked external immunizations as reviewed. |
| 13 | `EXTIMM_D_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 14 | `EXTIMM_Q_UTC_DTTM` | DATETIME (UTC) |  | Instant (UTC) when external immunizations were last queried. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

