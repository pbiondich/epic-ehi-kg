# MC_PRICER_METADATA

> This table contains a variety of metadata returned from the Epic Pricer.

**Primary key:** `PRICER_MSG_ID`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRICER_MSG_ID` | NUMERIC | PK shared | The unique identifier for the Epic Pricer message record. |
| 2 | `MC_PRICER_TYPE_C_NAME` | VARCHAR |  | The pricer type calculated by the Epic Pricer. |
| 3 | `PRICER_RETURN_CODE` | VARCHAR |  | The return code returned from the Epic Pricer. |
| 4 | `PRICER_PROV_CCN` | VARCHAR |  | The CMS Certified Numer (CCN) used when the Epic Pricer was invoked. |
| 5 | `PRICER_CCN_EFF_DATE` | DATETIME |  | The effective date associated with the CCN in column PRICER_PROV_CCN for the Epic Pricer. |
| 6 | `MC_PRICER_PROV_TYPE_C_NAME` | VARCHAR |  | The Instituional provider type defined by CMS. |
| 7 | `MPFS_STATUS_INDICATOR_C_NAME` | VARCHAR |  | The status indicator returned for a service priced using a physician fee schedule. The released values are extracted from the CMS Medicare physician fee schedule and are owned by CMS. |
| 8 | `ASC_PAYMENT_INDICATOR_C_NAME` | VARCHAR |  | The payment indicator returned for a service priced using an ASC fee schedule. The released values are extracted from the CMS ASC fee schedule and are owned by CMS. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

