# AN_HSB_LINK_INFO

> This table stores Anesthesia episode-level information.

**Primary key:** `SUMMARY_BLOCK_ID`  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID of the Episode (HSB) record for this row. Episodes store information including the start and end dates, episode status and type, and any contacts associated with the episode. |
| 2 | `ANES_EPT_CSN_LINK` | NUMERIC |  | Patient encounter linked to this episode, if one exists (true for surgical or scheduled reasons, false for order or other reasons). |
| 3 | `AN_UNLINKED_FLAG_YN` | VARCHAR |  | Flag indicating that episode is not linked to a reason. |
| 4 | `ANES_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 5 | `ANES_PROC_DATE` | DATETIME |  | Stores the date for the procedure of the anesthesia episode. |
| 6 | `ANES_PRE_OP_DIAG_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 7 | `ANES_PROC_TIME` | DATETIME (Local) |  | Stores the time when the procedure associated with the anesthesia episode was performed. |
| 8 | `ANES_PROC_CMT` | VARCHAR |  | Comment for anesthesia procedure. |
| 9 | `ANES_PREOP_COMP_YN` | VARCHAR |  | This item indicates whether Pre-op documentation has been completed for Anesthesia. |
| 10 | `ANES_INTRAOP_COM_YN` | VARCHAR |  | This item indicates whether Intra-op documentation has been completed for Anesthesia. |
| 11 | `ANES_PACU_COMP_YN` | VARCHAR |  | This item indicates whether PACU documentation has been completed for Anesthesia. |
| 12 | `ANES_POSTOP_COMP_YN` | VARCHAR |  | This item indicates whether Post-op documentation has been completed for Anesthesia. |
| 13 | `ANES_DOC_COMP_YN` | VARCHAR |  | This item indicates whether or not the anesthetic record is complete. |
| 14 | `AN_DOC_COMP_INSTANT` | DATETIME (Local) |  | The instant that all documentation for an anesthesia episode was marked as complete. |
| 15 | `AN_BATCH_CLS_DON_YN` | VARCHAR |  | This item indicates whether the batch job that closes Anesthesia records has run on this record. It will be set to No with the Anesthesia record is marked completed and Yes when all the constituent contacts are closed. |
| 16 | `AN_RESP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 17 | `AN_DATE` | DATETIME |  | Stores the anesthesia procedure date for the anesthesia record. |
| 18 | `AN_TIME` | DATETIME (Local) |  | Stores the time when the procedure associated with the anesthesia record was performed. |
| 19 | `AN_START_DATETIME` | DATETIME (Local) |  | Stores the instant at which anesthesia started for the anesthesia record. |
| 20 | `AN_STOP_DATETIME` | DATETIME (Local) |  | Stores the instant at which anesthesia stopped for the anesthesia record. |
| 21 | `NAME` | VARCHAR |  | The name of the anesthesia episode. |
| 22 | `AN_52_ENC_CSN_ID` | NUMERIC | FK→ | Stores the unique contact serial number for the 52-Anesthesia patient encounter associated with the anesthesia record. This number is unique across all patient encounters in any given system. |
| 23 | `AN_RECORD_DATE` | DATETIME |  | The date for this anesthesia record. |
| 24 | `AN_BILLING_CSN_ID` | NUMERIC |  | The unique contact serial number for the Billing Encounter. This contains all the billing information needed to drop charges. |
| 25 | `PRIMARY_LOG_ENC_CSN` | NUMERIC | FK→ | Identifies the anesthesia record's primary log encounter contact serial number (CSN). |
| 26 | `PRIMARY_PRC_ENC_CSN` | NUMERIC | FK→ | Identifies the primary procedure's encounter contact serial number (CSN). |
| 27 | `AN_PRIMARY_NOTE_ID` | VARCHAR |  | Indicates which note record (HNO) to treat as the anesthesia preop note. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AN_52_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PRIMARY_LOG_ENC_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PRIMARY_PRC_ENC_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

