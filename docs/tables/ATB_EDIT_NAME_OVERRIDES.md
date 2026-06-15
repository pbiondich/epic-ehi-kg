# ATB_EDIT_NAME_OVERRIDES

> ATB Edit segment name overrides table.

**Primary key:** `AUTH_BUNDLE_ID`, `LINE`  
**Columns:** 21  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the auth bundle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OVR_NAME_S_ENTITY_AUTH_ROLE_C_NAME` | VARCHAR |  | Edit Segment - Override Name Table - Scope Role |
| 4 | `OVR_NAME_S_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `OVR_NAME_S_FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 6 | `OVR_NAME_S_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 7 | `OVR_NAME_S_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 8 | `OVR_NAME_B_ORG_NAME` | VARCHAR |  | Edit Segment - Override Name Table - Basis Org Name |
| 9 | `OVR_NAME_B_FST_NAME` | VARCHAR |  | Edit Segment - Override Name Table - Basis First Name |
| 10 | `OVR_NAME_B_MID_NAME` | VARCHAR |  | Edit Segment - Override Name Table - Basis Middle Name |
| 11 | `OVR_NAME_B_LST_NAME` | VARCHAR |  | Edit Segment - Override Name Table - Basis Last Name |
| 12 | `OVR_NAME_B_SUFFIX_C_NAME` | VARCHAR | org | Edit Segment - Override Name Table - Basis Suffix |
| 13 | `OVR_NAME_R_ORG_NAME` | VARCHAR |  | Edit Segment - Override Name Table - Replacement Organization Name |
| 14 | `OVR_NAME_R_FST_NAME` | VARCHAR |  | Edit Segment - Override Name Table - Replacement First Name |
| 15 | `OVR_NAME_R_MID_NAME` | VARCHAR |  | Edit Segment - Override Name Table - Replacement Middle Name |
| 16 | `OVR_NAME_R_LST_NAME` | VARCHAR |  | Edit Segment - Override Name Table - Replacement Last Name |
| 17 | `OVR_NAME_R_SUFFIX_C_NAME` | VARCHAR |  | Edit Segment - Override Name Table - Replacement Suffix |
| 18 | `OVR_NAME_IS_ACT_YN` | VARCHAR |  | Edit Segment - Override Name Table - Is Override Active |
| 19 | `OVR_NAME_USER_ID` | VARCHAR |  | Edit Segment - Override Name Table - Activation User |
| 20 | `OVR_NAME_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 21 | `OVR_NAME_ACT_INST_UTC_DTTM` | DATETIME (UTC) |  | Edit Segment - Override Name Table - Activation Instant |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

