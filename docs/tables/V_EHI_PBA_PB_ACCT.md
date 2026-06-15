# V_EHI_PBA_PB_ACCT

> This view filters out account data that is not appropriate for member level EHI exports when group billing is used.

**Primary key:** `PB_ACCT_ID`  
**Columns:** 18  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_ACCT_ID` | VARCHAR | PK FK→ | The unique ID for the premium billing account. |
| 2 | `BILL_ADDR1` | VARCHAR |  | Street address line 1 for premium billing account billing address. |
| 3 | `BILL_ADDR2` | VARCHAR |  | Street address line 2 for premium billing account billing address. |
| 4 | `BILL_CITY` | VARCHAR |  | City for premium billing account billing address. |
| 5 | `BILL_STATE_C_NAME` | VARCHAR | org | State for premium billing account billing address. |
| 6 | `BILL_ZIP` | VARCHAR |  | ZIP Code for premium billing account billing address. |
| 7 | `BILL_COUNTY_C_NAME` | VARCHAR | org | County for premium billing account billing address. |
| 8 | `BILL_COUNTRY_C_NAME` | VARCHAR | org | Country for premium billing account billing address. |
| 9 | `BILL_PHONE` | VARCHAR |  | Billing phone number for premium billing account. |
| 10 | `BILL_FAX` | VARCHAR |  | Billing fax number for premium billing account. |
| 11 | `BILL_EMAIL` | VARCHAR |  | Billing e-mail address for premium billing account. |
| 12 | `INVMSG_NOTE_ID` | VARCHAR |  | The unique ID of note to be included on premium billing invoices for the premium billing account. |
| 13 | `BAL_DUE` | NUMERIC |  | Balance due for the premium billing account. |
| 14 | `HIX_ACCT_BAL_DUE` | NUMERIC |  | This item contains the subscriber's portion of the balance due on the associated group premium billing account. |
| 15 | `TOTAL_BAL_DUE` | NUMERIC |  | This item contains the total of the account balance plus the subscriber's portion of the balance due on the associated group premium billing account. |
| 16 | `AR_ACCT_BALANCE` | NUMERIC |  | The account balance stores the sum of all transaction amounts for transactions that have filed to the account. |
| 17 | `BILL_HOUSE_NUM` | VARCHAR |  | House number for premium billing account billing address. |
| 18 | `BILL_DISTRICT_C_NAME` | VARCHAR | org | District for the premium billing account billing address. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_ACCT_ID` | [PB_ACCT](PB_ACCT.md) | name_stem | high |

