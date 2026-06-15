# DENT_TREAT_HX

> This table contains history items of changes in dental treatments.

**Primary key:** `TREATMENT_ID`, `LINE`  
**Columns:** 21  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_ID` | NUMERIC | PK FK→ | The unique identifier for the treatment plan record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TPL_MOD_INSTANT_DTTM` | DATETIME (Local) |  | Stores date and time for when the dental treatment was modified. |
| 4 | `TPL_MOD_USER_ID` | VARCHAR |  | User who modifies data in a treatment record |
| 5 | `TPL_MOD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `TR_LINKED_CSN` | NUMERIC |  | Stores the patient encounter in which a particular piece of the treatment record was modified if it was available. |
| 7 | `TR_COMP_INST_HIST_DTTM` | DATETIME (Local) |  | Stores the revision history for the completed date and time of a treatment |
| 8 | `TR_STATUS_HX_C_NAME` | VARCHAR |  | stores the revision history of treatment status |
| 9 | `TR_START_DATE_HIST_DT` | DATETIME |  | stores the revision history for start date for a treatment |
| 10 | `TR_ORDER_NUM_HX` | INTEGER |  | stores revision history of sequence number of a treatment |
| 11 | `DENT_SER_HX_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 12 | `TREAT_CHRON_INSTANT_DTTM` | DATETIME (Attached) |  | This column records the date and time of a documentation change to the dental treatment. |
| 13 | `DENT_OPT_STAT_HX_C_NAME` | VARCHAR |  | The history of changes to the status of a treatment option within a dental treatment. |
| 14 | `DENT_HB_ESTIMATE_YN` | VARCHAR |  | This flag indicates whether the an estimate was calculated for the dental treatment option at a given time. |
| 15 | `DENT_HB_GUARANTOR_ID` | NUMERIC |  | The guarantor used when calculating estimates for the dental treatment option. This only applies to Hospital Billing (HB) estimates. |
| 16 | `DENT_HB_PRIMARY_CVG_ID` | NUMERIC |  | The primary coverage used when calculating the dental treatment option's estimate. This only applies to Hospital Billing (HB) estimates. |
| 17 | `TR_APRV_DTTM_HX_DTTM` | DATETIME (Attached) |  | The revision history for the date and time when the treatment was approved. |
| 18 | `TR_APRV_USER_HX_ID` | VARCHAR |  | The revision history containing the unique ID for the user who approved the treatment. |
| 19 | `TR_APRV_USER_HX_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 20 | `TR_APRV_STATUS_HX_C_NAME` | VARCHAR |  | The revision history of the approval status category ID for the treatment. |
| 21 | `TR_RSCND_RSN_HX_C_NAME` | VARCHAR | org | The revision history for the rescind reason category ID for the treatment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TREATMENT_ID` | [DENT_TREATMENT](DENT_TREATMENT.md) | sole_pk | high |

