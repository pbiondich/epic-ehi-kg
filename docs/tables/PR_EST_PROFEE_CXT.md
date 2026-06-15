# PR_EST_PROFEE_CXT

> Context information for the professional fees in the price estimate. Context information is used to define the expected circumstances of the charges such as provider and department. Professional fees are generated in Resolute Professional Billing.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the price estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 5 | `POS_TYPE_C_NAME` | VARCHAR | org | The place of service (POS) type that is used to provide context for the price estimate's professional fees. |
| 6 | `VISIT_TYPE_ID_PRC_NAME` | VARCHAR |  | The name of the visit type. |
| 7 | `SERVICE_TYPE_ID` | VARCHAR | FK→ | The benefit service type used to determine benefit information for the professional fees section. This information comes from the benefit record attached to the estimate. Use the PR_EST_INFO table, BENEFITS_INFO_ID column to link this data. |
| 8 | `SERVICE_TYPE_ID_SERVICE_TYPE_NAME` | VARCHAR |  | The name of this benefit service type. |
| 9 | `PB_PR_EST_TEMPLATE_ID` | NUMERIC |  | The estimate template that was used to create this context. |
| 10 | `PB_PR_EST_TEMPLATE_ID_PR_EST_TEMPLATE_NAME` | VARCHAR |  | The name of the estimate template record. |
| 11 | `PB_DENT_PROC_SUBSTATUS_C_NAME` | VARCHAR | org | Status explaining why a procedure is not scheduled. Also groups procedures in the estimates activity and on the letter. |
| 12 | `PB_LOCATION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 13 | `PRICING_CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the pricing contract. |
| 14 | `PRICING_CNTR_OVR_YN` | VARCHAR |  | This item stores whether a user has overridden the pricing contract that is stored in I PES 311. There are two values: 0) No - Contract has been selected by the system. 1) Yes - Contract has been chosen by the user. The default is No. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SERVICE_TYPE_ID` | [BENEFIT_SVC_TYPE](BENEFIT_SVC_TYPE.md) | sole_pk | high |

