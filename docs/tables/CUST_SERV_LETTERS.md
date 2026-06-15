# CUST_SERV_LETTERS

> Extracts list of letters and envelopes attached to Customer Service (NCS) communication.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique identifier for the customer service communication. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LTR_HNO_ID` | VARCHAR |  | The ID of the note record that stores the text of the letter or envelope. |
| 4 | `LTR_ETX_ID` | VARCHAR |  | The ID of the SmartText template record for the letter or envelope. |
| 5 | `LTR_ETX_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 6 | `LTR_SUMMARY` | VARCHAR |  | This column contains the first 254 characters of the letter or envelope associated with the customer service communication. |
| 7 | `LTR_NAME` | VARCHAR |  | The name of the letter or envelope template. |
| 8 | `LTR_CREATE_DATE` | DATETIME |  | The date the letter or envelope was added to the customer service communication. |
| 9 | `LTR_CREATE_TIME` | DATETIME (Local) |  | The time the letter or envelope was added to the customer service communication. |
| 10 | `LTR_USER_ID` | VARCHAR |  | The ID of the user who created the letter or envelope in the customer service communication. |
| 11 | `LTR_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

