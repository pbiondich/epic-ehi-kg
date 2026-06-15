# GUAR_ACCT_STMT_HX

> This table contains statement history information for the guarantor account.

**Primary key:** `ACCOUNT_ID`, `LINE`  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier for the account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STMT_HX_STMT_DATE` | DATETIME |  | The date on which statement was generated. |
| 4 | `STMT_HX_INVOICE_NUM` | VARCHAR |  | The invoice number of the invoice that was sent to the guarantor on this date. |
| 5 | `STMT_HX_NEW_CHARGE` | NUMERIC |  | The original amount of all new charges on this invoice. New charges are those that were not on the last invoice sent. |
| 6 | `STMT_HX_NEW_BALANCE` | NUMERIC |  | The new balance on the statement. |
| 7 | `STMT_HX_TTL_PMT` | NUMERIC |  | Total payment amount on the statement. |
| 8 | `STMT_HX_TTL_DB_ADJ` | NUMERIC |  | Total debit adjustment amount on the statement. |
| 9 | `STMT_HX_TTL_CR_ADJ` | NUMERIC |  | Total credit adjustment amount on the statement. |
| 10 | `STMT_HX_TTL_AMT_HLD` | NUMERIC |  | Total amount held on the statement. |
| 11 | `STMT_HX_TTL_AMT_VD` | NUMERIC |  | Total amount voided since last statement. |
| 12 | `STMT_HX_DVRY_MTHD_C_NAME` | VARCHAR |  | The statement delivery method category ID for the guarantor. |
| 13 | `STMT_HX_LST_VW_DTTM` | DATETIME (UTC) |  | Last date/time when the statement was most recently access from MyChart. |
| 14 | `STMT_HX_1ST_VW_DTTM` | DATETIME (UTC) |  | The date/time when the statement was first accessed from MyChart. |
| 15 | `STMT_HX_WHY_2_PR_C_NAME` | VARCHAR |  | Reason type why the paperless statement is forced to paper statement. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |

