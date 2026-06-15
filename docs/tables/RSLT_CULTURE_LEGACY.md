# RSLT_CULTURE_LEGACY

> This table stores legacy information about microbiology culture identification results.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MEDIA_CONTAINER_TYPE_ID` | VARCHAR |  | The unique ID for the media plate container type associated with an observation on the culture identification. |
| 4 | `MEDIA_CONTAINER_TYPE_ID_CONTAINER_TYPE_NAME` | VARCHAR |  | The name of the container type record. |
| 5 | `DESCRIPTION` | VARCHAR |  | The description of an observation for the culture identification. |
| 6 | `REPORT_YN` | VARCHAR |  | Indicates whether the culture identification will be reported to the patient's chart. 'Y' indicates that the culture identification will be reported. 'N' or NULL indicate that the culture identification will not be reported. |
| 7 | `CMT_MICRO_QUANTITY_C_NAME` | VARCHAR | org | The quantity category ID for the culture identification. |
| 8 | `MICRO_GENUS_C_NAME` | VARCHAR | org | The Genus category ID for the culture identification. |
| 9 | `MICRO_SPECIES_C_NAME` | VARCHAR | org | The Species category ID for the culture identification. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

