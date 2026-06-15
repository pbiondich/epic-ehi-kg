# FA_NOTES_QUERY_RESP

> Query data for the Financial Information Query.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `QRY_INCOME_TYPE_C_NAME` | VARCHAR | org | Stores data that was received in response to a financial information query from Financial Assistance. This is the type of income (I FNC 131) the patient or patient contact has. |
| 4 | `QRY_EXPENSE_TYPE_C_NAME` | VARCHAR | org | Stores data that was received in response to a financial information query from Financial Assistance. This is the type of expense (I FNC 151) the patient or patient contact has. |
| 5 | `QRY_ASSET_TYPE_C_NAME` | VARCHAR | org | Stores data that was received in response to a financial information query from Financial Assistance. This is the type of asset (I FNC 171) the patient or patient contact has. |
| 6 | `QRY_FREQUENCY_C_NAME` | VARCHAR |  | Stores data that was received in response to a financial information query from Financial Assistance. This is the frequency at which the amount applies to the patient or patient contact. |
| 7 | `QRY_AMOUNT` | NUMERIC |  | Stores data that was received in response to a financial information query from Financial Assistance. This is the monetary amount. |
| 8 | `QRY_NUM_HOURS` | INTEGER |  | Stores data that was received in response to a financial information query from Financial Assistance. This is the number of hours the patient or patient contact works. This is used to calculate hourly income. |
| 9 | `QRY_PAT_ID` | VARCHAR | FK→ | Stores data that was received in response to a financial information query from Financial Assistance. This is the patient the financial data pertains to. |
| 10 | `QRY_PAT_REL_ID` | NUMERIC |  | Stores data that was received in response to a financial information query from Financial Assistance. This is the patient contact the financial data pertains to. |
| 11 | `QRY_ERR_CODE` | VARCHAR |  | Stores an error code that was received in response to a financial information query from Financial Assistance. |
| 12 | `QRY_ERR_MSG` | VARCHAR |  | Stores the description of the error that was received in response to a financial information query from Financial Assistance. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `QRY_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

