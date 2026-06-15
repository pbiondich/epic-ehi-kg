# UNCONFIRMED_PAT_STAT_HX

> Clarity table for historical information regarding unconfirmed patient statuses.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UNCNFRM_HX_STAT_C_NAME` | VARCHAR | org | Holds the historical information regarding the patient unconfirmed status (EPT 2023). |
| 4 | `UNCNFRM_HX_STAT_SRC_C_NAME` | VARCHAR |  | Stores whether the patient status from EPT 2043 was added or removed. |
| 5 | `UNCNFRM_HX_WKFW_C_NAME` | VARCHAR | org | Holds historical information regarding the unconfirmed patient source workflow in EPT 2044. |
| 6 | `UNCNFRM_HX_UTC_DTTM` | DATETIME (UTC) |  | Historical information regarding the instant the patient unconfirmed status changed. |
| 7 | `UNCNFRM_HX_CLI_DTTM` | DATETIME (Attached) |  | Historical information regarding the client instant of the patient's unconfirmed status. |
| 8 | `UNCNFRM_HX_DTTM` | DATETIME (Local) |  | Historical information regarding the server instant of the patient's unconfirmed status. |
| 9 | `UNCNFRM_HX_MYPT_ID` | VARCHAR |  | Holds historical information regarding the patient's unconfirmed status. This item holds the MyChart user linked to the patient's unconfirmed status change. |
| 10 | `UNCNFRM_HX_USER_ID` | VARCHAR |  | Holds historical information regarding the patient's unconfirmed status. This item holds the Hyperspace user linked to the patient's unconfirmed status change. |
| 11 | `UNCNFRM_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `UNCNFRM_HX_RSN_C_NAME` | VARCHAR | org | Holds historical information regarding the patient's unconfirmed status. This item holds the reason linked to the patient's unconfirmed status change. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

