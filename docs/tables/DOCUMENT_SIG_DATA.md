# DOCUMENT_SIG_DATA

> Contains data about the signatures collected for an electronic signature document.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique identifier for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SIG_IMAGE_FILE` | VARCHAR |  | Stores the key of a signature image file for a e-signature document. |
| 4 | `SIGNATURE_NAME` | VARCHAR |  | Stores the name of the signature from the signature template record for the signature collected in this field. |
| 5 | `SIG_TIMESTAMP_DTTM` | DATETIME |  | Stores the date and time that this signature was collected. |
| 6 | `AUTH_USER_ID` | VARCHAR |  | The unique ID of the Hyperspace user who has signed the corresponding document signature. |
| 7 | `AUTH_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `AUTH_MYPT_ID` | VARCHAR |  | The unique ID of the patient portal (MyChart) user who has signed the corresponding document signature. |
| 9 | `SIGNATURE_HIDDEN_YN` | VARCHAR |  | Whether the signature field is hidden on the document. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

