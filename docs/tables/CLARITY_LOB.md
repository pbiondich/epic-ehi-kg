# CLARITY_LOB

> The CLARITY_LOB table contains information from the line of business master file.

**Primary key:** `LOB_ID`  
**Columns:** 3  
**Joined by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOB_ID` | VARCHAR | PK | The unique ID for the line of business record. |
| 2 | `LOB_ID_LOB_NAME` | VARCHAR |  | The name of the line of business record. |
| 3 | `LOB_NAME` | VARCHAR |  | The name of the line of business record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (6)

| From | Column | Confidence |
|------|--------|------------|
| [APPEAL_GRV](APPEAL_GRV.md) | `LOB_ID` | high |
| [AUTH_REQUEST](AUTH_REQUEST.md) | `LOB_ID` | high |
| [CASE_MGMT](CASE_MGMT.md) | `LOB_ID` | high |
| [CUST_SERVICE](CUST_SERVICE.md) | `LOB_ID` | high |
| [LCI_CONTACT_DATA](LCI_CONTACT_DATA.md) | `LOB_ID` | high |
| [MEM_LIST_REPL](MEM_LIST_REPL.md) | `LOB_ID` | high |

