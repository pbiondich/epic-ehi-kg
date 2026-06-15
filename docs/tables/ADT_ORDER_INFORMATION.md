# ADT_ORDER_INFORMATION

> This table contains information about ADT Orders.

**Primary key:** `ORDER_ID`  
**Columns:** 26  
**Org-specific columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `ACCOMMODATION_C_NAME` | VARCHAR | org | Stores the accommodation code. |
| 3 | `ACCOM_REASON_C_NAME` | VARCHAR | org | Stores the accommodation code reason. |
| 4 | `ADT_ADMT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `ADT_ATTEND_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `ADM_COND_C_NAME` | VARCHAR | org | Stores the patient condition. |
| 7 | `ADT_CONSULT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `ADT_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 9 | `ADT_EXPECT_ADMSN_DATE` | DATETIME |  | Stores the date the patient is expected to be admitted. |
| 10 | `ADT_EXPECT_DISCHRG_DATE` | DATETIME |  | Stores the date the patient is expected to be discharged. |
| 11 | `ADT_EXPECT_STAY_LEN` | INTEGER |  | Stores the number of days the patient is expected to stay. |
| 12 | `PAS_HAR_CHNG_RSN_C_NAME` | VARCHAR | org | Stores the reason why the patient's current hospital account is ending, and a new hospital account is beginning. |
| 13 | `ADT_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 14 | `ADT_INTERN_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 15 | `LEVEL_OF_CARE_C_NAME` | VARCHAR | org | Stores the level of care. |
| 16 | `ADT_PAT_CLASS_C_NAME` | VARCHAR | org | Stores the patient class. |
| 17 | `REASON_C_NAME` | VARCHAR | org | Stores the reason for inserting a patient update event. |
| 18 | `ADT_RES_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 19 | `ADT_RESP_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 20 | `ADT_RESP_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 21 | `HOSP_SERV_C_NAME` | VARCHAR | org | Stores the service. |
| 22 | `ADT_SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 23 | `ADT_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 24 | `ADT_ORDER_TYPE_C_NAME` | VARCHAR |  | This item stores the type of ADT order. |
| 25 | `ADT_PRIM_PROVIDERTEAM_ID` | NUMERIC |  | Stores the primary provider team. |
| 26 | `ADT_PRIM_PROVIDERTEAM_ID_RECORD_NAME` | VARCHAR |  | The name of the record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

