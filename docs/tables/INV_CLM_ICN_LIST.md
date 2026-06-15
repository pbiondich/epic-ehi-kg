# INV_CLM_ICN_LIST

> This table holds information on all internal control numbers (ICN) associated with an invoice record in Resolute Professional Billing. This ICN list is compiled from multiple sources including manual overrides, claim status responses, and posted payments.

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the invoice record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLAIM_ICN` | VARCHAR |  | Contains an Internal Control Number (ICN) that was either received or overridden for this claim. |
| 4 | `COVERAGE_ID` | NUMERIC | FK→ | Contains the coverage ID associated with an Internal Control Number (ICN). |
| 5 | `CROSSOVER_FLAG` | NUMERIC |  | Contains a numeric counter that identifies crossover Internal Control Numbers (ICNs). |
| 6 | `INVOICE_NUM` | VARCHAR |  | Contains the invoice number that received an Internal Control Number (ICN). |
| 7 | `ICN_SOURCE_C_NAME` | VARCHAR |  | Indicates the source workflow that saved an Internal Control Number (ICN) to this invoice. |
| 8 | `SOURCE_PMT_TX_ID` | NUMERIC |  | Indicates the payment (ETR) ID that added this Internal Control Number (ICN) to the invoice. |
| 9 | `SOURCE_CLAIM_RECON_ID` | VARCHAR |  | Indicates the Claims Reconciliation Database (CRD) record ID that added this Internal Control Number (ICN) to the invoice. |
| 10 | `ICN_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | Displays the most recent time (in UTC) that this Internal Control Number (ICN) was updated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

