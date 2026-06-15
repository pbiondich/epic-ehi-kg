# ORG_DETAILS

> Details about the organization. Includes external name, phone/e-mail, hours of operation, HSI, URL.

**Primary key:** `ORGANIZATION_ID`  
**Columns:** 3  
**Joined by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORGANIZATION_ID` | NUMERIC | PK | The unique ID associated with the organization for this row. |
| 2 | `ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 3 | `EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (4)

| From | Column | Confidence |
|------|--------|------------|
| [CLAIM_REFERENCE_DATA](CLAIM_REFERENCE_DATA.md) | `ORGANIZATION_ID` | high |
| [DIFFERENCE_PERIOD_EVENT](DIFFERENCE_PERIOD_EVENT.md) | `ORGANIZATION_ID` | high |
| [IB_MESSAGES](IB_MESSAGES.md) | `ORGANIZATION_ID` | high |
| [LCA_COMM_USERS](LCA_COMM_USERS.md) | `ORGANIZATION_ID` | high |

