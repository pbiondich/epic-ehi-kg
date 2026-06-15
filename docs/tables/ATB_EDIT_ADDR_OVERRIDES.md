# ATB_EDIT_ADDR_OVERRIDES

> ATB Edit segment address overrides table.

**Primary key:** `AUTH_BUNDLE_ID`, `LINE`  
**Columns:** 27  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the auth bundle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OVR_ADDR_S_ENTITY_AUTH_ROLE_C_NAME` | VARCHAR |  | Edit Segment - Override Address Table - Scope Role |
| 4 | `OVR_ADDR_S_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `OVR_ADDR_S_FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 6 | `OVR_ADDR_S_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 7 | `OVR_ADDR_S_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 8 | `OVR_ADDR_B_HOUSENUM` | VARCHAR |  | Edit Segment - Override Address Table - Basis House Number |
| 9 | `OVR_ADDR_B_STADDR` | VARCHAR |  | Edit Segment - Override Address Table - Basis Street Address |
| 10 | `OVR_ADDR_B_CITY` | VARCHAR |  | Edit Segment - Override Address Table - Basis City |
| 11 | `OVR_ADDR_B_ZIP` | VARCHAR |  | Edit Segment - Override Address Table - Basis Zip |
| 12 | `OVR_ADDR_B_DISTRICT_C_NAME` | VARCHAR | org | Edit Segment - Override Address Table - Basis District |
| 13 | `OVR_ADDR_B_COUNTY_2_C_NAME` | VARCHAR | org | Edit Segment - Override Address Table - Basis County |
| 14 | `OVR_ADDR_B_COUNTRY_2_C_NAME` | VARCHAR | org | Edit Segment - Override Address Table - Basis Country |
| 15 | `OVR_ADDR_R_HOUSENUM` | VARCHAR |  | Edit Segment - Override Address Table - Replacement House Number |
| 16 | `OVR_ADDR_R_STADDR` | VARCHAR |  | Edit Segment - Override Address Table - Replacement Street Address |
| 17 | `OVR_ADDR_R_CITY` | VARCHAR |  | Edit Segment - Override Address Table - Replacement City |
| 18 | `OVR_ADDR_R_TAX_STATE_C_NAME` | VARCHAR | org | Edit Segment - Override Address Table - Replacement State |
| 19 | `OVR_ADDR_R_ZIP` | VARCHAR |  | Edit Segment - Override Address Table - Replacement Zip |
| 20 | `OVR_ADDR_R_DISTRICT_C_NAME` | VARCHAR |  | Edit Segment - Override Address Table - Replacement District |
| 21 | `OVR_ADDR_R_COUNTY_2_C_NAME` | VARCHAR |  | Edit Segment - Override Address Table - Replacement County |
| 22 | `OVR_ADDR_R_COUNTRY_2_C_NAME` | VARCHAR |  | Edit Segment - Override Address Table - Replacement Country |
| 23 | `OVR_ADDR_IS_ACT_YN` | VARCHAR |  | Edit Segment - Override Address Table - Is Override Active |
| 24 | `OVR_ADDR_USER_ID` | VARCHAR |  | Edit Segment - Override Address Table - Activation User |
| 25 | `OVR_ADDR_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 26 | `OVR_ADDR_INST_UTC_DTTM` | DATETIME (UTC) |  | Edit Segment - Override Address Table - Activation Instant |
| 27 | `OVR_ADDR_B_TAX_STATE_C_NAME` | VARCHAR |  | Edit Segment - Override Address Table - Basis State |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

