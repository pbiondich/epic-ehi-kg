# NSQIP_CDIFF_POSITIVE_TEST

> The NSQIP_CDIFF_POSITIVE_TEST table contains the tests that resulted positive for patients with postoperative occurrences of C. diff. The information is part of NSQIP registry submissions.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NSQIP_CDIFF_TEST_C_NAME` | VARCHAR |  | The category ID for the C. diff tests performed that resulted positive for a patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

