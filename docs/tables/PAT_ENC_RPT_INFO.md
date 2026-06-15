# PAT_ENC_RPT_INFO

> This table contains the result order report information for an encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 19  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `LINE` | INTEGER | PK | The line number of the report for the patient encounter. |
| 3 | `REPORT_TYPE_C_NAME` | VARCHAR | org | The type of result order report created for this encounter. |
| 4 | `REPORT_ID` | VARCHAR | FK→ | The unique ID of the result order report for this encounter. |
| 5 | `REPORT_STATUS_C_NAME` | VARCHAR | org | The status of the result order report for this encounter. |
| 6 | `CREATE_DATETIME` | DATETIME (Local) |  | The date and time the result order report was created for this encounter. |
| 7 | `REPORT_AUTHOR_ID` | VARCHAR |  | The unique ID of the system user who created the result order report for this encounter. |
| 8 | `REPORT_AUTHOR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `LAST_UPDATE_TIME` | DATETIME (Local) |  | The date and time the result order report was last updated for this encounter. |
| 10 | `LAST_UPDATE_USR_ID` | VARCHAR |  | The unique ID of the system user who last updated the result order report for this encounter. |
| 11 | `LAST_UPDATE_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `SIGN_DATETIME` | DATETIME (Local) |  | The date and time the result order report was signed for this encounter. |
| 13 | `SIGN_USER_ID` | VARCHAR |  | The unique ID of the system user who signed the result order report for this encounter. |
| 14 | `SIGN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `COSIGN_STATUS_C_NAME` | VARCHAR | org | The cosign status of the result order report for this encounter. |
| 16 | `COSIGN_DATETIME` | DATETIME (Local) |  | The date and time the result order report was cosigned for this encounter. |
| 17 | `COSIGN_USER_ID` | VARCHAR |  | The unique ID of the system user who cosigned the result order report for this encounter. |
| 18 | `COSIGN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 19 | `REPORT_ORDER_ID` | NUMERIC |  | The unique ID of the order resulted in this encounter, on which the report is based. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `REPORT_ID` | [CLARITY_RPT](CLARITY_RPT.md) | sole_pk | high |

