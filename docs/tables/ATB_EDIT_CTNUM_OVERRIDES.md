# ATB_EDIT_CTNUM_OVERRIDES

> ATB Edit segment provider phone overrides table.

**Primary key:** `AUTH_BUNDLE_ID`, `LINE`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the auth bundle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OVR_CTNUM_S_ENTITY_AUTH_ROLE_C_NAME` | VARCHAR |  | Edit Segment - Override Provider Phone Table - Scope Role |
| 4 | `OVR_CTNUM_S_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `OVR_CTNUM_S_FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 6 | `OVR_CTNUM_S_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 7 | `OVR_CTNUM_S_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 8 | `OVR_ATB_OVRCONTACTNUM_TYPE_C_NAME` | VARCHAR |  | Edit Segment - Override Contact Number Table - Scope Contact Number Type |
| 9 | `OVR_CTNUM_B_NUM` | VARCHAR |  | Edit Segment - Override Contact Number Table - Basis Contact Number |
| 10 | `OVR_CTNUM_R_NUM` | VARCHAR |  | Edit Segment - Override Contact Number Table - Replacement Contact Number |
| 11 | `OVR_CTNUM_ACTIVE_YN` | VARCHAR |  | Edit Segment - Override Contact Number Table - Override Is Active |
| 12 | `OVR_CTNUM_USER_ID` | VARCHAR |  | Edit Segment - Override Contact Number Table - Activation User |
| 13 | `OVR_CTNUM_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 14 | `OVR_CTNUM_ACT_UTC_DTTM` | DATETIME (UTC) |  | Edit Segment - Override Contact Number Table - Activation Instant |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

