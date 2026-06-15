# HSP_BDC_DENIAL_DATA

> This table contains denial information stored in the Denial/Remark/Correspondence records in the Denial/Correspondence (BDC) master file. There can be multiple lines of data for each record. Each line represents one claim/explanations of benefits (EOB) line that was denied.

**Primary key:** `BDC_ID`, `LINE_COUNT`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BDC_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the denial or correspondence record. |
| 2 | `LINE_COUNT` | INTEGER | PK | Line number of denial data. There can be multiple lines of denial data and this is the number of the line that enterprise reporting is extracting. |
| 3 | `LINE_ON_EOB` | INTEGER |  | This column stores the line on explanation of benefits that was denied. "-1" represents the total denial data that is the sum of the invoice-level and sum of line-level data. "0" represents the invoice-level data. |
| 4 | `LINE_BILLED_AMOUNT` | NUMERIC |  | Billed amount on the claim line that was denied. If the denial was at the invoice level - this is the billed amount for the entire claim |
| 5 | `LINE_ALLWD_AMT` | NUMERIC |  | The payment allowed amount for claim line that was denied. If the denial was for the entire invoice this is the allowed amount on the entire payment. |
| 6 | `LINE_PAID_AMT` | NUMERIC |  | This column stores the amount paid for the line that was denied. $0.00 if fully denied, >0 if partially denied. If the denial was for the entire invoice then this is the amount paid for the entire claim. |
| 7 | `LINE_DENIED_AMT` | NUMERIC |  | Denied amount for claim line that was denied. If the denial is for the entire invoice then this is the denied amount for the claim. |
| 8 | `LINE_COMMENTS` | VARCHAR |  | This column stores comments on explanation of benefits for denied line. |
| 9 | `LINE_REVENUE_CODE_ID` | NUMERIC |  | This column stores the unique identifier for the line-level revenue code for the denial. |
| 10 | `LINE_REVENUE_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 11 | `LINE_CPT_CODE` | VARCHAR |  | This item stores the line-level CPT(R) code for the denial. |
| 12 | `LINE_PRIMARY_CHARGE_TX_ID` | NUMERIC |  | Charge with the greatest amount from the claim line that was denied. If two charges have the same amount the older one will be the primary charge. |
| 13 | `LINE_SERVICE_DATE` | DATETIME |  | The line level service date of the denial. |
| 14 | `LINE_QUANTITY` | NUMERIC |  | The line level quantity for the denied line. |
| 15 | `LINE_ON_CLAIM` | INTEGER |  | This item stores the line-level expected allowed amount for the denied claim line. |
| 16 | `LINE_EXPECTED_ALLOWED_AMT` | NUMERIC |  | This item stores the line-level expected allowed amount for the denied claim line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BDC_ID` | [BDC_INFO](BDC_INFO.md) | sole_pk | high |

