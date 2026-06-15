# PAT_ENC_CLAIMS

> This table stores claim-related information for the patient encounter.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 5 | `EXPRESS_CLAIM_TRIGGERED_YN` | VARCHAR |  | Indicates whether express claims were triggered. "Y" indicates that Express Claims Processing was initiated for the patient encounter. "N" or NULL indicates that Express Claims Processing was not initiated for the patient encounter. |
| 6 | `EC_TRIGGERED_UTC_DTTM` | DATETIME (UTC) |  | the instant of the most recent attempt to trigger Express Claims |
| 7 | `EXPR_CLM_NOT_TRGR_RSN_C_NAME` | VARCHAR |  | the most recent reason that Express Claims were not triggered |
| 8 | `NO_TRGR_INVOICE_ID` | NUMERIC |  | the invoice that was previously created |
| 9 | `NO_TRGR_UCL_ID` | VARCHAR |  | the charge that was not ready for claim creation |
| 10 | `NO_TRGR_WORKQUEUE_ID` | VARCHAR |  | the workqueue that held the charge |
| 11 | `NO_TRGR_WORKQUEUE_ID_WORKQUEUE_NAME` | VARCHAR |  | The name of the workqueue |
| 12 | `NO_TRGR_TAR_ID` | NUMERIC |  | the charge session that was not ready for claim creation |
| 13 | `NO_TRGR_ORDER_ID` | NUMERIC |  | the order that needed charges triggered or that was awaiting transmittal |
| 14 | `NO_TRIG_RECORD_ID` | NUMERIC |  | the unprocessed charge entry batch |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

