# DOCS_RCVD_CLM

> This table stores information about claims received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 18  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CLAIM_SRC_PAYER_C_NAME` | VARCHAR | org | This item stores the claim's source payer. |
| 6 | `CLAIM_SRC_NAME` | VARCHAR |  | This item stores the free text name of the source of the claim. |
| 7 | `CLAIM_SRC_ID` | VARCHAR |  | This item stores the identifier of the claim. |
| 8 | `CLAIM_START_DATE` | DATETIME |  | This item stores the date on the claim that services were first rendered. |
| 9 | `CLAIM_END_DATE` | DATETIME |  | This item stores the date on the claim that services were last rendered. |
| 10 | `CLAIM_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 11 | `CLAIM_LOC_TEXT` | VARCHAR |  | This item stores the free text location of the claim. |
| 12 | `CLAIM_LOC_ADDR_STREET` | VARCHAR |  | This item stores the street component of the address for the claim's source. |
| 13 | `CLAIM_LOC_ADDR_CITY` | VARCHAR |  | This item stores the city component of the address for the claim's source. |
| 14 | `CLAIM_LOC_ADDR_STATE` | VARCHAR |  | This item stores the state component of the address for the claim's source. |
| 15 | `CLAIM_LOC_ADDR_ZIP` | VARCHAR |  | This item stores the zip code component of the address for the claim's source. |
| 16 | `CLAIM_LOC_ADDR_COUNTRY` | VARCHAR |  | This item stores the country component of the address for the claim's source. |
| 17 | `CLAIM_EVENT_ID` | VARCHAR |  | This item holds the event identifier of the event information for the claim. |
| 18 | `CLAIM_IS_RMVD_YN` | VARCHAR |  | Used for auditing purposes to mark whether or not a claim source was removed from the source record |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

