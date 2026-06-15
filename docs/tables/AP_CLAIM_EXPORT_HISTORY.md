# AP_CLAIM_EXPORT_HISTORY

> This table contains the history of a claim's outgoing 837 exports and encounter reporting data.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXPORT_TYPE_C_NAME` | VARCHAR | org | The export type for this row of export history. |
| 4 | `EXPORT_SUBTYPE_C_NAME` | VARCHAR |  | The export subtype for this row of export history, if there is a subtype for the export. |
| 5 | `EXPORT_BATCH_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 6 | `CLAIM_RUN_IDENT` | INTEGER |  | The export batching claim run ID that processed and includes this claim. If a claim errored during processing due to edit checks, no claim run identifier is set in this column. |
| 7 | `CLAIM_RECON_ID` | VARCHAR |  | The unique ID of the Claim Reconciliation record that tracks the encounter and reconciliation data for this row. |
| 8 | `EXPORT_DEST_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 9 | `EXPORT_CEV_RECORD_ID` | NUMERIC |  | The unique ID of the most recent claim values record created for this row's outgoing claim export data. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

