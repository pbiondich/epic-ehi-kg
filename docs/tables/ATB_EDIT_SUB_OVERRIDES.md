# ATB_EDIT_SUB_OVERRIDES

> Edit segment substitution overrides table.

**Primary key:** `AUTH_BUNDLE_ID`, `LINE`  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the auth bundle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OVR_SUB_S_ENTITY_AUTH_ROLE_C_NAME` | VARCHAR |  | Edit Segment - Override Substitutions Table - Scope Role |
| 4 | `OVR_SUB_S_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `OVR_SUB_S_FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 6 | `OVR_SUB_S_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 7 | `OVR_SUB_R_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `OVR_SUB_R_FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 9 | `OVR_SUB_R_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 10 | `OVR_SUB_ACTIVE_YN` | VARCHAR |  | Edit Segment - Override Substitutions Table - Substitution Is Active |
| 11 | `OVR_SUB_ACT_USER_ID` | VARCHAR |  | Edit Segment - Override Substitutions Table - Activation User |
| 12 | `OVR_SUB_ACT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `OVR_SUB_ACT_UTC_DTTM` | DATETIME (UTC) |  | Edit Segment - Override Substitutions Table - Activation Instant |
| 14 | `OVR_SUB_S_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 15 | `OVR_SUB_R_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

