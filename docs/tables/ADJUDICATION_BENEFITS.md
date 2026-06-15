# ADJUDICATION_BENEFITS

> This table contains information about the levels of the adjudication formula that were used to price this service, including how the amounts were divided between those services.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BENEFIT_LEVEL` | VARCHAR |  | The level used in adjudication benefits calculation. |
| 4 | `LIMIT_VARIABLE_ID` | NUMERIC |  | The limit variable used by the level in adjudication benefits calculation. |
| 5 | `LIMIT_VARIABLE_ID_BEN_VAR_NAME` | VARCHAR |  | The name of the benefit variable. |
| 6 | `BEN_LMT_VAR_SPEC_C_NAME` | VARCHAR |  | The limit type of the limit variable used by the level in adjudication benefits calculation. |
| 7 | `LIMIT_AMOUNT` | NUMERIC |  | The limit amount at the level in adjudication benefits calculation. |
| 8 | `LIMIT_REMAINING` | NUMERIC |  | The limit amount remaining at the level in adjudication benefits calculation. |
| 9 | `PAYMENT_VARIABLE_ID` | NUMERIC |  | The payment variable used by the level in adjudication benefits calculation. |
| 10 | `PAYMENT_VARIABLE_ID_BEN_VAR_NAME` | VARCHAR |  | The name of the benefit variable. |
| 11 | `PAY_METHOD_EPP_C_NAME` | VARCHAR |  | The payment type for the payment variable used by the level in adjudication benefits calculation. |
| 12 | `PAYMENT_AMOUNT` | NUMERIC |  | The payment amount for the payment variable used by the level in adjudication benefits calculation. |
| 13 | `COVERED_AMOUNT` | NUMERIC |  | The covered amount used by the level in adjudication benefits calculation. |
| 14 | `COVERED_QUANTITY` | NUMERIC |  | The covered quantity used by the level in adjudication benefits calculation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

