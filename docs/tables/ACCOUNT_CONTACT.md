# ACCOUNT_CONTACT

> This table contains the information recorded in billing system account contact for each account. Each row in this table contains information about one contact and is uniquely identified by the Account ID and line number combination.

**Overflow family:** [ACCOUNT_CONTACT_2](ACCOUNT_CONTACT_2.md)  
**Primary key:** `ACCOUNT_ID`, `LINE`  
**Columns:** 22  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK FK→ | The unique ID for the account record. This ID number could be encrypted if you have elected to implement enterprise reporting’s encryption security function. |
| 2 | `LINE` | INTEGER | PK | Line number to identify the account contact information within the account. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date the contact was recorded. |
| 4 | `USER_ID` | VARCHAR | FK→ | The ID of the system user who recorded the contact. This ID may be encrypted if you have elected to use enterprise reporting’s security utility. |
| 5 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `CONTACT_STATUS_C_NAME` | VARCHAR | org | The category value associated with the activity performed by collections staff on the account, such as No Contact, Check Mailed, Promised Payment, etc. |
| 7 | `TICKLER_DATE` | DATETIME |  | The date the account should be contacted again. |
| 8 | `LETTER_NUMBER` | VARCHAR |  | The letter number of the letter associated with this guarantor. |
| 9 | `REFUND_REQ_ID` | NUMERIC |  | Stores payment transaction numbers of a refund request for the Account Contact activity. |
| 10 | `REFUND_REQ_STATUS_C_NAME` | VARCHAR |  | Stores the refund request status associated with the Account Contact activity. |
| 11 | `REFUND_REQ_AMT` | NUMERIC |  | Stores the amount of the refund request associated with the activity. |
| 12 | `PAYMENT_TXS` | VARCHAR |  | A comma-delimited list of follow-up transactions. |
| 13 | `FOL_UP_CUR_INS_BAL` | NUMERIC |  | Follow-up current insurance balance. |
| 14 | `FOL_UP_CUR_PAT_BAL` | NUMERIC |  | Follow-up current patient balance. |
| 15 | `FOL_UP_ACT_INFO` | VARCHAR |  | This item stores the activity info to be displayed in account contact. |
| 16 | `LETTER_SUMMARY` | VARCHAR |  | A short summary of the letter that was sent to the patient. This can be customized by your organization, and may include information like the patient's name, address and balance. |
| 17 | `LETTER_STATUS_C_NAME` | VARCHAR |  | The letter status category ID for the guarantor, for example "queued" or "sent". |
| 18 | `NOTE_ID` | VARCHAR | shared | The ID of the note associated with this contact. |
| 19 | `FOL_UP_HX_CRM_ID` | NUMERIC |  | Stores the ID for an customer service record that is related to the guarantor. |
| 20 | `FOL_UP_NOTE` | VARCHAR |  | Each guarantor account may have a follow-up note posted to it per contact. This column holds either a system generated or custom note that further describes the contact, if a note was produced. |
| 21 | `LETTER_NAME` | VARCHAR |  | The name of the letter. |
| 22 | `PAPERLESS_UPD_WHY_C_NAME` | VARCHAR | org | Reason for updating the guarantor's MyChart paperless billing status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

