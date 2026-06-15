# CLARITY_VENDOR

> The CLARITY_VENDOR table contains basic data about the various organizations to which you pay checks. These vendors may receive AP claims payments, PCP capitation, or specialty capitation payments.

**Primary key:** `VENDOR_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 2 | `VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 3 | `DFLT_UB_PRICING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

