# NSQIP_OTHER_PROCS

> The NSQIP_OTHER_PROCS table contains information about other procedures associated with the surgery. Other procedures are additional procedures performed on the same panel as the principal operative procedure. Other procedures also include procedures on other panels performed by a surgeon with the same service as the service of the surgeon performing the principal operative procedure. This table is used in conjunction with NSQIP_INFO to provide NSQIP registry data for the surgeries that are selected for NSQIP submission.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NSQIP_OTHER_PROC` | VARCHAR |  | The name of the other procedure. |
| 4 | `NSQIP_OTHER_CPT` | VARCHAR |  | The CPT® code of the other procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

