# DOC_INFO_CE_ORGS

> Care Everywhere Organization patient authorization related items.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | ID of the document record |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `AUTH_SCAN_STATUS_C_NAME` | VARCHAR |  | Scan status for a Care Everywhere authorization form |
| 4 | `AUTH_NO_SCAN_REASON` | VARCHAR |  | This item specifies the reason why a user did not attach a scan to a Care Everywhere authorization |
| 5 | `SIGNED_COLL_USER_ID` | VARCHAR |  | The ID of the user who last set the authorization status to 'signed' |
| 6 | `SIGNED_COLL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `SIGNED_DTTM` | DATETIME (Attached) |  | The instant a signed authorization was received |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

