# ATB_EDIT_ID_OVERRIDES

> ATB Edit segment ID overrides table.

**Primary key:** `AUTH_BUNDLE_ID`, `LINE`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the auth bundle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OVR_ID_S_ENTITY_AUTH_ROLE_C_NAME` | VARCHAR |  | Edit Segment - Override IDs Table - Scope Role |
| 4 | `OVR_ID_S_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `OVR_ID_S_FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 6 | `OVR_ID_S_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 7 | `OVR_ID_S_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 8 | `OVR_ID_S_IDTYPE_C_NAME` | VARCHAR |  | Edit Segment - Override IDs Table - Scope ID Type |
| 9 | `OVR_ID_BASIS_IDENTIFIER` | VARCHAR |  | Edit Segment - Override IDs Table - Basis ID |
| 10 | `OVR_ID_ACT_USER_ID` | VARCHAR |  | Edit Segment - Override IDs Table - Activation User |
| 11 | `OVR_ID_ACT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `OVR_ID_ACT_INST_UTC_DTTM` | DATETIME (UTC) |  | Edit Segment - Override IDs Table - Activation Instant |
| 13 | `OVR_ID_REPL_IDENTIFIER` | VARCHAR |  | Edit Segment - Override IDs Table - Basis ID |
| 14 | `OVR_ID_IS_ACTIVE_YN` | VARCHAR |  | Edit Segment - Override IDs Table - Is Override Active |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

