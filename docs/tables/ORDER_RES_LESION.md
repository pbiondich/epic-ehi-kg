# ORDER_RES_LESION

> The ORDER_RES_LESION table contains information about breast imaging findings and pathology results. Specifically, the MAMMO_LESION_ID column contains the lesion associated with the breast imaging finding or the pathology result. A lesion may be linked to multiple findings if the lesion was evaluated on multiple imaging exams. A lesion may be linked to multiple pathology results if the lesion was biopsied multiple times.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MAMMO_LESION_ID` | NUMERIC |  | This column contains breast lesion IDs. In mammography, each lesion might have more than one finding record that contains information such as radiologist findings and pathology results. All finding records that are for the same lesion are linked to the lesion record using lesion IDs. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

