# HSP_CLM_EDIT_ERROR

> The HSP_CLM_EDIT_ERROR table contains information about your Hospital Billing claim edit errors. This table will have one row for each error that is on the claim print record (CLP) at the time of the extract. For each daily extract, the data will be appended on to the existing data in this table and this historical data will be preserved. So, if a claim had two errors and was in the claim error pool for three days, there will be six rows for that claim in this table (two rows for each of the three days that the claim had errors). The EXTRACT_DT column can be used to restrict your results to claim errors on a specific day. To see the errors in the claim error pool as of the last extract use EXTRACT_DT = today's date. This assumes the last extract for HSP_CLM_EDIT_ERROR was today. Historical data for this table cannot be rebuilt, so full extracts should not be performed on this table.

**Primary key:** `CLAIM_PRINT_ID`, `EXTRACT_DT`, `OVERALL_LINE`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique ID of the claim record that entered the claim edit workqueue. |
| 2 | `EXTRACT_DT` | DATETIME (Local) | PK | The instant at which the extract occurred (date and time). |
| 3 | `OVERALL_LINE` | INTEGER | PK | This column tracks the overall number of lines in the table for the CLP_ID for the date it was extracted. This produces a unique number for a single CLP_ID for a single extract date. This allows the selection of a single CLP_ID for reporting on total number of CLP's errored in a given day. For any given date, set the report to select on an overall line = 1 to pull a single CLP_ID for each errored CLP into the report. This reduces the chance for record duplication in the report. You are not able to report on the errors on the CLP_ID. |
| 4 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 5 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 6 | `GUARANTOR_ID` | NUMERIC |  | The guarantor ID that appears on the claim. |
| 7 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | The ID of the hospital account that appears on this claim. |
| 8 | `BUCKET_ID` | NUMERIC | shared | The ID of the hospital liability bucket that appears on this claim. |
| 9 | `COVERAGE_ID` | NUMERIC | FK→ | The coverage ID that appears on the claim. |
| 10 | `PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 11 | `BENEFIT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 12 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 13 | `TOTAL_CHARGES` | NUMERIC |  | The dollar amount of charges on the claim. |
| 14 | `TOTAL_PAYMENTS` | NUMERIC |  | The dollar amount in payments that appear on the claim. This applies to claims that have already had payments made on them. |
| 15 | `AMOUNT_DUE` | NUMERIC |  | The dollar amount due from the claim. For cancel claims, the amount due is always zero. For other claims, this is the amount of charges on the bucket minus any payments, adjustments, or previous credits. In cases where a payment, adjustment, or previous credit could be applied to more than one claim, the amount is prorated based on the ratio of the claim charge amount to the total charge amount of all applicable claims on that bucket. |
| 16 | `INVOICE_NUMBER` | VARCHAR |  | The invoice number that appears on the claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

