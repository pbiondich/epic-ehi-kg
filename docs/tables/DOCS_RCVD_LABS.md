# DOCS_RCVD_LABS

> This table contains a list of name and address information for various performing sites data has been received from.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `LAB_REFERENCE_IDENT` | VARCHAR |  | Stores the reference ID of a performing site. The reference ID is the checksum of name, street address, city, state, postal code, phone number, and CLIA number in that order. |
| 4 | `LAB_NAME` | VARCHAR |  | Stores the name of a performing site associated with either a result component, the narrative, or the impression |
| 5 | `LAB_DIRECTOR` | VARCHAR |  | Stores the director of the performing site associated with either a result component, the narrative, or the impression |
| 6 | `LAB_STREET` | VARCHAR |  | Stores the street address of the performing site associated with either a result component, the narrative, or the impression |
| 7 | `LAB_CITY` | VARCHAR |  | Stores the city of the performing site associated with either a result component, the narrative, or the impression |
| 8 | `LAB_STATE_C_NAME` | VARCHAR | org | Stores the state of the performing site associated with either a result component, the narrative, or the impression |
| 9 | `LAB_POSTAL_CODE` | VARCHAR |  | Stores the postal code of the performing site associated with either a result component, the narrative, or the impression |
| 10 | `LAB_PHONE_NUM` | VARCHAR |  | Stores the phone number of the performing site associated with either a result component, the narrative, or the impression. |
| 11 | `LAB_CLIA_NUM` | VARCHAR |  | Stores the CLIA number of the performing site associated with either a result component, the narrative, or the impression |
| 12 | `LAB_OBFUSCATED_ID` | VARCHAR |  | Stores the Obfuscated ID of a resulting agency. Populated only on the Cosmos Host. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

