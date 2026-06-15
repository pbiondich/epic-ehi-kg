# OR_IMP_IMPLANT

> The OR_IMP_IMPLANT table contains implantation information for implants that were marked as being implanted for a surgery or invasive procedure .

**Primary key:** `IMPLANT_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique ID of the implant record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the implant information for the implant. |
| 3 | `IMPLANTED_DATE` | DATETIME |  | The date the implant was implanted. |
| 4 | `IMPLANT_LOG_ID` | VARCHAR |  | The unique ID of the log in which the implant was implanted. |
| 5 | `MANUF_NOTIFY_DATE` | DATETIME |  | The date the manufacturer was notified of the implantation of the implant. |
| 6 | `IMPLANTED_TIME` | DATETIME (Local) |  | The time when the listed implant was marked as implanted. |
| 7 | `IMP_STAFF_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `NUM_IMPLANTED` | INTEGER |  | The number of items implanted. |
| 9 | `IMPLANT_LOG_REF_IDENT` | VARCHAR |  | This item stores the reference ID of the implant surgical log used to generate this data. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

