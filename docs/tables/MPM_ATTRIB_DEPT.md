# MPM_ATTRIB_DEPT

> This table contains data about departments attributed to patients for My Panel Metrics.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 4 | `MEASURE_GROUP_C_NAME` | VARCHAR | org | Measure groups attributed to departments for this patient for the purpose of My Panel Metrics. |
| 5 | `ATTRIB_RULE_LIST` | VARCHAR |  | A comma-delimited list of attribution rules that attributed the department to the measure group. |
| 6 | `ATTRIB_PROV_LIST` | VARCHAR |  | A comma-delimited list of providers that attributed the department to the measure group. |
| 7 | `ATTRIB_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 8 | `ATTRIB_SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

