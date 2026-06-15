# EMBRYOLOGY_SPECIMEN

> Contains information about oocyte, embryo, sperm, or tissue specimens.

**Primary key:** `SPECIMEN_ID`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the specimen record. |
| 2 | `REI_SPEC_STATE_C_NAME` | VARCHAR |  | The state of a specimen in an embryology or andrology lab. This tracks whether a specimen is currently in-culture, frozen, discarded, etc. |
| 3 | `EMB_SPEC_TYPE_C_NAME` | VARCHAR |  | The type of embryology specimen: oocyte, embryo, sperm, or tissue. |
| 4 | `EMB_SPEC_RECEIVE_CULTURE_DAY` | INTEGER |  | This item stores the number of culture days that have occurred for the specimen when it was received in the lab. |
| 5 | `EMB_SPEC_EXT_RETRIEVAL_DATE` | DATETIME |  | This item stores the date on which the oocyte or tissue retrieval occurred for the given embryology specimen. |
| 6 | `EMB_SPEC_EXTERNAL_FREEZE_DATE` | DATETIME |  | This item stores the date on which the embryology specimen was frozen. |
| 7 | `EMB_SPEC_EXTERNAL_COMMENTS` | VARCHAR |  | This item stores relevant comments associated with the embryology specimen that came from an external lab. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

