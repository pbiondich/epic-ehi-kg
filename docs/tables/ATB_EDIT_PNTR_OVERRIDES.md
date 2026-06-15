# ATB_EDIT_PNTR_OVERRIDES

> ATB Edit segment pointer overrides table.

**Primary key:** `AUTH_BUNDLE_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the auth bundle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OVR_PNTR_ENTITY_AUTH_ROLE_C_NAME` | VARCHAR |  | Edit Segment - Override Pointer Table - Role |
| 4 | `OVR_PNTR_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `OVR_PNTR_FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 6 | `OVR_PNTR_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 7 | `OVR_PNTR_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 8 | `OVR_PNTR_S_TYPE_C_NAME` | VARCHAR |  | Edit Segment - Override Pointer Table - Scope Pointer Type |
| 9 | `OVR_PNT_USER_ID` | VARCHAR |  | Edit Segment - Override Pointer Table - Set User |
| 10 | `OVR_PNT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `OVR_PNTR_SET_INST_UTC_DTTM` | DATETIME (UTC) |  | Edit Segment - Override Pointer Table - Set Instant |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

