# BUNDLE_CHARGE_MAIN

> Main bundleable charge line table.

**Primary key:** `RECORD_ID`  
**Columns:** 26  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the bundleable charge line record. |
| 2 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 3 | `ACCT_ID` | NUMERIC | shared | The unique ID of the account that is associated with this bundleable charge line record. |
| 4 | `ACCT_SERIAL_NUM` | INTEGER |  | The account serial number associated with this charge. |
| 5 | `CVG_ID` | NUMERIC | FK→ | The unique ID of the coverage that is associated with this bundleable charge line record. |
| 6 | `DO_NOT_BILL_INS_YN` | VARCHAR |  | Indicates whether to not bill insurance for this charge. Y indicates that the charge should not be billed to insurance. |
| 7 | `SERVICE_DATE` | DATETIME |  | The date of service for this charge. |
| 8 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 9 | `REQ_GROUPER_ID` | NUMERIC |  | The unique ID of the requisition grouper that is associated with this bundleable charge line record. |
| 10 | `SUBMITTER_ID` | NUMERIC |  | The unique ID of the submitter that is associated with this bundleable charge line record. |
| 11 | `SUBMITTER_ID_RECORD_NAME` | VARCHAR |  | The name of the submitter record. |
| 12 | `PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 13 | `FINANCIAL_CLASS_C_NAME` | VARCHAR | org | The financial class category number for the bundleable charge line record. |
| 14 | `ORDERING_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 15 | `PERFORMING_LAB_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |
| 16 | `CHARGE_TYPE_C_NAME` | VARCHAR |  | The linked charge type category ID for the bundleable charge line. |
| 17 | `NOT_CHARGE_REASON_C_NAME` | VARCHAR | org | The category ID of the reason the charge was voided. |
| 18 | `NOT_CHARGE_USER_ID` | VARCHAR |  | The unique ID of the user who voided this charge. |
| 19 | `NOT_CHARGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 20 | `NOT_CHARGE_COMMENT` | VARCHAR |  | The comment entered by the user who voided this charge. |
| 21 | `NOT_CHARGE_UTC_DTTM` | DATETIME (UTC) |  | The date and time when this charge was voided. |
| 22 | `TASK_ID_C_NAME` | VARCHAR | org | The task category ID that triggered the charge. |
| 23 | `PERFORMING_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 24 | `BILL_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 25 | `SERV_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 26 | `PAT_CSN` | NUMERIC | FK→ | The unique patient contact series number that is associated with this bundleable charge line record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |
| `PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

