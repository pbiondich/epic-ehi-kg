# REHAB_REVIEW_CHOICE

> This table stores the Unique Tracking Number (UTN) and the status for tracking the Review Choice initiative from CMS.

**Primary key:** `SUMMARY_BLOCK_ID`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `REHAB_UTN_IDENT` | VARCHAR |  | This alphanumeric code is used for tracking the review choice affirmation provided by CMS. This Unique Tracking Number (UTN) will need to be included on the final claim on the IRF-PAI. |
| 3 | `REHAB_UTN_STATUS_C_NAME` | VARCHAR | org | This category is used for tracking the status of the Review Choice claim. This is used for filtering in workqueues to help with new workflows required by CMS. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

