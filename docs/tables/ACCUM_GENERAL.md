# ACCUM_GENERAL

> This table contains general information about accumulation (ACC) records.

**Primary key:** `ACCUMULATION_ID`  
**Columns:** 24  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCUMULATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the accumulation record. |
| 2 | `ACCUM_PAT_ID` | VARCHAR | FK→ | The ID of the associated member. |
| 3 | `ACCUM_DATE` | DATETIME |  | The service date of the accumulation. |
| 4 | `ACCUM_INST_UPDATE_DTTM` | DATETIME (UTC) |  | The instant this accumulation was created. |
| 5 | `ACCUM_USER_ID` | VARCHAR |  | The user the accumulation was applied by. |
| 6 | `ACCUM_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `ACCUM_COMMENT` | VARCHAR |  | The free-text comment associated with the accumulation. |
| 8 | `ACCUM_AMT` | NUMERIC |  | The default accumulation amount. |
| 9 | `ACCUM_SRC_C_NAME` | VARCHAR |  | The source type of the accumulation. |
| 10 | `ACCUM_SRC_CLAIM_ID` | NUMERIC |  | The ID of the associated claim if the accumulation source is a claim. |
| 11 | `ACCUM_SRC_TX_ID` | NUMERIC |  | The ID of the associated service if the accumulation source is a claim. |
| 12 | `REVERSAL_OF_ACC_ID` | NUMERIC |  | The ID of the accumulation record that this record reverses. |
| 13 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status (hidden, soft-deleted, etc...) |
| 14 | `MAN_ACC_EDIT_TYPE_C_NAME` | VARCHAR | org | Indicates if a manual accumulation entry was an accrual, payout, or correction. Data is entered for this item during manual accumulation entry and is not stored for accumulation updates made by the system. |
| 15 | `MAN_ACCUM_IDENT` | VARCHAR |  | Indicates the source of the change. Data is entered for this item during manual accumulation entry and is not stored for accumulation updates made by the system. |
| 16 | `SKIP_CARRYOVER_YN` | VARCHAR |  | This flag will be set if this accumulation should be carried over during carrover. |
| 17 | `ALLOWED_ACCUM_GRP_FUN_TYP_C_NAME` | VARCHAR |  | The functionality types on accumulation groups that this accumulation is allowed to contribute to. |
| 18 | `COUNTED_UNIT_TYPE_C_NAME` | VARCHAR |  | The type of entity counted by this accumulation. |
| 19 | `PAT_PMT_RMT_CAT_C_NAME` | VARCHAR |  | The remittance categorization subtype for the patient payment amount unit type. |
| 20 | `ACCUM_SRC_BEN_EVAL_ID` | NUMERIC |  | The benefits engine evaluator that generated the accumulation. |
| 21 | `ACCUM_SRC_BEN_EVAL_ID_BEN_EVAL_NAME` | VARCHAR |  | The name of the benefit evaluator record. |
| 22 | `ACCUM_SRC_PAYMENT_MECH_ID` | NUMERIC |  | The benefits payment mechanism that generated this accumulation. |
| 23 | `ACCUM_SRC_PAYMENT_MECH_ID_PAYMENT_MECH_NAME` | VARCHAR |  | The name of the payment mechanism record. |
| 24 | `ACCUM_SRC_HTR_TX_ID` | NUMERIC |  | The ID of the associated hospital transaction if the accumulation source is a HB charge. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCUM_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

