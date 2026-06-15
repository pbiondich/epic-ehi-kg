# INV_EOB_PAID_LINE

> This table holds the service line level secondary information for a non-primary claim. It contains the paid amount and other secondary amounts other than claim adjustments (CAS).

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The invoice record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EOB_LN_CVG_ID` | NUMERIC |  | The line coverage ID for a secondary claim. |
| 4 | `EOB_LN_CLM_LN` | INTEGER |  | This item points to the service line with which this related group line is associated. |
| 5 | `EOB_LN_PAID` | NUMERIC |  | The line level paid amount for a secondary claim. |
| 6 | `EOB_LN_CONTRACT` | NUMERIC |  | The lines contract amount for a secondary claim. |
| 7 | `EOB_LN_DATE` | DATETIME |  | The line adjudication date for a secondary claim. |
| 8 | `EOB_LN_REMIT_IMAGE_ID` | VARCHAR |  | For ANSI secondaries this item may hold a line level matched remittance image (IMD) record ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

