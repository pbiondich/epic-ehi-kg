# CARE_PATH_HX_AUDIT

> Audit information for care path step documentation.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `CM_LOG_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| 5 | `STEP_HX_AUDIT` | INTEGER |  | Audit information for item HSB-70010 - CI CARE PATH HX STEP. |
| 6 | `INST_HX_AUDIT_UTC_DTTM` | DATETIME (UTC) |  | Audit information for item HSB-70020 - CI CARE PATH HX INSTANT. |
| 7 | `USER_HX_AUDIT_USER_ID` | VARCHAR |  | Audit information for item HSB-70030 - CI CARE PATH HX USER. |
| 8 | `USER_HX_AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `LINK_HX_AUDIT` | INTEGER |  | Audit information for item HSB-70040 - CI CARE PATH HX LINK. |
| 10 | `ALT_HX_AUDIT_ALERT_CSN_ID` | NUMERIC |  | Audit information for item HSB-70050 - CI CARE PATH HX ALT. |
| 11 | `EFF_HX_AUDIT_DATE` | DATETIME |  | Audit information for item HSB-70060 - CI CARE PATH HX EFFECTIVE DATE. |
| 12 | `CARE_PATH_EVT_HX_AUDIT_C_NAME` | VARCHAR |  | Audit information for care path step documentation. This item stores the type of modification that occurred. |
| 13 | `WHO_HX_AUDIT_USER_ID` | VARCHAR |  | Audit information for the user who edited a care path step. |
| 14 | `WHO_HX_AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `WHEN_HX_AUDIT_UTC_DTTM` | DATETIME (UTC) |  | Audit information for when a care path step was edited. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

